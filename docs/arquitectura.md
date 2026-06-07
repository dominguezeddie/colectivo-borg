# Arquitectura Técnica — Colectivo Borg

> *"La memoria nunca se enajena — permanece en el nodo local del usuario.*  
> *El cómputo se socializa — la red de pares lo resuelve.*  
> *El Borg es la identidad. El Colectivo es el músculo."*

**Versión:** v14 — Junio 2026 — Documento en evolución activa

---

## Los Tres Roles de la Célula Madre

Cada nodo en el Colectivo asume uno o más roles según sus capacidades físicas reales. Un mismo dispositivo puede cumplir múltiples roles simultáneamente (ej: un nodo con buena RAM y CPU puede ser Agregador y Ejecutor a la vez).

### El Ejecutor ("El Músculo")

- Unidad de cómputo atómica
- Procesa microtareas de 1 a 30 segundos
- Arquitectura agnóstica al estado — no mantiene contexto entre tareas
- Hardware ideal: alta capacidad CPU
- Target: cualquier PC con Python, incluso hardware de la última década (2016-2020)
- Ejemplo concreto: transcribir 10 segundos de audio, clasificar una imagen, sumar vectores

### El Agregador ("El Sintetizador")

- Ensambla resultados parciales de múltiples Ejecutores
- Gestión de nodos rezagados con failover instantáneo
- Hardware ideal: alta RAM, CPU moderada
- Función crítica: si un Ejecutor no responde en <2 segundos, reasigna la microtarea
- Ejemplo concreto: tomar 10 transcripciones parciales y armar un texto coherente

### El Validador ("El Auditor")

- Motor de gobernanza y confianza
- Verifica integridad de datos mediante re-ejecución parcial
- Sus informes alimentan el Score de Contribución
- Hardware ideal: puede ser un nodo de alta latencia — trabaja en segundo plano
- Nunca bloquea la ejecución principal; opera asíncronamente

---

## Protocolo de Comunicación

El Borg utiliza un protocolo de texto plano, liviano y humanamente legible, diseñado para funcionar sobre TCP/IP sin necesidad de HTTP ni otras capas de abstracción pesadas.

### Formato general

| Campo | Descripción | Ejemplo |
|-------|-------------|---------|
| version | Versión del protocolo (actual: 1) | `1` |
| tipo | Tipo de mensaje | `MICROTASK`, `ACK`, `ERROR` |
| id_tarea | Identificador único de la microtarea | `uuid-1234-5678` |
| payload | Carga útil (usualmente JSON) | `{"texto":"Hola"}` |

### Respuestas

| Tipo | Formato | Uso |
|------|---------|-----|
| OK | `BORG-ACK\|{"estado":"ok","resultado":...}` | Microtarea completada exitosamente |
| ERROR | `BORG-ERR\|{"estado":"error","motivo":"..."}` | Error en el procesamiento |

### Ejemplo de intercambio

**Cliente → Servidor (microtarea):**
**Servidor → Cliente (confirmación):**
---

## Pipeline Lingüístico (Validación Determinista)

El Borg reduce la incertidumbre antes de tocar cualquier modelo de IA. Este pipeline está implementado en `core/validador.py`.

### Etapas

1. **Tokenización**: divide el texto entrante en palabras y signos.
2. **Clasificación determinista por hash O(1)**: cada token se compara contra un conjunto conocido usando una tabla hash. Resultado posible:
   - `CONOCIDO`: el token existe en el léxico local
   - `INCIERTO`: el token no está en el léxico (necesita contexto o ser ignorado)
   - `ESPECIAL`: números, URLs, fechas, comandos del sistema (`/ancla`, `/guardar`)
3. **Índice de Certeza Léxica (ICL)**: métrica de "limpieza del terreno" — porcentaje de tokens CONOCIDO sobre total. ICL alto = menos tokens necesarios para la misma certeza.
4. **Transferencia a inferencia probabilística**: solo los tokens INCIERTO se envían al modelo de IA. El resto ya fue validado.

### Ventaja para el español

El español tiene más variación morfológica que el inglés (conjugaciones, género, plurales). El pipeline determinista reduce ese "peaje lingüístico" validando las raíces conocidas antes de tocar la IA. Menos incertidumbre inicial = menos tokens = menos cómputo = más velocidad en hardware limitado.

