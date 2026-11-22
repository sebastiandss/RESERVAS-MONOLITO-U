"""Pruebas de duplicados con acentos (RN-01)."""

from pruebas.apoyo_gestion_espacios import BaseGestionEspacios
from service.espacios.GestionarEspacios import agregar_espacio
from service.exceptions.excepciones import ErrorReserva


class TestAcentosEspacios(BaseGestionEspacios):
    def test_nombre_con_acento_se_guarda_igual(self):
        espacio = agregar_espacio("Salón", 10, "", self.ruta_espacios)
        self.assertEqual(espacio["nombre"], "Salón")

    def test_duplicado_sin_acento_se_rechaza(self):
        agregar_espacio("Salón", 10, "", self.ruta_espacios)
        for nombre in ("SALON", "salon", " Salón "):
            with self.subTest(nombre=nombre):
                with self.assertRaises(ErrorReserva):
                    agregar_espacio(nombre, 10, "", self.ruta_espacios)

    def test_duplicado_con_acento_se_rechaza(self):
        agregar_espacio("Salón", 10, "", self.ruta_espacios)
        with self.assertRaises(ErrorReserva):
            agregar_espacio("SALÓN", 10, "", self.ruta_espacios)

    def test_nombres_distintos_no_se_confunden(self):
        agregar_espacio("Salón", 10, "", self.ruta_espacios)
        otro = agregar_espacio("Sala", 10, "", self.ruta_espacios)
        self.assertEqual(otro["nombre"], "Sala")
