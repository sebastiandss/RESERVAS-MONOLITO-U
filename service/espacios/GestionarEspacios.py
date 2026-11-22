from modelos.espacio import crear_espacio
from service.datos.almacen_json import cargar_datos, guardar_datos
from service.exceptions.excepciones import ErrorReserva
from service.espacios.apoyo_espacios import reservas_del_espacio, siguiente_id
from service.espacios.validaciones_espacios import (
    normalizar_nombre,
    validar_capacidad,
    validar_nombre_unico,
)

RUTA_ESPACIOS = "data/espacios.json"
RUTA_RESERVAS = "data/reservas.json"


def agregar_espacio(nombre, capacidad, descripcion="", ruta_espacios=RUTA_ESPACIOS):
    nombre = normalizar_nombre(nombre)
    capacidad = validar_capacidad(capacidad)
    espacios = cargar_datos(ruta_espacios)
    validar_nombre_unico(nombre, espacios)
    espacio = crear_espacio(siguiente_id(espacios), nombre, capacidad, descripcion)
    espacios.append(espacio)
    guardar_datos(ruta_espacios, espacios)
    return espacio


def listar_espacios(ruta_espacios=RUTA_ESPACIOS):
    espacios = cargar_datos(ruta_espacios)
    return sorted(espacios, key=lambda e: str(e.get("nombre", "")).casefold())


def eliminar_espacio(id_espacio, ruta_espacios=RUTA_ESPACIOS, ruta_reservas=RUTA_RESERVAS):
    espacios = cargar_datos(ruta_espacios)
    espacio = next((e for e in espacios if e.get("id") == id_espacio), None)
    if espacio is None:
        raise ErrorReserva("No existe un espacio con ese ID.")
    reservas = reservas_del_espacio(id_espacio, ruta_reservas)
    if reservas:
        raise ErrorReserva(
            f"No se puede eliminar '{espacio['nombre']}' porque tiene "
            f"{len(reservas)} reserva(s) asociada(s)."
        )
    espacios.remove(espacio)
    guardar_datos(ruta_espacios, espacios)
    return True
