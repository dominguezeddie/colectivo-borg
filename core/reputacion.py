"""
Colectivo B.O.R.G. — Sistema de Reputación, Rangos y Red
=========================================================
core/reputacion.py

Gestiona la identidad, el score de contribución y el rango
de cada nodo participante en el Colectivo.

Sistema de Rangos:
    BRONCE → hardware limitado o nodos nuevos     (RAM < 2GB  | score < 40)
    PLATA  → nodos estándar estables              (RAM ≥ 2GB  | score 40-79)
    ORO    → alta capacidad y alta disponibilidad (RAM ≥ 4GB  | score ≥ 80)

Filosofía:
    "La reputación la construye la persona, no el hardware."
    "Los Borg aportan capacidad. Las personas aportan identidad."

Persistencia:
    La reputación vive donde vive el Borg — en el pendrive,
    en el disco local, o en el dispositivo del usuario.
    Nunca en un servidor central que alguien pueda cancelar.
"""

import json
import time
import hashlib
from pathlib import Path

# ─── Umbrales de rango por score ─────────────────────────────────────────────
UMBRAL_ORO         = 80
UMBRAL_PLATA       = 40

# ─── Umbrales de rango por RAM (hardware) ────────────────────────────────────
RAM_ORO_MB         = 4096
RAM_PLATA_MB       = 2048

# ─── Pesos de scoring ────────────────────────────────────────────────────────
PESO_EXITO         = +0.5   # tarea completada exitosamente
PESO_FALLO         = -15.0  # penalización drástica — aísla nodos inestables
SCORE_INICIAL      = 100.0  # score de arranque
SCORE_MAX          = 100.0
SCORE_MIN          = 0.0


def _rango_por_hardware(ram_mb: int) -> str:
    """Rango inicial basado en capacidad física del hardware."""
    if ram_mb >= RAM_ORO_MB:
        return "ORO"
    elif ram_mb >= RAM_PLATA_MB:
        return "PLATA"
    return "BRONCE"


def _rango_por_score(score: float) -> str:
    """Rango dinámico basado en comportamiento acumulado."""
    if score >= UMBRAL_ORO:
        return "ORO"
    elif score >= UMBRAL_PLATA:
        return "PLATA"
    return "BRONCE"


def _id_nodo(nombre: str, host: str, puerto: int) -> str:
    """
    Genera identificador único del nodo.
    Versión Embrión: hash SHA-256 del nombre+host+puerto.
    Versión Órgano: reemplazado por clave criptográfica real (identidad portátil).
    """
    semilla = f"{nombre}:{host}:{puerto}"
    return hashlib.sha256(semilla.encode("utf-8")).hexdigest()[:16]


class GestorReputacion:
    """
    Gestiona el registro de nodos y su reputación dentro del Colectivo.

    Embrión  → almacenamiento en memoria + persistencia JSON local.
    Órgano   → sincronización cifrada entre nodos (pendrive portátil).
    Organismo→ red de confianza distribuida global.
    """

    def __init__(self, ruta_persistencia: str = None):
        self.nodos: dict = {}
        self.ruta = Path(ruta_persistencia) if ruta_persistencia else None

        if self.ruta and self.ruta.exists():
            self._cargar()

    # ─── Registro ────────────────────────────────────────────────────────────

    def registrar_nodo(self, nombre: str, ram_mb: int = 1024,
                       cpu_cores: int = 1, host: str = "local",
                       puerto: int = 0) -> dict:
        """
        Registra un nodo nuevo. Si ya existe, retorna su estado actual.
        El rango inicial se asigna por hardware; evoluciona por comportamiento.
        """
        id_nodo = _id_nodo(nombre, host, puerto)

        if id_nodo not in self.nodos:
            rango_hw = _rango_por_hardware(ram_mb)
            self.nodos[id_nodo] = {
                "id":                 id_nodo,
                "nombre":             nombre,
                "host":               host,
                "puerto":             puerto,
                "ram_mb":             ram_mb,
                "cpu_cores":          cpu_cores,
                "rango":              rango_hw,
                "score":              SCORE_INICIAL,
                "tareas_completadas": 0,
                "tareas_fallidas":    0,
                "primera_conexion":   int(time.time()),
                "ultima_actividad":   int(time.time()),
            }
            self._persistir()

        return self.nodos[id_nodo]

    # ─── Actividad ───────────────────────────────────────────────────────────

    def registrar_actividad(self, nombre: str, exito: bool = True,
                            host: str = "local", puerto: int = 0):
        """
        Registra el resultado de una microtarea y actualiza score y rango.
        Penalización drástica ante fallos para aislar nodos inestables.
        """
        id_nodo = _id_nodo(nombre, host, puerto)

        if id_nodo not in self.nodos:
            self.registrar_nodo(nombre, host=host, puerto=puerto)

        nodo = self.nodos[id_nodo]
        delta = PESO_EXITO if exito else PESO_FALLO
        nodo["score"] = max(SCORE_MIN, min(SCORE_MAX, nodo["score"] + delta))
        nodo["rango"] = _rango_por_score(nodo["score"])
        nodo["ultima_actividad"] = int(time.time())

        if exito:
            nodo["tareas_completadas"] += 1
        else:
            nodo["tareas_fallidas"] += 1

        self._persistir()

    # ─── Consultas ───────────────────────────────────────────────────────────

    def estado_nodo(self, nombre: str, host: str = "local",
                    puerto: int = 0) -> dict:
        """Retorna el estado actual de un nodo."""
        id_nodo = _id_nodo(nombre, host, puerto)
        if id_nodo not in self.nodos:
            return self.registrar_nodo(nombre, host=host, puerto=puerto)
        return self.nodos[id_nodo]

    def listar_nodos(self) -> list:
        """Lista todos los nodos ordenados por score descendente."""
        return sorted(
            self.nodos.values(),
            key=lambda n: n["score"],
            reverse=True
        )

    def nodos_por_rango(self, rango: str) -> list:
        """Filtra nodos por rango."""
        return [n for n in self.nodos.values()
                if n["rango"] == rango.upper()]

    def resumen_red(self) -> dict:
        """Resumen estadístico del estado actual de la red."""
        nodos = list(self.nodos.values())
        return {
            "total_nodos":    len(nodos),
            "oro":            len([n for n in nodos if n["rango"] == "ORO"]),
            "plata":          len([n for n in nodos if n["rango"] == "PLATA"]),
            "bronce":         len([n for n in nodos if n["rango"] == "BRONCE"]),
            "score_promedio": (
                round(sum(n["score"] for n in nodos) / len(nodos), 1)
                if nodos else 0.0
            ),
        }

    # ─── Persistencia ────────────────────────────────────────────────────────

    def _persistir(self):
        """Guarda el estado en disco si hay ruta configurada."""
        if self.ruta:
            try:
                with open(self.ruta, "w", encoding="utf-8") as f:
                    json.dump(self.nodos, f, ensure_ascii=False, indent=2)
            except Exception:
                pass  # Fallo silencioso — el Borg continúa en memoria

    def _cargar(self):
        """Carga el estado desde disco."""
        try:
            with open(self.ruta, "r", encoding="utf-8") as f:
                self.nodos = json.load(f)
        except Exception:
            self.nodos = {}
