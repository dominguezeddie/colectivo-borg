# Hardware Compatible — Colectivo Borg

## No es reciclaje — es universalidad

El Borg no discrimina por antigüedad, marca ni capacidad. Una PC nueva
de última generación y un celular de 2018 son ambos nodos válidos. Cada
uno contribuye según lo que tiene.

El Borg NO habla de CPUs 486 ni Pentium de los años 90.
El hardware objetivo es aquel capaz de correr **Windows 10 o superior**,
fabricado aproximadamente entre 2016 y 2020, con arquitectura x86 de 64 bits
(o ARM en el caso de celulares y Raspberry Pi).

## ¿Por qué no 2011?

Porque una década es el límite real donde el hardware empieza a convertirse
en obstáculo, no solo en "viejito pero usable". Un equipo de 2011 típicamente
tiene 2GB de RAM, CPU de 32 bits y una instalación de Windows 7 sin soporte.
Eso no es reciclaje funcional — es arqueología. El Borg es una lagartija,
no un paleontólogo.

**El principio se mantiene:** no se pide hardware nuevo. Se aprovecha el
que ya está encendido en las instituciones, pero dentro de un rango que
todavía puede hacer algo útil sin frustrar al usuario.

---

## Requisitos mínimos reales (actualización 2026)

- CPU de 64 bits fabricado aproximadamente entre 2016 y 2020
  (Intel Core de 6ta a 10ma generación, AMD Ryzen 1xxx a 3xxx,
   o equivalente ARM en dispositivos móviles)
- 4 GB de RAM como mínimo recomendado (2 GB pueden funcionar para tareas
  muy livianas pero con experiencia degradada)
- Almacenamiento: 8 GB libres (para sistema base más historial persistente)
- Conexión a internet (WiFi, datos móviles, ethernet) — puede ser intermitente
- Algún recurso para ofrecer: CPU, RAM o disponibilidad horaria

**Nota sobre equipos más antiguos:** Un equipo de hace una década con 2GB de RAM
y CPU de 32 bits puede seguir siendo nodo Ejecutor para microtareas
extremadamente simples (sumas, validaciones básicas). Pero no puede ser el
target de diseño. El Borg no excluye a esos equipos, pero tampoco se ata a ellos.

---

## Tabla de Hardware Mínimo por Tipo de Dispositivo

| Dispositivo | Requisito mínimo | CPU / Chip | RAM | SO recomendado | Rol en el Borg |
|-------------|------------------|------------|-----|-----------------|----------------|
| PC de escritorio / Laptop | 2015 en adelante | CPU 64-bit, 2+ núcleos | 4 GB | Linux minimal (Alpine/Debian) o Windows 10 LTSC | Ejecutor, Agregador liviano |
| Celular Android | 2018 en adelante (Android 8+) | ARM 64-bit, 4+ núcleos | 3 GB | Android 8 Oreo o superior | Ejecutor móvil, nodo itinerante |
| Raspberry Pi / SBC | Raspberry Pi 3B+ en adelante | ARM Cortex-A53 64-bit | 1 GB (Pi 3) / 4 GB (Pi 4) | Raspberry Pi OS Lite / Alpine ARM | Nodo Faro liviano, Ejecutor permanente |
| PC muy antigua (opcional) | 2010-2014, 2 GB RAM | x86 32-bit o 64-bit lento | 2 GB | Alpine Linux 32-bit | Ejecutor para microtareas mínimas |

**Nota:** los equipos de la última fila no son el target de diseño del Borg,
pero tampoco se excluyen. Pueden participar como nodos de baja capacidad
para microtareas elementales. El sistema adapta la asignación de tareas
al perfil de hardware declarado por el nodo al registrarse.

---

## Base de Conocimiento Estática Precargada

Para que el primer nodo tenga valor inmediato incluso sin red, el pendrive
del Embrión incluirá una biblioteca portátil incorruptible con:

- Diccionarios locales y modelos ligeros de compresión
- Manuales de agricultura local, primeros auxilios y guías técnicas WISP
- Textos de filosofía, derecho básico y conocimiento general (dominio público)
- La documentación completa del Colectivo Borg

Esta base de conocimiento ocupa menos de 500 MB y permite que el usuario
consulte información útil desde el Día Cero, sin depender de internet ni
de servidores corporativos. El pendrive no es solo una llave de red. Es una
biblioteca de bolsillo que viaja con el usuario.

---

## Potencia aproximada por era (actualizado 2016-2026)

| Período | Potencia aprox. | Ejemplos | Lo que puede hacer para el Borg |
|---------|-----------------|----------|--------------------------------|
| 2016-2017 (hace ~10 años) | 100-200 GFLOPS | Intel Core i5-6400, AMD A10-9700, Raspberry Pi 3 | Microtareas simples: clasificación básica, cálculo, transcripción de audio corto con modelos livianos |
| 2018-2019 (hace ~7 años) | 200-500 GFLOPS | Intel Core i7-8700, AMD Ryzen 5 2600, Apple A12 | Inferencia local de modelos tiny, agregación simple |
| 2020-2021 (hace ~5 años) | ~1 TFLOP | AMD Ryzen 7 5800X, Intel Core i9-11900K, Apple M1 | Inferencia local fluida, modelos pequeños, agregación |
| 2024-2026 (hoy) | 1-5 TFLOPS CPU / 50+ GPU | AMD Ryzen 9 7950X, Intel Core Ultra 7, Apple M4 | Nodo Agregador o Validador de alta capacidad |

**Dato clave:** un equipo fabricado hace una década (2016) sigue siendo útil
para microtareas distribuidas. Lo que hace 10 años era una "PC normal" hoy es
el piso de entrada del Borg. La brecha digital no se salta exigiendo hardware
moderno — se salta usando lo que ya hay, no lo que había hace 15 años.

---

## Modalidades de despliegue por hardware

### PC vieja sin uso (Borg Dedicado)
- Sin disco rígido: arranca desde pendrive con RootFS on RAM
- Con disco rígido: instalación dedicada, sin escritorio
- Consume recursos mínimos — CPU antigua trabajando en su rango

### PC o notebook en uso (Borg Instalado)
- Corre como servicio en segundo plano
- Solo usa recursos ociosos
- Transparente para el usuario

### Celular Android (Termux)
- Termux instala entorno Linux sin root
- Requiere Android 8 o superior, 3GB RAM mínimo recomendado
- Nodo móvil conectado por WiFi o datos
- En Latinoamérica y África: una de las puertas de entrada más comunes

### Pendrive booteable (Borg Portable)
- 64 GB o 128 GB recomendado (para base de conocimiento precargada)
- Alpine Linux (~500 MB) + Python + núcleo Borg
- Base de conocimiento precargada (~500 MB)
- Todo el espacio restante pertenece al Colectivo
- RootFS on RAM: al desenchufar, la PC queda intacta

---

## Control térmico para hardware antiguo

El parámetro `BORG_CICLO=4.0` (4 segundos de pausa entre ciclos) es crucial
para equipos de la última década. Evita busy-waiting y mantiene el hardware
frío y estable durante operación continua.

Ajustar a valores menores (0.5-1 segundo) solo en hardware moderno con buena
refrigeración.

---

## La escala compensa la eficiencia individual

Una neurona biológica es ineficiente comparada con un chip moderno. Pero
86 mil millones de neuronas juntas producen algo que ningún chip puede
replicar. Un nodo lento en el Borg no es un problema — es una neurona más.
El sistema no depende de que cada nodo sea potente. Depende de que haya muchos
nodos.

---

*La máquina es temporal. El Borg te acompaña.*
