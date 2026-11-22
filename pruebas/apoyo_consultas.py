"""Base con JSON temporales para las pruebas de consultas."""

import json
import os
import tempfile
import unittest
from unittest.mock import patch

from service.reservas import (
    consultas_asignaciones,
    consultas_coincidentes,
    consultas_disponibilidad,
)

FECHA = "2026-12-01"


class BaseConsultas(unittest.TestCase):
    def setUp(self):
        self.carpeta = tempfile.TemporaryDirectory()
        self.ruta_usuarios = os.path.join(self.carpeta.name, "usuarios.json")
        self.ruta_espacios = os.path.join(self.carpeta.name, "espacios.json")
        self.ruta_reservas = os.path.join(self.carpeta.name, "reservas.json")
        self.espacios = [
            {"id": 1, "nombre": "Salón", "capacidad": 50, "descripcion": "Norte"},
            {"id": 2, "nombre": "Cancha", "capacidad": 30, "descripcion": "Sur"},
        ]
        self.usuarios = [
            {"id": 7, "nombre": "Ana", "documento": "1001", "telefono": "3001112233"},
            {"id": 8, "nombre": "Luis", "documento": "1002", "telefono": "3001112244"},
        ]
        self.escribir(self.ruta_espacios, self.espacios)
        self.escribir(self.ruta_usuarios, self.usuarios)
        self.escribir(self.ruta_reservas, [])

    def tearDown(self):
        self.carpeta.cleanup()

    def escribir(self, ruta, datos):
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False)

    def reserva(self, id_reserva, espacio_id=1, usuario_id=7,
                estado="Aprobada", fecha=FECHA, inicio="09:00", fin="11:00"):
        return {
            "id": id_reserva, "espacio_id": espacio_id, "usuario_id": usuario_id,
            "fecha": fecha, "hora_inicio": inicio, "hora_fin": fin,
            "actividad": "Taller", "estado": estado,
        }

    def consultar(self, funcion, *args):
        with patch.object(consultas_asignaciones, "RUTA_USUARIOS", self.ruta_usuarios), \
             patch.object(consultas_asignaciones, "RUTA_ESPACIOS", self.ruta_espacios), \
             patch.object(consultas_asignaciones, "RUTA_RESERVAS", self.ruta_reservas), \
             patch.object(consultas_disponibilidad, "RUTA_ESPACIOS", self.ruta_espacios), \
             patch.object(consultas_disponibilidad, "RUTA_RESERVAS", self.ruta_reservas), \
             patch.object(consultas_coincidentes, "RUTA_RESERVAS", self.ruta_reservas):
            return funcion(*args)
