from pruebas.apoyo_gestion_espacios import BaseGestionEspacios
from service.espacios.GestionarEspacios import agregar_espacio, eliminar_espacio
from service.exceptions.excepciones import ErrorReserva


class TestBorradoEspacios(BaseGestionEspacios):
    def test_inexistente(self):
        with self.assertRaises(ErrorReserva):
            eliminar_espacio(99, self.ruta_espacios, self.ruta_reservas)

    def test_sin_reservas(self):
        espacio = agregar_espacio("Salón", 10, "", self.ruta_espacios)
        self.assertTrue(eliminar_espacio(espacio["id"], self.ruta_espacios, self.ruta_reservas))
        self.assertEqual(self.leer(self.ruta_espacios), [])

    def test_con_reserva_nueva(self):
        espacio = agregar_espacio("Salón", 10, "", self.ruta_espacios)
        self.escribir(self.ruta_reservas, [{"id": 1, "espacio_id": espacio["id"]}])
        with self.assertRaises(ErrorReserva):
            eliminar_espacio(espacio["id"], self.ruta_espacios, self.ruta_reservas)
        self.assertEqual(len(self.leer(self.ruta_espacios)), 1)

    def test_con_reserva_legada(self):
        espacio = agregar_espacio("Salón", 10, "", self.ruta_espacios)
        self.escribir(self.ruta_reservas, [{"id": 1, "id_espacio": str(espacio["id"])}])
        with self.assertRaises(ErrorReserva):
            eliminar_espacio(espacio["id"], self.ruta_espacios, self.ruta_reservas)

    def test_con_reserva_cancelada(self):
        espacio = agregar_espacio("Salón", 10, "", self.ruta_espacios)
        reserva = {"id": 1, "espacio_id": espacio["id"], "estado": "Cancelada"}
        self.escribir(self.ruta_reservas, [reserva])
        with self.assertRaises(ErrorReserva):
            eliminar_espacio(espacio["id"], self.ruta_espacios, self.ruta_reservas)
