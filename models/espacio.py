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


class Espacio:
    """Representa un espacio del centro comunitario."""

    def __init__(self, id_espacio, nombre, capacidad, descripcion):
        """Inicializa los datos del espacio."""
        self.id = id_espacio
        self.nombre = nombre
        self.capacidad = capacidad
        self.descripcion = descripcion

    def a_diccionario(self):
        """Convierte el espacio en diccionario."""
        return crear_espacio(self.id, self.nombre,
                             self.capacidad, self.descripcion)

