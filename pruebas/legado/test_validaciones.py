"""Pruebas de las validaciones de fecha, hora y campos."""

import unittest

from service.exceptions import (
    ErrorReserva,
    validar_campos_obligatorios,
    validar_fecha,
    validar_hora,
    validar_rango_horas,
)


class TestValidaciones(unittest.TestCase):
    def test_fecha_valida(self):
        self.assertTrue(validar_fecha("2026-12-01"))
        self.assertTrue(validar_fecha("2024-02-29"))

    def test_fecha_invalida(self):
        casos = ["2026-02-29", "2026-13-01", "2026-04-31", "2026-1-1", ""]
        for fecha in casos:
            with self.assertRaises(ErrorReserva):
                validar_fecha(fecha)

    def test_hora_valida(self):
        self.assertTrue(validar_hora("00:00"))
        self.assertTrue(validar_hora("23:59"))

    def test_hora_invalida(self):
        casos = ["24:00", "9:00", "09:60", "09:00:00"]
        for hora in casos:
            with self.assertRaises(ErrorReserva):
                validar_hora(hora)

    def test_rango_valido(self):
        self.assertTrue(validar_rango_horas("09:00", "11:00"))

    def test_rango_invalido(self):
        with self.assertRaises(ErrorReserva):
            validar_rango_horas("11:00", "09:00")
        with self.assertRaises(ErrorReserva):
            validar_rango_horas("09:00", "09:00")

    def test_campos_obligatorios(self):
        self.assertTrue(
            validar_campos_obligatorios({"nombre": "Salón"}, ["nombre"])
        )

    def test_campos_vacios(self):
        with self.assertRaises(ErrorReserva):
            validar_campos_obligatorios({"nombre": "  "}, ["nombre"])
        with self.assertRaises(ErrorReserva):
            validar_campos_obligatorios({}, ["nombre"])
        with self.assertRaises(ErrorReserva):
            validar_campos_obligatorios({"nombre": None}, ["nombre"])

    def test_mensaje_de_error(self):
        with self.assertRaises(ErrorReserva) as contexto:
            validar_fecha("mal")
        self.assertIn("AAAA-MM-DD", str(contexto.exception))
