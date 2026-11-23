"""Consulta de reservas coincidentes (RF-06)."""

from service.datos.almacen_json import cargar_datos
from service.apoyo_consultas import esta_activa, se_cruzan
from service.reservas.validaciones_consultas import sin_resultados, validar_consulta

RUTA_RESERVAS = "data/reservas.json"


def consultar_reservas_coincidentes(espacio_id, fecha, hora_inicio, hora_fin):
    """Lista las reservas activas que se cruzan con la franja pedida."""
    validar_consulta(fecha, hora_inicio, hora_fin)
    reservas = cargar_datos(RUTA_RESERVAS)

    coincidentes = []
    for reserva in reservas:
        if (esta_activa(reserva)
                and reserva["espacio_id"] == espacio_id
                and reserva["fecha"] == fecha
                and se_cruzan(hora_inicio, hora_fin, reserva)):
            coincidentes.append(reserva)

    if not coincidentes:
        sin_resultados("No se encontraron reservas coincidentes en ese horario.")
    return coincidentes
