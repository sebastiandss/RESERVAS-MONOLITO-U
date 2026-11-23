"""Modelo de datos para la entidad Reserva."""

ESTADOS_RESERVA = ("Pendiente", "Aprobada", "Rechazada", "Cancelada")


class Reserva(dict):
    """Representa una reserva y centraliza sus reglas de estado y solape."""

    ESTADOS = ESTADOS_RESERVA
    ESTADOS_ACTIVOS = ("Pendiente", "Aprobada")

    def __init__(self, id_reserva, espacio_id, usuario_id, fecha,
                 hora_inicio, hora_fin, actividad, estado):
        super().__init__(
            id=id_reserva,
            espacio_id=espacio_id,
            usuario_id=usuario_id,
            fecha=fecha,
            hora_inicio=hora_inicio,
            hora_fin=hora_fin,
            actividad=actividad,
            estado=estado,
        )

    @classmethod
    def desde_datos(cls, datos):
        """Convierte un registro guardado en una instancia de Reserva."""
        if isinstance(datos, cls):
            return datos
        reserva = cls(
            datos["id"], datos["espacio_id"], datos["usuario_id"],
            datos["fecha"], datos["hora_inicio"], datos["hora_fin"],
            datos["actividad"], datos["estado"],
        )
        reserva.update({clave: valor for clave, valor in datos.items()
                        if clave not in reserva})
        return reserva

    @classmethod
    def es_estado_valido(cls, estado):
        """Indica si el estado está entre los definidos para una reserva."""
        return estado in cls.ESTADOS

    def esta_activa(self):
        """Pendiente y Aprobada son los estados que cuentan como activos."""
        return self["estado"] in self.ESTADOS_ACTIVOS

    def esta_aprobada(self):
        """Indica si la reserva ya ocupa efectivamente el espacio."""
        return self["estado"] == "Aprobada"

    def se_cruzan(self, inicio, fin):
        """Indica si la franja consultada se solapa con esta reserva."""
        return inicio < self["hora_fin"] and fin > self["hora_inicio"]


def crear_reserva(id_reserva, espacio_id, usuario_id, fecha,
                  hora_inicio, hora_fin, actividad, estado):
    """Crea y devuelve una Reserva con los datos de una reserva."""
    return Reserva(
        id_reserva, espacio_id, usuario_id, fecha,
        hora_inicio, hora_fin, actividad, estado,
    )
