from pruebas.apoyo_gestion_usuarios import BaseGestionUsuarios
from service.usuarios.GestionUsuarios import agregar_usuario, listar_usuarios


class TestListadoUsuarios(BaseGestionUsuarios):
    def test_lista_vacia(self):
        self.assertEqual(listar_usuarios(self.ruta_usuarios), [])

    def test_orden_por_nombre(self):
        agregar_usuario("Zoe", "1001", "300", self.ruta_usuarios)
        agregar_usuario("ana", "1002", "301", self.ruta_usuarios)
        agregar_usuario("Marta", "1003", "302", self.ruta_usuarios)
        nombres = []
        for usuario in listar_usuarios(self.ruta_usuarios):
            nombres.append(usuario["nombre"])
        self.assertEqual(nombres, ["ana", "Marta", "Zoe"])
