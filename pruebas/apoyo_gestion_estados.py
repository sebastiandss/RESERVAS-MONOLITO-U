"""Base con JSON temporales para las pruebas de cambio de estado."""

import json
import os
import tempfile
import unittest
from unittest.mock import patch

from service.reservas import GestorEstados

FECHA = "2026-12-01"


class BaseGestionEstados(unittest.TestCase):
    def setUp(self):
        self.carpeta = tempfile.TemporaryDirectory()
        self.ruta_reservas = os.path.join(self.carpeta.name, "reservas.json")
        self.escribir([])

    def tearDown(self):
        self.carpeta.cleanup()

    def escribir(self, reservas):
        with open(self.ruta_reservas, "w", encoding="utf-8") as archivo:
            json.dump(reservas, archivo, ensure_ascii=False)

    def leer(self):
        with open(self.ruta_reservas, encoding="utf-8") as archivo:
            return json.load(archivo)

    def reserva(self, id_reserva, estado="Pendiente", espacio_id=1,
                fecha=FECHA, inicio="09:00", fin="11:00"):
        return {
            "id": id_reserva, "espacio_id": espacio_id, "usuario_id": 7,
            "fecha": fecha, "hora_inicio": inicio, "hora_fin": fin,
            "actividad": "Taller", "estado": estado,
        }

    def cambiar(self, id_reserva, estado):
        with patch.object(GestorEstados, "RUTA_RESERVAS", self.ruta_reservas):
            return GestorEstados.cambiar_estado_reserva(id_reserva, estado)
