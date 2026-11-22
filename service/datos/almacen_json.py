import json


def cargar_datos(ruta):
    archivo = open(ruta, "r", encoding="utf-8")
    contenido = archivo.read()
    archivo.close()
    if contenido.strip() == "":
        return []
    return json.loads(contenido)


def guardar_datos(ruta, datos):
    archivo = open(ruta, "w", encoding="utf-8")
    json.dump(datos, archivo, indent=4, ensure_ascii=False)
    archivo.close()
