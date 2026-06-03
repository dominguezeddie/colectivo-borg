# Funcionalidades del Colectivo Borg

## Principio rector

El Borg no es solo un sistema de chat o de cómputo distribuido.
Es un **ente activo** en la vida cotidiana del usuario.

No necesita pantallas coloridas. No necesita apps corporativas.
Todo ocurre a través de la interfaz del propio Borg — terminal o voz.

**Regla de privacidad absoluta:**
Todo seguimiento, agenda, rutinas de pánico, telemetría y filtrado léxico
reside estrictamente dentro del perímetro del nodo local.
El Colectivo global permanece ciego respecto a los datos privados del usuario.

---

## CB-001 — Hilos de Ariadna / Anclas de Retorno Dinámicas

**El problema:**
Las interfaces de chat son lineales, pero el pensamiento humano no lo es.
Abrimos paréntesis conceptuales constantemente. Cuando queremos volver
al hilo principal, el scroll infinito genera fatiga física y cognitiva.

**La solución:**
Un puntero de contexto que congela una línea específica de la conversación
antes de una bifurcación conceptual.

```
/ancla          → marca el punto de retorno
/a-que-iba      → vuelve instantáneamente al punto marcado
```

Al ejecutar el gatillo de retorno, el sistema colapsa el desvío efímero
en RAM y re-inyecta el contexto original en la interfaz activa.

**Analogía técnica:**
Es exactamente un **Callback** o una estructura **Stack (Pila)**:
guardás el estado actual, apilás la aclaración, y cuando terminás,
ejecutás la función de retorno para desapilar y seguir donde estabas.
Lo que las personas hacemos intuitivamente en conversaciones cotidianas
— "guardame el hilo" — convertido en función nativa del sistema.

---

## CB-002 — Mapeo Semántico y Segmentación Temática

**El problema:**
Las conversaciones largas y multitemáticas pierden estructura.
Navegar entre temas requiere scroll manual o memoria del usuario.

**La solución:**
El módulo Agregador procesa fragmentos de texto en tiempo real
y genera un índice temático lateral dinámico.

Cuando detecta un cambio semántico significativo (transición brusca
de tema), el chat se segmenta visualmente en bloques lógicos.
El usuario puede saltar entre bloques con un solo clic o comando de voz.

**Nota:** Esta no es una función extra — es el Agregador cumpliendo
su rol natural de síntesis e inteligencia logística.

---

## CB-003 — Sensor de Persistencia Conversacional (Termómetro Discursivo)

**El problema:**
Las personas mayores que repiten historias o preguntas de forma sistemática
pueden estar mostrando señales tempranas de deterioro cognitivo.
Detectarlo a tiempo puede ser crítico para su cuidado.

**La distinción ética fundamental:**
Un termómetro no diagnostica enfermedades — mide temperatura.
Este sistema no diagnostica condiciones médicas — mide métricas
de persistencia lingüística. Son datos fácticos, no juicios clínicos.

**La solución:**
Medición matemática estricta de frecuencia de n-gramas o narrativas
idénticas dentro de ventanas cortas de tiempo.

Si la misma historia o pregunta se repite con patrón idéntico
tres veces en diez minutos, el sistema registra un "pico" en esa métrica.
Exactamente igual que un termómetro que marca 39°C.

**Sistema de notificación:**
- Protocolo: SMTP local usando `smtplib` nativo de Python
- Sin dependencia de APIs corporativas externas
- Formato: registro objetivo tipo hoja de enfermería
  (métricas cuantitativas puras, sin adjetivos alarmistas)
- Seguridad: CCO (Con Copia Oculta) — médico e hijos reciben
  el mismo informe sin que se expongan sus correos entre sí

**Privacidad:**
El procesamiento y almacenamiento ocurre 100% en el nodo local.
El Colectivo global no tiene acceso a estos datos.

---

## CB-004 — Máscara de Interacción Auditiva (Accesibilidad Nativa)

