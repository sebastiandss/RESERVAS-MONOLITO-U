"""Validaciones para altas, cambios de estado y consultas de reservas."""

from models.reserva import Reserva
from service.exceptions import ErrorReserva
from service.exceptions.fechas import validar_fecha
from service.exceptions.horas import validar_rango_horas


def validar_actividad(actividad):
    """Rechaza una actividad vacía."""
    if actividad == "" or actividad is None:
        raise ErrorReserva("Escribe cuál es la actividad de la reserva.")


def validar_fecha_y_horario(fecha, hora_inicio=None, hora_fin=None,
                            fecha_actual=None):
    """Valida fecha y franja; con fecha actual, prohíbe reservar en el pasado."""
    validar_fecha(fecha)
    if fecha_actual is not None:
        validar_fecha(fecha_actual)
    if hora_inicio is not None:
        validar_rango_horas(hora_inicio, hora_fin)
    if fecha_actual is not None and fecha < fecha_actual:
        raise ErrorReserva("No puedes reservar en una fecha que ya pasó.")


def validar_estado(nuevo_estado):
    """Acepta solo los estados definidos en el modelo."""
    if not Reserva.es_estado_valido(nuevo_estado):
        raise ErrorReserva(
            "Estado no válido. Solo se permite: Pendiente, Aprobada, "
            "Rechazada o Cancelada."
        )


def sin_resultados(mensaje):
    """Lanza un aviso claro cuando una consulta no devuelve filas."""
    raise ErrorReserva(mensaje)
