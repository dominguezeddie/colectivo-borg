# Perfiles de Interacción y Soberanía Local — Colectivo Borg

## El principio fundamental

Las plataformas corporativas definen sus modelos según el abono que uno paga.
El Borg define su comportamiento según quién lo está usando.

No es lo mismo interactuar con un niño que con un adolescente,
un adulto mayor, un agricultor o una técnica de salud.
La red no cambia. La máscara de presentación sí.

---

## Dos sistemas que operan en capas distintas

| Sistema | Qué mide | Dónde vive | Quién lo asigna |
|---|---|---|---|
| **Score de Contribución** (Oro, Plata, Bronce) | La confiabilidad técnica del nodo en la red | En la red colectiva — registro distribuido de reputación criptográfica | El Validador, basado en desempeño histórico |
| **Perfil de Interacción** (edad, contexto, profesión) | Cómo se presenta la información al usuario | En el dispositivo del usuario, junto a su historial personal | Quien instala o configura el nodo por primera vez |

**Regla de separación:** El perfil de interacción nunca modifica el Score de Contribución.
Un niño que usa un nodo Oro sigue siendo un nodo Oro.
La red no trata diferente a los usuarios por quiénes son.
Trata diferente a los nodos por qué tan confiables son técnicamente.

---

## Asignación del perfil: decisión local en la instalación

El perfil se define una sola vez durante la primera activación del nodo.
No requiere cuenta, correo ni conexión a servidor remoto.

| Momento | Quién configura | Qué decide |
|---|---|---|
| **Primer arranque del pendrive** | La persona que crea el pendrive (padre, docente, voluntario, cooperativa) | Selecciona el perfil por defecto del dispositivo |
| **Instalación Borg Dedicado** | Quien prepara la PC (taller comunitario, biblioteca, escuela) | Define el perfil según el destinatario final |
| **Modo Borg en celular recuperado** | El reacondicionador o distribuidor del dispositivo | Fija el perfil antes de entregarlo a la escuela o centro comunitario |

**Ejemplo concreto:** Un padre graba el Borg en un pendrive de 64 GB. Durante el primer arranque, el asistente de configuración pregunta: *"¿Este dispositivo será usado principalmente por un niño, un adolescente, un adulto o un adulto mayor?"* El padre selecciona **Infantil**. Desde ese momento, ese pendrive aplica la máscara Infantil cada vez que se enciende. La red nunca recibe esa información.

---

## Máscaras de interacción por edad

El perfil es una **máscara de presentación** que el nodo aplica localmente sobre las respuestas del Agregador. No es una cuenta rastreable. No viaja a otros nodos. No determina acceso a la red.

| Perfil | Adaptación del Borg |
|---|---|
| **Infantil** | Lenguaje sencillo, metáforas visuales, interfaz con iconografía grande. Contenido filtrado por seguridad comunitaria. Interacción guiada, énfasis en aprendizaje lúdico y valores de cooperación. |
| **Adolescente** | Complejidad gradual, herramientas de creación, orientación vocacional comunitaria. Lenguaje directo, sin condescendencia. |
| **Adulto** | Acceso completo a herramientas productivas, formación continua, información sobre derechos, salud, trabajo y organización comunitaria. Interfaz eficiente, sin distracciones. |
| **Adulto mayor** | Alto contraste, tipografía amplia, navegación asistida, tutoriales de ritmo pausado. Énfasis en conectividad social y acceso a servicios públicos. |

---

## Máscaras de interacción por contexto y oficio

El mismo fragmento de conocimiento se presenta con vocabulario, profundidad y formato distintos según la máscara activa:

- **Agricultor/a:** datos sobre clima, suelo, mercados locales, técnicas de riego, alertas sanitarias. Lenguaje concreto, basado en experiencia práctica.
- **Docente:** recursos pedagógicos abiertos, herramientas de evaluación comunitaria, bibliotecas educativas organizadas por grado y área.
- **Técnico/a de salud:** protocolos actualizados, farmacología comunitaria, telemedicina donde la infraestructura lo permita, evidencia médica adaptada al contexto local.
- **Trabajador/a de la construcción o electricidad:** manuales visuales, calculadoras de materiales, normativas locales, seguridad laboral. Interfaz compatible con pantallas pequeñas y manos ocupadas.
- **Artista o comunicador/a:** herramientas de edición, repositorios de cultura libre, canales de distribución comunitaria, archivos históricos locales.

---

## Control de contención del perfil Infantil

