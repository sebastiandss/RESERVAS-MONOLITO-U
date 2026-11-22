"""Pruebas de la consulta de espacios disponibles."""

from pruebas.apoyo_consultas import FECHA, BaseConsultas
from service.exceptions.excepciones import ErrorReserva
from service.reservas.consultas_disponibilidad import consultar_espacios_disponibles


class TestConsultasDisponibilidad(BaseConsultas):
    def test_espacios_libres(self):
        resultados = self.consultar(
            consultar_espacios_disponibles, FECHA, "09:00", "11:00")
        self.assertEqual([e["nombre"] for e in resultados], ["Salón", "Cancha"])

    def test_aprobada_bloquea(self):
        self.escribir(self.ruta_reservas, [self.reserva(1)])
        resultados = self.consultar(
            consultar_espacios_disponibles, FECHA, "09:00", "11:00")
        self.assertEqual([e["nombre"] for e in resultados], ["Cancha"])

    def test_pendiente_no_bloquea(self):
        self.escribir(self.ruta_reservas, [self.reserva(1, estado="Pendiente")])
        resultados = self.consultar(
            consultar_espacios_disponibles, FECHA, "09:00", "11:00")
        self.assertEqual(len(resultados), 2)

    def test_cancelada_no_bloquea(self):
        self.escribir(self.ruta_reservas, [self.reserva(1, estado="Cancelada")])
        resultados = self.consultar(
            consultar_espacios_disponibles, FECHA, "09:00", "11:00")
        self.assertEqual(len(resultados), 2)

    def test_franja_adyacente(self):
        self.escribir(self.ruta_reservas, [
            self.reserva(1, inicio="11:00", fin="12:00")])
        resultados = self.consultar(
            consultar_espacios_disponibles, FECHA, "09:00", "11:00")
        self.assertEqual(len(resultados), 2)

    def test_sin_resultados(self):
        self.escribir(self.ruta_reservas, [
            self.reserva(1), self.reserva(2, espacio_id=2)])
        with self.assertRaises(ErrorReserva):
            self.consultar(
                consultar_espacios_disponibles, FECHA, "09:00", "11:00")

    def test_validaciones(self):
        with self.assertRaises(ErrorReserva):
            self.consultar(
                consultar_espacios_disponibles, "no-fecha", "09:00", "11:00")
        with self.assertRaises(ErrorReserva):
            self.consultar(
                consultar_espacios_disponibles, FECHA, "12:00", "09:00")
