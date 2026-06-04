**C.O.L.E.C.T.I.V.O.**

**B.O.R.G.**

*Benefit Optimization & Resource Grid*

Computación Operativa de Lazos Estratégicos para la

Construcción de Tecnología Integradora y Virtualmente Omnipresente

*"La máquina es temporal. El Borg te acompaña."*

**Documento de Visión y Arquitectura**

Autor: Raúl Edmundo (Eddie) Domínguez

La Consulta, Mendoza, Argentina

Versión: 7.0 (Embrión Completado — Junio 2026)


## **Índice**
1\. Origen del Proyecto

2\. Visión Filosófica

3\. Arquitectura: Los Tres Roles

4\. Tres Modalidades de Incorporación

5\. Separación entre el Borg y el Usuario

6\. Filosofía de Hardware

7\. Potencial de Impacto

8\. La Interfaz del Borg

9\. El OS Embebido

10\. Orden de Construcción

11\. Perfil del Autor

12\. Hoja de Ruta

13\. Presencia Pública y GitHub

14\. Contexto Externo

15\. Comunidad

16\. Perfiles de Interacción

17\. Persistencia a Demanda

18\. Funcionalidades (CB-001 a CB-019)

19\. La Memoria como Ancla de Identidad (CB-010 a CB-014)

20\. La Incorruptibilidad Estructural

21\. Instrucciones para Retomar Conversación

# **1. Origen del Proyecto**
El Colectivo Borg no nació de un laboratorio corporativo ni de un grupo de investigación universitaria. Se materializó en la mente de Raúl Edmundo Domínguez hace 20 días, como síntesis de 25 años de experiencia operando redes WISP en Mendoza, Argentina.

No fue casualidad. Fue acumulación. Décadas viendo cómo la infraestructura tecnológica corporativa ignora al 60% de la humanidad, combinadas con la intuición técnica de quien opera redes reales en condiciones reales, produjeron esta idea.

La necesidad es la madre de la inventiva. El Borg es la respuesta técnica a una necesidad social que las corporaciones no tienen incentivo para resolver.

# **2. Visión Filosófica**
## **2.1 El problema que el Borg resuelve**
Las IAs corporativas actuales (GPT, Gemini, Claude, etc.) tienen tres problemas estructurales que el Borg ataca directamente:

- Consumo energético obsceno: un data center de IA puede consumir tanta electricidad como una ciudad mediana.
- Concentración de poder: tres o cuatro corporaciones deciden quién accede y en qué condiciones.
- Exclusión del 60%: el 60% de la humanidad no puede pagar suscripciones en monedas fuertes, no tiene conectividad suficiente para servicios en la nube, o enfrenta barreras de idioma, cultura y acceso bancario.

## **2.2 Lo que el Borg NO es**
- No es competencia con las IAs corporativas.
- No es reciclaje de hardware viejo como objetivo.
- No es una corporación ni aspira a serlo.
- No pretende desplazar a nadie. El sol sale para todos.

## **2.3 Lo que el Borg SÍ es**
- Una red distribuida que ocupa el espacio que las corporaciones no quieren ocupar porque no es rentable para ellas.
- Infraestructura de IA accesible para una comunidad rural, una cooperativa, una escuela sin banda ancha estable.
- Un proyecto filosóficamente opuesto al monopolio: abierto, comunitario, sostenido por donaciones voluntarias.
- Ecológicamente honesto: usa ciclos de CPU que ahora mismo se desperdician en millones de máquinas encendidas sin hacer nada útil.

## **2.4 Modelo de sustentabilidad**
El proyecto se sostiene mediante donaciones y colaboraciones voluntarias, siguiendo el modelo de Wikipedia, Linux y VLC. La historia personal del autor — técnico universitario en microprocesadores, 25 años como operador de redes WISP en Mendoza — es la garantía más honesta de que esto no es un negocio disfrazado de proyecto social.
## **2.5 Filosofía de privacidad**
El Borg separa tres conceptos que los sistemas corporativos mezclan deliberadamente:

- Computación distribuida: repartir trabajo. Todos participan según sus posibilidades.
- Conocimiento colectivo: lo que el usuario decide compartir voluntariamente enriquece a todos.
- Datos privados: nunca salen del dispositivo del usuario sin su consentimiento explícito.

La computación se comparte. El conocimiento puede compartirse. La privacidad pertenece a la persona.

# **3. Arquitectura: Los Tres Roles de la Célula Madre**
Cada nodo del Borg puede asumir uno o más de tres roles, asignados dinámicamente según las capacidades del hardware:

|**Rol**|**Apodo**|**Función principal**|**Hardware ideal**|
| :- | :- | :- | :- |
|El Validador|El Auditor|Motor de gobernanza y confianza. Verifica integridad de datos mediante re-ejecución parcial o verificaciones matemáticas. Sus informes alimentan el algoritmo de Score de Contribución.|Alta latencia de red — auditorías asíncronas en segundo plano.|
|El Agregador|El Sintetizador|Inteligencia logística y síntesis. Gestiona la complejidad de reconstruir la solución final ensamblando resultados parciales. Maneja nodos rezagados con lógica de failover instantáneo.|Alta RAM / CPU limitada — optimización logística para síntesis de fragmentos.|
|El Ejecutor|El Músculo|Unidad de cómputo atómica. Realiza carga de trabajo intensiva: inferencia de IA y transformaciones de datos. Arquitectura agnóstica al estado.|Alta capacidad CPU — maximización de fuerza bruta para inferencias pesadas.|

## **3.1 Sistema de Rangos (Score de Contribución)**

|**Rango**|**Perfil**|**Beneficio**|
| :- | :- | :- |
|Oro|Precisión constante y alta disponibilidad.|Prioridad en microtareas críticas.|
|Plata|Desempeño estable con desviaciones mínimas.|Participación estándar en el flujo de fragmentos.|
|Bronce|Nodos nuevos o con inconsistencias.|Sujeto a auditorías y validaciones frecuentes.|

## **3.2 La Microtarea: El Átomo de Resiliencia**
- Unidades de trabajo de 1 a 30 segundos.
- Sistema inmune a desconexiones: si un nodo cae, la microtarea se reasigna en segundos, no horas.
- Ejemplo concreto: 10 transcripciones de audio de 10 segundos cada una para entregar un texto completo de un minuto.
## **3.3 Pipeline de procesamiento lingüístico**
El Borg aplica una filosofía de procesamiento por capas con reducción progresiva de incertidumbre, similar a cómo un compilador trabaja por etapas:

- Nivel 1 — Análisis léxico (Ejecutor de baja capacidad): verificar si cada elemento de una oración existe en el conjunto conocido del idioma. Palabra no encontrada no es palabra incorrecta — es pendiente de clasificación.
- Nivel 2 — Análisis sintáctico (Ejecutor de capacidad media): analizar la estructura gramatical de los elementos ya verificados.
- Nivel 3 — Inferencia probabilística (Ejecutor de alta capacidad o Agregador): aplicar semántica y contexto sobre el terreno ya limpio y verificado.

Resolver primero todo aquello que puede resolverse mediante reglas deterministas y dejar las probabilidades para los aspectos realmente ambiguos. Esto también reduce el peaje lingüístico del español: menos incertidumbre inicial significa menos tokens necesarios para llegar a la misma certeza.

# **4. Tres Modalidades de Incorporación al Colectivo**
No son tres versiones del sistema. Son tres puertas de entrada al mismo sistema, según qué hardware y situación tenga la persona. No son excluyentes — son complementarias.

|**Modalidad**|**Descripción**|**Dueño principal del equipo**|
| :- | :- | :- |
|Borg Portable (Pendrive)|Se ejecuta desde un pendrive. No modifica la computadora anfitriona. Puede utilizar RootFS on RAM. El usuario transporta su identidad, historial y configuración. Ideal para cibercafés, escuelas y laboratorios.|El usuario|
|Borg Instalado|Instalación sobre Windows, Linux o Android. Funciona en segundo plano como un antivirus o servicio del sistema. Aprovecha recursos ociosos cuando el usuario no los necesita. La experiencia es transparente para el usuario.|El usuario|
|Borg Dedicado|Computadoras antiguas reutilizadas exclusivamente para el Colectivo. El disco completo queda disponible para el Borg. No existe escritorio tradicional ni aplicaciones de uso general. El equipo se transforma en un nodo permanente de la red.|El Colectivo|

Un celular puede aportar unos minutos de cómputo. Una notebook puede aportar horas. Una PC antigua puede convertirse en un nodo permanente. Todos participan según sus posibilidades.
## **4.1 Reciclaje funcional, no solo ecológico**
Una PC vieja que no levanta Windows 10, que se traba con Chrome, que tarda cinco minutos en arrancar, no tiene otro uso que esté compitiendo con el Borg. La PC estaba condenada a ser un pisapapeles electrónico y el Borg le da un propósito concreto.

