"""Fachada orientada a objetos para las consultas del sistema."""

from service.reservas.consultas_reservas import (
    consultar_espacios_disponibles,
    consultar_quien_tiene_espacios,
    consultar_reservas_coincidentes,
)


class GestorConsultas:
    """Agrupa las consultas de reservas y disponibilidad."""

    def consultar_asignaciones(self, fecha):
        """Devuelve quién tiene cada espacio en una fecha."""
        return consultar_quien_tiene_espacios(fecha)

    def consultar_disponibles(self, fecha, hora_inicio, hora_fin):
        """Devuelve espacios disponibles en una fecha y franja."""
        return consultar_espacios_disponibles(fecha, hora_inicio, hora_fin)

    def consultar_coincidentes(self, espacio_id, fecha, hora_inicio, hora_fin):
        """Devuelve reservas que coinciden en espacio y franja."""
        return consultar_reservas_coincidentes(espacio_id, fecha,
                                               hora_inicio, hora_fin)
