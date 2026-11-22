from service.datos.almacen_json import cargar_datos


def siguiente_id(espacios):
    ids = [int(e["id"]) for e in espacios if str(e.get("id", "")).isdigit()]
    return max(ids, default=0) + 1


def reservas_del_espacio(id_espacio, ruta_reservas):
    reservas = cargar_datos(ruta_reservas)
    clave = str(id_espacio)
    return [
        reserva for reserva in reservas
        if str(reserva.get("espacio_id", "")) == clave
        or str(reserva.get("id_espacio", "")) == clave
    ]
