from service.datos.almacen_json import cargar_datos, guardar_datos
from service.exceptions.excepciones import ErrorReserva
from service.GeracionIdUnicos import generar_id, existe_id

RUTA_USUARIOS = "data/usuarios.json"
RUTA_RESERVAS = "data/reservas.json"


def agregar_usuario(nombre, documento, telefono):

    if nombre == "" or nombre is None:
        raise ErrorReserva("El nombre del usuario es obligatorio.")

    if documento == "" or documento is None:
        raise ErrorReserva("El documento del usuario es obligatorio.")

    if telefono == "" or telefono is None:
        raise ErrorReserva("El teléfono del usuario es obligatorio.")

  
    if not str(documento).isdigit():
        raise ErrorReserva("El documento debe contener solo números.")

    usuarios = cargar_datos(RUTA_USUARIOS)


    for usuario in usuarios:
        if str(usuario["documento"]) == str(documento):
            raise ErrorReserva("Ya existe un usuario con ese documento.")

  
    nuevo_id = generar_id()
    while existe_id(nuevo_id, usuarios, "id"):
        nuevo_id = generar_id()

    nuevo_usuario = {
        "id": nuevo_id,
        "nombre": nombre,
        "documento": str(documento),
        "telefono": str(telefono)
    }

    usuarios.append(nuevo_usuario)
    guardar_datos(RUTA_USUARIOS, usuarios)

    return nuevo_usuario


def listar_usuarios():
    return cargar_datos(RUTA_USUARIOS)

def eliminar_usuario(id_usuario):
    usuarios = cargar_datos(RUTA_USUARIOS)

    usuario_encontrado = None
    for usuario in usuarios:
        if usuario["id"] == id_usuario:
            usuario_encontrado = usuario
            break

    if usuario_encontrado is None:
        raise ErrorReserva("No existe un usuario con ese ID.")

    reservas = cargar_datos(RUTA_RESERVAS)
    for reserva in reservas:
        if "usuario_id" in reserva and reserva["usuario_id"] == id_usuario:
            raise ErrorReserva("No se puede eliminar el usuario porque tiene reservas.")
        if "id_usuario" in reserva and reserva["id_usuario"] == id_usuario:
            raise ErrorReserva("No se puede eliminar el usuario porque tiene reservas.")

    usuarios.remove(usuario_encontrado)
    guardar_datos(RUTA_USUARIOS, usuarios)

    return True