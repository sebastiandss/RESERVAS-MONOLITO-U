"""Cambio de estado de reservas existentes."""

from service.datos.almacen_json import cargar_datos, guardar_datos
from service.exceptions.excepciones import ErrorReserva
from service.reservas.apoyo_estados import buscar_reserva, hay_conflicto_aprobada
from service.reservas.validaciones_estados import validar_estado

RUTA_RESERVAS = "data/reservas.json"


def cambiar_estado_reserva(id_reserva, nuevo_estado):
    """Cambia el estado de una reserva y guarda el resultado."""
    validar_estado(nuevo_estado)

    reservas = cargar_datos(RUTA_RESERVAS)
    reserva = buscar_reserva(reservas, id_reserva)

    if nuevo_estado == "Aprobada" and hay_conflicto_aprobada(
            reservas, reserva, id_reserva):
        raise ErrorReserva(
            "No se puede aprobar porque se cruza con otra reserva aprobada."
        )

    reserva["estado"] = nuevo_estado
    guardar_datos(RUTA_RESERVAS, reservas)
    return reserva
