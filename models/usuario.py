"""Modelo de datos para la entidad Usuario."""


class Usuario(dict):
    """Representa un solicitante y conoce la etiqueta mostrada en la interfaz."""

    def __init__(self, id_usuario, nombre, documento, telefono):
        super().__init__(
            id=id_usuario,
            nombre=nombre,
            documento=documento,
            telefono=telefono,
        )

    @classmethod
    def desde_datos(cls, datos):
        """Convierte un registro guardado en una instancia de Usuario."""
        if isinstance(datos, cls):
            return datos
        usuario = cls(
            datos["id"], datos["nombre"],
            datos["documento"], datos["telefono"],
        )
        usuario.update({clave: valor for clave, valor in datos.items()
                        if clave not in usuario})
        return usuario

    def etiqueta(self):
        """Devuelve el texto 'id - nombre' usado en los combos."""
        return f"{self['id']} - {self['nombre']}"


def crear_usuario(id_usuario, nombre, documento, telefono):
    """Crea y devuelve un Usuario con los datos de un usuario."""
    return Usuario(id_usuario, nombre, documento, telefono)
