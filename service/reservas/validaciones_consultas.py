"""Validaciones y avisos para las consultas de reservas."""

from service.exceptions.excepciones import ErrorReserva
from service.exceptions.fechas import validar_fecha
from service.exceptions.horas import validar_rango_horas


def validar_consulta(fecha, hora_inicio=None, hora_fin=None):
    """Valida la fecha y, si se da, la franja horaria consultada."""
    validar_fecha(fecha)
    if hora_inicio is not None:
        validar_rango_horas(hora_inicio, hora_fin)


def sin_resultados(mensaje):
    """Lanza un aviso claro cuando una consulta no devuelve filas."""
    raise ErrorReserva(mensaje)
