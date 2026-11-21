import json

path = "usuarios.json"

# 1. Leer el archivo
with open(path, "r") as archivo:
    datos = json.load(archivo)

# 2. Crear el usuario
nuevo_usuario = {
    "id": len(datos) + 1,
    "nombre": input("Nombre: "),
    "documento": input("Documento: "),
    "telefono": input("Teléfono: ")
}

# 3. Agregarlo a la lista
datos.append(nuevo_usuario)

# 4. Guardar en el archivo
with open(path, "w") as archivo:
    json.dump(datos, archivo, indent=4)

print(datos)