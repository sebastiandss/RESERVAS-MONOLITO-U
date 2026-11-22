"""Pruebas de solapes al registrar reservas (paso 7)."""

from pruebas.apoyo_gestion_reservas import BaseGestionReservas
from service.exceptions.excepciones import ErrorReserva


class TestConflictosReservas(BaseGestionReservas):
    def reserva_aprobada(self, **cambios):
        reserva = {
            "id": 1, "espacio_id": 1, "usuario_id": 7,
            "fecha": "2026-12-01", "hora_inicio": "10:00", "hora_fin": "12:00",
            "actividad": "Otra", "estado": "Aprobada",
        }
        reserva.update(cambios)
        return reserva

    def test_solape_parcial_con_aprobada(self):
        self.escribir(self.ruta_reservas, [self.reserva_aprobada()])
        with self.assertRaises(ErrorReserva):
            self.registrar(inicio="09:00", fin="11:00")
        self.assertEqual(len(self.leer(self.ruta_reservas)), 1)

    def test_solape_total_con_aprobada(self):
        aprobada = self.reserva_aprobada(hora_inicio="09:00", hora_fin="11:00")
        self.escribir(self.ruta_reservas, [aprobada])
        with self.assertRaises(ErrorReserva):
            self.registrar()

    def test_franja_adyacente_no_bloquea(self):
        aprobada = self.reserva_aprobada(hora_inicio="11:00", hora_fin="12:00")
        self.escribir(self.ruta_reservas, [aprobada])
        self.assertEqual(self.registrar()["estado"], "Pendiente")

    def test_otro_espacio_no_bloquea(self):
        self.escribir(self.ruta_reservas, [self.reserva_aprobada(espacio_id=2)])
        self.assertEqual(self.registrar()["estado"], "Pendiente")

    def test_otra_fecha_no_bloquea(self):
        self.escribir(self.ruta_reservas, [self.reserva_aprobada(fecha="2026-12-02")])
        self.assertEqual(self.registrar()["estado"], "Pendiente")

    def test_estados_no_bloqueantes(self):
        for estado in ("Pendiente", "Rechazada", "Cancelada"):
            with self.subTest(estado=estado):
                self.escribir(self.ruta_reservas, [self.reserva_aprobada(estado=estado)])
                self.assertEqual(self.registrar()["estado"], "Pendiente")