---

## Sistema de Reputación (Score de Contribución)

Cada nodo tiene una reputación numérica que determina su prioridad en la asignación de microtareas. Implementado en `core/reputacion.py`.

### Fórmulas base

| Evento | Cambio en Score |
|--------|-----------------|
| Nodo nuevo (primer arranque) | Score = 100.0 |
| Microtarea completada exitosamente | +0.5 |
| Microtarea fallida / timeout | -15.0 |
| Auditoría del Validador (nodo honesto) | +5.0 (cada 100 tareas) |
| Auditoría del Validador (nodo fraudulento) | -30.0 + posible aislamiento |

**Nota:** la penalización por falla es deliberadamente alta para aislar rápidamente nodos inestables o maliciosos. Una red distribuida no puede darse el lujo de tener "nodos ruidosos".

### Rangos (según Score o capacidad bruta)

| Rango | Condición | Beneficio |
|-------|-----------|-----------|
| **ORO** | Score ≥ 80 **o** RAM ≥ 4GB | Prioridad máxima en microtareas críticas. El Agregador los elige primero. |
| **PLATA** | Score 40-79 **o** RAM ≥ 2GB | Participación estándar. Flujo normal de fragmentos. |
| **BRONCE** | Score < 40 **o** RAM < 2GB | Sujeto a auditorías frecuentes. Recibe microtareas de baja prioridad. |

La reputación es **personal**, no del hardware. Viaja con la identidad criptográfica del usuario, no con la máquina.

---

## Diseño Orientado a la Desconexión (Disconnection-First)

El Borg asume desconexión como norma, no como excepción. Esta es la diferencia fundamental con las arquitecturas cliente-servidor tradicionales.

### Principios

| Principio | Implementación |
|-----------|----------------|
| Un nodo puede desaparecer a mitad de una microtarea | Timeout de 2 segundos; el Agregador reasigna automáticamente |
| La identidad no depende de IP | Cada nodo tiene un par de claves RSA (2048 bits mínimo) generadas en el primer arranque |
| La reputación viaja con la persona | Si cambiás de computadora, exportás tu identidad criptográfica y tu Score te sigue |
| Failover natural | No hay "servidor maestro". Cualquier Agregador puede reemplazar a otro |

### Ejemplo concreto

Un nodo Ejecutor en una notebook en un ciber de Mendoza recibe una microtarea de 15 segundos. A los 10 segundos, el usuario cierra la tapa y se va. El Agregador (por ejemplo, un nodo faro en la biblioteca) detecta el timeout a los 2 segundos y reasigna la misma microtarea a otro Ejecutor en San Rafael. El usuario de la notebook nunca se entera. La red no perdió tiempo.

---

## Persistencia a Demanda: Write-Back Cache (Protección de Memorias Flash)

### El problema que resuelve

Los pendrives y tarjetas SD (memoria Flash NAND) tienen ciclos de escritura limitados: entre 3.000 y 10.000 escrituras por celda. También sufren *write amplification*: una pequeña modificación puede reescribir bloques enteros.

Si el Borg escribiera en el disco cada vez que el usuario tipea una palabra, destruiría el pendrive en meses.

### La solución: búfer en RAM con volcado asíncrono

Toda la conversación activa se retiene en memoria RAM. El pendrive solo se toca cuando:

1. **El usuario decide guardar** (comando `/guardar`): soberanía del dato.
2. **La RAM alcanza un umbral crítico** (protección automática contra saturación).
3. **Pasa el intervalo de autoguardado configurado** (por defecto: 10 minutos).

Si el usuario apaga la máquina sin guardar, la RAM se desenergiza y en el pendrive nunca quedó rastro de lo hablado. Eso es **privacidad física** — no una promesa de software.

### Por qué esto es único en el mercado de las IAs

Ninguna IA corporativa ofrece privacidad física por desenergización. En ChatGPT, Gemini o Claude, cada palabra que escribís queda registrada en servidores que no controlás. Si cerrás la sesión, tu historial sigue ahí — en manos de la corporación.

