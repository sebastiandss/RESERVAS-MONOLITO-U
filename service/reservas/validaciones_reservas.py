"""Validaciones para el alta de reservas."""

from service.exceptions.excepciones import ErrorReserva
from service.exceptions.fechas import validar_fecha
from service.exceptions.horas import validar_rango_horas


def validar_actividad(actividad):
    """Rechaza una actividad vacía."""
    if actividad == "" or actividad is None:
        raise ErrorReserva("Escribe cuál es la actividad de la reserva.")


def validar_fecha_y_horario(fecha, hora_inicio, hora_fin, fecha_actual):
    """Valida fechas, franja horaria y que la reserva no sea pasada."""
    validar_fecha(fecha)
    validar_fecha(fecha_actual)
    validar_rango_horas(hora_inicio, hora_fin)
    if fecha < fecha_actual:
        raise ErrorReserva("No puedes reservar en una fecha que ya pasó.")
