"""Pruebas de la capa de persistencia JSON."""

import os
import tempfile
import unittest

from service.datos.almacen_json import cargar_datos, guardar_datos


class TestAlmacenJson(unittest.TestCase):
    def test_guardar_y_cargar(self):
        with tempfile.TemporaryDirectory() as carpeta:
            ruta = os.path.join(carpeta, "datos.json")
            datos = [{"id": 1, "nombre": "Salón"}]
            guardar_datos(ruta, datos)
            self.assertEqual(cargar_datos(ruta), datos)

    def test_archivo_vacio(self):
        with tempfile.TemporaryDirectory() as carpeta:
            ruta = os.path.join(carpeta, "vacio.json")
            open(ruta, "w", encoding="utf-8").close()
            self.assertEqual(cargar_datos(ruta), [])

    def test_archivo_inexistente_devuelve_lista_vacia(self):
        # Resuelto: si no existe, devuelve [].
        with tempfile.TemporaryDirectory() as carpeta:
            ruta = os.path.join(carpeta, "no_existe.json")
            self.assertEqual(cargar_datos(ruta), [])

    def test_json_danado_se_respalda(self):
        # Resuelto: renombra a .dañado.json y devuelve [].
        with tempfile.TemporaryDirectory() as carpeta:
            ruta = os.path.join(carpeta, "danado.json")
            with open(ruta, "w", encoding="utf-8") as archivo:
                archivo.write("{esto no es json")
            self.assertEqual(cargar_datos(ruta), [])
            self.assertTrue(os.path.exists(ruta + ".dañado.json"))
