"""Aviso automático de solicitudes Pendiente que coinciden (RN-05)."""

from service.apoyo_consultas import se_cruzan


def aviso_para(nueva_reserva, reservas):
    """Agrega un aviso transitorio a la reserva devuelta, sin persistirlo."""
    coincidencias = [
        reserva for reserva in reservas
        if reserva["estado"] == "Pendiente"
        and reserva["id"] != nueva_reserva["id"]
        and reserva["espacio_id"] == nueva_reserva["espacio_id"]
        and reserva["fecha"] == nueva_reserva["fecha"]
        and se_cruzan(nueva_reserva["hora_inicio"],
                      nueva_reserva["hora_fin"], reserva)
    ]
    if coincidencias:
        nueva_reserva["aviso"] = (
            f"Aviso: hay {len(coincidencias)} reserva(s) Pendiente "
            "que coinciden con esta solicitud."
        )
    return nueva_reserva
