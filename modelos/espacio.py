"""Modelo de datos para la entidad Espacio."""


def crear_espacio(id_espacio, nombre, capacidad, descripcion):
    """Crea y devuelve un diccionario con los datos de un espacio."""
    return {
        "id": id_espacio,
        "nombre": nombre,
        "capacidad": capacidad,
        "descripcion": descripcion
    }


def campos_espacio():
    """Devuelve la lista de campos de la entidad Espacio."""
    return ["id", "nombre", "capacidad", "descripcion"]
