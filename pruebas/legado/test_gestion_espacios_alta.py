from pruebas.apoyo_gestion_espacios import BaseGestionEspacios
from service.espacios.GestionarEspacios import agregar_espacio
from service.exceptions.excepciones import ErrorReserva


class TestAltaEspacios(BaseGestionEspacios):
    def test_alta_valida(self):
        espacio = agregar_espacio("  Salón  ", "10", "Principal", self.ruta_espacios)
        self.assertEqual(espacio["id"], 1)
        self.assertEqual(espacio["nombre"], "Salón")
        self.assertEqual(espacio["capacidad"], 10)
        self.assertEqual(self.leer(self.ruta_espacios), [espacio])

    def test_nombre_normalizado(self):
        espacio = agregar_espacio("  Sala   de  actos ", 5, "", self.ruta_espacios)
        self.assertEqual(espacio["nombre"], "Sala de actos")

    def test_segundo_id(self):
        agregar_espacio("Salón", 10, "", self.ruta_espacios)
        segundo = agregar_espacio("Cancha", 20, "", self.ruta_espacios)
        self.assertEqual(segundo["id"], 2)

    def test_nombre_invalido(self):
        for nombre in ("", "   ", None, 123):
            with self.assertRaises(ErrorReserva):
                agregar_espacio(nombre, 10, "", self.ruta_espacios)

    def test_capacidad_invalida(self):
        for capacidad in (0, -1, "abc", None, True, 1.5):
            with self.assertRaises(ErrorReserva):
                agregar_espacio("Salón", capacidad, "", self.ruta_espacios)

    def test_duplicados(self):
        agregar_espacio("Salón", 10, "", self.ruta_espacios)
        for nombre in ("Salón", "SALÓN", "  Salón  "):
            with self.assertRaises(ErrorReserva):
                agregar_espacio(nombre, 10, "", self.ruta_espacios)
