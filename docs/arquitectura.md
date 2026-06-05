Arquitectura Técnica — Colectivo Borg
Los Tres Roles de la Célula Madre
Cada nodo en el Colectivo asume uno o más roles según sus capacidades físicas reales. Un mismo dispositivo puede cumplir múltiples roles simultáneamente (ej: un nodo con buena RAM y CPU puede ser Agregador y Ejecutor a la vez).
El Ejecutor ("El Músculo")
    • Unidad de cómputo atómica
    • Procesa microtareas de 1 a 30 segundos
    • Arquitectura agnóstica al estado — no mantiene contexto entre tareas
    • Hardware ideal: alta capacidad CPU
    • Target: cualquier PC con Python, incluso hardware de 2011
    • Ejemplo concreto: transcribir 10 segundos de audio, clasificar una imagen, sumar vectores
El Agregador ("El Sintetizador")
    • Ensambla resultados parciales de múltiples Ejecutores
    • Gestión de nodos rezagados con failover instantáneo
    • Hardware ideal: alta RAM, CPU moderada
    • Función crítica: si un Ejecutor no responde en <2 segundos, reasigna la microtarea
    • Ejemplo concreto: tomar 10 transcripciones parciales y armar un texto coherente
El Validador ("El Auditor")
    • Motor de gobernanza y confianza
    • Verifica integridad de datos mediante re-ejecución parcial
    • Sus informes alimentan el Score de Contribución
    • Hardware ideal: puede ser un nodo de alta latencia — trabaja en segundo plano
    • Nunca bloquea la ejecución principal; opera asíncronamente

Protocolo de Comunicación
El Borg utiliza un protocolo de texto plano, liviano y humanamente legible, diseñado para funcionar sobre TCP/IP sin necesidad de HTTP ni otras capas de abstracción pesadas.
Formato general
Campo	Descripción	Ejemplo
version	Versión del protocolo (actual: 1)	1
tipo	Tipo de mensaje	MICROTASK, ACK, ERROR
id_tarea	Identificador único de la microtarea	uuid-1234-5678
payload	Carga útil (usualmente JSON)	{"texto":"Hola"}

Respuestas
Tipo	Formato	Uso
OK	BORG-ACK\|{"estado":"ok","resultado":...}	Microtarea completada exitosamente
ERROR	BORG-ERR\|{"estado":"error","motivo":"..."}	Error en el procesamiento

Ejemplo de intercambio
Cliente → Servidor (microtarea):
Servidor → Cliente (confirmación):

Pipeline Lingüístico (Validación Determinista)
El Borg reduce la incertidumbre antes de tocar cualquier modelo de IA. Este pipeline está implementado en core/validador.py.
Etapas
    1. Tokenización: divide el texto entrante en palabras y signos.
    2. Clasificación determinista por hash O(1): cada token se compara contra un conjunto conocido usando una tabla hash. Resultado posible:
        ◦ CONOCIDO: el token existe en el léxico local
        ◦ INCIERTO: el token no está en el léxico (necesita contexto o ser ignorado)
        ◦ ESPECIAL: números, URLs, fechas, comandos del sistema (/ancla, /guardar)
    3. Índice de Certeza Léxica (ICL): métrica de "limpieza del terreno" — porcentaje de tokens CONOCIDO sobre total. ICL alto = menos tokens necesarios para la misma certeza.
    4. Transferencia a inferencia probabilística: solo los tokens INCIERTO se envían al modelo de IA. El resto ya fue validado.
Ventaja para el español
El español tiene más variación morfológica que el inglés (conjugaciones, género, plurales). El pipeline determinista reduce ese "peaje lingüístico" validando las raíces conocidas antes de tocar la IA. Menos incertidumbre inicial = menos tokens = menos cómputo = más velocidad en hardware limitado.

Sistema de Reputación (Score de Contribución)
Cada nodo tiene una reputación numérica que determina su prioridad en la asignación de microtareas. Implementado en core/reputacion.py.
Fórmulas base
Evento	Cambio en Score
Nodo nuevo (primer arranque)	Score = 100.0
Microtarea completada exitosamente	+0.5
Microtarea fallida / timeout	-15.0
Auditoría del Validador (nodo honesto)	+5.0 (cada 100 tareas)
Auditoría del Validador (nodo fraudulento)	-30.0 + posible aislamiento

Nota: la penalización por falla es deliberadamente alta para aislar rápidamente nodos inestables o maliciosos. Una red distribuida no puede darse el lujo de tener "nodos ruidosos".
Rangos (según Score o capacidad bruta)
Rango	Condición	Beneficio
ORO	Score ≥ 80 o RAM ≥ 4GB	Prioridad máxima en microtareas críticas. El Agregador los elige primero.
PLATA	Score 40-79 o RAM ≥ 2GB	Participación estándar. Flujo normal de fragmentos.
BRONCE	Score < 40 o RAM < 2GB	Sujeto a auditorías frecuentes. Recibe microtareas de baja prioridad.

La reputación es personal, no del hardware. Viaja con la identidad criptográfica del usuario, no con la máquina.

