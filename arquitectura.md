# Arquitectura Técnica — Colectivo Borg

## Los Tres Roles de la Célula Madre

Cada nodo en el Colectivo asume uno o más roles según sus capacidades físicas reales.

### El Ejecutor ("El Músculo")
- Unidad de cómputo atómica
- Procesa microtareas de 1 a 30 segundos
- Arquitectura agnóstica al estado — no mantiene contexto entre tareas
- Hardware ideal: alta capacidad CPU
- Target: cualquier PC con Python, incluso hardware de 2011

### El Agregador ("El Sintetizador")
- Ensambla resultados parciales de múltiples Ejecutores
- Gestión de nodos rezagados con failover instantáneo
- Hardware ideal: alta RAM, CPU moderada

### El Validador ("El Auditor")
- Motor de gobernanza y confianza
- Verifica integridad de datos mediante re-ejecución parcial
- Sus informes alimentan el Score de Contribución
- Hardware ideal: puede ser un nodo de alta latencia — trabaja en segundo plano

## Protocolo de Comunicación

Formato: `BORG|<version>|<tipo>|<id_tarea>|<payload>`

Respuesta OK: `BORG-ACK|<json>`
Respuesta ERROR: `BORG-ERR|<json>`

## Pipeline Lingüístico

Ver `core/validador.py` para implementación completa.

1. Tokenización
2. Clasificación determinista por hash O(1): CONOCIDO / INCIERTO / ESPECIAL
3. Índice de Certeza Léxica (ICL) como métrica de limpieza del terreno
4. Transferencia a inferencia probabilística con contexto verificado

## Sistema de Reputación

Ver `core/reputacion.py` para implementación completa.

- Score inicial: 100.0
- Tarea exitosa: +0.5
- Tarea fallida: -15.0 (penalización drástica para aislar nodos inestables)
- Rango ORO: score ≥ 80 o RAM ≥ 4GB
- Rango PLATA: score 40-79 o RAM ≥ 2GB  
- Rango BRONCE: score < 40 o RAM < 2GB

## Diseño Orientado a la Desconexión (Disconnection-First)

El Borg asume desconexión como norma, no como excepción.

- Un nodo puede desaparecer a mitad de una microtarea
- El Agregador detecta timeout y reasigna en segundos
- La identidad es por clave criptográfica, no por IP
- La reputación viaja con el nodo, no con la máquina

---

## Persistencia a Demanda: Write-Back Cache

### El problema que resuelve

Los pendrives (memoria Flash NAND) tienen ciclos de escritura limitados
(entre 3.000 y 10.000 escrituras por celda) y sufren write amplification.
Si el Borg escribiera en el historial cada vez que el usuario tipea una palabra,
destruiría el pendrive en pocos meses.

### La solución: búfer en RAM con volcado asíncrono

```
[Chat activo] ──> Escribe en búfer (RAM)
                        │
                        ├──> ¿Usuario cierra/guarda? ──> FLUSH voluntario ──> Pendrive
                        │
                        ├──> ¿Búfer al límite de RAM? ──> FLUSH automático ──> Pendrive
                        │
                        └──> ¿Pasaron X minutos?      ──> FLUSH periódico  ──> Pendrive
```

El historial vive en RAM durante la sesión. Se vuelca al pendrive solo cuando:
1. El usuario decide guardarlo (soberanía del dato)
2. La RAM alcanza un umbral crítico (protección automática)
3. Pasa el intervalo de autoguardado configurado

Si el usuario apaga la máquina sin guardar, la RAM se desenergiza
y en el pendrive nunca quedó rastro de lo hablado.
Eso es privacidad física — no una promesa de software.

### Configuración del Auto-Flush

```bash
BORG_PERSISTIR_CHAT=true        # Activa o desactiva el guardado
BORG_AUTOFLUSH_MINUTOS=10       # Intervalo por defecto (0 = solo manual)
```

| Modo | Intervalo | Cuándo usarlo |
|---|---|---|
| Por defecto | 10 minutos | Balance entre protección y desgaste del silicio |
| Red inestable | 3 minutos | Zonas con cortes de luz frecuentes (ej: rural con viento Zonda) |
| Pendrive muy viejo | 30 minutos | Priorizar vida útil física del hardware |
| Solo manual | 0 (desactivado) | El usuario controla completamente cuándo persiste |

El autoguardado es inteligente: si el búfer no cambió desde el último volcado,
el sistema se salta el proceso y no escribe nada. No se gasta el pendrive
si no hay datos nuevos.

### Nombre técnico del patrón

**Write-Back Cache con Lazy Writing y Flush Asíncrono.**
Es el mismo patrón que usan los sistemas operativos modernos para manejar
archivos en disco. El Borg lo adapta para hardware de trinchera
con memoria flash de vida limitada.
