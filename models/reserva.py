"""Modelo de datos para la entidad Reserva."""

ESTADOS_RESERVA = ("Pendiente", "Aprobada", "Rechazada", "Cancelada")


def crear_reserva(id_reserva, espacio_id, usuario_id, fecha,
                  hora_inicio, hora_fin, actividad, estado):
    """Crea y devuelve un diccionario con los datos de una reserva."""
    return {
        "id": id_reserva,
        "espacio_id": espacio_id,
        "usuario_id": usuario_id,
        "fecha": fecha,
        "hora_inicio": hora_inicio,
        "hora_fin": hora_fin,
        "actividad": actividad,
        "estado": estado
    }


def campos_reserva():
    """Devuelve la lista de campos de la entidad Reserva."""
    return [
        "id", "espacio_id", "usuario_id", "fecha",
        "hora_inicio", "hora_fin", "actividad", "estado"
    ]