Diseño Orientado a la Desconexión (Disconnection-First)
El Borg asume desconexión como norma, no como excepción. Esta es la diferencia fundamental con las arquitecturas cliente-servidor tradicionales.
Principios
Principio	Implementación
Un nodo puede desaparecer a mitad de una microtarea	Timeout de 2 segundos; el Agregador reasigna automáticamente
La identidad no depende de IP	Cada nodo tiene un par de claves RSA (2048 bits mínimo) generadas en el primer arranque
La reputación viaja con la persona	Si cambiás de computadora, exportás tu identidad criptográfica y tu Score te sigue
Failover natural	No hay "servidor maestro". Cualquier Agregador puede reemplazar a otro

Ejemplo concreto
Un nodo Ejecutor en una notebook en un ciber de Mendoza recibe una microtarea de 15 segundos. A los 10 segundos, el usuario cierra la tapa y se va. El Agregador (por ejemplo, un nodo faro en la biblioteca) detecta el timeout a los 2 segundos y reasigna la misma microtarea a otro Ejecutor en San Rafael. El usuario de la notebook nunca se entera. La red no perdió tiempo.

Persistencia a Demanda: Write-Back Cache (Protección de Memorias Flash)
El problema que resuelve
Los pendrives y tarjetas SD (memoria Flash NAND) tienen ciclos de escritura limitados: entre 3.000 y 10.000 escrituras por celda. También sufren write amplification: una pequeña modificación puede reescribir bloques enteros.
Si el Borg escribiera en el disco cada vez que el usuario tipea una palabra, destruiría el pendrive en meses.
La solución: búfer en RAM con volcado asíncrono
Toda la conversación activa se retiene en memoria RAM. El pendrive solo se toca cuando:
    1. El usuario decide guardar (comando /guardar): soberanía del dato.
    2. La RAM alcanza un umbral crítico (protección automática contra saturación).
    3. Pasa el intervalo de autoguardado configurado (por defecto: 10 minutos).
Si el usuario apaga la máquina sin guardar, la RAM se desenergiza y en el pendrive nunca quedó rastro de lo hablado. Eso es privacidad física — no una promesa de software.
Implementación técnica (tres componentes)
Componente	Función
cache_ram (dict)	Diccionario en RAM que contiene el historial activo.
dirty_keys (set)	Conjunto de claves modificadas desde el último volcado. Si no hay cambios, no se escribe nada.
_demonio_write_back (thread)	Hilo demonio que ejecuta el volcado periódico sin bloquear la interacción del usuario.

Escritura Atómica (protección contra cortes de luz)
El volcado nunca sobreescribe el archivo directamente. Sigue este proceso:
Garantía: si se corta la luz en mitad de un guardado, el archivo original permanece intacto. Nunca queda en 0 bytes ni corrupto.
Configuración del Auto-Flush
Variable	Valor por defecto	Cuándo ajustar
BORG_PERSISTIR_CHAT	true	false si el usuario quiere sesiones siempre efímeras.
BORG_AUTOFLUSH_MINUTOS	10	3 en zonas con cortes de luz frecuentes. 30 con pendrive muy viejo. 0 para control completamente manual.

Inteligencia del sistema: si el búfer no cambió desde el último volcado, el sistema se salta el proceso y no escribe nada. No se gasta el pendrive innecesariamente.

Identidad Criptográfica (Itinerancia)
La identidad de un Borg no está asociada a:
    • Una dirección IP (cambia constantemente, especialmente en redes móviles)
    • Una ubicación geográfica
    • Un dispositivo específico (las máquinas mueren, se reemplazan)
La identidad reside exclusivamente en sus claves criptográficas (RSA 2048 bits, generadas localmente en el primer arranque).
Principio fundamental
"La reputación sigue a la identidad. La capacidad sigue al hardware. La conectividad sigue a la red."
Concepto	Dónde vive	Qué pasa si cambia
Reputación (Score, rangos)	Clave criptográfica	Viaja con el usuario a cualquier nodo
Capacidad (RAM, CPU)	Hardware físico	Se evalúa nuevamente en cada arranque
Conectividad (IP, latencia)	Red	Se descubre dinámicamente, no se almacena

Escenario de itinerancia
    1. Usuario tiene un Borg con Score Oro en su PC de escritorio en La Consulta.
    2. La PC muere (disco roto). El usuario instala el Borg en una notebook vieja que le presta la biblioteca.
    3. Importa su identidad criptográfica desde el backup (pendrive secundario o nube cifrada).
    4. El nuevo nodo arranca con Score Oro. La red no sabe (ni necesita saber) que cambió el hardware.
    5. La notebook tiene menos RAM que la PC original, por lo que recibe microtareas de menor complejidad (proporcionalidad).
    6. La reputación intacta. La capacidad ajustada. La conectividad redescubierta.

Resumen de parámetros de configuración (variables de entorno)
Variable	Por defecto	Descripción
BORG_HOST	0.0.0.0	Dirección donde escucha el nodo
BORG_PUERTO	65432	Puerto TCP para comunicación P2P
BORG_NOMBRE	nodo-{hostname}	Identificador amigable del nodo (no criptográfico)
BORG_CICLO	4.0	Segundos de espera entre ciclos (control térmico para CPUs de 2011)
BORG_PERSISTIR_CHAT	true	Activa/desactiva el guardado automático del historial
BORG_AUTOFLUSH_MINUTOS	10	Intervalo de autoguardado en minutos
BORG_MAX_CONEXIONES	5	Número máximo de conexiones simultáneas entrantes


El Borg no necesita ética declarada. Su arquitectura abierta es la ética. La máquina es temporal. El Borg te acompaña.