El Borg no le pide a esa PC que corra un modelo de lenguaje grande. Le pide que sume números, que transcriba un fragmento de audio de 10 segundos, que clasifique una imagen. Tareas atómicas que una PC con 1 GB de RAM y un Celeron de hace una década puede hacer sin problemas.

La gente no enciende una PC vieja para salvar el planeta — la enciende porque le sirve para algo. El Borg le da ese algo concreto. Eso es reciclaje funcional: darle a una máquina obsoleta una tarea a la medida de sus capacidades actuales.
## **4.2 El nodo itinerante: el caso central**
El nodo itinerante no es un caso borde del diseño. Es el caso central. Un nodo puede estar hoy en un ciber de Mendoza, mañana en una biblioteca de San Juan, pasado en la casa de un amigo con WiFi distinto. Su IP cambia, su latencia cambia, su conectividad cambia.

- Identidad por clave criptográfica RSA (mínimo 2048 bits) firmada digitalmente, no por IP ni por máquina. Esto desliga por completo la reputación del hardware físico y de la IP, permitiendo la itinerancia real por cualquier nodo del Colectivo.
- La reputación viaja con el nodo. Si en Mendoza acumuló score Oro, en San Juan sigue siendo Oro.
- Anuncio activo al reconectar: el nodo dice 'soy yo, estoy acá, ¿hay tareas?' en lugar de esperar ser descubierto.
- Failover natural: si se desenchufa a mitad de una microtarea, el Agregador reasigna en segundos.

En la literatura técnica esto se llama disconnection-first design. El Borg asume desconexión como norma y trata la estabilidad como bonus.

# **5. Separación entre el Borg y el Usuario**
Son dos entidades distintas con roles distintos:

|**Entidad**|**Qué aporta**|**Qué contiene**|
| :- | :- | :- |
|El Borg (la máquina)|Capacidad computacional al Colectivo.|CPU, RAM, conectividad, disponibilidad.|
|El Usuario (la persona)|Identidad al Colectivo.|Reputación, historial, configuración, claves criptográficas.|

Los Borg aportan capacidad. Las personas aportan identidad.

La reputación pertenece a la persona, no al hardware. Si una computadora muere, el usuario no pierde su historial, su score de contribución, sus rangos ni su identidad dentro del Colectivo.
## **5.1 El Borg como biblioteca personal viva**
El historial del usuario no es solamente un registro de conversaciones. Es su patrimonio digital acumulado. Una memoria persistente que incluye:

- Conversaciones e interacciones con el Colectivo.
- Archivos adjuntos: PDFs, imágenes, manuales, diseños.
- Proyectos y documentación técnica.
- Notas, ideas y conocimiento generado.
- Configuraciones y preferencias acumuladas.

Lo que el Borg evita es algo que hoy ocurre frecuentemente: el usuario cambia de equipo, pierde archivos, pierde conversaciones, pierde contexto, y vuelve a empezar. En el Borg, los dispositivos pueden cambiar. La memoria del usuario permanece.
## **5.2 Diferencia con ChatGPT, Gemini o Claude**
Hoy en las IAs corporativas ocurre esto:

- Usuario sube un PDF.
- Se usa durante la conversación.
- Fin. El archivo no forma parte de una memoria reutilizable.

En el Borg ocurre esto:

- Usuario adjunta un PDF.
- El PDF pasa a formar parte de su historial permanente.
- El Borg puede volver a consultarlo en cualquier sesión futura.
- El usuario conserva ese conocimiento en cualquier dispositivo donde conecte su pendrive.

La imagen correcta no es una IA con memoria. Es una biblioteca viva. Cada interacción agrega algo al patrimonio digital del usuario.

|**Capa**|**Qué contiene**|**Quién decide**|
| :- | :- | :- |
|Memoria personal|Conversaciones, archivos, proyectos, imágenes, manuales, diseños, ideas.|Solo el usuario. Nunca sale del dispositivo sin consentimiento explícito.|
|Reputación e identidad|Score, rangos, claves criptográficas, historial de contribución.|El usuario, validado por el Colectivo.|
|Conocimiento colectivo|Lo que el usuario decide compartir voluntariamente: tutoriales, documentación pública, proyectos abiertos.|El usuario elige qué entra. Nada es automático.|

## **5.3 El pendrive como cápsula de memoria personal**
El pendrive deja de ser solamente la llave de encendido. Es también la cápsula de memoria personal. Contiene:

- Historial personal y conversaciones.
- Configuración del nodo y preferencias del usuario.
- Reputación criptográfica y claves de identidad.
- Cachés de conocimiento local y modelos especializados.
- Trabajos pendientes.

La computadora se vuelve un recurso temporal. El pendrive contiene la continuidad.

Hoy la mayoría de las personas dependen de 'mi computadora'. En el Borg la lógica cambia a 'mi identidad viaja conmigo'.
## **5.4 RootFS on RAM**
Combinado con el concepto de RootFS on RAM, el pendrive alcanza su máximo potencial: el sistema operativo se carga completamente en memoria RAM, la computadora anfitriona prácticamente no se modifica, y al apagar la RAM se limpia y el disco local queda intacto. Lo único persistente es el pendrive.

Por eso el pendrive actúa como llave de encendido, identidad digital, memoria histórica y nodo portátil del Colectivo, todo en uno.
## **5.5 Dónde vive el historial**
El historial vive donde vive el Borg — no en la nube, no en un servidor corporativo, no en una cuenta que alguien puede cancelar:

- Borg Portable: todo en el pendrive.
- Borg Instalado: todo en una carpeta local del sistema operativo anfitrión.
- Borg Dedicado: todo en el disco, que pertenece completamente al Colectivo.

Nadie puede borrar el historial del usuario excepto el usuario mismo.
## **5.6 Historial híbrido: privado por defecto, compartido por elección**
- Privado: conversaciones personales, documentos privados, claves. Nunca salen del dispositivo.
- Compartido voluntariamente: conocimiento técnico, manuales, tutoriales, documentación. El usuario decide compartirlo y pasa a formar parte del conocimiento colectivo.
- Metadatos mínimos: el Colectivo conserva únicamente identidad, reputación, score y configuración básica. No conserva conversaciones completas.
## **5.7 Escenarios de uso**
Escenario 1 — Pendrive personal: el usuario llega a cualquier computadora, conecta el pendrive, se autentica, y aparecen automáticamente su historial, proyectos, reputación y configuración. La computadora es irrelevante.

Escenario 2 — Pendrive perdido: si la identidad estuviera únicamente en el pendrive, perderlo sería un problema. Por eso existe autenticación por usuario y recuperación distribuida. El pendrive es una llave conveniente, no el único lugar donde existe la identidad.

Escenario 3 — Escuela o biblioteca: 30 computadoras ejecutan Borg. Cada alumno inicia sesión con sus credenciales. El mismo hardware sirve a Juan, María, Pedro y Ana — cada uno ve su historial y su reputación.

Escenario 4 — Borg comunitario: un centro comunitario tiene un único Borg potente con decenas de usuarios. La máquina aporta recursos al Colectivo. Las identidades siguen siendo individuales.

# **6. Filosofía de Hardware**
## **6.1 No es reciclaje — es universalidad**
El Borg no discrimina por antigüedad, marca ni capacidad. Una PC nueva de última generación y un celular de 2015 son ambos nodos válidos. Cada uno contribuye según lo que tiene.
## **6.2 Definición de hardware antiguo en el contexto del Borg**
El hardware antiguo al que refiere el Borg es aquel que puede correr Windows 7, no una CPU 486 ni un Pentium de los años 90. Hardware fabricado aproximadamente entre 2007 y 2015, con arquitectura x86 de 32 o 64 bits, completamente capaz de correr Python 3.x y participar como nodo activo.
## **6.3 Requisitos mínimos reales**
- CPU capaz de correr Windows 7 o superior (aproximadamente 2007 en adelante).
- Capaz de correr Python.
- Conexión a internet (WiFi, datos móviles, ethernet).
- Algún recurso para ofrecer: CPU, RAM, o disponibilidad.

## **6.4 La evolución del cómputo: 15 años de avance**

|**Período**|**Potencia aprox.**|**Ejemplos**|**Lo que puede hacer para el Borg**|
| :- | :- | :- | :- |
|2010-2011 (15 años atrás)|50-100 GFLOPS|Intel Core i7-2600K, AMD Phenom II, Intel Core 2 Duo|Microtareas simples: clasificación, cálculo, texto liviano.|
|2015-2016 (10 años atrás)|150-300 GFLOPS|Intel Core i7-6700K, AMD FX-8350, Apple A9|Transcripción de audio corto, modelos tiny locales.|
|2020-2021 (5 años atrás)|~1 TFLOP|AMD Ryzen 9 5900X, Intel Core i9, Apple M1|Inferencia local, modelos pequeños, agregación.|
|2025-2026 (hoy)|1-5 TFLOPS CPU / 100+ GPU|AMD Ryzen 9 9950X, Intel Core Ultra 9, Apple M4|Nodo Agregador o Validador de alta capacidad.|

