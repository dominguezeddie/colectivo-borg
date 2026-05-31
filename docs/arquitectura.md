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
