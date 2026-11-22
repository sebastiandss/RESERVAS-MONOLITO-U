"""Funciones de apoyo para el cambio de estado de reservas."""

from service.exceptions.excepciones import ErrorReserva


def buscar_reserva(reservas, id_reserva):
    """Devuelve la reserva con ese ID o lanza un error."""
    for reserva in reservas:
        if reserva["id"] == id_reserva:
            return reserva
    raise ErrorReserva("No existe ninguna reserva con ese ID.")


def hay_conflicto_aprobada(reservas, reserva, id_reserva):
    """Indica si otra reserva Aprobada ocupa la misma fecha y franja."""
    for otra in reservas:
        if otra["id"] == id_reserva:
            continue
        mismo_espacio = otra["espacio_id"] == reserva["espacio_id"]
        mismo_dia = otra["fecha"] == reserva["fecha"]
        esta_aprobada = otra["estado"] == "Aprobada"
        se_cruza = (reserva["hora_inicio"] < otra["hora_fin"]
                    and reserva["hora_fin"] > otra["hora_inicio"])
        if mismo_espacio and mismo_dia and esta_aprobada and se_cruza:
            return True
    return False
