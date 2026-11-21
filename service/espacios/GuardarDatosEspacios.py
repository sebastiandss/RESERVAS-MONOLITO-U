import json
from service.espacios.EntradaDeDatosEspacios import pedir_datos_espacio

def guardar_espacio(nuevo_espacio, ruta="data/espacios.json"):
    if nuevo_espacio is None:
        return

    archivo = open(ruta, "r", encoding="utf-8")
    espacios = json.load(archivo)
    archivo.close()

    espacios.append(nuevo_espacio)

    archivo = open(ruta, "w", encoding="utf-8")
    json.dump(espacios, archivo, indent=4, ensure_ascii=False)
    archivo.close()

    print("Espacio guardado correctamente.")

if __name__ == "__main__":
    datos = pedir_datos_espacio()
    guardar_espacio(datos)