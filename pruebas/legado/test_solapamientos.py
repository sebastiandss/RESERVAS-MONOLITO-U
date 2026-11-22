"""Pruebas de los cruces esperados en el dataset de ejemplo."""

import json
import os
import unittest

BASE = os.path.join(os.path.dirname(__file__), "..", "..", "datos_ejemplo")


def cargar(nombre):
    with open(os.path.join(BASE, nombre), encoding="utf-8") as archivo:
        return json.load(archivo)


def se_cruzan(a, b):
    # Se reemplazará por la función real cuando exista en la lógica.
    return (
        a["espacio_id"] == b["espacio_id"]
        and a["fecha"] == b["fecha"]
        and a["hora_inicio"] < b["hora_fin"]
        and b["hora_inicio"] < a["hora_fin"]
    )


class TestSolapamientos(unittest.TestCase):
    def test_pares_activos(self):
        reservas = cargar("reservas.json")
        activas = [
            r for r in reservas
            if r["estado"] in ("Pendiente", "Aprobada")
        ]
        pares = []
        for i in range(len(activas)):
            for j in range(i + 1, len(activas)):
                if se_cruzan(activas[i], activas[j]):
                    pares.append((activas[i]["id"], activas[j]["id"]))
        self.assertEqual(pares, [(1, 2), (2, 3)])

    def test_adyacentes_no_se_cruzan(self):
        reservas = {r["id"]: r for r in cargar("reservas.json")}
        self.assertFalse(se_cruzan(reservas[1], reservas[3]))
        self.assertFalse(se_cruzan(reservas[10], reservas[11]))
