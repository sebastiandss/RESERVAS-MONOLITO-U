from models.usuario import crear_usuario
from service.datos.almacen_json import cargar_datos, guardar_datos
from service.exceptions.excepciones import ErrorReserva
from service.usuarios.apoyo_usuarios import clave_orden, reservas_del_usuario, siguiente_id
from service.usuarios.validaciones_usuarios import (
    normalizar_documento,
    normalizar_nombre,
    normalizar_telefono,
    validar_documento_unico,
)

RUTA_USUARIOS = "data/usuarios.json"
RUTA_RESERVAS = "data/reservas.json"

def agregar_usuario(nombre, documento, telefono, ruta_usuarios=RUTA_USUARIOS):
    nombre = normalizar_nombre(nombre)
    documento = normalizar_documento(documento)
    telefono = normalizar_telefono(telefono)
    usuarios = cargar_datos(ruta_usuarios)
    validar_documento_unico(documento, usuarios)
    usuario = crear_usuario(siguiente_id(usuarios), nombre, documento, telefono)
    usuarios.append(usuario)
    guardar_datos(ruta_usuarios, usuarios)
    return usuario

def listar_usuarios(ruta_usuarios=RUTA_USUARIOS):
    usuarios = cargar_datos(ruta_usuarios)
    return sorted(usuarios, key=clave_orden)

def eliminar_usuario(id_usuario, ruta_usuarios=RUTA_USUARIOS, ruta_reservas=RUTA_RESERVAS):
    usuarios = cargar_datos(ruta_usuarios)
    usuario = None
    for item in usuarios:
        if item.get("id") == id_usuario:
            usuario = item
            break
    if usuario is None:
        raise ErrorReserva("No existe un usuario con ese ID.")
    reservas = reservas_del_usuario(id_usuario, ruta_reservas)
    if reservas:
        raise ErrorReserva("No se puede eliminar el usuario porque tiene reservas.")
    usuarios.remove(usuario)
    guardar_datos(ruta_usuarios, usuarios)
    return True
