from pruebas.apoyo_gestion_usuarios import BaseGestionUsuarios
from service.exceptions.excepciones import ErrorReserva
from service.usuarios.GestionUsuarios import agregar_usuario


class TestAltaUsuarios(BaseGestionUsuarios):
    def test_alta_valida(self):
        usuario = agregar_usuario("  Ana Torres ", "1001", "3001112233", self.ruta_usuarios)
        self.assertEqual(usuario["id"], 1)
        self.assertEqual(usuario["nombre"], "Ana Torres")
        self.assertEqual(usuario["documento"], "1001")
        self.assertEqual(usuario["telefono"], "3001112233")
        self.assertEqual(self.leer(self.ruta_usuarios), [usuario])

    def test_nombre_normalizado(self):
        usuario = agregar_usuario("  Ana   Torres ", 1002, "300", self.ruta_usuarios)
        self.assertEqual(usuario["nombre"], "Ana Torres")

    def test_segundo_id(self):
        agregar_usuario("Ana", "1001", "300", self.ruta_usuarios)
        segundo = agregar_usuario("Luis", "1002", "301", self.ruta_usuarios)
        self.assertEqual(segundo["id"], 2)

    def test_nombre_invalido(self):
        for nombre in ("", "   ", None, 123):
            with self.assertRaises(ErrorReserva):
                agregar_usuario(nombre, "1001", "300", self.ruta_usuarios)

    def test_documento_invalido(self):
        for documento in ("", "   ", None, "abc", "12a", True):
            with self.assertRaises(ErrorReserva):
                agregar_usuario("Ana", documento, "300", self.ruta_usuarios)

    def test_telefono_invalido(self):
        for telefono in ("", "   ", None):
            with self.assertRaises(ErrorReserva):
                agregar_usuario("Ana", "1001", telefono, self.ruta_usuarios)

    def test_duplicados(self):
        agregar_usuario("Ana", "1001", "300", self.ruta_usuarios)
        for documento in ("1001", " 1001 ", 1001):
            with self.assertRaises(ErrorReserva):
                agregar_usuario("Otro", documento, "301", self.ruta_usuarios)