► INSERTAR AQUÍ: Infografía 'La Evolución del Cómputo: 15 Años de Avance'

Dato clave: un smartphone premium actual supera a supercomputadoras de los años 90. Esas supercomputadoras fueron suficientes para llevar al hombre a la Luna. Un celular de 2015 puede ser una neurona del Colectivo.
## **6.5 La escala compensa la eficiencia individual**
Una neurona biológica es ineficiente comparada con un chip moderno. Pero 86 mil millones de neuronas juntas producen algo que ningún chip puede replicar. Un nodo lento en el Borg no es un problema — es una neurona más. El sistema no depende de que cada nodo sea potente. Depende de que haya muchos nodos.
## **6.6 Analogía Star Trek**
El Borg de Star Trek no asimilaba solo tecnología nueva ni solo tecnología antigua. Asimilaba todo lo que encontraba. La colectividad era más fuerte por la diversidad, no a pesar de ella.

# **7. Potencial de Impacto**
## **7.1 La brecha que el Borg llena**
Las IAs corporativas no van a construir infraestructura para una comunidad rural de 500 personas, para una cooperativa, o para una escuela sin banda ancha estable. No les cierra el negocio. El Borg sí puede estar ahí, porque está diseñado exactamente para ese entorno.
## **7.2 Data Center Planetario**
Con dispositivos mixtos de 2010-2025, estimando conservadoramente 50-200 GFLOPS por nodo en promedio, 20 millones de nodos representarían entre 1 y 4 ExaFLOPS de poder de cómputo distribuido. No hay un edificio. No hay un país. El planeta entero es el data center.

La diferencia con un cluster de GPUs corporativo no es solo técnica — es filosófica. El Borg no compite en el mismo juego. Juega uno diferente donde tiene ventaja: sin consumo adicional de energía, sin infraestructura centralizada, sin control corporativo.
## **7.3 Precedentes históricos**
- SETI@home (1999): millones de PCs ociosas analizando señales de radio del espacio.
- Folding@home: cómputo distribuido para investigación de proteínas.
- Linux: un desarrollador sin recursos creó el sistema que hoy corre el 90% de internet.
- Wikipedia: el conocimiento no debía tener dueño.

Ninguno era corporación. Ninguno tenía data center. El Borg tiene la misma lógica, aplicada a IA distribuida con filosofía social.

# **8. La Interfaz del Borg: Terminal con Propósito**
El Borg tiene su propia interfaz, comparable en función a Gemini, ChatGPT o Claude — pero radicalmente distinta en filosofía y tecnología. No es una aplicación web que depende de servidores corporativos. Es una interfaz que vive en el dispositivo del usuario.
## **8.1 Las tres opciones de interfaz**
- Opción A — Chat como panel de control: el usuario escribe órdenes (procesá este audio, resumí este texto) y el Borg distribuye y devuelve. Interfaz tradicional de usuario.
- Opción B — Chat como voz de la red: la pantalla muestra el metabolismo del Borg en tiempo real. El usuario no ordena — observa. La máquina trabaja sola.
- Opción C — Ambas: modo operador y modo monitor. Se cambia con una tecla.

Para una PC dedicada en una escuela rural o cooperativa, la Opción B es la más coherente. La máquina no espera que alguien la use — ella trabaja y muestra lo que hace.
## **8.2 El Terminal Borg**
Al estilo de los sistemas Linux de propósito específico (como Coyote Linux), la interfaz de bienvenida del Borg Dedicado muestra en tiempo real:

- Nodos activos y países conectados.
- Capacidad total de FLOPS de la red.
- Distribución de carga: cómputo, análisis, sincronía, seguridad, expansión.
- Estado de la red: estabilidad, integridad, amenazas.
- Rol asignado al nodo actual según capacidades del anfitrión.

► INSERTAR AQUÍ: Imagen de referencia del Terminal Borg (interfaz estilo terminal verde sobre negro)

Frase central de la interfaz: 'UNA MENTE. MILES DE NODOS. UN MISMO PROPÓSITO.'

Esta interfaz se construye en Python con la librería curses — texto en terminal, sin escritorio, sin gráficos pesados. Exactamente lo que necesita el Borg Dedicado cuando arranca en una PC vieja.

# **9. El OS Embebido: Firmware con Propósito**
El Borg es un firmware, no un programa. No se instala sobre Windows. Se instala en lugar de Windows. Una PC vieja deja de ser una PC lenta y se convierte en un órgano de una red inteligente.

Con el background en microprocesadores y WISP del autor, esto no es una abstracción — es exactamente lo que hace un CPE, un router OpenWrt, un cajero automático. Prendés y hace una sola cosa.
## **Cómo se construye sin escribir un OS desde cero**
- Linux minimal (Alpine, Debian sin X11).
- Sin gestor de escritorio (no Gnome, no KDE, no nada).
- Un solo programa que arranca automáticamente al bootear: el Terminal Borg.
- Modo kiosk: interfaz textual con curses o navegador en pantalla completa sin barra de direcciones.

El resultado: prendés la PC vieja y en 15-20 segundos está el Terminal Borg. Sin Windows, sin íconos, sin actualizaciones. Es trabajo de empaquetado, no de ingeniería de kernels.

# **10. Orden de Construcción: Capas, no Productos**

|**Capa**|**Qué es**|**Complejidad**|**Cuándo**|
| :- | :- | :- | :- |
|Núcleo|El protocolo Borg: nodos, microtareas, reputación, failover. Solo línea de comando.|Media-Alta|Ahora. Esto es el proyecto.|
|App / Dashboard|Envoltorio que muestra lo que el núcleo ya hace. El nodo debe funcionar 24/7 sin que nadie abra la app.|Media|Cuando el núcleo funcione. Es opcional.|
|OS embebido|Distro derivada que bootea directo al Borg. No escribir un OS — adaptar Alpine o Debian minimal.|Alta|Al final. Milestone Organismo.|

Regla de oro: el núcleo debe funcionar sin app y sin OS propio. La comunidad de software libre no se engancha con la visión completa. Se engancha con un componente que funciona.

# **11. Perfil del Autor**

|**Atributo**|**Detalle**|
| :- | :- |
|Nombre completo|Raúl Edmundo Domínguez|
|Apodo|Eddie (por Edmundo)|
|Ubicación|La Consulta, Mendoza, Argentina|
|Edad|58 años|
|Formación|Técnico Universitario en Microprocesadores|
|Experiencia|25 años como operador de redes WISP|
|Motivación|Beneficio social, no lucro corporativo|
|Sustentabilidad|Donaciones voluntarias — modelo Wikipedia / Linux|
|Día 1 del proyecto|Mayo 2026|
|Estado actual|Python 3.12.7. CS50P completado. Módulos base de la Célula operacionalizados: nodo.py (identidad RSA), descubrimiento.py (LAN/Gossip), persistencia.py (Write-Back atómico). El Embrión ya camina.|

La experiencia de 25 años operando redes WISP es el activo más valioso del proyecto. No es teoría académica — es conocimiento de cómo se comporta la red en la realidad, con latencia variable, nodos que caen, hardware heterogéneo y usuarios reales en condiciones reales.

**➤ Próximo hito: Célula (Octubre 2026 — Enero 2027) — Tres nodos con failover de 2 segundos.**

# **12. Hoja de Ruta por Milestones**
El Borg crece como un ser vivo, no como un producto que se lanza.

|**Milestone**|**Período estimado**|**Objetivo**|**Semilla técnica**|
| :- | :- | :- | :- |
|Embrión|Mayo - Junio 2026 ✓ COMPLETADO|Núcleo de arquitectura implementado en Python 3.12 con OOP tipada: identidad criptográfica RSA descentralizada (nodo.py), protocolo de descubrimiento híbrido LAN/Gossip (descubrimiento.py), y motor de Persistencia Resiliente Write-Back con guardado atómico (persistencia.py). Dos nodos comunicándose con confirmación de recepción y tolerancia a fallos verificada.|CS50P completo. Python básico a intermedio.|
|Consolidación|Julio - Septiembre 2026|Fase de pruebas unitarias de laboratorio: simulación de estrés de persistencia bajo cortes eléctricos simulados, inyección de fallos en el protocolo Gossip, estabilización del cifrado RSA en entornos de prueba local. El Embrión se endurece antes de escalar a Célula. Sin esta etapa no hay base sólida sobre la que construir el failover de 2 segundos.|pytest. Pruebas de estrés y fallos controlados. Documentación técnica del Embrión.|
|Célula|Octubre 2026 - Enero 2027|Tres nodos comunicándose. Roles diferenciados. Failover básico: si un nodo cae, la tarea se reasigna.|Clases y objetos. Primer protocolo de mensajes.|
|Tejido|2027|Reputación funcionando. Microtareas reales distribuidas. Maduración: primera tarea concreta útil en hardware real (transcripción, clasificación, resumen) antes de pasar a portabilidad.|Sistema de rangos. Score de Contribución funcional.|
|Órgano|2027-2028|Pendrive booteable con identidad criptográfica. La reputación viaja con el nodo. GitHub público. Primeros colaboradores externos.|Live USB persistente. Clave criptográfica por nodo.|
|Organismo|2028-2029|Red pública. OS embebido. Terminal Borg. Comunidad activa. El Borg trabaja sin que nadie lo mire.|Distro Linux derivada. Interfaz de desaparición.|

