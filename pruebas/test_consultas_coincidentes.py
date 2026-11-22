"""Pruebas de la consulta de reservas coincidentes."""

from pruebas.apoyo_consultas import FECHA, BaseConsultas
from service.exceptions.excepciones import ErrorReserva
from service.reservas.consultas_coincidentes import consultar_reservas_coincidentes


class TestConsultasCoincidentes(BaseConsultas):
    def test_reservas_activas(self):
        self.escribir(self.ruta_reservas, [
            self.reserva(1),
            self.reserva(2, estado="Pendiente", inicio="10:00", fin="12:00"),
        ])
        resultados = self.consultar(
            consultar_reservas_coincidentes, 1, FECHA, "09:00", "11:00")
        self.assertEqual([r["id"] for r in resultados], [1, 2])

    def test_excluye_inactivas(self):
        self.escribir(self.ruta_reservas, [
            self.reserva(1, estado="Cancelada"),
            self.reserva(2, estado="Rechazada"),
        ])
        with self.assertRaises(ErrorReserva):
            self.consultar(
                consultar_reservas_coincidentes, 1, FECHA, "09:00", "11:00")

    def test_franja_adyacente(self):
        self.escribir(self.ruta_reservas, [
            self.reserva(1, inicio="11:00", fin="12:00")])
        with self.assertRaises(ErrorReserva):
            self.consultar(
                consultar_reservas_coincidentes, 1, FECHA, "09:00", "11:00")

    def test_otro_espacio_o_fecha(self):
        self.escribir(self.ruta_reservas, [
            self.reserva(1, espacio_id=2),
            self.reserva(2, fecha="2026-12-02"),
        ])
        with self.assertRaises(ErrorReserva):
            self.consultar(
                consultar_reservas_coincidentes, 1, FECHA, "09:00", "11:00")

    def test_validaciones(self):
        with self.assertRaises(ErrorReserva):
            self.consultar(
                consultar_reservas_coincidentes, 1, "2026-13-01", "09:00", "11:00")
        with self.assertRaises(ErrorReserva):
            self.consultar(
                consultar_reservas_coincidentes, 1, FECHA, "12:00", "09:00")
