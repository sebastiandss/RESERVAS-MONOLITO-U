"""Validaciones para el cambio de estado de reservas."""

from models.reserva import ESTADOS_RESERVA
from service.exceptions.excepciones import ErrorReserva


def validar_estado(nuevo_estado):
    """Acepta solo los estados definidos en el modelo."""
    if nuevo_estado not in ESTADOS_RESERVA:
        raise ErrorReserva(
            "Estado no válido. Solo se permite: Pendiente, Aprobada, "
            "Rechazada o Cancelada."
        )