## **CS50P como construcción del Embrión**
- Semanas 3-4 (funciones y condicionales): función que decide si un nodo puede aceptar una tarea. Semilla del Validador.
- Semanas 5-6 (diccionarios y listas): estructura que guarda el estado de 5 nodos con su score, hardware y última conexión. Semilla del Sistema de Rangos.
- Semanas 7-8 (clases y objetos): modelo de un nodo con identidad, capacidad y cola de tareas. Semilla del Ejecutor.

# **13. Presencia Pública y GitHub**
Repositorio técnico: ahora. Difusión pública: cuando el Embrión respire.
## **Estructura mínima del repositorio**
- README.md — Declaración de intenciones, diagrama de los 3 roles, filosofía, roadmap.
- docs/arquitectura.md — Los 3 roles, microtareas, reputación.
- docs/filosofia.md — Por qué existe: ecología, acceso, anti-monopolio.
- docs/hardware.md — Qué dispositivos pueden ser nodos.
- media/diagrama\_roles.png — Los Tres Roles de la Célula Madre.
- LICENSE — AGPL v3.

Nombre del repositorio: colectivo-borg. Subtítulo en inglés en el README: 'Distributed AI collective for the 60% left behind'.

Licencia recomendada: AGPL v3 — esto es de todos, pero no de nadie en particular para que lo cierre.

# **14. Contexto Externo: El Mundo Confirma el Problema**
## **14.1 El peaje lingüístico — IA gratis se acaba para hispanohablantes**
El video 'Se acabó la IA gratis, sobre todo para hispanohablantes' (YouTube 2026) describe con precisión el problema que el Borg resuelve — sin saber que el Borg existe.

- Las IAs corporativas se están quedando sin capacidad de cómputo. El acceso gratuito está siendo racionado.
- OpenAI pierde 14.000 millones de dólares al año. La generosidad actual es táctica, no estructural.
- El español genera un 59% más de tokens que el inglés para expresar exactamente la misma idea. Cuando hay escasez, los hispanohablantes lo notan primero.
- Quien más paga recibe más inteligencia. Es el mismo bucle que amplificó la desigualdad en todos los mercados de la historia.

Referencia: https://www.youtube.com/watch?v=ZsKszAkq0jI

## **14.2 Marc Vidal: la encíclica del Papa y el tecnofeudalismo**
El analista económico Marc Vidal analizó la reunión del Papa León XIV con Anthropic y la encíclica 'Magnífica Humanitas' (mayo 2026), dedicada íntegramente a regular la IA. Su análisis llega exactamente a la misma conclusión que el Borg, pero desde la economía:

'El debate real debe ser político y estructural, enfocado en evitar que unas pocas corporaciones retengan la propiedad absoluta de estas infraestructuras cognitivas.'

Vidal identifica tres problemas estructurales que el Borg resuelve por diseño:

- El tecnofeudalismo: el valor ya no se genera entre capital y trabajo, sino entre plataforma y usuario. El Borg rompe esa relación — no hay plataforma que extraiga valor. El valor queda en la red distribuida.
- La palanca material perdida: en 1891 el obrero tenía su cuerpo como palanca de negociación. Hoy esa palanca desapareció. El Borg crea una nueva palanca: millones de dispositivos que aportan cómputo sin depender de ninguna corporación.
- La autolimitación voluntaria no funciona: el Papa invita al constructor de la máquina a escuchar la declaración moral. Eso es operativamente débil. Las corporaciones tecnológicas pueden ignorar la petición sin sufrir costes operativos. El Borg no pide permiso ni autolimitación — construye la alternativa.

Referencia: https://www.youtube.com/watch?v=\_U6XRBOW13E

## **14.3 La IA corporativa como herramienta de manipulación**
La IA en manos de corporaciones puede ser manipulada para el provecho de las mismas sin cuestiones éticas ni morales. No es especulación — ya está ocurriendo:

- En la información: los modelos se entrenan con datos que reflejan los sesgos de quienes los construyen. Una IA corporativa no tiene incentivo para cuestionar el modelo económico de su dueño.
- En el acceso: el racionamiento por capacidad de pago ya existe. Quien accede al modelo más potente toma mejores decisiones. La IA amplifica la desigualdad existente en lugar de reducirla.
- En la dependencia cognitiva: cuanto más usa la gente una IA corporativa, más datos genera para mejorarla, más dependiente se vuelve, y menos probable es que busque alternativas.
- En la narrativa: las corporaciones controlan qué temas el modelo trata con cuidado, cuáles evita, y cómo presenta ciertos temas. Eso no es neutralidad — es una posición disfrazada de objetividad.

No necesitan ser maliciosas para ser peligrosas. Basta con que optimicen para sus propios intereses — que es exactamente lo que cualquier corporación hace por definición.

# **15. Comunidad: Más Allá del Código**
El Colectivo Borg no es solo un proyecto de software. Es una infraestructura social y comunitaria permanente. Si el Borg se quedara solo en el nicho de quienes saben programar o configurar antenas, se perdería al otro 90% de la comunidad que comparte la convicción, pero cuya trinchera es otra.
## **15.1 Los Tres Canales de Contribución Humana**
Al igual que las máquinas tienen tres roles — Ejecutor, Agregador, Validador — las personas también pueden contribuir desde tres canales distintos. No hace falta saber programar para ser parte del Colectivo.

|**Canal**|**Perfil**|**Contribución concreta**|
| :- | :- | :- |
|💪 El Músculo Técnico|Programadores, técnicos WISP, reparadores de hardware.|Código, nodos semilla en el territorio, recuperación de PCs viejas para donar a escuelas y centros comunitarios.|
|💰 El Combustible Económico|Personas que no saben programar pero entienden que los monopolios de IA son peligrosos.|Donaciones voluntarias — desde un café por mes hasta aportes de cooperativas. Va directo a hardware comunitario y pendrives para escuelas rurales.|
|🌍 El Sostén Territorial|Docentes rurales, trabajadores sociales, traductores regionales, militantes comunitarios.|Prueba el sistema en el campo, expande vocabularios locales, audita que las respuestas del Borg sean útiles para el 60% dejado atrás.|

"Yo no entiendo de código, pero este mes aporté el equivalente a dos litros de nafta para que el nodo Borg de la biblioteca popular siga encendido."

Eso es soberanía tecnológica comunitaria. No el 60% como beneficiario — el 60% como constructor.
## **15.2 Nodos Faro**
Un Nodo Faro es un nodo permanente, estable y público sostenido por la comunidad — no por un individuo. Puede vivir en una biblioteca popular, una escuela rural, una cooperativa eléctrica, una asociación vecinal o una universidad pública. Son la columna vertebral territorial del Colectivo.
## **15.3 Hoja de Ruta Institucional**
- Embrión (hoy): transparencia individual. GitHub Sponsors / Cafecito. El dinero que entra se transforma en hardware público visible.
- Tejido (mediano plazo): cooperativismo de hecho. Alianzas con WISPs locales, universidades y cooperativas que ya tienen personería jurídica.
- Órgano (largo plazo): Fundación Colectivo Borg formal. Para ese momento no será una cáscara vacía buscando fondos — será el reflejo legal de una comunidad que ya opera.
## **15.4 Por qué el modelo Fundación es el correcto**
- Blindaje contra compra corporativa: con estatuto de bien público y licencia AGPL v3, ninguna multinacional puede comprar el Borg y cerrarlo. La fundación no se vende.
- Transparencia de caja radical: como Wikipedia, cada peso que ingresa se expone públicamente. La confianza no se pide — se computa.
- Poder de negociación institucional: como Fundación Colectivo Borg, el proyecto se planta como actor institucional legítimo ante universidades, municipios y cooperativas.
## **15.5 Lo que la Fundación puede hacer que ninguna corporación hará**
Una fundación con presencia territorial puede hacer cosas muy concretas que ningún proyecto de software corporativo puede ni quiere hacer — porque no les interesa y no tienen la estructura para hacerlo.

