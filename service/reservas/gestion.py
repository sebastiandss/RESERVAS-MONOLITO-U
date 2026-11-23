"""Alta y cambio de estado de reservas."""

from models.reserva import crear_reserva
from service.apoyo_entidades import siguiente_id
from service.datos.almacen_json import (
    RUTA_ESPACIOS, RUTA_RESERVAS, RUTA_USUARIOS, cargar_datos, guardar_datos,
)
from service.exceptions import ErrorReserva
from service.reservas.apoyo import (
    buscar_reserva, hay_conflicto, se_cruzan, verificar_registro,
)
from service.reservas.validaciones import (
    validar_actividad, validar_estado, validar_fecha_y_horario,
)


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

    nueva = crear_reserva(
        siguiente_id(reservas), espacio_id, usuario_id, fecha,
        hora_inicio, hora_fin, actividad, "Pendiente",
    )
    reservas.append(nueva)
    guardar_datos(RUTA_RESERVAS, reservas)
    _avisar_pendientes(nueva, reservas)
    return nueva


def cambiar_estado_reserva(id_reserva, nuevo_estado):
    """Cambia el estado de una reserva y guarda el resultado."""
    validar_estado(nuevo_estado)

    reservas = cargar_datos(RUTA_RESERVAS)
    reserva = buscar_reserva(reservas, id_reserva)

    if nuevo_estado == "Aprobada" and hay_conflicto(
            reservas, reserva["espacio_id"], reserva["fecha"],
            reserva["hora_inicio"], reserva["hora_fin"], id_reserva):
        raise ErrorReserva(
            "No se puede aprobar porque se cruza con otra reserva aprobada."
        )

    reserva["estado"] = nuevo_estado
    guardar_datos(RUTA_RESERVAS, reservas)
    return reserva


def _avisar_pendientes(reserva, reservas):
    """Agrega un aviso transitorio si hay Pendientes coincidentes (RN-05)."""
    coincidencias = [
        otra for otra in reservas
        if otra["estado"] == "Pendiente"
        and otra["id"] != reserva["id"]
        and otra["espacio_id"] == reserva["espacio_id"]
        and otra["fecha"] == reserva["fecha"]
        and se_cruzan(reserva["hora_inicio"], reserva["hora_fin"], otra)
    ]
    if coincidencias:
        reserva["aviso"] = (
            f"Aviso: hay {len(coincidencias)} reserva(s) Pendiente "
            "que coinciden con esta solicitud."
        )
