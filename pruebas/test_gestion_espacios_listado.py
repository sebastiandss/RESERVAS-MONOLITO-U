from pruebas.apoyo_gestion_espacios import BaseGestionEspacios
from service.espacios.GestionarEspacios import agregar_espacio, listar_espacios


class TestListadoEspacios(BaseGestionEspacios):
    def test_lista_vacia(self):
        self.assertEqual(listar_espacios(self.ruta_espacios), [])

    def test_orden_por_nombre(self):
        agregar_espacio("Zumba", 10, "", self.ruta_espacios)
        agregar_espacio("auditorio", 20, "", self.ruta_espacios)
        agregar_espacio("Sala", 30, "", self.ruta_espacios)
        nombres = [e["nombre"] for e in listar_espacios(self.ruta_espacios)]
        self.assertEqual(nombres, ["auditorio", "Sala", "Zumba"])
