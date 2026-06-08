### Selección Automática del Modelo de IA

El Borg no le pregunta al usuario qué modelo de IA quiere usar. No ofrece opciones. No pide permiso.

En cada arranque, el nodo detecta los recursos disponibles (RAM, CPU, GPU) y selecciona automáticamente el modelo más adecuado para ese hardware:

| Perfil de hardware | RAM disponible | Modelo seleccionado | Uso |
|--------------------|----------------|---------------------|-----|
| **BÁSICO** | < 6 GB | Phi-4-mini (3.8B) | Tareas livianas: clasificación, validación léxica, handshakes |
| **MEDIO** | 6 - 20 GB | Qwen3 7B / 8B | Tareas estándar: transcripción, resumen, análisis semántico |
| **ALTO** | > 20 GB | Qwen3 30B / 32B | Tareas pesadas: inferencia compleja, agregación, validación avanzada |

**Regla de oro:** El usuario no configura nada. El Borg se adapta al terreno como una lagartija cambia de comportamiento según la temperatura o la presencia de depredadores.

Si un usuario mueve su pendrive de una PC vieja (4GB RAM) a una PC moderna (32GB RAM), el Borg detecta el cambio en el próximo arranque y actualiza automáticamente el modelo de IA. No hay que reinstalar nada. No hay que elegir nada.
