from pruebas.apoyo_gestion_usuarios import BaseGestionUsuarios
from service.exceptions.excepciones import ErrorReserva
from service.usuarios.GestionUsuarios import agregar_usuario, eliminar_usuario


class TestBorradoUsuarios(BaseGestionUsuarios):
    def test_inexistente(self):
        with self.assertRaises(ErrorReserva):
            eliminar_usuario(99, self.ruta_usuarios, self.ruta_reservas)

    def test_sin_reservas(self):
        usuario = agregar_usuario("Ana", "1001", "300", self.ruta_usuarios)
        self.assertTrue(eliminar_usuario(usuario["id"], self.ruta_usuarios, self.ruta_reservas))
        self.assertEqual(self.leer(self.ruta_usuarios), [])

    def test_con_reserva_nueva(self):
        usuario = agregar_usuario("Ana", "1001", "300", self.ruta_usuarios)
        self.escribir(self.ruta_reservas, [{"id": 1, "usuario_id": usuario["id"]}])
        with self.assertRaises(ErrorReserva):
            eliminar_usuario(usuario["id"], self.ruta_usuarios, self.ruta_reservas)
        self.assertEqual(len(self.leer(self.ruta_usuarios)), 1)

    def test_con_reserva_legada(self):
        usuario = agregar_usuario("Ana", "1001", "300", self.ruta_usuarios)
        self.escribir(self.ruta_reservas, [{"id": 1, "id_usuario": str(usuario["id"])}])
        with self.assertRaises(ErrorReserva):
            eliminar_usuario(usuario["id"], self.ruta_usuarios, self.ruta_reservas)

    def test_con_reserva_cancelada(self):
        usuario = agregar_usuario("Ana", "1001", "300", self.ruta_usuarios)
        reserva = {"id": 1, "usuario_id": usuario["id"], "estado": "Cancelada"}
        self.escribir(self.ruta_reservas, [reserva])
        with self.assertRaises(ErrorReserva):
            eliminar_usuario(usuario["id"], self.ruta_usuarios, self.ruta_reservas)
