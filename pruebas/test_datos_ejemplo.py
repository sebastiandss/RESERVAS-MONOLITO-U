"""Pruebas de integridad del dataset de ejemplo."""

import json
import os
import unittest

from modelos.reserva import ESTADOS_RESERVA
from service.exceptions import validar_fecha, validar_hora, validar_rango_horas

BASE = os.path.join(os.path.dirname(__file__), "..", "datos_ejemplo")


def cargar(nombre):
    with open(os.path.join(BASE, nombre), encoding="utf-8") as archivo:
        return json.load(archivo)


class TestDatosEjemplo(unittest.TestCase):
    def setUp(self):
        self.espacios = cargar("espacios.json")
        self.usuarios = cargar("usuarios.json")
        self.reservas = cargar("reservas.json")

    def test_ids_unicos(self):
        for lista in (self.espacios, self.usuarios, self.reservas):
            ids = [registro["id"] for registro in lista]
            self.assertEqual(len(ids), len(set(ids)))

    def test_fks(self):
        ids_espacios = {e["id"] for e in self.espacios}
        ids_usuarios = {u["id"] for u in self.usuarios}
        for reserva in self.reservas:
            self.assertIn(reserva["espacio_id"], ids_espacios)
            self.assertIn(reserva["usuario_id"], ids_usuarios)

    def test_formatos_y_estados(self):
        for reserva in self.reservas:
            self.assertTrue(validar_fecha(reserva["fecha"]))
            self.assertTrue(validar_hora(reserva["hora_inicio"]))
            self.assertTrue(validar_hora(reserva["hora_fin"]))
            self.assertTrue(
                validar_rango_horas(
                    reserva["hora_inicio"], reserva["hora_fin"]
                )
            )
            self.assertIn(reserva["estado"], ESTADOS_RESERVA)

    def test_cantidades(self):
        self.assertEqual(len(self.espacios), 5)
        self.assertEqual(len(self.usuarios), 5)
        self.assertEqual(len(self.reservas), 11)