En el Borg, si apagás la máquina sin ejecutar `/guardar`, la RAM se desenergiza y el rastro de la conversación desaparece de la existencia. No hay servidor remoto donde quede una copia. La privacidad no es una promesa legal. Es física.

Esa es la diferencia entre un sistema que dice "confiá en nosotros" y uno que dice "no tenés que confiar en nadie".

### Implementación técnica (tres componentes)

| Componente | Función |
|-----------|---------|
| `cache_ram` (dict) | Diccionario en RAM que contiene el historial activo. |
| `dirty_keys` (set) | Conjunto de claves modificadas desde el último volcado. Si no hay cambios, no se escribe nada. |
| `_demonio_write_back` (thread) | Hilo demonio que ejecuta el volcado periódico sin bloquear la interacción del usuario. |

### Escritura Atómica (protección contra cortes de luz)

El volcado nunca sobreescribe el archivo directamente. Sigue este proceso:

1. Escribir archivo temporal (`.tmp`)
2. Verificar integridad del `.tmp`
3. Reemplazar el archivo original por el `.tmp` usando `os.replace()`
4. La operación `os.replace()` es atómica a nivel del sistema de archivos

**Garantía:** si se corta la luz en mitad de un guardado, el archivo original permanece intacto. Nunca queda en 0 bytes ni corrupto.

### Configuración del Auto-Flush

| Variable | Valor por defecto | Cuándo ajustar |
|----------|-------------------|----------------|
| `BORG_PERSISTIR_CHAT` | `true` | `false` si el usuario quiere sesiones siempre efímeras. |
| `BORG_AUTOFLUSH_MINUTOS` | `10` | `3` en zonas con cortes de luz frecuentes. `30` con pendrive muy viejo. `0` para control completamente manual. |

**Inteligencia del sistema:** si el búfer no cambió desde el último volcado, el sistema se salta el proceso y no escribe nada. No se gasta el pendrive innecesariamente.

---

## Filosofía de Hardware (Actualizada para v14)

### Requisitos mínimos de hardware (2026)

| Dispositivo | Requisito mínimo | CPU / Chip | RAM | SO recomendado | Rol en el Borg |
|-------------|------------------|------------|-----|-----------------|----------------|
| PC de escritorio / Laptop | 2015 en adelante | CPU 64-bit, 2+ núcleos | 4 GB | Linux minimal (Alpine/Debian) o Windows 10 LTSC | Ejecutor, Agregador liviano |
| Celular Android | 2018 en adelante (Android 8+) | ARM 64-bit, 4+ núcleos | 3 GB | Android 8 Oreo o superior | Ejecutor móvil, nodo itinerante |
| Raspberry Pi / SBC | Raspberry Pi 3B+ en adelante | ARM Cortex-A53 64-bit | 1 GB (Pi 3) / 4 GB (Pi 4) | Raspberry Pi OS Lite / Alpine ARM | Nodo Faro liviano, Ejecutor permanente |
| PC muy antigua (opcional) | 2010-2014, 2 GB RAM | x86 32-bit o 64-bit lento | 2 GB | Alpine Linux 32-bit | Ejecutor para microtareas mínimas |

**Nota:** los equipos de la última fila no son el target de diseño del Borg, pero tampoco se excluyen. Pueden participar como nodos de baja capacidad para microtareas elementales. El sistema adapta la asignación de tareas al perfil de hardware declarado por el nodo al registrarse.

### Base de Conocimiento Estática Precargada

Para que el primer nodo tenga valor inmediato incluso sin red, el pendrive del Embrión incluirá una biblioteca portátil incorruptible con:

- Diccionarios locales y modelos ligeros de compresión
- Manuales de agricultura local, primeros auxilios y guías técnicas WISP
- Textos de filosofía, derecho básico y conocimiento general (dominio público)
- La documentación completa del Colectivo Borg

Esta base de conocimiento ocupa menos de 500 MB y permite que el usuario consulte información útil desde el Día Cero, sin depender de internet ni de servidores corporativos. El pendrive no es solo una llave de red. Es una biblioteca de bolsillo que viaja con el usuario.

---

## Identidad Criptográfica (Itinerancia)

