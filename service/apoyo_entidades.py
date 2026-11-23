"""Ayudas compartidas por espacios y usuarios."""

from service.datos.almacen_json import cargar_datos


def siguiente_id(registros):
    """Devuelve el siguiente ID entero (máximo + 1)."""
    ids = [int(r["id"]) for r in registros if str(r.get("id", "")).isdigit()]
    return max(ids, default=0) + 1


def reservas_de(reservas, id_registro, clave, clave_vieja):
    """Devuelve las reservas vinculadas a un registro por ambas claves."""
    valor = str(id_registro)
    return [
        reserva for reserva in reservas
        if str(reserva.get(clave, "")) == valor
        or str(reserva.get(clave_vieja, "")) == valor
    ]


def reservas_del_espacio(id_espacio, ruta_reservas):
    """Devuelve las reservas del espacio, incluida la clave vieja."""
    return reservas_de(cargar_datos(ruta_reservas), id_espacio,
                       "espacio_id", "id_espacio")


def reservas_del_usuario(id_usuario, ruta_reservas):
    """Devuelve las reservas del usuario, incluida la clave vieja."""
    return reservas_de(cargar_datos(ruta_reservas), id_usuario,
                       "usuario_id", "id_usuario")


def clave_orden(usuario):
    """Devuelve el nombre en minúsculas para ordenar usuarios."""
    return str(usuario.get("nombre", "")).lower()
