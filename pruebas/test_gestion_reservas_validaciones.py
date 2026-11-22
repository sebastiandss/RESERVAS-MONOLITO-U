"""Pruebas de validaciones al registrar reservas (paso 7)."""

from pruebas.apoyo_gestion_reservas import FECHA_ACTUAL, BaseGestionReservas
from service.exceptions.excepciones import ErrorReserva


class TestValidacionesReservas(BaseGestionReservas):
    def test_usuario_inexistente(self):
        with self.assertRaises(ErrorReserva):
            self.registrar(usuario_id=999)
        self.assertEqual(self.leer(self.ruta_reservas), [])

    def test_espacio_inexistente(self):
        with self.assertRaises(ErrorReserva):
            self.registrar(espacio_id=999)
        self.assertEqual(self.leer(self.ruta_reservas), [])

    def test_actividad_obligatoria(self):
        for actividad in ("", None):
            with self.assertRaises(ErrorReserva):
                self.registrar(actividad=actividad)

    def test_fecha_pasada(self):
        with self.assertRaises(ErrorReserva):
            self.registrar(fecha="2026-11-21")

    def test_fecha_actual_es_valida(self):
        reserva = self.registrar(fecha=FECHA_ACTUAL)
        self.assertEqual(reserva["estado"], "Pendiente")

    def test_fecha_invalida(self):
        for fecha in ("2026-13-01", "2026-02-30", "no-fecha"):
            with self.assertRaises(ErrorReserva):
                self.registrar(fecha=fecha)

    def test_hora_invalida(self):
        casos = (("25:00", "26:00"), ("09:00", "09:00"), ("12:00", "11:00"))
        for inicio, fin in casos:
            with self.assertRaises(ErrorReserva):
                self.registrar(inicio=inicio, fin=fin)
