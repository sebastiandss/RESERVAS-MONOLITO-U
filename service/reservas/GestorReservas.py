"""Registro de reservas con validaciones y control de solapes."""

from modelos.reserva import crear_reserva
from service.datos.almacen_json import cargar_datos, guardar_datos
from service.exceptions.excepciones import ErrorReserva
from service.reservas.apoyo_reservas import (
    hay_conflicto,
    siguiente_id,
    verificar_registro,
)
from service.reservas.validaciones_reservas import (
    validar_actividad,
    validar_fecha_y_horario,
)

RUTA_USUARIOS = "data/usuarios.json"
RUTA_ESPACIOS = "data/espacios.json"
RUTA_RESERVAS = "data/reservas.json"


def registrar_reserva(espacio_id, usuario_id, fecha, hora_inicio, hora_fin,
                      actividad, fecha_actual):
    """Registra una solicitud de reserva con estado Pendiente."""
    validar_actividad(actividad)

    usuarios = cargar_datos(RUTA_USUARIOS)
    verificar_registro(usuarios, usuario_id, "Ese usuario no está registrado.")

    espacios = cargar_datos(RUTA_ESPACIOS)
    verificar_registro(espacios, espacio_id, "Ese espacio no está registrado.")

    validar_fecha_y_horario(fecha, hora_inicio, hora_fin, fecha_actual)

    reservas = cargar_datos(RUTA_RESERVAS)
    if hay_conflicto(reservas, espacio_id, fecha, hora_inicio, hora_fin):
        raise ErrorReserva("Ese espacio ya está ocupado en ese horario.")

    nueva_reserva = crear_reserva(
        siguiente_id(reservas), espacio_id, usuario_id, fecha,
        hora_inicio, hora_fin, actividad, "Pendiente",
    )
    reservas.append(nueva_reserva)
    guardar_datos(RUTA_RESERVAS, reservas)
    return nueva_reserva
