"""Pruebas de los modelos de datos."""

import unittest

from models.espacio import campos_espacio, crear_espacio
from models.reserva import ESTADOS_RESERVA, campos_reserva, crear_reserva
from models.usuario import campos_usuario, crear_usuario


class TestModelos(unittest.TestCase):
    def test_espacio(self):
        esperado = {
            "id": 1, "nombre": "Salón",
            "capacidad": 50, "descripcion": "Norte",
        }
        self.assertEqual(crear_espacio(1, "Salón", 50, "Norte"), esperado)
        self.assertEqual(
            campos_espacio(), ["id", "nombre", "capacidad", "descripcion"]
        )

    def test_usuario(self):
        esperado = {
            "id": 1, "nombre": "Ana",
            "documento": "1001", "telefono": "3001112233",
        }
        self.assertEqual(
            crear_usuario(1, "Ana", "1001", "3001112233"), esperado
        )
        self.assertEqual(
            campos_usuario(), ["id", "nombre", "documento", "telefono"]
        )

    def test_reserva(self):
        esperado = {
            "id": 1, "espacio_id": 1, "usuario_id": 1,
            "fecha": "2026-12-01", "hora_inicio": "09:00",
            "hora_fin": "11:00", "actividad": "Taller",
            "estado": "Pendiente",
        }
        self.assertEqual(
            crear_reserva(
                1, 1, 1, "2026-12-01", "09:00", "11:00",
                "Taller", "Pendiente",
            ),
            esperado,
        )
        self.assertEqual(campos_reserva(), list(esperado.keys()))
        self.assertEqual(
            ESTADOS_RESERVA,
            ("Pendiente", "Aprobada", "Rechazada", "Cancelada"),
        )
