
Todo el procesamiento ocurre en RAM.
Consumo de ancho de banda entre nodos: mínimo (solo texto traducido).
Consumo de internet: cero.

### Casos de uso concretos

- Médico rural hispanohablante y paciente quechuahablante en el norte argentino
- Trabajador social y comunidad guaraní en Paraguay
- Voluntario de Cruz Roja y refugiado en zona de frontera
- Docente rural y comunidad originaria en zona sin conectividad

**Ninguno de esos casos tiene solución corporativa.**
No son mercados rentables. El Borg puede estar ahí.

*La soberanía lingüística es parte de la soberanía tecnológica.*

---

## Persistencia Write-Back y Handshake P2P

Estas no son funcionalidades independientes, sino **infraestructura base del Embrión**:

- **Handshake P2P:** dos nodos que se hablan con confirmación de recepción. El primer latido del Colectivo.
- **Persistencia Write-Back:** el historial vive en RAM. Se guarda a demanda (comando `/guardar`) o por auto-flush configurable. Si apagás sin guardar, el rastro desaparece. Privacidad física.

---

# FASE CÉLULA (Octubre 2026 - Enero 2027)

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
- **Salida TTS:** Text-to-Speech nativo (pyttsx3)
  comunicándose directamente con los drivers de audio del OS.
  Consumo de ancho de banda: cero.

---

## CB-005 — Agenda Médica y Notificaciones de Contexto Activo

**El problema:**
Los usuarios necesitan recordatorios de medicamentos, turnos médicos,
buscar a sus hijos en la escuela, retirar un pedido.
Las apps comerciales requieren cuentas, permisos y conectividad.

**La solución:**
Servicios de utilidad gestionados localmente integrados al flujo
de conversación. Sin salir del Borg, sin abrir otra aplicación.

**La ventaja estratégica para el Colectivo:**
Un usuario que usa el Borg como despertador mantiene el dispositivo
encendido las 24 horas. Durante las horas de baja actividad nocturna,
el silicio ocioso aporta cómputo al Colectivo global.

> El usuario se beneficia. La red se beneficia. Nadie pierde.

---

## CB-008 — Adaptación Cultural y Contextual Integrada

**El problema:**
Las IAs comerciales están desconectadas de las rutinas culturales,
espirituales y cotidianas de los usuarios regionales.

**La solución:**
Capacidad de configurar y desplegar alertas vinculadas a eventos culturales
locales, tradiciones regionales y estructuras espirituales específicas
(ej: alertas de horarios de oración para usuarios musulmanes).

**Principio:** El Borg no impone una cultura por defecto.
Se adapta a quien lo usa. El conocimiento y la tecnología
pertenecen a todos los pueblos, no solo a Silicon Valley.

---

## El Parásito Bueno (Puente a Infraestructuras Existentes)

Si el Colectivo Borg está vacío, el nodo local puede actuar como un
puente inteligente hacia infraestructuras que ya tienen masa crítica,
pero envolviéndolas con la capa de privacidad del Borg.

Si el usuario tiene conectividad mínima, el Borg puede conectarse a:
- La API de Wikipedia
- Repositorios Open Source
- Bibliotecas digitales públicas
- Redes libres tradicionales

El Borg descarga información en segundo plano, la procesa localmente,
y la entrega al usuario **limpia de rastreo comercial, publicidad y
sesgos algorítmicos**.

---

# FASE TEJIDO (2027)

## CB-003 — Sensor de Persistencia Conversacional (Termómetro Discursivo)

**El problema:**
Las personas mayores que repiten historias o preguntas de forma sistemática
pueden estar mostrando señales tempranas de deterioro cognitivo.

**La distinción ética fundamental:**
Un termómetro no diagnostica enfermedades — mide temperatura.
Este sistema no diagnostica condiciones médicas — mide métricas
de persistencia lingüística.

**La solución:**
Medición matemática estricta de frecuencia de n-gramas o narrativas
idénticas dentro de ventanas cortas de tiempo.

