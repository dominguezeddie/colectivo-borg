## Sistema de Reputación y Capacidad

El Borg distingue dos conceptos que los sistemas corporativos mezclan deliberadamente: la **confiabilidad** del nodo (su compromiso) y su **capacidad bruta** (su hardware).

### Rango de Confianza (Oro/Plata/Bronce)

Mide la **constancia y confiabilidad** del nodo. No depende del hardware. Se construye con el historial de participación.

| Rango | Condición (solo por participación) | Beneficio |
|-------|-------------------------------------|-----------|
| **ORO** | Score ≥ 80 | Prioridad máxima en microtareas. Elige primero. |
| **PLATA** | Score 40-79 | Participación estándar. |
| **BRONCE** | Score < 40 (o nodo nuevo) | Sujeto a auditorías. Recibe tareas cuando hay disponibilidad. |

**Fórmulas base del Score de Contribución:**

| Evento | Cambio en Score |
|--------|-----------------|
| Nodo nuevo (primer arranque) | Score = 100.0 |
| Microtarea completada exitosamente | +0.5 |
| Microtarea fallida / timeout | -15.0 |
| Auditoría del Validador (nodo honesto) | +5.0 (cada 100 tareas) |
| Auditoría del Validador (nodo fraudulento) | -30.0 + posible aislamiento |

**Nota:** la penalización por falla es deliberadamente alta para aislar rápidamente nodos inestables o maliciosos. Una red distribuida no puede darse el lujo de tener "nodos ruidosos".

### Perfil de Capacidad (Alto/Medio/Básico)

Mide la **potencia bruta del hardware**. Se detecta automáticamente en cada arranque. No afecta el rango de confianza.

| Perfil | Condición | Qué tareas recibe |
|--------|-----------|-------------------|
| **ALTO** | RAM ≥ 4GB o CPU moderno (2018+) | Tareas pesadas (inferencia local, agregación) |
| **MEDIO** | RAM ≥ 2GB, CPU 2014-2017 | Tareas estándar (clasificación, transcripción corta) |
| **BÁSICO** | RAM < 2GB o CPU anterior a 2014 | Tareas livianas (sumas, validaciones, handshakes) |

### Combinación práctica

- Un nodo **Oro + Básico** (PC vieja siempre encendida) recibe prioridad en tareas livianas y handshakes. Es la columna vertebral de la red.
- Un nodo **Bronce + Alto** (PC nueva pero poco uso) recibe tareas pesadas cuando está disponible, pero sin prioridad.
- La red no penaliza el hardware limitado. Solo mide el compromiso real.

**Principio fundamental:** La reputación se gana con constancia, no con poder adquisitivo.
