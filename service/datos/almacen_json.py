"""Lectura y escritura tolerante de los archivos JSON del sistema."""

import json
import os

RUTA_ESPACIOS = "data/espacios.json"
RUTA_USUARIOS = "data/usuarios.json"
RUTA_RESERVAS = "data/reservas.json"


def cargar_datos(ruta):
    """Devuelve la lista guardada; si no hay archivo o es inválida, devuelve []."""
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
    except OSError:
        return []
    if contenido.strip() == "":
        return []
    try:
        datos = json.loads(contenido)
    except (ValueError, TypeError):
        os.replace(ruta, ruta + ".dañado.json")
        return []
    return datos if isinstance(datos, list) else []


def guardar_datos(ruta, datos):
    """Escribe en un archivo temporal y lo reemplaza al terminar."""
    temporal = ruta + ".tmp"
    with open(temporal, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)
    os.replace(temporal, ruta)
