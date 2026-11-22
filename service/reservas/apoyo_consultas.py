"""Funciones de apoyo para las consultas de reservas."""

ESTADOS_ACTIVOS = ("Pendiente", "Aprobada")


def nombre_registro(registros, registro_id, defecto):
    """Devuelve el nombre del registro con ese ID."""
    for registro in registros:
        if registro["id"] == registro_id:
            return registro["nombre"]
    return defecto


def se_cruzan(hora_inicio, hora_fin, reserva):
    """Indica si la franja consultada se cruza con la reserva."""
    return (hora_inicio < reserva["hora_fin"]
            and hora_fin > reserva["hora_inicio"])


def esta_activa(reserva):
    """Solo Pendiente y Aprobada cuentan como reservas activas."""
    return reserva["estado"] in ESTADOS_ACTIVOS


def ocupada_por_aprobada(reservas, espacio_id, fecha, inicio, fin):
    """Indica si una Aprobada ocupa el espacio en esa fecha y franja."""
    for reserva in reservas:
        if (reserva["espacio_id"] == espacio_id
                and reserva["fecha"] == fecha
                and reserva["estado"] == "Aprobada"
                and se_cruzan(inicio, fin, reserva)):
            return True
    return False