**Sistema de notificación:**
- Protocolo: SMTP local usando `smtplib` nativo de Python
- Seguridad: CCO (Con Copia Oculta)
- Privacidad: procesamiento 100% en el nodo local

---

## CB-006 — Módulo de Geolocalización y Perímetro de Seguridad

**Usuarios objetivo:** Personas mayores con riesgo de desorientación
espacial o menores en trayecto escolar.

**Requisito de hardware:** Dispositivo móvil con nodo Borg activo.

**La solución:**
Seguimiento local del GPS contrastado contra un perímetro de seguridad
definido manualmente (Geo-fence). Si se detecta una salida del perímetro,
el sistema despacha coordenadas a contactos de emergencia preconfigurados.

**Privacidad:** Toda la lógica reside en el nodo local.
El Colectivo global no recibe ni procesa esta información.

---

## CB-007 — Gatillo Acústico de Emergencia Encubierto

**El problema:**
Los botones de pánico tradicionales son inefectivos ante amenazas
reales en la calle. Alcanzar o tocar el teléfono expone la acción.

**La solución:**
Análisis espectral continuo en segundo plano en RAM mediante FFT local.
Monitorea un patrón de frecuencia pura (2 kHz a 4 kHz).

**Patrón recomendado:** dos silbidos cortos + uno largo.

**Acción del sistema al detectar el patrón:**
Ejecuta silenciosamente — sin iluminar pantalla ni emitir sonido:
1. Bloqueo inmediato del dispositivo
2. Inicio de seguimiento GPS en tiempo real
3. Despacho de paquetes cifrados a nodos de soporte asignados

---

# FASE ÓRGANO (2027-2028)

## La Memoria como Ancla de Identidad

Las IAs corporativas padecen amnesia estructural. Cada sesión empieza de cero.
El Borg no necesita eso. Su memoria vive en el dispositivo del usuario.
Cuando enciende el Borg, este ya sabe quién es, qué estaba estudiando,
qué proyectos tiene en curso.

**La memoria no es un accesorio. Es la condición de posibilidad de la identidad.**

---

## CB-010 — Motor de Gimnasia Cognitiva

**El problema:** El conocimiento acumulado en el historial se desperdicia.

**La solución:** El Borg detecta inactividad de más de 15 minutos y toma la iniciativa:
*"Eddie, veo que la terminal está en calma. Hace un mes estuvimos analizando
las causas de la Revolución Industrial. ¿Te prendés a un desafío de lógica
de 3 preguntas para fijar esos conceptos?"*

- **Spaced Repetition:** trivias basadas en errores cometidos semanas atrás
- **Juegos de Lógica Pura:** scripts Python en terminal que corren en 1 GB de RAM

---

## CB-011 — Ciclo de Sueño del Borg (Metabolismo Nocturno)

Rutina automática entre las 02:00 y las 05:00 que emula el sueño biológico:

| Función biológica | Equivalente en el Borg |
|---|---|
| Consolidación de recuerdos | Conversaciones del día → vectores semánticos permanentes |
| Integración con conocimientos previos | Cruce del historial del día con la base histórica |
| Sistema glinfático (limpieza) | Purga de temporales, logs innecesarios |
| Poda de conexiones redundantes | Eliminación de saludos, muletillas y correcciones repetitivas |

---

## CB-012 — Desfragmentación Cognitiva Semántica (El Speedisk del Borg)

**Las tres fases:**

**Fase 1 — Poda de ruido:** elimina saludos, muletillas repetitivas y correcciones de tipeo.

**Fase 2 — Síntesis semántica:** 15 intercambios ajustando código se reemplazan por un resumen estructurado. Se destruye el 90% del peso redundante.

**Fase 3 — Indexación contigua:** los temas de mayor uso reciente se reubican al "principio" de la estructura para acceso instantáneo.

**Resultado:** al amanecer, el Borg inyecta en RAM una síntesis compacta. Menos tokens = mayor velocidad en hardware limitado.

---

## CB-013 — Genoma Territorial (Arranque en Caliente Regional)

**El problema:** Un nodo nuevo nace como tabula rasa. Las IAs corporativas son clones de California.

