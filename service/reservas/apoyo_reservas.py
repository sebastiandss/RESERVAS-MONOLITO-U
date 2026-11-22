"""Funciones de apoyo para el registro de reservas."""

from service.exceptions.excepciones import ErrorReserva
from service.GeracionIdUnicos import existe_id, generar_id


def verificar_registro(registros, registro_id, mensaje):
    """Lanza ErrorReserva si no existe un registro con ese ID."""
    for registro in registros:
        if registro["id"] == registro_id:
            return
    raise ErrorReserva(mensaje)


def hay_conflicto(reservas, espacio_id, fecha, hora_inicio, hora_fin):
    """Indica si una reserva Aprobada ocupa la misma fecha y franja."""
    for reserva in reservas:
        mismo_espacio = reserva["espacio_id"] == espacio_id
        mismo_dia = reserva["fecha"] == fecha
        esta_aprobada = reserva["estado"] == "Aprobada"
        se_cruza = (hora_inicio < reserva["hora_fin"]
                    and hora_fin > reserva["hora_inicio"])
        if mismo_espacio and mismo_dia and esta_aprobada and se_cruza:
            return True
    return False


def siguiente_id(reservas):
    """Devuelve un ID único con el generador actual (sin cambios)."""
    nuevo_id = generar_id()
    while existe_id(nuevo_id, reservas, "id"):
        nuevo_id = generar_id()
    return nuevo_id