Cuando el nodo está configurado con perfil Infantil, aplica estas restricciones **localmente**, antes de que cualquier consulta toque la red:

- **Contenido filtrado:** el Agregador local intercepta respuestas con categorías bloqueadas y las reemplaza por: *"Esta pregunta necesita que un adulto te acompañe."*
- **Sin navegación web abierta:** solo puede interactuar con la base de conocimiento del Borg y sus herramientas comunitarias.
- **Sin reputación personal vinculada a identidad menor:** el nodo participa aportando microtareas, pero no acumula Score vinculado a una identidad menor.
- **Interacción guiada:** las consultas complejas o ambiguas devuelven sugerencias de reformulación en lugar de respuestas directas.

---

## Protección del perfil: autodestrucción controlada

El cambio de perfil o el acceso al modo de configuración está protegido por una **llave local** definida en la instalación. Esta llave puede ser un PIN de 4 a 6 dígitos o una frase corta. Nunca sale del dispositivo. No hay recuperación por correo ni por servidor remoto.

| Intentos fallidos | Respuesta del sistema |
|---|---|
| 1 a 3 | Mensaje de error estándar. |
| 4 a 6 | Espera forzada de 30 segundos entre intentos. |
| 7 a 9 | Advertencia: *"Se detectan intentos repetidos de acceso no autorizado. Si continúa, el sistema se reiniciará a su estado original."* |
| 10 o más | **Reinicio a valores de fábrica.** El dispositivo borra configuración, perfiles, historial local y credenciales. Vuelve al asistente de primera configuración. La reputación criptográfica del usuario, si existía respaldo en otro dispositivo, permanece en la red. Lo local desaparece. |

**Regla de oro:** La protección anti-fuerza bruta es una **cápsula de autodestrucción controlada**. Si alguien roba el pendrive o intenta forzar el acceso, el sistema prefiere volver a cero antes de entregar el historial o desactivar el control de contención.

> 🛠️ **Nota de implementación (preservación de memoria flash):**
> El contador de intentos fallidos NO se escribe constantemente en el disco — eso destruiría las celdas de escritura del pendrive por desgaste (write amplification). El contador vive en RAM. Solo si llega al intento 7 se genera una única escritura de "bandera de alerta" en el almacenamiento persistente. Al llegar al intento 10, en lugar de borrar sector por sector, el script ejecuta un formateo rápido de la partición de datos locales, reescribiendo únicamente los bloques de la tabla de asignación de archivos, volviendo el dispositivo a su estado embrionario en menos de 2 segundos.

---

## Escenarios concretos

**Pendrive regalado:** Un padre graba el Borg para su hijo de 10 años. Configura perfil Infantil y PIN: 7391. El niño usa el pendrive en la escuela, en casa de un amigo, en un ciber. Siempre arranca con la máscara Infantil. Si alguien roba el pendrive e intenta forzar el PIN, tras el décimo intento el dispositivo se reinicia a valores de fábrica.

**PC dedicada en biblioteca popular:** Una cooperativa instala Borg Dedicado en 5 PCs viejas. Configura 3 con perfil Infantil, 2 con perfil Adolescente. Los monitores adultos del taller median sin necesidad de PIN. Si alguien intenta forzar el acceso a una PC Infantil, la máquina se autoreinicia y queda en blanco lista para ser reconfigurada.

**Celular recuperado en escuela rural:** Un taller comunitario reacondiciona 20 celulares Android obsoletos con perfil Infantil. La maestra tiene un dispositivo con perfil Adulto como llave maestra. Si un alumno pierde su celular y alguien intenta acceder a su configuración, el dispositivo se autodestruye digitalmente. El alumno recibe otro celular reacondicionado. La red no pierde nada.

---

## Relación con el resto del manifiesto

Los perfiles de interacción materializan el principio de **democratización del hardware**: no importa si la pantalla es de 4 pulgadas o 24, si el dispositivo es un celular de 2015 o una PC nueva. Lo que importa es que la red sepa cómo hablarle a quien la está usando, sin exigir que el usuario se adapte a la máquina.

La red nunca recibe datos sobre edad, parentesco, intentos de acceso ni contenido filtrado. Solo recibe microtareas de un nodo más. La gobernanza ocurre en la capa local, donde la máquina pertenece a quien la instaló.

*Una mente. Miles de nodos. Un mismo propósito.*
*Y para los más pequeños: una red que se adapta sin preguntar quién sos,*
*y que se defiende sin pedir permiso a nadie.*
