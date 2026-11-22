"""Pruebas de transiciones de estado (paso 8)."""

from pruebas.apoyo_gestion_estados import BaseGestionEstados


class TestTransicionesEstados(BaseGestionEstados):
    def test_aprobar_dos_veces(self):
        self.escribir([self.reserva(1, "Aprobada")])
        self.assertEqual(self.cambiar(1, "Aprobada")["estado"], "Aprobada")

    def test_cancelar_y_aprobar_otra(self):
        self.escribir([
            self.reserva(1, "Aprobada"),
            self.reserva(2),
        ])
        self.assertEqual(self.cambiar(1, "Cancelada")["estado"], "Cancelada")
        self.assertEqual(self.cambiar(2, "Aprobada")["estado"], "Aprobada")