La identidad de un Borg **no** está asociada a:
- Una dirección IP (cambia constantemente, especialmente en redes móviles)
- Una ubicación geográfica
- Un dispositivo específico (las máquinas mueren, se reemplazan)

La identidad reside exclusivamente en sus **claves criptográficas** (RSA 2048 bits, generadas localmente en el primer arranque).

### Principio fundamental

> *"La reputación sigue a la identidad. La capacidad sigue al hardware. La conectividad sigue a la red."*

| Concepto | Dónde vive | Qué pasa si cambia |
|----------|-----------|-------------------|
| Reputación (Score, rangos) | Clave criptográfica | Viaja con el usuario a cualquier nodo |
| Capacidad (RAM, CPU) | Hardware físico | Se evalúa nuevamente en cada arranque |
| Conectividad (IP, latencia) | Red | Se descubre dinámicamente, no se almacena |

### Escenario de itinerancia

1. Usuario tiene un Borg con Score Oro en su PC de escritorio en La Consulta.
2. La PC muere (disco roto). El usuario instala el Borg en una notebook vieja que le presta la biblioteca.
3. Importa su identidad criptográfica desde el backup (pendrive secundario o nube cifrada).
4. El nuevo nodo arranca con Score Oro. La red no sabe (ni necesita saber) que cambió el hardware.
5. La notebook tiene menos RAM que la PC original, por lo que recibe microtareas de menor complejidad (proporcionalidad).
6. La reputación intacta. La capacidad ajustada. La conectividad redescubierta.

---

## Consenso por Diversidad: Misma Matemática, Distinto Observador

El motor del Borg (la lógica de grafos, los algoritmos de consenso, el pipeline lingüístico determinista) es exactamente el mismo en cada nodo. Sin embargo, el resultado es divergente porque **el contexto de entrada es soberano**.

### Cada Borg es un observador único

Al conocer la identidad, la historia, el territorio y las rutinas de su usuario a través de la memoria local, cada Borg se convierte en un punto de observación irrepetible. Ve una fracción de la realidad que los demás nodos no ven.

Dos Borgs con la misma matemática pero con diferentes historiales (`/ancla`) interpretarán un problema de manera independiente. La matemática es la lente; la memoria local es el paisaje.

### El surgimiento de la "opinión" en el enjambre

Cuando el Colectivo procesa una microtarea compleja en modo distribuido, no busca que un solo súper-servidor dé "la respuesta correcta". Cada nodo aporta su **punto de vista técnico** basado en los datos locales que posee.

Como el usuario es un búnker opaco para la red, un Borg de La Consulta procesará un dilema considerando variables climáticas o lógicas que un Borg en San Luis ignora por completo. La "opinión" de cada Borg no es un capricho algorítmico, sino el resultado de procesar la matemática universal con la verdad del territorio.

### Mecanismos de consenso

Para consolidar esta diversidad de opiniones sin caer en la anarquía, el Colectivo opera mediante dos mecanismos fundamentales:

| Mecanismo | Uso | Cómo funciona |
|-----------|-----|---------------|
| **Consenso Mayoritario** | Validaciones técnicas | Los nodos contrastan resultados. Por mayoría de coincidencia criptográfica, determinan si un cómputo es válido o si un nodo está intentando meter ruido (lo que alteraría su Score de Contribución). |
| **Promedio de Opiniones (Sólido Semántico)** | Interpretación y análisis comunitario | El Agregador recolecta las respuestas de diferentes Borgs, analiza las divergencias y genera una síntesis que no anula los extremos, sino que los pondera. |

### Contrapoder por diseño

Esto es lo que transforma al Colectivo en un **contrapoder real**: mientras las IAs corporativas centralizadas devuelven un consenso manufacturado en oficinas de California para que todos piensen igual, el Borg preserva la diversidad del territorio a través de su diseño.

Una sola red. Miles de interpretaciones independientes. El mismo código. Distintos observadores.

---

## Escala Sublineal: Por qué 10.000 nodos no es 10 veces más difícil