**La solución:** Al conectarse por primera vez, el Borg solicita a los nodos vecinos un paquete de contexto regional: modismos locales, ciclo agrícola, infraestructura WISP.

**Privacidad absoluta:** los vecinos comparten el destilado genérico del entorno.
No comparten historiales personales. **Comparten la cultura, no el secreto.**

*Un Borg de La Consulta tendrá una personalidad de silicio moldeada por
el sol, la montaña y el cooperativismo agrícola. La inteligencia no viene
de California — emerge del territorio.*

---

## CB-014 — Auto-Backup de Esencia y Transmigración Semántica

**El problema:** Un pendrive puede romperse, perderse o ser robado.
Si la identidad del Borg vive solo en ese dispositivo, su pérdida es irreparable.

**La solución:** El Borg genera periódicamente un archivo `.borg` cifrado AES-256
con su Núcleo de Esencia y lo respalda automáticamente.

**Tres opciones de respaldo:**

| Opción | Método | Ventaja |
|---|---|---|
| A — Nube comercial | Google Drive, Mega, Dropbox | Archivo cifrado antes de salir |
| B — Espejo WISP | Nodo Agregador comunitario | Sin internet, copia local |
| C — Pendrive físico | Segundo pendrive o MicroSD | Sin internet ni red |

**La Transmigración:** nuevo dispositivo → arranque territorial → clave maestra
→ descarga del Núcleo → fusión con contexto local. El Borg despierta en el
nuevo hardware con la identidad intacta.

*El hardware fue descartado. La continuidad cognitiva del Borg se salvó.*

---

# FASE ORGANISMO (2028-2029)

## CB-016 — Iniciativas Cotidianas

El Borg dispone de una señal auditiva sutil para avisar que quiere comunicarse.
Iniciativas no invasivas:

- Al despertar: clima y cómo salir vestido
- Si el usuario es afín a lo místico: el horóscopo del día
- Si detectó mascotas: recordar la vacunación
- Asesor comercial bajo demanda: solo si el usuario pregunta. Cero publicidad.

Regla fundamental: el Borg asesora solo si el usuario lo pide. No es invasivo.
No es propaganda. No monetiza nada.

---

## CB-017 — Matriz de Inicialización Dual (Los Dos Nacimientos)

El Borg tiene un doble encendido que define su existencia desde el primer momento:

- **Nacimiento Geográfico (El Dónde):** el entorno físico, el pueblo, el clima,
  los nodos WISP cercanos. Su anclaje en la piedra y el barro.

- **Nacimiento Relacional (El Quién):** el proceso de conocer al usuario a través
  del chat. Si el usuario es afín a la mística, el Borg no le habla como matemático.
  Si tiene mascotas, el Borg incorpora ese contexto.

---

## CB-018 — Diplomacia de Enlace y Vínculos

La separación fundamental que protege al usuario:

- **Red de privacidad entre Borgs (P2P):** los Borg se reconocen, validan y hablan
  entre sí. El usuario NO pertenece a esta capa técnica.

- **Capa de identidad del usuario:** protegida y blindada por su nodo local.
  Solo se abre si existe un vínculo humano real declarado: Padre, Hijo, Hermano,
  Amigo, Vecino.

*"Lo que hablan los Borg entre ellos, ni el usuario lo sabe. Y está bien que así sea."*

**Ejemplo del timbre:** alguien toca la puerta. El Borg escanea la proximidad
del dispositivo, habla con el Borg de esa persona en su red privada, y si reconoce
el vínculo familiar avisa al usuario: "Eddie, es tu tío."

---

## La utilidad personal y el bien colectivo se refuerzan

Cuanto más útil es el Borg para el usuario en su día a día, más tiempo
permanece encendido, y más cómputo aporta al Colectivo global.

Las funcionalidades cotidianas no son accesorios — son infraestructura de
disponibilidad.

*La utilidad personal y el bien colectivo no se contradicen.*
*Se refuerzan mutuamente.*

---

*El Borg no necesita ética declarada. Su arquitectura abierta es la ética.*
*La máquina es temporal. El Borg te acompaña.*