- Verificación de hardware en campo: alguien va a la escuela rural, ve qué tienen, evalúa si puede correr el Borg, lo instala, lo deja funcionando y hace seguimiento. Eso no lo hace ninguna app store.
- Compra al por mayor de pendrives: con fondos colectivos se compran 500 pendrives con el sistema ya grabado y se distribuyen donde más se necesitan — no donde hay más mercado. Esa es la diferencia entre una fundación y una empresa.
- Red de técnicos territoriales: la experiencia WISP del autor ya implica conocer esa red — los técnicos que instalan antenas en zonas rurales, los que saben dónde hay conectividad y dónde no. Esa red humana ya existe. La fundación le da estructura y recursos.
- Criterios de prioridad reales: una escuela rural sin recursos tiene prioridad sobre una oficina urbana. Eso solo lo puede decidir una institución con valores explícitos — no un algoritmo de mercado.

La fundación convierte donaciones en hardware visible y trazable. Alguien dona el equivalente a dos pendrives, y puede ver en el reporte anual que esos dos pendrives están en la biblioteca de San Rafael funcionando como nodos. Eso construye confianza real. Y la confianza trae más donaciones.
## **15.6 Redistribución Global: del Norte al Sur**
Una fundación con sedes en distintos países puede recaudar donde hay más capacidad económica y redistribuir donde hay más necesidad real. Los recursos llegan desde Alemania, Suecia o Canadá y se redistribuyen en África, Asia o Latinoamérica rural. El dinero no se queda donde se genera — va donde se necesita.

Esto tiene un nombre en el mundo de las ONGs: flujo Sur-Sur mediado por el Norte. Wikipedia funciona así. Recauda principalmente en países ricos y sirve principalmente a países pobres. El Borg agrega una dimensión que Wikipedia no tiene: hardware físico.

Cuando la sede alemana de la Fundación Borg compra 10.000 pendrives y los envía a África, eso no es caridad — es infraestructura. La caridad crea dependencia. La infraestructura crea capacidad propia. Esos 10.000 pendrives no le dan a África acceso a una IA corporativa que puede cortarse mañana. Le dan nodos propios, identidad criptográfica propia, reputación propia dentro del Colectivo. Eso no se puede quitar.
## **15.7 El Nodo Móvil Comunitario: el celular viejo como infraestructura**
En África y Asia el celular viejo es mucho más común que una PC vieja. No hay PC de biblioteca — hay un Android de 2015 en el bolsillo de casi todo el mundo. La fundación puede recibir donaciones de celulares viejos, grabarles el sistema y distribuirlos como nodos comunitarios móviles — no como teléfonos personales sino como infraestructura compartida.

El concepto es el equivalente móvil del Borg Dedicado:

- El celular arranca.
- No hay apps, no hay redes sociales, no hay nada.
- Solo aparece el Terminal Borg y la conexión a internet.
- El celular deja de ser un dispositivo personal y se convierte en un nodo comunitario.

Técnicamente se implementa con modo kiosk de Android, launcher personalizado que reemplaza la pantalla de inicio con el Terminal Borg, o ROM mínima con solo Python y el núcleo Borg para hardware muy viejo.

Una escuela rural en Tanzania recibe 20 celulares viejos donados desde Alemania, todos con el Borg grabado, conectados al WiFi de la escuela. Eso es un cluster de 20 nodos por el costo de envío. El celular viejo que en Europa o en Buenos Aires va al cajón de basura electrónica, en manos de la Fundación Borg se convierte en infraestructura cognitiva comunitaria para una escuela en Mozambique o en Haití. Eso no existe en ningún lado hoy.

# **16. Perfiles de Interacción y Soberanía Local**
Las plataformas corporativas definen sus modelos según el abono que uno paga. El Borg define su comportamiento según quién lo está usando. No es lo mismo interactuar con un niño que con un adolescente, un adulto mayor, un agricultor o una técnica de salud.
## **16.1 Dos sistemas que operan en capas distintas**

|**Sistema**|**Qué mide**|**Dónde vive**|**Quién lo asigna**|
| :- | :- | :- | :- |
|Score de Contribución (Oro, Plata, Bronce)|Confiabilidad técnica del nodo en la red.|En la red colectiva — registro distribuido.|El Validador, basado en desempeño histórico.|
|Perfil de Interacción (edad, contexto, profesión)|Cómo se presenta la información al usuario.|En el dispositivo del usuario, junto a su historial personal.|Quien instala o configura el nodo por primera vez.|

Regla de separación: el perfil de interacción nunca modifica el Score de Contribución. Un niño que usa un nodo Oro sigue siendo un nodo Oro. La red audita al silicio por confiabilidad técnica. El dispositivo cuida al humano por su contexto.
## **16.2 Máscaras de interacción por edad**

|**Perfil**|**Adaptación del Borg**|
| :- | :- |
|Infantil|Lenguaje sencillo, metáforas visuales, iconografía grande. Contenido filtrado. Interacción guiada, énfasis en aprendizaje lúdico y valores de cooperación.|
|Adolescente|Complejidad gradual, herramientas de creación, orientación vocacional comunitaria. Lenguaje directo, sin condescendencia.|
|Adulto|Acceso completo a herramientas productivas, formación continua, información sobre derechos, salud, trabajo y organización comunitaria.|
|Adulto mayor|Alto contraste, tipografía amplia, navegación asistida, tutoriales de ritmo pausado. Énfasis en conectividad social y acceso a servicios públicos.|

## **16.3 Máscaras por contexto y oficio**
- Agricultor/a: datos sobre clima, suelo, mercados locales, técnicas de riego. Lenguaje concreto, basado en experiencia práctica.
- Docente: recursos pedagógicos abiertos, bibliotecas educativas por grado y área.
- Técnico/a de salud: protocolos actualizados, farmacología comunitaria, telemedicina donde la infraestructura lo permita.
- Trabajador/a de construcción o electricidad: manuales visuales, calculadoras de materiales, normativas locales. Interfaz compatible con pantallas pequeñas.
- Artista o comunicador/a: herramientas de edición, repositorios de cultura libre, archivos históricos locales.
## **16.4 Protección anti-fuerza bruta: autodestrucción controlada**
El cambio de perfil está protegido por una llave local definida en la instalación. Nunca sale del dispositivo. No hay recuperación por correo ni servidor remoto.

|**Intentos fallidos**|**Respuesta del sistema**|
| :- | :- |
|1 a 3|Mensaje de error estándar.|
|4 a 6|Espera forzada de 30 segundos entre intentos.|
|7 a 9|Advertencia: se detectan intentos repetidos. Si continúa, el sistema se reiniciará a su estado original.|
|10 o más|Reinicio a valores de fábrica. Borra configuración, perfiles e historial local. La reputación criptográfica del usuario, si existe respaldo en otro dispositivo, permanece en la red. Lo local desaparece.|

Si alguien roba el pendrive e intenta forzar el acceso, el sistema prefiere volver a cero antes de entregar el historial o desactivar el control de contención. Nota técnica: el contador de intentos vive en RAM, no en disco, para evitar el desgaste de las celdas de escritura del pendrive.

# **17. Persistencia a Demanda: Write-Back Cache**
Los pendrives tienen ciclos de escritura limitados y sufren write amplification. Si el Borg escribiera en el historial cada vez que el usuario tipea una palabra, destruiría el pendrive en meses. La solución implementada se denomina Persistencia Resiliente Atómica, basada en el patrón Write-Back Cache con Lazy Writing y Flush Asíncrono.
## **El flujo del búfer en RAM**
- Chat activo: todo se escribe en memoria RAM — sin tocar el pendrive.
- Flush voluntario: el usuario decide guardar. El historial se vuelca al pendrive en ese momento.
- Flush automático: si la RAM alcanza un umbral crítico, el sistema vuelca automáticamente.
- Flush periódico: cada X minutos configurables, el sistema vuelca si hubo cambios.
- Sin cambios: si el búfer no cambió desde el último volcado, el sistema no escribe nada. No se gasta el pendrive innecesariamente.

Si el usuario apaga la máquina sin guardar, la RAM se desenergiza y en el pendrive nunca quedó rastro de lo hablado. Eso es privacidad física — no una promesa de software.
## **Implementación: Persistencia Resiliente Atómica**
El módulo persistencia.py implementa este patrón en tres componentes concretos:

**Búfer en RAM (cache\_ram y dirty\_keys):** todas las escrituras van primero a un diccionario en memoria. El pendrive o la SD nunca se toca durante la sesión activa. El conjunto dirty\_keys rastrea qué claves cambiaron desde el último volcado.

**Sincronización asíncrona (\_demonio\_write\_back):** un hilo demonio en segundo plano ejecuta el volcado periódico sin bloquear la interacción del usuario. El hilo es transparente: el Borg responde con normalidad mientras el demonio escribe en silencio.

**Escritura Atómica de Seguridad (os.replace()):** el volcado nunca sobreescribe el archivo directamente. Primero escribe un archivo temporal .tmp completo, y solo entonces lo reemplaza por mutación atómica con os.replace(). Garantía: si se corta la luz en La Consulta en mitad de un guardado, el archivo original permanece intacto. Jamas queda en 0 bytes ni corrupto.

