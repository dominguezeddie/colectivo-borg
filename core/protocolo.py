"""
Colectivo B.O.R.G. — Protocolo de Comunicación entre Nodos
===========================================================
core/protocolo.py

Formato estándar de mensajes Borg:
    BORG|<version>|<tipo>|<id_tarea>|<payload>

Ejemplos:
    BORG|1|texto|tarea-a1b2c3d4|El sistema funciona correctamente
    BORG|1|ping|tarea-e5f6g7h8|nodo-mendoza-01
    BORG|1|audio|tarea-i9j0k1l2|[datos_base64]

Tipos de tarea soportados en el Embrión:
    texto  → validación léxica + procesamiento de texto
    ping   → anuncio de presencia en la red
    audio  → (futuro Tejido) transcripción de audio corto
    imagen → (futuro Tejido) clasificación de imagen
"""

import json
import uuid
import time

VERSION_PROTOCOLO = "1"
SEPARADOR         = "|"
PREFIJO           = "BORG"


class Protocolo:

    @staticmethod
    def construir(tipo: str, payload: str, id_tarea: str = None) -> str:
        """Construye un mensaje Borg estándar."""
        if not id_tarea:
            id_tarea = f"tarea-{uuid.uuid4().hex[:8]}"
        return SEPARADOR.join([
            PREFIJO,
            VERSION_PROTOCOLO,
            tipo,
            id_tarea,
            payload
        ])

    @staticmethod
    def parsear(mensaje: str) -> dict | None:
        """
        Parsea un mensaje Borg.
        Retorna dict con campos o None si el formato es inválido.
        """
        partes = mensaje.strip().split(SEPARADOR, 4)
        if len(partes) < 5 or partes[0] != PREFIJO:
            return None
        return {
            "prefijo":  partes[0],
            "version":  partes[1],
            "tipo":     partes[2],
            "id_tarea": partes[3],
            "payload":  partes[4],
        }

    @staticmethod
    def confirmar(nombre_nodo: str, tarea: dict) -> str:
        """Construye mensaje de confirmación de procesamiento."""
        respuesta = {
            "estado":     "OK",
            "nodo":       nombre_nodo,
            "id_tarea":   tarea.get("id_tarea", "desconocida"),
            "tipo":       tarea.get("tipo", "desconocido"),
            "timestamp":  int(time.time()),
            "validacion": tarea.get("validacion", None),
        }
        return f"BORG-ACK|{json.dumps(respuesta, ensure_ascii=False)}"

    @staticmethod
    def error(motivo: str) -> str:
        """Construye mensaje de error."""
        respuesta = {
            "estado":    "ERROR",
            "motivo":    motivo,
            "timestamp": int(time.time()),
        }
        return f"BORG-ERR|{json.dumps(respuesta, ensure_ascii=False)}"

    @staticmethod
    def ping(nombre_nodo: str) -> str:
        """Mensaje de anuncio de presencia en la red."""
        return Protocolo.construir("ping", nombre_nodo)
