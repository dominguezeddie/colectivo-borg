## Sistema de Reputación y Capacidad

### Rango de Confianza (Oro/Plata/Bronce)

Mide la **constancia y confiabilidad** del nodo. No depende del hardware.

| Rango | Condición (solo por participación) | Beneficio |
|-------|-------------------------------------|-----------|
| **ORO** | Score ≥ 80 | Prioridad máxima en microtareas. Elige primero. |
| **PLATA** | Score 40-79 | Participación estándar. |
| **BRONCE** | Score < 40 (o nodo nuevo) | Sujeto a auditorías. Recibe tareas cuando hay disponibilidad. |

### Perfil de Capacidad (Alto/Medio/Básico)

Mide la **potencia bruta del hardware**. Se detecta en cada arranque.

| Perfil | Condición | Qué tareas recibe |
|--------|-----------|-------------------|
| **ALTO** | RAM ≥ 4GB o CPU moderno (2018+) | Tareas pesadas (inferencia local, agregación) |
| **MEDIO** | RAM ≥ 2GB, CPU 2014-2017 | Tareas estándar (clasificación, transcripción corta) |
| **BÁSICO** | RAM < 2GB o CPU anterior a 2014 | Tareas livianas (sumas, validaciones, handshakes) |

### Combinación práctica

- Un nodo **Oro + Básico** (PC vieja siempre encendida) recibe prioridad en tareas livianas y handshakes. Es la columna vertebral de la red.
- Un nodo **Bronce + Alto** (PC nueva pero poco uso) recibe tareas pesadas cuando está disponible, pero sin prioridad.
- La red no penaliza el hardware limitado. Solo mide el compromiso real.