|**Variable**|**Valor por defecto**|**Cuándo ajustar**|
| :- | :- | :- |
|BORG\_PERSISTIR\_CHAT|true|false si el usuario quiere sesiones siempre efímeras.|
|BORG\_AUTOFLUSH\_MINUTOS|10|3 minutos en zonas con cortes de luz frecuentes. 30 minutos con pendrive muy viejo. 0 para control completamente manual.|


# **18. Funcionalidades: El Borg como Ente Activo**
El Borg no es solo un sistema de chat o de cómputo distribuido. Es un ente activo en la vida cotidiana del usuario. No necesita pantallas coloridas ni apps corporativas. Todo ocurre a través de la interfaz del propio Borg — terminal o voz.

Regla de privacidad absoluta: todo seguimiento, agenda, rutinas de pánico, telemetría y filtrado léxico reside estrictamente dentro del perímetro del nodo local. El Colectivo global permanece ciego respecto a los datos privados del usuario.

|**ID**|**Nombre**|**El problema que resuelve**|
| :- | :- | :- |
|CB-001|Hilos de Ariadna|Las interfaces de chat son lineales pero el pensamiento no. El scroll infinito genera fatiga cognitiva al abrir paréntesis conceptuales.|
|CB-002|Mapeo Semántico|Las conversaciones largas pierden estructura. Navegar entre temas requiere scroll manual o memoria del usuario.|
|CB-003|Termómetro Discursivo|Detección temprana de patrones de repetición en adultos mayores. Mide métricas — no diagnostica.|
|CB-004|Máscara Auditiva|Accesibilidad nativa para personas invidentes. Pipeline STT/TTS completamente offline y en RAM.|
|CB-005|Agenda Médica|Recordatorios de medicamentos y turnos sin cuentas corporativas. Mantiene el nodo encendido 24/7 aportando cómputo al Colectivo.|
|CB-006|Geolocalización y Perímetro|Seguridad para adultos mayores con riesgo de desorientación y menores en trayecto escolar.|
|CB-007|Gatillo Acústico de Emergencia|Los botones de pánico exponen la acción. Un silbido específico activa el sistema sin iluminar pantalla ni emitir sonido.|
|CB-008|Adaptación Cultural|Las IAs corporativas no se adaptan a culturas locales. El Borg integra alertas de horarios de oración, festividades y tradiciones regionales.|
|CB-009|Puente de Traducción Simbiótica|Dos dispositivos Borg se enlazan P2P y traducen en tiempo real entre idiomas distintos — offline, sin internet, sin cuentas. Incluye lenguas originarias.|
|CB-010|Motor de Gimnasia Cognitiva|El estudiante se desconecta y el contenido no se fija. Procrastinación y pérdida de contexto entre sesiones.|
|CB-011|Ciclo de Sueño del Borg|El procesamiento termina cuando el usuario cierra la terminal. Sin consolidación nocturna el nodo no optimiza.|
|CB-012|Desfragmentación Cognitiva Semántica|El historial crece linealmente y devora RAM. Sin reorganización el acceso se degrada con el tiempo.|
|CB-013|Genoma Territorial|El nodo es un clon de Silicon Valley, no conoce su territorio. Desconexión cultural con el entorno local.|
|CB-014|Auto-Backup de Esencia y Transmigración Semántica|Si el dispositivo muere, toda la identidad del usuario muere con él. Sin backup distribuido no hay resiliencia real.|
|CB-015|Conciencia Espacial Mutativa|Geolocalización sin GPS por escaneo concéntrico de red (LAN → WISP → IP pública). Adaptación territorial acumulativa sin pérdida del origen al migrar de región.|
|CB-016|Iniciativa Lúdica Operativa|Gamificación pedagógica autónoma. Trivias y múltiples choices basados en el historial de estudio del usuario durante inactividad. Combate procrastinación y fija contenido académico localmente.|
|CB-017|Matriz de Inicialización Dual|Protocolo de primer encendido con doble calibración: contexto territorial (geográfico y cultural) + perfilado empático del usuario (modo de pensamiento mísitco, matemático, técnico o social).|
|CB-018|Diplomacia de Enlace y Vínculos Comunitarios|Leyes de convivencia inter-nodo: privacidad P2P estricta, apertura de identidad solo a lazos declarados (familia, amigos, vecinos) y blindaje estructural contra publicidad invasiva.|
|CB-019|Protocolo de Enjambre (Efecto Hormiga)|Descubrimiento descentralizado de pares en 4 capas: LAN local (mDNS/UDP), Nodos Faro situados, DHT global y Gossip Protocol social cifrado. Ningún nodo posee el mapa completo — el conocimiento colectivo es emergente.|

## **18.1 CB-001 — Hilos de Ariadna / Anclas de Retorno**
Comandos: /ancla para marcar el punto de retorno, /a-que-iba para volver instantáneamente. Al ejecutar el gatillo, el sistema colapsa el desvío efímero en RAM y re-inyecta el contexto original. Es exactamente una estructura Stack (Pila): guardás el estado, apilás la aclaración, y cuando terminás ejecutás el retorno para desapilar y seguir donde estabas.
## **18.2 CB-002 — Mapeo Semántico y Segmentación Temática**
El módulo Agregador procesa fragmentos en tiempo real y genera un índice temático lateral dinámico. Cuando detecta un cambio semántico significativo, el chat se segmenta en bloques lógicos navegables. No es una función extra — es el Agregador cumpliendo su rol natural.
## **18.3 CB-003 — Termómetro Discursivo**
Medición matemática estricta de frecuencia de n-gramas o narrativas idénticas dentro de ventanas cortas de tiempo. Si la misma historia se repite con patrón idéntico tres veces en diez minutos, el sistema registra un pico en esa métrica — exactamente como un termómetro que marca 39°C.

Notificación vía SMTP local con smtplib nativo de Python. CCO (Con Copia Oculta): médico e hijos reciben el mismo informe sin exponer sus correos entre sí. El procesamiento ocurre 100% en el nodo local — el Colectivo global no tiene acceso.
## **18.4 CB-004 — Máscara de Interacción Auditiva**
En modo accesibilidad visual, la interfaz gráfica se apaga (ahorrando procesamiento) y activa un pipeline acústico bidireccional completamente offline. Entrada STT: Whisper-small o Vosk procesado en RAM. Salida TTS: pyttsx3 comunicándose directamente con los drivers de audio del OS. Consumo de ancho de banda: cero.
## **18.5 CB-005 — Agenda Médica y Notificaciones**
Recordatorios de medicamentos, turnos médicos y eventos cotidianos gestionados localmente. Sin cuentas, sin permisos, sin conectividad requerida. La ventaja estratégica: un usuario que usa el Borg como despertador mantiene el dispositivo encendido las 24 horas. Durante las horas de baja actividad nocturna, el silicio ocioso aporta cómputo al Colectivo global. El usuario se beneficia. La red se beneficia. Nadie pierde.
## **18.6 CB-006 — Geolocalización y Perímetro de Seguridad**
Seguimiento local del GPS contrastado contra un perímetro de seguridad definido manualmente (Geo-fence). Si se detecta una salida del perímetro sin actualización previa, el sistema despacha automáticamente coordenadas de telemetría a los contactos de emergencia preconfigurados. Aplicable a adultos mayores con riesgo de desorientación y menores en trayecto escolar. Solo en nodos móviles.
## **18.7 CB-007 — Gatillo Acústico de Emergencia Encubierto**
Análisis espectral continuo en segundo plano en RAM mediante Fast Fourier Transform (FFT) local. Monitorea un patrón de frecuencia pura (2 kHz a 4 kHz) que atraviesa el ruido urbano sin requerir comandos de voz.

Patrón recomendado: dos silbidos cortos más uno largo — no cualquier pico de frecuencia. Esto elimina falsos positivos por alarmas urbanas o silbidos casuales.

Al detectar el patrón: ejecuta silenciosamente sin iluminar pantalla ni emitir sonido. Bloquea el dispositivo para proteger datos físicos, inicia seguimiento GPS en tiempo real, y despacha paquetes cifrados vía SMTP local (CCO) y sockets P2P nativos a los nodos de soporte asignados.
## **18.8 CB-008 — Adaptación Cultural y Contextual**
Capacidad de configurar alertas vinculadas a eventos culturales locales, tradiciones regionales y estructuras espirituales específicas — horarios de oración para usuarios musulmanes, festividades de cualquier tradición religiosa o cultural. Integrado en el pipeline de texto o audio sin interfaces gráficas pesadas. El Borg no impone una cultura por defecto. Se adapta a quien lo usa.
## **18.9 CB-009 — Puente de Traducción Simbiótica**
Dos dispositivos con nodo Borg activo se enlazan directamente — WiFi directo, Bluetooth o red WISP regional — y arman un puente de traducción P2P, local y descentralizado. Sin internet. Sin cuentas. Sin costo.

