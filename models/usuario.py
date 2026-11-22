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


class Usuario:
    """Representa un usuario solicitante."""

    def __init__(self, id_usuario, nombre, documento, telefono):
        """Inicializa los datos del usuario."""
        self.id = id_usuario
        self.nombre = nombre
        self.documento = documento
        self.telefono = telefono

    def a_diccionario(self):
        """Convierte el usuario en diccionario."""
        return crear_usuario(self.id, self.nombre,
                             self.documento, self.telefono)

