"""Pruebas de solapes al aprobar reservas (paso 8)."""

from pruebas.apoyo_gestion_estados import BaseGestionEstados
from service.exceptions.excepciones import ErrorReserva


class TestConflictosEstados(BaseGestionEstados):
    def test_aprobar_con_solape_parcial(self):
        self.escribir([
            self.reserva(1),
            self.reserva(2, "Aprobada", inicio="10:00", fin="12:00"),
        ])
        with self.assertRaises(ErrorReserva):
            self.cambiar(1, "Aprobada")

    def test_no_guarda_si_hay_conflicto(self):
        self.escribir([
            self.reserva(1),
            self.reserva(2, "Aprobada", inicio="09:00", fin="11:00"),
        ])
        with self.assertRaises(ErrorReserva):
            self.cambiar(1, "Aprobada")
        self.assertEqual([r["estado"] for r in self.leer()], ["Pendiente", "Aprobada"])

    def test_franja_adyacente(self):
        self.escribir([
            self.reserva(1),
            self.reserva(2, "Aprobada", inicio="11:00", fin="12:00"),
        ])
        self.assertEqual(self.cambiar(1, "Aprobada")["estado"], "Aprobada")

    def test_otro_espacio(self):
        self.escribir([
            self.reserva(1),
            self.reserva(2, "Aprobada", espacio_id=2),
        ])
        self.assertEqual(self.cambiar(1, "Aprobada")["estado"], "Aprobada")

    def test_otra_fecha(self):
        self.escribir([
            self.reserva(1),
            self.reserva(2, "Aprobada", fecha="2026-12-02"),
        ])
        self.assertEqual(self.cambiar(1, "Aprobada")["estado"], "Aprobada")

    def test_estados_no_bloqueantes(self):
        for estado in ("Pendiente", "Rechazada", "Cancelada"):
            with self.subTest(estado=estado):
                self.escribir([
                    self.reserva(1),
                    self.reserva(2, estado, inicio="10:00", fin="12:00"),
                ])
                self.assertEqual(self.cambiar(1, "Aprobada")["estado"], "Aprobada")
