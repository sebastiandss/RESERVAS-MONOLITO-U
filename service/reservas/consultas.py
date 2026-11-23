"""Consultas sobre reservas (API única)."""

from models.espacio import Espacio
from models.reserva import Reserva
from service.datos.almacen_json import (
    RUTA_ESPACIOS, RUTA_RESERVAS, RUTA_USUARIOS, cargar_datos,
)
from service.reservas.apoyo import (
    esta_activa, hay_conflicto, nombre_registro, se_cruzan,
)
from service.reservas.validaciones import sin_resultados, validar_fecha_y_horario


def consultar_quien_tiene_espacios(fecha):
    """Lista las reservas Aprobadas de una fecha con nombres legibles."""
    validar_fecha_y_horario(fecha)
    reservas = [Reserva.desde_datos(r) for r in cargar_datos(RUTA_RESERVAS)]
    espacios = cargar_datos(RUTA_ESPACIOS)
    usuarios = cargar_datos(RUTA_USUARIOS)

    resultados = []
    for reserva in reservas:
        if reserva["fecha"] == fecha and reserva.esta_aprobada():
            resultados.append({
                "espacio": nombre_registro(
                    espacios, reserva["espacio_id"], "Espacio no encontrado"),
                "usuario": nombre_registro(
                    usuarios, reserva["usuario_id"], "Usuario no encontrado"),
                "hora_inicio": reserva["hora_inicio"],
                "hora_fin": reserva["hora_fin"],
                "estado": reserva["estado"],
            })

    if not resultados:
        sin_resultados("No hay espacios reservados para esa fecha.")
    return resultados


def consultar_espacios_disponibles(fecha, hora_inicio, hora_fin):
    """Lista los espacios sin reservas Aprobadas en la franja pedida."""
    validar_fecha_y_horario(fecha, hora_inicio, hora_fin)
    espacios = [Espacio.desde_datos(e) for e in cargar_datos(RUTA_ESPACIOS)]
    reservas = [Reserva.desde_datos(r) for r in cargar_datos(RUTA_RESERVAS)]

    libres = [
        espacio for espacio in espacios
        if not hay_conflicto(
            reservas, espacio["id"], fecha, hora_inicio, hora_fin)
    ]
    if not libres:
        sin_resultados("No hay espacios disponibles en esa fecha y horario.")
    return libres


def consultar_reservas_coincidentes(espacio_id, fecha, hora_inicio, hora_fin):
    """Lista las reservas activas que se cruzan con la franja pedida."""
    validar_fecha_y_horario(fecha, hora_inicio, hora_fin)
    reservas = [Reserva.desde_datos(r) for r in cargar_datos(RUTA_RESERVAS)]

    coincidentes = [
        reserva for reserva in reservas
        if (esta_activa(reserva)
                and reserva["espacio_id"] == espacio_id
                and reserva["fecha"] == fecha
                and se_cruzan(hora_inicio, hora_fin, reserva))
    ]
    if not coincidentes:
        sin_resultados("No se encontraron reservas coincidentes en ese horario.")
    return coincidentes
