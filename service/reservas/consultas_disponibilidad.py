"""Consulta de espacios disponibles en una fecha y franja (RF-08)."""

from service.datos.almacen_json import cargar_datos
from service.reservas.apoyo_consultas import ocupada_por_aprobada
from service.reservas.validaciones_consultas import sin_resultados, validar_consulta

RUTA_ESPACIOS = "data/espacios.json"
RUTA_RESERVAS = "data/reservas.json"


def consultar_espacios_disponibles(fecha, hora_inicio, hora_fin):
    """Lista los espacios sin reservas Aprobadas en la franja pedida."""
    validar_consulta(fecha, hora_inicio, hora_fin)
    espacios = cargar_datos(RUTA_ESPACIOS)
    reservas = cargar_datos(RUTA_RESERVAS)

    libres = []
    for espacio in espacios:
        if not ocupada_por_aprobada(
                reservas, espacio["id"], fecha, hora_inicio, hora_fin):
            libres.append(espacio)

    if not libres:
        sin_resultados("No hay espacios disponibles en esa fecha y horario.")
    return libres
