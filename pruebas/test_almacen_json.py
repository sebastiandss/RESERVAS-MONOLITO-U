"""Pruebas de persistencia tolerante (RF-10)."""

import os
import tempfile
import unittest

from service.datos.almacen_json import cargar_datos, guardar_datos


class TestAlmacenJson(unittest.TestCase):
    def setUp(self):
        self.carpeta = tempfile.TemporaryDirectory()
        self.ruta = os.path.join(self.carpeta.name, "datos.json")

    def tearDown(self):
        self.carpeta.cleanup()

    def escribir(self, contenido):
        with open(self.ruta, "w", encoding="utf-8") as archivo:
            archivo.write(contenido)

    def test_archivo_inexistente_devuelve_lista_vacia(self):
        self.assertEqual(cargar_datos(self.ruta), [])

    def test_archivo_vacio_devuelve_lista_vacia(self):
        self.escribir("   ")
        self.assertEqual(cargar_datos(self.ruta), [])

    def test_json_danado_devuelve_lista_vacia(self):
        self.escribir("{ esto no es json")
        self.assertEqual(cargar_datos(self.ruta), [])

    def test_json_no_lista_devuelve_lista_vacia(self):
        self.escribir('{"id": 1}')
        self.assertEqual(cargar_datos(self.ruta), [])

    def test_guardar_y_recargar(self):
        datos = [{"id": "A1", "nombre": "Salón"}]
        guardar_datos(self.ruta, datos)
        self.assertEqual(cargar_datos(self.ruta), datos)
        self.assertFalse(os.path.exists(self.ruta + ".tmp"))