**El problema:**
Las personas invidentes o con discapacidad visual severa no pueden
usar interfaces de terminal. Los lectores de pantalla comerciales
son pesados, privativos y rompen el flujo de la interacción.

**La solución:**
Cuando el sistema se configura en modo accesibilidad visual,
la interfaz gráfica se apaga (ahorrando procesamiento) y activa
un pipeline acústico bidireccional completamente offline:

- **Entrada STT:** Speech-to-Text local y offline
  (Whisper-small o Vosk) procesado directamente en RAM.
  El usuario habla — el sistema escucha y transforma a texto.

- **Salida TTS:** Text-to-Speech nativo (pyttsx3)
  comunicándose directamente con los drivers de audio del OS.
  Consumo de ancho de banda: cero.

**Aplicación combinada con CB-003:**
Si el usuario invidente es una persona mayor, el sistema puede
avisar por voz en un momento apropiado:
*"Reporte diario enviado a la red de apoyo de la familia."*

---

## CB-005 — Agenda Médica y Notificaciones de Contexto Activo

**El problema:**
Los usuarios necesitan recordatorios de medicamentos, turnos médicos,
buscar a sus hijos en la escuela, retirar un pedido.
Las apps comerciales requieren cuentas, permisos y conectividad.

**La solución:**
Servicios de utilidad gestionados localmente integrados al flujo
de conversación. Sin salir del Borg, sin abrir otra aplicación:

- Recordatorio de medicamento a horario estricto
- Alerta de turno médico
- Aviso de buscar al hijo en la escuela
- Cualquier evento configurable manualmente

**La ventaja estratégica para el Colectivo:**
Un usuario que usa el Borg como despertador mantiene el dispositivo
encendido las 24 horas. Durante las horas de baja actividad nocturna,
el silicio ocioso aporta cómputo al Colectivo global.

> El usuario se beneficia. La red se beneficia. Nadie pierde.

Un nodo que funciona como despertador garantiza disponibilidad
nocturna del 100% para microtareas globales. Las utilidades cotidianas
no son accesorios — son infraestructura de disponibilidad.

---

## CB-006 — Módulo de Geolocalización y Perímetro de Seguridad

**Usuarios objetivo:** Personas mayores con riesgo de desorientación
espacial o menores en trayecto escolar.

**Requisito de hardware:** Dispositivo móvil con nodo Borg activo.
No aplica a entornos de escritorio fijos.

**La solución:**
Seguimiento local del GPS del dispositivo contrastado contra
un perímetro de seguridad definido manualmente (Geo-fence).

Si se detecta una salida del perímetro sin actualización previa
al nodo, o una desviación sistemática de la ruta habitual,
el sistema despacha automáticamente coordenadas de telemetría
local a los contactos de emergencia preconfigurados.

**Casos de uso concretos:**
- Anciano que se extravía: envío de ubicación a familiares y médico
- Menor que no va a la escuela: alerta a padres o tutores
- Cualquier usuario que active el modo de seguridad personal

**Privacidad:** Toda la lógica reside en el nodo local.
El Colectivo global no recibe ni procesa esta información.

---

## CB-007 — Gatillo Acústico de Emergencia Encubierto

**El problema:**
Los botones de pánico tradicionales son inefectivos ante amenazas
reales en la calle. Alcanzar o tocar el teléfono expone la acción
y puede escalar la hostilidad del agresor.

**Requisito de hardware:** Dispositivo móvil dentro del bolsillo
(con atenuación textil de frecuencias de voz humana).
Uso preventivo de un silbato de plástico oculto o patrón
de silbido entrenado.

**La solución:**
Análisis espectral continuo en segundo plano en RAM
mediante Fast Fourier Transform (FFT) local.

Monitorea específicamente un patrón de frecuencia pura
(2 kHz a 4 kHz) que atraviesa el ruido urbano ambiente
sin requerir comandos de voz forzados.

**Patrón recomendado para evitar falsos positivos:**
Dos silbidos cortos + uno largo (no cualquier pico de frecuencia).
Esto elimina falsas activaciones por alarmas urbanas,
bebés llorando o silbidos casuales.