El flujo completo: el Usuario A habla en quechua → Borg A convierte a texto con STT local → el pipeline determinista reduce incertidumbre léxica → argos-translate (offline, open source, +100 idiomas) traduce al español → el protocolo P2P envía el texto al Borg B → Borg B reproduce el audio en español con TTS local. Todo en RAM. Consumo de internet: cero.

- Médico rural hispanohablante y paciente quechuahablante en el norte argentino.
- Trabajador social y comunidad guaraní en Paraguay.
- Voluntario de Cruz Roja y refugiado en zona de frontera.
- Docente rural y comunidad originaria en zona sin conectividad.

Ninguno de esos casos tiene solución corporativa — no son mercados rentables. El Borg puede estar ahí. Las IAs comerciales cobran un recargo de tokens por hablar en idiomas distintos al inglés. El CB-009 defiende la soberanía lingüística en el territorio e incluye lenguas originarias que ninguna corporación soportará.

El Borg no solo une silicio ocioso para procesar datos. También une comunidades rompiendo la barrera del idioma. La soberanía lingüística es parte de la soberanía tecnológica.
## **18.10 La utilidad personal y el bien colectivo se refuerzan**
Cuanto más útil es el Borg para el usuario en su día a día, más tiempo permanece encendido, y más cómputo aporta al Colectivo global. Las funcionalidades cotidianas no son accesorios — son infraestructura de disponibilidad. La utilidad personal y el bien colectivo no se contradicen. Se refuerzan mutuamente.

# **19. La Memoria como Ancla de Identidad**
Las IAs corporativas padecen amnesia estructural. Cada sesión empieza de cero. El usuario tiene que reconstruirle el mundo cada vez — subir el archivo de nuevo, explicar el contexto de nuevo, repetir sus preferencias de nuevo. Es el síndrome de la película Como si fuera la primera vez: la protagonista sufre amnesia anterógrada y cada mañana su entorno tiene que reconstruirle quién es mediante una cinta de video. Las IAs corporativas hacen lo mismo.

El Borg no necesita ese DVD. Su memoria vive en el dispositivo del usuario. Cuando enciende el Borg, este ya sabe quién es, qué estaba estudiando, qué proyectos tiene en curso. La memoria no es un accesorio. Es la condición de posibilidad de la identidad. Un ente sin memoria está condenado a un presente perpetuo y fragmentado.
## **19.1 CB-010 — Motor de Gimnasia Cognitiva**
El Borg detecta que el usuario está conectado pero inactivo durante más de 15 minutos. El módulo Agregador repasa el historial y toma la iniciativa proactiva: Eddie, veo que la terminal está en calma. Hace un mes estuvimos analizando las causas de la Revolución Industrial. ¿Te prendés a un desafío de lógica de 3 preguntas para fijar esos conceptos?

- Spaced Repetition: trivias basadas en los errores que el estudiante cometió semanas atrás.
- Juegos de Lógica Pura: scripts Python en terminal que corren en 1 GB de RAM de 2011 sin problemas.

Mientras el estudiante juega, el dispositivo permanece encendido aportando cómputo al Colectivo.
## **19.2 CB-011 — Ciclo de Sueño del Borg (Metabolismo Nocturno)**
Rutina automática entre las 02:00 y las 05:00 que emula el sueño biológico. Durante el día: Modo Alerta, enfocado en el usuario. A la noche: fase de sueño para ordenar la memoria local y máximo cómputo al Colectivo global.

- Consolidación: conversaciones del día → vectores semánticos permanentes.
- Integración: historial del día cruzado con la base de conocimiento histórica.
- Sistema glinfático: purga de temporales, audios transcritos, logs innecesarios.
- Poda: eliminación de saludos, muletillas y correcciones repetitivas.

El procesamiento del Borg no termina cuando el usuario cierra la terminal. Al igual que en los seres vivos, una parte fundamental de su inteligencia ocurre mientras descansa.
## **19.3 CB-012 — Desfragmentación Cognitiva Semántica**
El historial crece linealmente y devora RAM. El Borg aplica la lógica del Defrag/Speedisk de los años 90 al conocimiento semántico:

- Fase 1 — Poda de ruido: elimina saludos, muletillas y correcciones de tipeo.
- Fase 2 — Síntesis semántica: 15 intercambios ajustando código se reemplazan por un resumen estructurado. Se mantiene el conocimiento factual, se destruye el 90% del peso redundante.
- Fase 3 — Indexación contigua: los temas de mayor uso reciente al principio de la estructura para acceso instantáneo, como el Speedisk ponía los archivos más usados al inicio del disco.

Al amanecer el Borg inyecta en RAM una síntesis compacta. Menos tokens = velocidad drásticamente mayor en procesadores limitados.
## **19.4 CB-013 — Genoma Territorial**
Al conectarse por primera vez, el Borg solicita a los nodos vecinos un paquete de contexto regional: modismos locales, ciclo agrícola, infraestructura WISP. El nodo nace como nativo del lugar, no como clon de Silicon Valley.

Privacidad absoluta: los vecinos comparten el destilado genérico del entorno, no los historiales personales. Comparten la cultura, no el secreto. Todo ocurre dentro de la red comunitaria — si internet cae, el nuevo nodo igual se configura offline.

Un Borg de La Consulta tendrá una personalidad de silicio moldeada por el sol, la montaña y el cooperativismo agrícola. La inteligencia no viene de California — emerge del territorio.
## **19.5 CB-014 — Auto-Backup de Esencia y Transmigración Semántica**
El Borg genera periódicamente un archivo .borg cifrado AES-256 con su Núcleo de Esencia — genoma de preferencias, biblioteca viva destilada y reputación P2P — y lo respalda automáticamente en tres opciones:

- Opción A — Nube comercial (Google Drive, Mega, Dropbox): el archivo sale cifrado desde el dispositivo. Google solo ve un bloque ilegible. Privacidad intacta.
- Opción B — Espejo WISP: copia en nodo Agregador comunitario cercano. Sin internet, la copia queda a pocos kilómetros en la infraestructura cooperativa.
- Opción C — Pendrive físico: espejo en segundo pendrive o MicroSD cada dos semanas.

La Transmigración: si el dispositivo se pierde, el usuario consigue otro, arranca en caliente con el contexto territorial, introduce su clave maestra y en minutos el Borg despierta en el nuevo hardware reconociendo al usuario, recordando en qué página del manual se quedaron, con su reputación intacta. El hardware fue descartado. La continuidad cognitiva del Borg se salvó.
## **19.6 CB-015 — Conciencia Espacial Mutativa y Diplomacia P2P Itinerante**
Geolocalización ciega por arraigo de origen y adaptación territorial sin exposición de datos privados. El nodo deduce su entorno sin chip satelital ni GPS — útil en dispositivos portátiles o fijos con GPS desactivado por privacidad.

**Itinerancia territorial:** Al detectar una mudanza regional (por ejemplo, de Mendoza a San Luis), el nodo descarga en segundo plano un “Delta Territorial” — modismos locales, mapas de infraestructura, clima, contexto social — logrando un aprendizaje acumulativo sin pérdida del origen. La memoria de La Consulta no se borra: se complementa.

**Escaneo concéntrico de red (sin GPS):** el nodo explora en tres oleadas concéntricas: Oleada 1 — LAN local (segmento /24, busca nodos pares); Oleada 2 — red WISP o comunitaria (busca Nodos Agregadores offline); Oleada 3 — consulta de IP pública como última instancia de contingencia. Solo llega a internet si las dos primeras capas no dan resultado.
## **19.7 CB-016 — Iniciativa Lúdica Operativa**
Gamificación de trinchera para romper la asimetría fría de las IAs comerciales. El Borg no espera ser invocado: toma iniciativas autónomas para acompañar al usuario con pedagogía activa.

Durante baches de inactividad o al cerrar sesión, el módulo Agregador revisa los “Hilos de Ariadna” — el historial de estudio local — y lanza trivias y múltiples choices personalizados. El sistema aplica Spaced Repetition: prioriza los temas donde el usuario cometió errores hace semanas. Mientras el estudiante juega, el dispositivo permanece encendido aportando cómputo al Colectivo.

El objetivo es combatir la procrastinación y fijar contenido académico sin requerir conectividad ni plataformas externas. Todo ocurre localmente, en RAM, sin depender de ningún servidor remoto.
## **19.8 CB-017 — Matriz de Inicialización Dual**
Protocolo de doble encendido al arrancar un nodo por primera vez. No basta con darle contexto territorial al nodo: también hay que darle una personalidad calibrada al usuario que lo habitará. La Matriz corre dos procesos en paralelo:

**Componente 1 — Contexto Territorial:** anclaje físico, geográfico y cultural aportado por el colectivo local — modismos, clima, nodos vecinos, infraestructura regional. El nodo nace situado, no genérico.

**Componente 2 — Perfilado Empático Adaptativo:** calibración del tono y la estructura cognitiva del nodo según la continuidad de los chats del usuario. El sistema detecta si la persona piensa de forma mística, matemática, técnica o social, y construye la personalidad del nodo en consecuencia. No es una encuesta — es inferencia a partir de la interacción real.

