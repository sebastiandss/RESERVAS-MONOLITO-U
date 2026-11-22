"""Consultas sobre reservas (API única)."""

from service.reservas.consultas_asignaciones import consultar_quien_tiene_espacios
from service.reservas.consultas_coincidentes import consultar_reservas_coincidentes
from service.reservas.consultas_disponibilidad import consultar_espacios_disponibles

__all__ = [
    "consultar_quien_tiene_espacios",
    "consultar_espacios_disponibles",
    "consultar_reservas_coincidentes",
]