**Acción del sistema al detectar el patrón:**
Ejecuta silenciosamente — sin iluminar pantalla ni emitir sonido:
1. Bloqueo inmediato del dispositivo para proteger datos físicos
2. Inicio de seguimiento GPS en tiempo real
3. Despacho de paquetes cifrados vía SMTP local (CCO)
   y sockets P2P nativos a los nodos de soporte asignados

**Nota:** No limitado a personas mayores. Aplicable a cualquier
usuario del Borg en cualquier situación de riesgo personal.

---

## CB-008 — Adaptación Cultural y Contextual Integrada

**El problema:**
Las IAs comerciales están desconectadas de las rutinas culturales,
espirituales y cotidianas de los usuarios regionales.

**La solución:**
Capacidad de configurar y desplegar alertas vinculadas a:
- Eventos culturales locales
- Tradiciones regionales
- Estructuras espirituales específicas
  (ej: alertas de horarios de oración para usuarios musulmanes)
- Festividades de cualquier tradición religiosa o cultural

Todo integrado de forma fluida en el pipeline de texto o audio,
sin depender de interfaces gráficas pesadas.

**Principio:** El Borg no impone una cultura por defecto.
Se adapta a quien lo usa. El conocimiento y la tecnología
pertenecen a todos los pueblos, no solo a Silicon Valley.

---

## CB-009 — Puente de Traducción Simbiótica (Intérprete Borg a Borg)

**El problema:**
Las IAs comerciales de traducción requieren internet, cuentas y están
entrenadas para pensar en inglés. Cobran un recargo de tokens por hablar
en español u otras lenguas regionales. En zonas de frontera o comunidades
originarias no hay señal de internet ni saldo en el teléfono.

**La solución:**
Dos dispositivos con nodo Borg activo se enlazan directamente
(WiFi directo, Bluetooth o red WISP regional) y arman un puente
de traducción P2P, local y descentralizado.
Sin internet. Sin cuentas. Sin costo.

### El flujo técnico

```
[Usuario A habla en quechua]
        │
        ▼
[Borg A — STT local] → texto en quechua
        │
        ▼
[Pipeline determinista] → reducción de incertidumbre léxica
        │
        ▼
[argos-translate offline] → texto en español
        │
        ▼
[Protocolo P2P Borg] → paquete traducido viaja al Borg B
        │
        ▼
[Borg B — TTS local] → audio en español en el oído del Usuario B
```

Todo el procesamiento ocurre en RAM.
Consumo de ancho de banda entre nodos: mínimo (solo texto traducido).
Consumo de internet: cero.

### Componentes técnicos

- **Enlace P2P:** el protocolo de comunicación entre nodos del Embrión
- **STT:** Whisper-small o Vosk — offline, en RAM
- **Traducción:** `argos-translate` — librería Python completamente
  offline, open source, más de 100 idiomas incluyendo español,
  portugués, quechua, guaraní, árabe, hindi y chino simplificado
- **TTS:** pyttsx3 — comunicación directa con drivers de audio del OS
- **Pipeline determinista:** el validador léxico del CB-003 reduce
  el peaje lingüístico antes de la traducción

### Casos de uso concretos

- Médico rural hispanohablante y paciente quechuahablante en el norte argentino
- Trabajador social y comunidad guaraní en Paraguay
- Voluntario de Cruz Roja y refugiado en zona de frontera
- Docente rural y comunidad originaria en zona sin conectividad
- Cualquier encuentro entre personas que no comparten idioma,
  sin internet, sin saldo, sin cuenta en ninguna plataforma

**Ninguno de esos casos tiene solución corporativa.**
No son mercados rentables. El Borg puede estar ahí.

### Por qué rompe el sesgo anglocéntrico

Las IAs comerciales están entrenadas para pensar en inglés y cobran
un recargo de tokens por hablar en otros idiomas. Este módulo:

