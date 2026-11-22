"""Pruebas de validaciones en el cambio de estado (paso 8)."""

from pruebas.apoyo_gestion_estados import BaseGestionEstados
from service.exceptions.excepciones import ErrorReserva


class TestValidacionesEstados(BaseGestionEstados):
    def test_estados_validos(self):
        for estado in ("Pendiente", "Aprobada", "Rechazada", "Cancelada"):
            with self.subTest(estado=estado):
                self.escribir([self.reserva(1)])
                self.assertEqual(self.cambiar(1, estado)["estado"], estado)

    def test_estado_invalido(self):
        self.escribir([self.reserva(1)])
        for estado in ("Borrador", "", None):
            with self.subTest(estado=estado):
                with self.assertRaises(ErrorReserva):
                    self.cambiar(1, estado)
        self.assertEqual(self.leer()[0]["estado"], "Pendiente")

    def test_id_inexistente(self):
        self.escribir([self.reserva(1)])
        with self.assertRaises(ErrorReserva):
            self.cambiar(999, "Aprobada")

    def test_guarda_el_cambio(self):
        self.escribir([self.reserva(1)])
        resultado = self.cambiar(1, "Cancelada")
        self.assertEqual(self.leer(), [resultado])
        self.assertEqual(resultado["estado"], "Cancelada")
