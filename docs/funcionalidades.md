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

## Notas de Arquitectura

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
