"""Ayudas compartidas por la lógica de reservas."""

from models.reserva import Reserva
from service.exceptions import ErrorReserva


def se_cruzan(inicio, fin, reserva):
    """Indica si la franja consultada se solapa con la de la reserva."""
    return Reserva.desde_datos(reserva).se_cruzan(inicio, fin)


def esta_activa(reserva):
    """Solo Pendiente y Aprobada cuentan como reservas activas."""
    return Reserva.desde_datos(reserva).esta_activa()


def hay_conflicto(reservas, espacio_id, fecha, inicio, fin, ignorar_id=None):
    """Indica si una Aprobada ocupa ese espacio en esa fecha y franja."""
    for datos in reservas:
        reserva = Reserva.desde_datos(datos)
        if (reserva["espacio_id"] == espacio_id
                and reserva["fecha"] == fecha
                and reserva.esta_aprobada()
                and (ignorar_id is None or reserva["id"] != ignorar_id)
                and reserva.se_cruzan(inicio, fin)):
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
            return Reserva.desde_datos(reserva)
    raise ErrorReserva("No existe ninguna reserva con ese ID.")


def verificar_registro(registros, registro_id, mensaje):
    """Lanza ErrorReserva si no existe un registro con ese ID."""
    for registro in registros:
        if registro["id"] == registro_id:
            return
    raise ErrorReserva(mensaje)