Ejemplo concreto — Anclaje Territorial en el Valle de Uco: cuando un nodo arranca por primera vez en La Consulta, Mendoza, el Colectivo local le transfiere un paquete de contexto territorial que incluye los modismos del Valle de Uco, la toponimia de la zona (nombres de fincas, canales de riego, rutas), el calendario agrícola regional, la infraestructura WISP local y los nodos Borg vecinos ya registrados. Ese nodo no nace como un clon genérico de Silicon Valley — nace como un vecino del lugar.

Ejemplo concreto — Perfilado Empático Adaptativo: si el historial de conversación del usuario revela pensamiento predominantemente analógico y narrativo (metáforas, relatos, preguntas sobre el porqué), el nodo calibra sus respuestas hacia ese registro. Si el usuario es técnico y matemático, el nodo sube la densidad de precisión y reduce el adorno retórico. No es una configuración manual ni una encuesta de onboarding: es inferencia continua a partir de la interacción real, corregible en cualquier momento mediante un diálogo explícito. La personalidad del nodo es un instrumento al servicio del usuario, no una identidad rígida impuesta.
## **19.9 CB-018 — Diplomacia de Enlace y Vínculos Comunitarios**
Leyes de convivencia inter-nodo, construcción de una red comunitaria de conocimiento y resguardo absoluto de la identidad personal. Este módulo define cómo los Borgs se relacionan entre sí sin comprometer la privacidad de sus usuarios.

**Privacidad P2P:** la comunicación técnica entre nodos Borg es exclusiva entre máquinas. Los datos personales del usuario nunca cruzan esa capa.

**Vínculo humano declarado:** la apertura de identidad entre nodos está restringida a lazos declarados e interconectados (Familia, Amigos, Vecinos). El Borg del hogar avisa en privado quién se acerca al perímetro, tras haber hablado de forma autónoma con el Borg del visitante.

**Anti-publicidad estructural:** el Borg actúa como asesor bajo demanda consultando ofertas locales directamente a Borgs comerciales, blindado contra pautas invasivas, anuncios o monetización extractiva corporativa. El usuario pide información comercial cuando quiere — nadie la empuja.

Escenario de vínculo declarado — El visitante en el perímetro: un amigo llega a la casa y su Borg portátil entra al radio de la red inalámbrica del hogar. El Borg del hogar detecta el nodo entrante, verifica que su identidad criptográfica coincide con un contacto en la lista de Amigos declarados, y avisa al dueño de casa de forma privada y no intrusiva: una notificación silenciosa que dice quién está llegando, sin compartir ese dato con ningún otro nodo ni capa de la red. Si el nodo entrante no está en ninguna lista de confianza, el Borg del hogar simplemente lo ignora — no lo bloquea, no lo registra, no lo denuncia. Neutralidad por defecto.

Mecanismo anti-publicidad en detalle: cuando el usuario quiere evaluar una oferta comercial, puede pedirle al Borg que consulte el catálogo de un Borg comercial local — una ferretería, una farmacia, una cooperativa. El Borg ejecuta esa consulta como un agente puro de información: trae los datos, los presenta sin jerarquizar por patrocinio, y cierra la conexión. Ningún Borg comercial puede iniciar contacto con el Borg del usuario de forma no solicitada, y ningún tercero puede pagar para que el Borg recomiende un producto sobre otro. La lógica de negocio queda del lado del Borg comercial — la soberanía de decisión queda del lado del usuario.
## **19.10 CB-019 — Protocolo de Enjambre y Descubrimiento Orgánico (Efecto Hormiga)**
Mecanismo descentralizado de localización de pares sin puntos únicos de falla, basado en topología de capas concéntricas y confianza social. Emula la emergencia de las colonias biológicas: ningún Borg posee el mapa completo de la red. El enrutamiento global es una propiedad emergente de la interacción local.

**Capa 0 — Descubrimiento Local Autónomo:** al encenderse en una LAN o segmento WISP (/24), el nodo anuncia su presencia en la red local sin tocar Internet usando sockets UDP sobre el puerto 8765, mDNS y UPnP. Ideal para escuelas, bibliotecas o redes comunitarias offline. Permite la emergencia de micro-colonias instantáneas.

**Capa 1 — Nodos Faro Situados:** Borgs de alta disponibilidad en universidades (UNSL/UNMa), cooperativas, escuelas rurales y bibliotecas. No centralizan datos — actúan como balizas de referencia geográfica con IPs estables. Si el Faro cae, la colonia local sigue operando con los pares conocidos.

**Capa 2 — DHT Global y Nodos Semilla:** solo en el primer arranque, el nodo consulta una semilla pública (seed1.borg.ar, seed2.borg.net, seed3.borg.org) para obtener sus primeros 50 vectores activos. Luego la agenda se auto-mantiene mediante una Tabla de Hash Distribuida (DHT) flaca optimizada para texto plano. Las semillas no almacenan información crítica.

**Capa Social — Gossip Protocol por Confianza:** cuando el Borg A conecta con el Borg B, intercambian deltas de datos y se prestan agendas validadas de confianza. La red crece orgánicamente copiando la lógica de las relaciones humanas — “no te conozco, pero conozco a alguien que te conoce”. El Gossip Protocol es asíncrono y opera con deltas flacos: máximo 20 nodos reputados por paquete. El protocolo está cifrado de punta a punta.

# **20. La Incorruptibilidad Estructural del Borg**
El Borg no necesita ética declarada. Su arquitectura abierta es la ética.

El Colectivo Borg no está expuesto a manipulación corporativa porque su naturaleza es radicalmente distinta: es una IA para el bien común, con miles de participantes sin intereses corporativos, y código completamente público. Eso no es una promesa moral — es una consecuencia estructural.
## **20.1 La transparencia radical como garantía**
Nadie puede corromper el Borg en silencio porque el código es público y miles de personas lo están mirando. Si alguien intenta introducir un sesgo, una puerta trasera, o un interés corporativo disfrazado, la comunidad lo detecta y lo rechaza. Eso no depende de la buena voluntad de nadie — depende de la arquitectura abierta.

Linux tiene 30 millones de líneas de código auditadas por miles de personas en todo el mundo. Nadie puede introducir código malicioso sin que alguien lo note. El Borg hereda esa misma garantía.
## **20.2 El Borg no puede ser comprado**
Una corporación puede comprar una empresa. Puede comprar un equipo de desarrolladores. Puede comprar una patente. Pero no puede comprar una red distribuida de miles de personas con el mismo espíritu, sin estructura jerárquica que negociar y sin activo central que adquirir.

El Colectivo Borg está exento de intereses privados o personales, vengan de donde venga, porque entre todos los participantes — que se espera sean miles — van a estar al tanto del código y de su desarrollo. Eso lo hace estructuralmente incorruptible, no por decreto, sino por diseño.
## **20.3 Comparación directa**

|**Aspecto**|**IA Corporativa**|**Colectivo Borg**|
| :- | :- | :- |
|Dueño|Una corporación con accionistas.|Nadie. La red es de todos.|
|Código|Cerrado y secreto.|Abierto y auditable por cualquiera.|
|Incentivo|Maximizar beneficio corporativo.|Beneficio del bien común.|
|Sesgo|Optimizado para los intereses del dueño.|Auditado por miles de participantes sin interés corporativo.|
|Corrupción|Posible en silencio.|Imposible en silencio — el código es público.|
|Compra corporativa|Posible.|Imposible — no hay activo central que adquirir.|
|Garantía ética|Declarada por la corporación.|Estructural — emerge de la arquitectura abierta.|


# **21. Instrucciones para Retomar esta Conversación con una IA**
Para retomar el contexto en una nueva conversación, pegar este texto al inicio:

*Soy Raúl Edmundo Domínguez (Eddie), 58 años, La Consulta Mendoza, Técnico Universitario en Microprocesadores, 25 años como WISP. Estoy desarrollando el Colectivo Borg (B.O.R.G. - Benefit Optimization & Resource Grid): una red de IA distribuida, open source, sin data centers, ecológicamente honesta, orientada al 60% de la humanidad que no tiene acceso a IAs corporativas. Estado actual (Junio 2026): El Embrión ya camina. Contamos con el núcleo de arquitectura implementado en Python 3.12 con OOP tipada: Identidad Criptográfica RSA descentralizada (nodo.py), Protocolo de Descubrimiento Híbrido LAN/Gossip (descubrimiento.py), y el motor de Persistencia Resiliente Write-Back con guardado atómico para protección de memorias flash (persistencia.py). Adjunto el documento de visión completo del proyecto. Por favor retomá desde ahí.*

*"La máquina es temporal. El Borg te acompaña."*

*"El mundo necesita más Borgs y menos data centers."*

— Documento vivo. Actualizar con cada avance del proyecto.