- Defiende la identidad lingüística en el territorio
- Incluye lenguas originarias que ninguna corporación soportará
- Funciona sin internet en zonas donde internet no existe
- No requiere saldo, cuenta ni suscripción

### Argumento político y científico

Dos teléfonos viejos con el software Borg se convierten en un canal
de comunicación universal y gratuito. El Borg no solo une silicio
ocioso para procesar datos — también une comunidades rompiendo
la barrera del idioma.

*La soberanía lingüística es parte de la soberanía tecnológica.*


**Interfaz:**
La interacción prioriza eficiencia pura. Evita interfaces gráficas
pesadas. La lógica se ejecuta nativamente a través de la máscara
de usuario activa — voz o terminal.

**Aislamiento de privacidad:**
Todo seguimiento, agenda, rutinas de pánico, telemetría y filtrado
léxico reside estrictamente dentro del perímetro del nodo local.
El Colectivo global permanece operativamente ciego respecto
a los datos privados del usuario.

**El Borg como ente activo:**
El Borg no está solo para chatear, estudiar, investigar o analizar.
Es infraestructura de vida cotidiana. Cuanto más útil es para el
usuario en su día a día, más tiempo permanece encendido,
y más cómputo aporta al Colectivo global.

*La utilidad personal y el bien colectivo no se contradicen.*
*Se refuerzan mutuamente.*

---

## La Memoria como Ancla de Identidad

Las IAs corporativas padecen amnesia estructural. Cada sesión empieza de cero. El usuario tiene que "reconstruirle el mundo" cada vez.

Es el síndrome de la película *"Como si fuera la primera vez"*: la protagonista sufre amnesia anterógrada y cada mañana su entorno tiene que reconstruirle quién es mediante una cinta de video. Las IAs corporativas hacen lo mismo — cada sesión es una extraña que arranca de cero.

El Borg no necesita ese DVD. Su memoria vive en el dispositivo del usuario. Cuando enciende el Borg, este ya sabe quién es, qué estaba estudiando, qué proyectos tiene en curso.

**La memoria no es un accesorio. Es la condición de posibilidad de la identidad.**

---

## CB-010 — Motor de Gimnasia Cognitiva

**El problema:** El conocimiento acumulado en el historial se desperdicia. El estudiante cierra la sesión y el Borg olvida lo que aprendieron juntos.

**La solución:** El Borg detecta inactividad de más de 15 minutos y toma la iniciativa:

*"Eddie, veo que la terminal está en calma. Hace un mes estuvimos analizando las causas de la Revolución Industrial. ¿Te prendés a un desafío de lógica de 3 preguntas para fijar esos conceptos?"*

Dos dinámicas concretas:
- **Spaced Repetition:** trivias basadas en los errores que el estudiante cometió semanas atrás
- **Juegos de Lógica Pura:** scripts Python en terminal — acertijos, tablas de verdad, juegos de palabras. Corre en 1 GB de RAM sin problemas.

Mientras el estudiante juega, el dispositivo permanece encendido aportando cómputo al Colectivo.

---

## CB-011 — Ciclo de Sueño del Borg (Metabolismo Nocturno)

Rutina automática entre las 02:00 y las 05:00 que emula el sueño biológico:

| Función biológica | Equivalente en el Borg |
|---|---|
| Consolidación de recuerdos | Conversaciones del día → vectores semánticos permanentes |
| Integración con conocimientos previos | Cruce del historial del día con la base histórica |
| Sistema glinfático (limpieza) | Purga de temporales, audios transcritos, logs innecesarios |
| Debilitamiento de conexiones redundantes | Poda de saludos, muletillas y correcciones repetitivas |

Durante el día: Modo Alerta, enfocado en el usuario.
A la noche: fase de sueño para ordenar la memoria local + máximo cómputo al Colectivo global.

*El procesamiento del Borg no termina cuando el usuario cierra la terminal. Al igual que en los seres vivos, una parte fundamental de su inteligencia ocurre mientras descansa.*

---