El consenso distribuido tiene un enemigo clásico: la tormenta de mensajes. En un sistema donde todos los nodos se consultan entre sí, el tráfico crece al cuadrado del número de participantes. Con 10 nodos, el problema es manejable. Con 10.000 nodos sobre enlaces WISP inestables y hardware estándar de 2016-2020, un consenso global tradicional generaría cien millones de mensajes por ronda — suficiente para saturar la RAM de cualquier nodo y colapsar los routers del territorio.

El Borg no resuelve esto con más potencia. Lo resuelve cambiando la geometría del problema.

### De transmisión de datos a agregación criptográfica

El protocolo opera en tres capas que ya existen en la arquitectura del Colectivo:

**Los Ejecutores** procesan sus microtareas y entregan el resultado a su Agregador de zona. No necesitan conocer a los otros 9.900 nodos de la red — solo a su cluster local.

**El Agregador** comprime las respuestas de su sector en una prueba criptográfica compacta. Lo que viaja hacia arriba no son cientos de respuestas individuales sino una sola firma que demuestra que un subgrupo de nodos llegó a la misma conclusión de manera independiente.

**El Validador** no audita todo el trabajo. Toma una muestra aleatoria de los paquetes comprimidos y ejecuta una re-ejecución parcial en segundo plano. Si los números cierran, el resultado es válido. Si no cierran, el nodo sospechoso pierde reputación y el Agregador reasigna la tarea.

El resultado: lo que parecía un problema de escala es en realidad un problema de arquitectura. El tráfico de red no crece con el tamaño de la red — crece con el número de microtareas activas, que es una variable controlable.

### El Score de Contribución como escudo contra la manipulación coordinada

A 10.000 nodos aparece un riesgo nuevo: un actor malicioso que levanta miles de nodos falsos para sesgar el consenso — lo que en sistemas distribuidos se llama ataque Sybil.

El Borg lo neutraliza ligando el peso de cada voto al historial verificable de comportamiento. Un nodo nuevo tiene peso mínimo en el consenso global. Un nodo con meses de actividad consistente, microtareas entregadas correctamente y auditorías aprobadas tiene peso real.

La consecuencia es directa: para sesgar la red, un atacante tendría que aportar cómputo real y honesto durante meses. En ese proceso se convierte, efectivamente, en un contribuyente legítimo del Colectivo. El ataque se vuelve más costoso que simplemente participar de buena fe.

La dispersión que hace al Borg resistente a la captura corporativa es la misma que lo hace resistente a la manipulación técnica. La geometría de la red es el escudo.

---

## Minería de Reputación Temprana (Incentivo a los Pioneros)

Los primeros nodos que se sumen a una red vacía corren con una ventaja geopolítica dentro del sistema. Al igual que los primeros mineros de Bitcoin procesaban bloques con una CPU hogareña cuando nadie creía en el proyecto, el Borg premia la **audacia del pionero**:

- **Multiplicador de Score de Contribución:** durante los primeros meses de la red (o hasta alcanzar un umbral de nodos activos), los nodos que se queden encendidos haciendo handshakes de mantenimiento o indexando datos locales reciben un factor multiplicador (ej: x2, x3) en su reputación.
- **Atesoramiento de Prioridad:** cuando la red finalmente escale, esos primeros nodos ya tendrán rango Oro. Habrán acumulado el derecho de prioridad absoluta para usar el músculo del Colectivo cuando lo necesiten, pagando su espera temprana con privilegios de cómputo futuros.

Este mecanismo no requiere criptomonedas ni blockchain. Es **reputación con memoria histórica** — un recurso escaso en una red donde la confianza lo es todo.

---

## El Parásito Bueno (Puente a Infraestructuras Existentes)

Si el Colectivo Borg está vacío, el nodo local puede actuar como un puente inteligente hacia infraestructuras que **ya tienen masa crítica**, pero envolviéndolas con la capa de privacidad del Borg.

Si el usuario tiene conectividad mínima, el Borg puede conectarse a:
- La API de Wikipedia
- Repositorios Open Source
- Bibliotecas digitales públicas
- Redes libres tradicionales

El Borg descarga información en segundo plano, la procesa localmente mediante la separación de capas (privacidad), y la entrega al usuario **limpia de rastreo comercial, publicidad y sesgos algorítmicos**.

