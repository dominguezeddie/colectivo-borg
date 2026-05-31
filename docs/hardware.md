# Hardware Compatible — Colectivo Borg

## Definición de "hardware antiguo" en el Borg

El Borg NO habla de CPUs 486 ni Pentium de los años 90.

El hardware objetivo es aquel capaz de correr **Windows 7 o superior**,
fabricado aproximadamente entre 2007 y 2015, con arquitectura x86/x64.

## Potencia aproximada por era

| Período | Potencia aprox. | Ejemplos | Rol sugerido en el Borg |
|---|---|---|---|
| 2007-2011 | 20-100 GFLOPS | Core 2 Duo, i3 1ra gen, AMD Phenom | Ejecutor básico — microtareas simples |
| 2012-2016 | 100-300 GFLOPS | i5/i7 3ra-6ta gen, AMD FX | Ejecutor estándar / Validador |
| 2017-2021 | 300-1000 GFLOPS | Ryzen 1-5, i7 8va-10ma gen | Agregador / Ejecutor avanzado |
| 2022+ | 1000+ GFLOPS | Ryzen 7000, i9 12va gen+, M1/M2/M4 | Agregador potente / coordinador |

## Requisitos mínimos absolutos

- CPU x86/x64 post-2007
- 512 MB RAM (1 GB recomendado)
- Python 3.8 o superior
- Conexión a internet (intermitente tolerada)

## Modalidades de despliegue por hardware

### PC vieja sin uso (Borg Dedicado)
- Sin disco rígido: arranca desde pendrive con RootFS on RAM
- Con disco rígido: instalación dedicada, sin escritorio
- Consume recursos mínimos — CPU antigua trabajando en su rango

### PC o notebook en uso (Borg Instalado)
- Corre como servicio en segundo plano
- Solo usa recursos ociosos
- Transparente para el usuario

### Celular Android viejo (Termux)
- Termux instala entorno Linux sin root
- Nodo móvil conectado por WiFi o datos
- En Latinoamérica: la puerta de entrada más común

### Pendrive booteable (Borg Portable)
- 64 GB o 128 GB recomendado
- Alpine Linux (~500 MB) + Python + núcleo Borg
- Todo el espacio restante pertenece al Colectivo
- RootFS on RAM: al desenchufar, la PC queda intacta

## Control térmico para hardware antiguo

El parámetro `BORG_CICLO=4.0` (4 segundos de pausa entre ciclos)
es crucial para CPUs de 2011. Evita busy-waiting y mantiene
el hardware frío y estable durante operación continua.

Ajustar a valores menores solo en hardware moderno con buena refrigeración.
