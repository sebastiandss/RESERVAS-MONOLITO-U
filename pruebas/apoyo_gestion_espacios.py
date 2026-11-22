import json
import os
import tempfile
import unittest


class BaseGestionEspacios(unittest.TestCase):
    def setUp(self):
        self.carpeta = tempfile.TemporaryDirectory()
        self.ruta_espacios = os.path.join(self.carpeta.name, "espacios.json")
        self.ruta_reservas = os.path.join(self.carpeta.name, "reservas.json")
        self.escribir(self.ruta_espacios, [])
        self.escribir(self.ruta_reservas, [])

    def tearDown(self):
        self.carpeta.cleanup()

    def escribir(self, ruta, datos):
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False)

    def leer(self, ruta):
        with open(ruta, encoding="utf-8") as archivo:
            return json.load(archivo)