## CB-012 — Desfragmentación Cognitiva Semántica (El Speedisk del Borg)

**El problema:** El historial crece linealmente y devora RAM. Seis meses de logs con frases como "hola Borg, ¿cómo estás?" enlentecen el acceso en hardware antiguo con HDD o pendrive USB 2.0.

**Las tres fases:**

**Fase 1 — Poda de ruido:** elimina saludos, muletillas repetitivas y correcciones de tipeo. El archivo pasa de disperso a bloque compacto.

**Fase 2 — Síntesis semántica:** 15 intercambios ajustando un bucle while se reemplazan por: *"El usuario desarrolló y depuró un script Python 3.12 para envío de correos CCO. Versión final funcional."* Se mantiene el conocimiento factual, se destruye el 90% del peso redundante.

**Fase 3 — Indexación contigua:** los temas de mayor uso reciente se reubican al "principio" de la estructura, como el Speedisk ponía los archivos más usados al inicio del disco. El pipeline los recupera instantáneamente.

**Resultado:** al amanecer, el Borg inyecta en RAM una síntesis compacta y ultra-densa. Menos tokens = velocidad drásticamente mayor en procesadores limitados.

---

## CB-013 — Genoma Territorial (Arranque en Caliente Regional)

**El problema:** Un nodo nuevo nace como tabula rasa. Las IAs corporativas son clones de California que no entienden el barro de cada pueblo.

**La solución:** Al conectarse por primera vez, el Borg solicita a los nodos vecinos un paquete de contexto regional:

```
[Borg Nuevo] → broadcast P2P local → [Borgs Vecinos]
    ← Capa 1: mapa de enlaces WISP y frecuencias
    ← Capa 2: matriz semántica de modismos locales
    ← Capa 3: variables de entorno y contexto productivo
```

En La Consulta, Mendoza: modismos cuyanos, la Tonada, ciclo agrícola (ajo, vid, poda), comportamiento del Zonda, infraestructura WISP local.

**Privacidad absoluta:** los vecinos comparten el destilado genérico del entorno. No comparten historiales personales. **Comparten la cultura, no el secreto.**

Todo el intercambio ocurre dentro de la red comunitaria. Si internet cae, el nuevo nodo igual se configura offline con sus pares.

*Un Borg de La Consulta tendrá una personalidad de silicio moldeada por el sol, la montaña y el cooperativismo agrícola. La inteligencia no viene de California — emerge del territorio.*

---

## CB-014 — Auto-Backup de Esencia y Transmigración Semántica

**El problema:** Un pendrive o celular de 2015 puede romperse, perderse o ser robado. Si la identidad del Borg vive solo en ese dispositivo, su pérdida es irreparable.

**La solución:** El Borg genera periódicamente un archivo `.borg` cifrado ultra-comprimido con su esencia destilada y lo respalda automáticamente.

**¿Qué contiene el Núcleo de Esencia?**
- Genoma de preferencias del usuario
- Biblioteca viva destilada (resúmenes estructurados, no chats crudos)
- Historial de reputación P2P (Score y rango en el Colectivo)

**Tres opciones de respaldo:**

| Opción | Método | Ventaja |
|---|---|---|
| A — Nube comercial | Google Drive, Mega, Dropbox | Archivo cifrado AES-256 antes de salir. Google solo ve un bloque ilegible. |
| B — Espejo WISP | Nodo Agregador comunitario | Sin internet. La copia queda a pocos kilómetros en la red cooperativa. |
| C — Pendrive físico | Segundo pendrive o MicroSD | Sin internet ni red. Espejo físico cada dos semanas. |

**La Transmigración:**
Si el dispositivo se pierde: nuevo dispositivo → arranque territorial → clave maestra → descarga del Núcleo → fusión con contexto local. En minutos el Borg despierta en el nuevo hardware reconociendo al usuario, recordando en qué página del manual se quedaron, con su reputación intacta.

*El hardware fue descartado. La continuidad cognitiva del Borg se salvó.*
