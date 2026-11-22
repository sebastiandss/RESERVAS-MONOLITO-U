"""Pruebas de la consulta de asignaciones por fecha."""

from pruebas.apoyo_consultas import FECHA, BaseConsultas
from service.exceptions.excepciones import ErrorReserva
from service.reservas.consultas_asignaciones import consultar_quien_tiene_espacios


class TestConsultasAsignaciones(BaseConsultas):
    def test_solo_aprobadas(self):
        self.escribir(self.ruta_reservas, [
            self.reserva(1),
            self.reserva(2, espacio_id=2, usuario_id=8, estado="Pendiente"),
            self.reserva(3, espacio_id=2, estado="Cancelada"),
        ])
        resultados = self.consultar(consultar_quien_tiene_espacios, FECHA)
        self.assertEqual(len(resultados), 1)
        self.assertEqual(resultados[0], {
            "espacio": "Salón", "usuario": "Ana",
            "hora_inicio": "09:00", "hora_fin": "11:00", "estado": "Aprobada",
        })

    def test_nombres_no_encontrados(self):
        self.escribir(self.ruta_reservas, [self.reserva(1, espacio_id=99, usuario_id=99)])
        resultado = self.consultar(consultar_quien_tiene_espacios, FECHA)[0]
        self.assertEqual(resultado["espacio"], "Espacio no encontrado")
        self.assertEqual(resultado["usuario"], "Usuario no encontrado")

    def test_sin_resultados(self):
        self.escribir(self.ruta_reservas, [self.reserva(1, estado="Cancelada")])
        with self.assertRaises(ErrorReserva):
            self.consultar(consultar_quien_tiene_espacios, FECHA)

    def test_fecha_invalida(self):
        with self.assertRaises(ErrorReserva):
            self.consultar(consultar_quien_tiene_espacios, "2026-13-01")
