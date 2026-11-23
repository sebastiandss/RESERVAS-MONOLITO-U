"""Ayudas compartidas por la lógica de reservas."""

from service.exceptions import ErrorReserva

ESTADOS_ACTIVOS = ("Pendiente", "Aprobada")


def se_cruzan(inicio, fin, reserva):
    """Indica si la franja consultada se solapa con la de la reserva."""
    return inicio < reserva["hora_fin"] and fin > reserva["hora_inicio"]


def esta_activa(reserva):
    """Solo Pendiente y Aprobada cuentan como reservas activas."""
    return reserva["estado"] in ESTADOS_ACTIVOS


def hay_conflicto(reservas, espacio_id, fecha, inicio, fin, ignorar_id=None):
    """Indica si una Aprobada ocupa ese espacio en esa fecha y franja."""
    for reserva in reservas:
        if (reserva["espacio_id"] == espacio_id
                and reserva["fecha"] == fecha
                and reserva["estado"] == "Aprobada"
                and (ignorar_id is None or reserva["id"] != ignorar_id)
                and se_cruzan(inicio, fin, reserva)):
            return True
    return False


def nombre_registro(registros, registro_id, defecto):
    """Devuelve el nombre del registro con ese ID."""
    for registro in registros:
        if registro["id"] == registro_id:
            return registro["nombre"]
    return defecto


def buscar_reserva(reservas, id_reserva):
    """Devuelve la reserva con ese ID o lanza un error."""
    for reserva in reservas:
        if reserva["id"] == id_reserva:
            return reserva
    raise ErrorReserva("No existe ninguna reserva con ese ID.")


def verificar_registro(registros, registro_id, mensaje):
    """Lanza ErrorReserva si no existe un registro con ese ID."""
    for registro in registros:
        if registro["id"] == registro_id:
            return
    raise ErrorReserva(mensaje)
