"""Modelo de datos para la entidad Espacio."""


class Espacio(dict):
    """Representa un espacio y conoce la etiqueta mostrada en la interfaz."""

    def __init__(self, id_espacio, nombre, capacidad, descripcion):
        super().__init__(
            id=id_espacio,
            nombre=nombre,
            capacidad=capacidad,
            descripcion=descripcion,
        )

    @classmethod
    def desde_datos(cls, datos):
        """Convierte un registro guardado en una instancia de Espacio."""
        if isinstance(datos, cls):
            return datos
        espacio = cls(
            datos["id"], datos["nombre"],
            datos["capacidad"], datos["descripcion"],
        )
        espacio.update({clave: valor for clave, valor in datos.items()
                        if clave not in espacio})
        return espacio

    def etiqueta(self):
        """Devuelve el texto 'id - nombre' usado en los combos."""
        return f"{self['id']} - {self['nombre']}"


def crear_espacio(id_espacio, nombre, capacidad, descripcion):
    """Crea y devuelve un Espacio con los datos de un espacio."""
    return Espacio(id_espacio, nombre, capacidad, descripcion)
