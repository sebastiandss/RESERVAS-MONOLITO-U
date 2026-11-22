"""Pruebas del aviso automático de Pendientes (RN-05)."""

from pruebas.apoyo_gestion_reservas import BaseGestionReservas


class TestAvisoPendientes(BaseGestionReservas):
    def test_primera_reserva_no_lleva_aviso(self):
        self.assertNotIn("aviso", self.registrar())

    def test_reserva_coincidente_lleva_aviso(self):
        self.registrar()
        segunda = self.registrar(inicio="10:00", fin="12:00", actividad="Otra")
        self.assertIn("Pendiente", segunda["aviso"])
        self.assertIn("1 reserva(s)", segunda["aviso"])

    def test_aviso_no_se_persiste(self):
        self.registrar()
        self.registrar(inicio="10:00", fin="12:00", actividad="Otra")
        guardadas = self.leer(self.ruta_reservas)
        self.assertTrue(all("aviso" not in r for r in guardadas))

    def test_franja_adyacente_no_avisa(self):
        self.registrar()
        siguiente = self.registrar(inicio="11:00", fin="12:00", actividad="Otra")
        self.assertNotIn("aviso", siguiente)

    def test_reserva_cancelada_no_avisa(self):
        primera = self.registrar()
        primera["estado"] = "Cancelada"
        self.escribir(self.ruta_reservas, [primera])
        siguiente = self.registrar(inicio="10:00", fin="12:00", actividad="Otra")
        self.assertNotIn("aviso", siguiente)
