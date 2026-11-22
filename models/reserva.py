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


class Reserva:
    """Representa una reserva de espacio."""

    def __init__(self, id_reserva, espacio_id, usuario_id, fecha,
                 hora_inicio, hora_fin, actividad, estado):
        """Inicializa los datos de la reserva."""
        self.id = id_reserva
        self.espacio_id = espacio_id
        self.usuario_id = usuario_id
        self.fecha = fecha
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.actividad = actividad
        self.estado = estado

    def a_diccionario(self):
        """Convierte la reserva en diccionario."""
        return crear_reserva(self.id, self.espacio_id, self.usuario_id,
                             self.fecha, self.hora_inicio, self.hora_fin,
                             self.actividad, self.estado)

