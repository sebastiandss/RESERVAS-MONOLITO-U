"""Ayudas para el alta y el cambio de estado de reservas."""

from service.exceptions.excepciones import ErrorReserva


def verificar_registro(registros, registro_id, mensaje):
    """Lanza ErrorReserva si no existe un registro con ese ID."""
    for registro in registros:
        if registro["id"] == registro_id:
            return
    raise ErrorReserva(mensaje)


def siguiente_id_reserva(reservas):
    """Devuelve el siguiente ID entero (máximo + 1)."""
    ids = [int(r["id"]) for r in reservas if str(r.get("id", "")).isdigit()]
    return max(ids, default=0) + 1


def buscar_reserva(reservas, id_reserva):
    """Devuelve la reserva con ese ID o lanza un error."""
    for reserva in reservas:
        if reserva["id"] == id_reserva:
            return reserva
    raise ErrorReserva("No existe ninguna reserva con ese ID.")


def hay_conflicto_aprobada(reservas, reserva, id_reserva):
    """Indica si otra Aprobada ocupa la misma fecha y franja."""
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


def hay_conflicto(reservas, espacio_id, fecha, inicio, fin):
    """Indica si una Aprobada ocupa ese espacio en esa fecha y franja."""
    reserva = {"espacio_id": espacio_id, "fecha": fecha,
               "hora_inicio": inicio, "hora_fin": fin}
    return hay_conflicto_aprobada(reservas, reserva, None)
