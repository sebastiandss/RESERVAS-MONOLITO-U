"""Base con JSON temporales para las pruebas de reservas."""

import json
import os
import tempfile
import unittest
from unittest.mock import patch

from service.reservas import GestorReservas

FECHA_ACTUAL = "2026-11-22"
FECHA_FUTURA = "2026-12-01"


class BaseGestionReservas(unittest.TestCase):
    def setUp(self):
        self.carpeta = tempfile.TemporaryDirectory()
        self.ruta_usuarios = os.path.join(self.carpeta.name, "usuarios.json")
        self.ruta_espacios = os.path.join(self.carpeta.name, "espacios.json")
        self.ruta_reservas = os.path.join(self.carpeta.name, "reservas.json")
        self.usuarios = [{"id": 7, "nombre": "Ana", "documento": "1001", "telefono": "3001112233"}]
        self.espacios = [{"id": 1, "nombre": "Salón", "capacidad": 50, "descripcion": "Norte"}]
        self.escribir(self.ruta_usuarios, self.usuarios)
        self.escribir(self.ruta_espacios, self.espacios)
        self.escribir(self.ruta_reservas, [])

    def tearDown(self):
        self.carpeta.cleanup()

    def escribir(self, ruta, datos):
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False)

    def leer(self, ruta):
        with open(ruta, encoding="utf-8") as archivo:
            return json.load(archivo)

    def registrar(self, espacio_id=1, usuario_id=7, fecha=FECHA_FUTURA,
                  inicio="09:00", fin="11:00", actividad="Taller",
                  fecha_actual=FECHA_ACTUAL):
        with patch.object(GestorReservas, "RUTA_USUARIOS", self.ruta_usuarios), \
             patch.object(GestorReservas, "RUTA_ESPACIOS", self.ruta_espacios), \
             patch.object(GestorReservas, "RUTA_RESERVAS", self.ruta_reservas):
            return GestorReservas.registrar_reserva(
                espacio_id, usuario_id, fecha, inicio, fin, actividad, fecha_actual
            )
