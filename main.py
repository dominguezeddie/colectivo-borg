"""
Colectivo B.O.R.G. — Benefit Optimization & Resource Grid
==========================================================
Módulo Ejecutor Principal — main.py

Autor original: Raúl Edmundo (Eddie) Domínguez
Lugar:          La Consulta, Mendoza, Argentina
Inicio:         Mayo 2026
Licencia:       AGPL v3
Repositorio:    https://github.com/colectivo-borg

"La máquina es temporal. El Borg te acompaña."
"El Borg no necesita ética declarada. Su arquitectura abierta es la ética."
"La resistencia a la obsolescencia tecnológica es fútil. Sumate al Colectivo."
"""

import time
import socket
import logging
import platform
import os
import sys

from core.protocolo import Protocolo
from core.validador import ValidadorLexico
from core.reputacion import GestorReputacion

# ─── Logging ─────────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
log = logging.getLogger("BORG")

# ─── Configuración del nodo (via variables de entorno o defaults) ─────────────
VERSION         = "0.1.0-embrion"
NOMBRE_NODO     = os.environ.get("BORG_NOMBRE", f"nodo-{socket.gethostname()}")
HOST            = os.environ.get("BORG_HOST", "0.0.0.0")
PUERTO          = int(os.environ.get("BORG_PUERTO", 65432))
MAX_CONEXIONES  = int(os.environ.get("BORG_MAX_CONN", 5))

# CONTROL TÉRMICO CRUCIAL:
# 4 segundos evitan busy-waiting y mantienen CPUs de 2011 frías y estables.
# Ajustar a 0.5 en hardware moderno si se desea mayor throughput.
CICLO_SEGUNDOS  = float(os.environ.get("BORG_CICLO", 4.0))


def banner():
    """Terminal Borg — pantalla de bienvenida al estilo Coyote Linux."""
    print("\n" + "═" * 62)
    print("   C O L E C T I V O   B . O . R . G .")
    print("   Benefit Optimization & Resource Grid")
    print("   " + "─" * 56)
    print(f"   Nodo     : {NOMBRE_NODO}")
    print(f"   Versión  : {VERSION}")
    print(f"   Sistema  : {platform.system()} {platform.machine()}")
    print(f"   Python   : {platform.python_version()}")
    print(f"   Puerto   : {PUERTO}")
    print(f"   Ciclo    : {CICLO_SEGUNDOS}s (control térmico)")
    print("   " + "─" * 56)
    print("   UNA MENTE. MILES DE NODOS. UN MISMO PROPÓSITO.")
    print("═" * 62 + "\n")


def procesar_microtarea(datos_raw: bytes,
                        validador: ValidadorLexico,
                        reputacion: GestorReputacion) -> str:
    """
    Pipeline de procesamiento de una microtarea:
      1. Decodificar mensaje entrante.
      2. Parsear protocolo Borg.
      3. Validación léxica determinista (reducción de incertidumbre).
      4. Ejecutar tarea.
      5. Devolver resultado con confirmación.
    """
    try:
        mensaje = datos_raw.decode("utf-8").strip()
        log.info(f"Microtarea recibida: {mensaje}")

        # 1. Parsear protocolo
        tarea = Protocolo.parsear(mensaje)
        if not tarea:
            return Protocolo.error("Formato de protocolo inválido.")

        # 2. Validación léxica si el payload es texto
        if tarea.get("tipo") == "texto":
            resultado_validacion = validador.analizar(tarea["payload"])
            tarea["validacion"] = resultado_validacion
            log.info(f"Validación léxica: {resultado_validacion['resumen']}")

        # 3. Registrar actividad en el sistema de reputación
        reputacion.registrar_actividad(NOMBRE_NODO, exito=True)

        # 4. Construir respuesta
        return Protocolo.confirmar(NOMBRE_NODO, tarea)

    except Exception as e:
        log.error(f"Error procesando microtarea: {e}")
        reputacion.registrar_actividad(NOMBRE_NODO, exito=False)
        return Protocolo.error(str(e))


def iniciar_servidor(validador: ValidadorLexico,
                     reputacion: GestorReputacion):
    """
    Bucle principal del nodo Ejecutor.
    Escucha conexiones entrantes y procesa microtareas de forma continua.
    Optimizado para RAM mínima — no mantiene estado entre conexiones.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv:
        srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        srv.bind((HOST, PUERTO))
        srv.listen(MAX_CONEXIONES)
        log.info(f"Nodo activo en {HOST}:{PUERTO} — esperando microtareas...")

        while True:
            try:
                conn, addr = srv.accept()
                with conn:
                    log.info(f"Conexión desde {addr}")
                    datos = conn.recv(4096)
                    if datos:
                        respuesta = procesar_microtarea(
                            datos, validador, reputacion
                        )
                        conn.sendall(respuesta.encode("utf-8"))

                # Control térmico — respeta CPUs de 2011
                time.sleep(CICLO_SEGUNDOS)

            except KeyboardInterrupt:
                log.info("Nodo detenido por el operador. El Colectivo sigue.")
                break
            except Exception as e:
                log.error(f"Error en el bucle principal: {e}")
                time.sleep(1)


def main():
    banner()

    # Detectar RAM disponible aproximada para asignación de rango
    try:
        import psutil
        ram_mb = psutil.virtual_memory().total // (1024 * 1024)
        cpu_cores = psutil.cpu_count(logical=False) or 1
    except ImportError:
        # psutil no disponible — usar valores conservadores
        ram_mb = 1024
        cpu_cores = 2

    log.info(f"Hardware detectado: RAM~{ram_mb}MB | Cores~{cpu_cores}")

    # Inicializar subsistemas
    log.info("Inicializando validador léxico...")
    validador = ValidadorLexico()

    log.info("Inicializando sistema de reputación...")
    reputacion = GestorReputacion(ruta_persistencia="borg_reputacion.json")

    # Registrar este nodo
    reputacion.registrar_nodo(NOMBRE_NODO, ram_mb=ram_mb,
                              cpu_cores=cpu_cores, host=HOST, puerto=PUERTO)

    estado = reputacion.estado_nodo(NOMBRE_NODO)
    log.info(
        f"Nodo registrado — Rango: {estado['rango']} | "
        f"Score: {estado['score']} | "
        f"Tareas completadas: {estado['tareas_completadas']}"
    )

    resumen = reputacion.resumen_red()
    log.info(
        f"Red actual — Nodos: {resumen['total_nodos']} | "
        f"ORO: {resumen['oro']} | PLATA: {resumen['plata']} | "
        f"BRONCE: {resumen['bronce']}"
    )

    # Iniciar servidor
    iniciar_servidor(validador, reputacion)


if __name__ == "__main__":
    main()
