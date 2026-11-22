"""Pruebas del alta de reservas (paso 7)."""

from models.reserva import campos_reserva
from pruebas.apoyo_gestion_reservas import BaseGestionReservas


class TestAltaReservas(BaseGestionReservas):
    def test_alta_valida(self):
        reserva = self.registrar()
        self.assertEqual(reserva["espacio_id"], 1)
        self.assertEqual(reserva["usuario_id"], 7)
        self.assertEqual(reserva["fecha"], "2026-12-01")
        self.assertEqual(reserva["hora_inicio"], "09:00")
        self.assertEqual(reserva["hora_fin"], "11:00")
        self.assertEqual(reserva["actividad"], "Taller")
        self.assertEqual(reserva["estado"], "Pendiente")
        self.assertEqual(self.leer(self.ruta_reservas), [reserva])

    def test_campos_del_modelo(self):
        self.assertEqual(list(self.registrar().keys()), campos_reserva())

    def test_ids_unicos(self):
        primera = self.registrar()
        segunda = self.registrar()
        self.assertNotEqual(primera["id"], segunda["id"])
        self.assertEqual(len(self.leer(self.ruta_reservas)), 2)
