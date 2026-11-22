from modelos.espacio import crear_espacio
from service.datos.almacen_json import cargar_datos, guardar_datos
from service.exceptions.excepciones import ErrorReserva
from service.GeracionIdUnicos import generar_id, existe_id

RUTA_ESPACIOS = "data/espacios.json"
RUTA_RESERVAS = "data/reservas.json"

def agregar_espacio(nombre, capacidad, descripcion=""):
    if nombre == "" or nombre is None:
        raise ErrorReserva("El nombre del espacio es obligatorio.")

    if not str(capacidad).isdigit() or int(capacidad) <= 0:
        raise ErrorReserva("La capacidad debe ser un número mayor a 0.")

    espacios = cargar_datos(RUTA_ESPACIOS)

    for espacio in espacios:
        if espacio["nombre"].lower() == nombre.lower():
            raise ErrorReserva("Ya existe un espacio con ese nombre.")

    nuevo_id = generar_id()
    while existe_id(nuevo_id, espacios, "id"):
        nuevo_id = generar_id()

    nuevo_espacio = crear_espacio(nuevo_id, nombre, int(capacidad), descripcion)
    espacios.append(nuevo_espacio)
    guardar_datos(RUTA_ESPACIOS, espacios)

    return nuevo_espacio

def listar_espacios():

    return cargar_datos(RUTA_ESPACIOS)

def eliminar_espacio(id_espacio):
    espacios = cargar_datos(RUTA_ESPACIOS)

    espacio_encontrado = None
    for espacio in espacios:
        if espacio["id"] == id_espacio:
            espacio_encontrado = espacio
            break

    if espacio_encontrado is None:
        raise ErrorReserva("No existe un espacio con ese ID.")

    reservas = cargar_datos(RUTA_RESERVAS)
    for reserva in reservas:
        if "espacio_id" in reserva and reserva["espacio_id"] == id_espacio:
            raise ErrorReserva("No se puede eliminar el espacio porque tiene reservas.")
        if "id_espacio" in reserva and reserva["id_espacio"] == id_espacio:
            raise ErrorReserva("No se puede eliminar el espacio porque tiene reservas.")
  
    espacios.remove(espacio_encontrado)
    guardar_datos(RUTA_ESPACIOS, espacios)

    return True