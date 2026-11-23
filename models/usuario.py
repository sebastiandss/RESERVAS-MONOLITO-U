"""Modelo de datos para la entidad Usuario."""


def crear_usuario(id_usuario, nombre, documento, telefono):
    """Crea y devuelve un diccionario con los datos de un usuario."""
    return {
        "id": id_usuario,
        "nombre": nombre,
        "documento": documento,
        "telefono": telefono
    }

