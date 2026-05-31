"""
Colectivo B.O.R.G. — Motor de Validación Léxica
================================================
core/validador.py

Motor híbrido de reducción de incertidumbre lingüística.
El "Machete Lingüístico" del Colectivo.

Filosofía (analogía con compiladores):
    Antes de aplicar inferencia probabilística costosa, resolver
    todo lo que puede resolverse de forma determinista:

    1. Desconstrucción léxica  → fragmentar la oración en tokens atómicos
    2. Filtrado determinista   → buscar cada token en diccionario de hashes O(1)
    3. Clasificación           → CONOCIDO / INCIERTO / ESPECIAL
    4. Terreno limpio          → el LLM trabaja con menos ruido y menos tokens

    "Resolver primero lo determinista.
     Las probabilidades para lo genuinamente ambiguo."

Ventaja para el español:
    Reducir incertidumbre léxica previa disminuye los tokens necesarios
    para la inferencia final, atacando directamente el peaje lingüístico
    del 59% extra que paga el español vs el inglés en sistemas corporativos.

Regla fundamental:
    PALABRA NO ENCONTRADA ≠ PALABRA INCORRECTA.
    Puede ser nombre propio, tecnicismo, neologismo, sigla, marca.
    El sistema clasifica — no corrige.
"""

import re
import hashlib
from pathlib import Path


# ─── Vocabulario semilla en español ──────────────────────────────────────────
# En producción se carga desde archivos locales en el pendrive/disco.
# Este conjunto semilla cubre vocabulario común + terminología técnica del Borg.
VOCABULARIO_SEMILLA = {
    # Artículos
    "el", "la", "los", "las", "un", "una", "unos", "unas",
    # Preposiciones
    "a", "ante", "bajo", "con", "contra", "de", "desde", "en",
    "entre", "hacia", "hasta", "para", "por", "según", "sin",
    "sobre", "tras",
    # Conjunciones
    "y", "e", "o", "u", "pero", "sino", "aunque", "porque",
    "si", "que", "cuando", "como", "donde",
    # Verbos comunes
    "es", "son", "era", "eran", "ser", "estar", "tener", "hacer",
    "poder", "querer", "saber", "ver", "dar", "ir", "venir",
    "puede", "tiene", "hace", "hay", "fue", "han", "tenía",
    # Pronombres
    "yo", "tú", "él", "ella", "nosotros", "vosotros", "ellos",
    "me", "te", "se", "nos", "les", "lo", "le",
    # Adverbios
    "no", "sí", "también", "más", "muy", "bien", "mal", "aquí",
    "allí", "ahora", "antes", "después", "siempre", "nunca",
    "solo", "mismo", "ya", "aún", "todavía",
    # Adjetivos comunes
    "grande", "pequeño", "nuevo", "viejo", "bueno", "malo",
    "primero", "último", "otro", "todo", "cada",
    # Sustantivos comunes
    "casa", "jardín", "tiempo", "parte", "vida", "mundo",
    "persona", "año", "día", "trabajo", "país",
    # Terminología técnica del Borg
    "red", "nodo", "datos", "sistema", "archivo", "memoria",
    "proceso", "tarea", "código", "protocolo", "servidor",
    "cliente", "conexión", "mensaje", "error", "resultado",
    "borg", "colectivo", "microtarea", "reputación", "rango",
    "ejecutor", "agregador", "validador", "embrión", "célula",
    "wisp", "antena", "enlace", "ram", "cpu", "núcleo",
    "computación", "distribuida", "ia", "hash", "clave",
    "bronce", "plata", "oro", "score", "pendrive", "usb",
    # Terminología lingüística
    "token", "léxico", "certeza", "incertidumbre", "análisis",
    "fútil",
}


class ValidadorLexico:
    """
    Motor de validación léxica y reducción de incertidumbre.

    Clasifica cada token de un texto en:
        CONOCIDO   → existe en el vocabulario local (hash encontrado)
        INCIERTO   → no encontrado — pendiente de clasificación,
                     NO necesariamente incorrecto
        ESPECIAL   → número, puntuación, símbolo
    """

    def __init__(self, ruta_vocabulario: str = None):
        self.vocabulario = set(VOCABULARIO_SEMILLA)

        if ruta_vocabulario:
            self._cargar_vocabulario_externo(ruta_vocabulario)

        # Índice de hashes MD5 para búsqueda O(1)
        self._hashes: set = set()
        self._construir_indice()

    def _cargar_vocabulario_externo(self, ruta: str):
        """Carga vocabulario adicional desde archivo (una palabra por línea)."""
        try:
            archivo = Path(ruta)
            if archivo.exists():
                with open(archivo, "r", encoding="utf-8") as f:
                    palabras = {
                        line.strip().lower()
                        for line in f
                        if line.strip()
                    }
                self.vocabulario.update(palabras)
        except Exception:
            pass  # Fallo silencioso — continúa con vocabulario base

    def _construir_indice(self):
        """Construye índice de hashes MD5 — búsqueda determinista O(1)."""
        self._hashes = {
            hashlib.md5(p.encode("utf-8")).hexdigest()
            for p in self.vocabulario
        }

    def _hash(self, token: str) -> str:
        return hashlib.md5(token.lower().encode("utf-8")).hexdigest()

    def _clasificar(self, token: str) -> str:
        """Clasifica un token individual."""
        # Números
        if re.match(r"^[\d.,]+$", token):
            return "ESPECIAL"
        # Puntuación / símbolos
        if re.match(r"^[^\w]+$", token, re.UNICODE):
            return "ESPECIAL"
        # Búsqueda determinista por hash — O(1)
        if self._hash(token) in self._hashes:
            return "CONOCIDO"
        return "INCIERTO"

    def analizar(self, texto: str) -> dict:
        """
        Analiza un texto completo token por token.

        Retorna:
            {
                "tokens":    [{"token": str, "clase": str}, ...],
                "conocidos": int,
                "inciertos": int,
                "especiales": int,
                "total":     int,
                "certeza":   float,   # % tokens conocidos
                "resumen":   str,
            }
        """
        tokens_raw = re.findall(r"\w+|[^\w\s]", texto, re.UNICODE)
        resultados = []
        contadores = {"CONOCIDO": 0, "INCIERTO": 0, "ESPECIAL": 0}

        for token in tokens_raw:
            clase = self._clasificar(token)
            resultados.append({"token": token, "clase": clase})
            contadores[clase] += 1

        total   = len(tokens_raw)
        certeza = (contadores["CONOCIDO"] / total * 100) if total > 0 else 0.0

        return {
            "tokens":     resultados,
            "conocidos":  contadores["CONOCIDO"],
            "inciertos":  contadores["INCIERTO"],
            "especiales": contadores["ESPECIAL"],
            "total":      total,
            "certeza":    round(certeza, 1),
            "resumen": (
                f"{contadores['CONOCIDO']}/{total} tokens conocidos "
                f"({certeza:.1f}% certeza léxica)"
            ),
        }

    def agregar_palabras(self, palabras: list):
        """Expande el vocabulario en tiempo de ejecución."""
        for palabra in palabras:
            self.vocabulario.add(palabra.lower())
        self._construir_indice()