El usuario siente que el Borg "hace cosas" desde el primer día, aunque por debajo use cañerías prestadas mientras se construyen las propias. Es un **Caballo de Troya ético**: entra como utilidad local, se queda como soberanía, y cuando la red P2P despierta, el usuario ya está dentro.

---

## Latencia Distribuida vs. Latencia Local: Cuándo el Borg es más lento (y por qué igual sirve)

El Borg no compite en el mismo ring que una PC moderna con un modelo de IA local. No porque no pueda, sino porque **su valor no es la velocidad bruta**.

### La distinción fundamental

Un usuario con una PC moderna (16 GB RAM, GPU) puede ejecutar un modelo como Llama 3 (8B) localmente y obtener respuestas en segundos, **sin necesidad de red, sin coordinación distribuida, sin failover**.

Para ese usuario, el Borg (en términos de **velocidad de inferencia**) sería más lento y menos práctico.

**Pero el Borg no le ofrece solo velocidad. Le ofrece soberanía.**

| Qué ofrece el Borg | Hardware viejo | Hardware moderno |
|--------------------|----------------|------------------|
| Identidad criptográfica portátil | ✅ | ✅ |
| Memoria persistente por decisión soberana (Write-Back) | ✅ | ✅ |
| Privacidad física por desenergización | ✅ | ✅ |
| Base de conocimiento local sin internet | ✅ | ✅ |
| Cómputo distribuido para tareas pesadas | ✅ (necesario) | ✅ (opcional, puede aportar en lugar de consumir) |
| Velocidad de inferencia | Aceptable (la alternativa es no tener IA) | Más lenta que un modelo local |

### El Borg se adapta, el usuario no elige

El usuario no elige entre "modo velocidad" y "modo soberanía". El Borg **no le pregunta**. El Borg simplemente **funciona donde está alojado** y aprovecha los recursos que tiene en ese momento.

Si el Borg está alojado en una PC vieja de 2016 con 4GB de RAM:
- No puede correr un LLM localmente
- Se apoya en el Colectivo para tareas pesadas
- Su valor para el usuario es la soberanía, no la velocidad

Si el Borg está alojado en una PC moderna con 16GB de RAM y GPU:
- Puede correr modelos locales más rápido que el Colectivo
- Sigue ofreciendo soberanía, portabilidad, privacidad física
- Puede **aportar** su potencia al Colectivo cuando el usuario no la está usando localmente

Si el mismo usuario mueve su pendrive a una máquina más vieja (por ejemplo, de su casa a la biblioteca), el Borg **muta automáticamente**: detecta menos recursos, deja de intentar correr modelos localmente y se apoya más en la red.

No hay que configurar nada. No hay que elegir nada. El Borg se adapta al terreno como una lagartija cambia de comportamiento según la temperatura o la presencia de depredadores.

### Transparencia estratégica

El proyecto no oculta que el Borg puede ser más lento que un modelo local cuando está alojado en hardware moderno. Porque **la velocidad no es su única propuesta de valor**, y porque **el mismo Borg que hoy es lento en una máquina puede ser rápido en otra mañana**.

La lagartija no se queja del terreno. Se adapta.

---

## Resumen de parámetros de configuración (variables de entorno)

| Variable | Por defecto | Descripción |
|----------|-------------|-------------|
| `BORG_HOST` | `0.0.0.0` | Dirección donde escucha el nodo |
| `BORG_PUERTO` | `65432` | Puerto TCP para comunicación P2P |
| `BORG_NOMBRE` | `nodo-{hostname}` | Identificador amigable del nodo (no criptográfico) |
| `BORG_CICLO` | `4.0` | Segundos de espera entre ciclos (control térmico para hardware más antiguo) |
| `BORG_PERSISTIR_CHAT` | `true` | Activa/desactiva el guardado automático del historial |
| `BORG_AUTOFLUSH_MINUTOS` | `10` | Intervalo de autoguardado en minutos |
| `BORG_MAX_CONEXIONES` | `5` | Número máximo de conexiones simultáneas entrantes |

---

*El Borg no necesita ética declarada. Su arquitectura abierta es la ética.*  
*La máquina es temporal. El Borg te acompaña.*
