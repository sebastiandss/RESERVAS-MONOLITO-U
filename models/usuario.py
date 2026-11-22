"""Modelo de datos para la entidad Usuario."""


def crear_usuario(id_usuario, nombre, documento, telefono):
    """Crea y devuelve un diccionario con los datos de un usuario."""
    return {
        "id": id_usuario,
        "nombre": nombre,
        "documento": documento,
        "telefono": telefono
    }


def campos_usuario():
    """Devuelve la lista de campos de la entidad Usuario."""
    return ["id", "nombre", "documento", "telefono"]
