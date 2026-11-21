import json
from service.usuarios.EntradaDeDatosUsuarios import pedir_datos
from service.GeracionIdUnicos import generar_id, existe_id

def guardar_usuario(nuevo_usuario, ruta="data/usuarios.json"):
    if nuevo_usuario is None:
        return

    archivo = open(ruta, "r", encoding="utf-8")
    usuarios = json.load(archivo)
    archivo.close()

    codigo = generar_id()
    while existe_id(codigo, usuarios, "id_usuario"):
        codigo = generar_id()
    nuevo_usuario["id_usuario"] = codigo

    usuarios.append(nuevo_usuario)

    archivo = open(ruta, "w", encoding="utf-8")
    json.dump(usuarios, archivo, indent=4, ensure_ascii=False)
    archivo.close()

    print("Usuario guardado correctamente con ID:", codigo)

if __name__ == "__main__":
    datos = pedir_datos()
    guardar_usuario(datos)