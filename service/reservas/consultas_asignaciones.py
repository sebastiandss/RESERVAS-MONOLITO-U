"""Consulta de asignaciones por fecha (RF-09)."""

from service.datos.almacen_json import cargar_datos
from service.apoyo_consultas import nombre_registro
from service.reservas.validaciones_consultas import sin_resultados, validar_consulta

RUTA_USUARIOS = "data/usuarios.json"
RUTA_ESPACIOS = "data/espacios.json"
RUTA_RESERVAS = "data/reservas.json"


def consultar_quien_tiene_espacios(fecha):
    """Lista las reservas Aprobadas de una fecha con nombres legibles."""
    validar_consulta(fecha)
    reservas = cargar_datos(RUTA_RESERVAS)
    espacios = cargar_datos(RUTA_ESPACIOS)
    usuarios = cargar_datos(RUTA_USUARIOS)

    resultados = []
    for reserva in reservas:
        if reserva["fecha"] == fecha and reserva["estado"] == "Aprobada":
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
