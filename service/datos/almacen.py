"""Clase de persistencia JSON para una entidad."""

from service.datos.almacen_json import cargar_datos, guardar_datos


class Almacen:
    """Encapsula la ruta y las operaciones de carga/guardado JSON."""

    def __init__(self, ruta):
        """Guarda la ruta del archivo JSON."""
        self.ruta = ruta

    def cargar(self):
        """Lee y devuelve los datos del archivo."""
        return cargar_datos(self.ruta)

    def guardar(self, datos):
        """Guarda los datos en el archivo."""
        guardar_datos(self.ruta, datos)
