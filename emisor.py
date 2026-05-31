"""
Colectivo B.O.R.G. — Nodo Emisor / Cliente de Prueba
=====================================================
emisor.py

Envía microtareas al nodo Ejecutor para pruebas del Embrión.
En el Tejido y Órgano, este rol será asumido por nodos reales
en dispositivos separados conectados por red.

Uso básico:
    python emisor.py

Uso avanzado:
    python emisor.py --host 192.168.1.100 --puerto 65432
    python emisor.py --texto "Procesá este fragmento de texto"
    python emisor.py --tipo ping
"""

import socket
import argparse
import sys

from core.protocolo import Protocolo


def enviar_microtarea(host: str, puerto: int,
                      tipo: str, payload: str) -> str:
    """Envía una microtarea y retorna la respuesta del nodo."""
    mensaje = Protocolo.construir(tipo, payload)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(10)
        s.connect((host, puerto))
        s.sendall(mensaje.encode("utf-8"))
        respuesta = s.recv(4096)
        return respuesta.decode("utf-8")


def main():
    parser = argparse.ArgumentParser(
        description="Colectivo Borg — Emisor de microtareas"
    )
    parser.add_argument(
        "--host", default="127.0.0.1",
        help="Host del nodo receptor (default: 127.0.0.1)"
    )
    parser.add_argument(
        "--puerto", default=65432, type=int,
        help="Puerto del nodo receptor (default: 65432)"
    )
    parser.add_argument(
        "--tipo", default="texto",
        help="Tipo de microtarea: texto, ping, audio, imagen (default: texto)"
    )
    parser.add_argument(
        "--texto",
        default="La casa era muy grande y tenía jardín.",
        help="Payload de la microtarea"
    )
    args = parser.parse_args()

    print(f"\n[EMISOR BORG] Conectando a {args.host}:{args.puerto}")
    print(f"[EMISOR BORG] Tipo    : {args.tipo}")
    print(f"[EMISOR BORG] Payload : {args.texto}\n")

    try:
        respuesta = enviar_microtarea(
            args.host, args.puerto, args.tipo, args.texto
        )
        print(f"[EMISOR BORG] Respuesta recibida:\n{respuesta}\n")

    except ConnectionRefusedError:
        print("[EMISOR BORG] ERROR: No hay nodo escuchando.")
        print("[EMISOR BORG] Ejecute 'python main.py' primero.")
        sys.exit(1)
    except Exception as e:
        print(f"[EMISOR BORG] ERROR: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
