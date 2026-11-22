import json
import os
import tempfile
import unittest


class BaseGestionUsuarios(unittest.TestCase):
    def setUp(self):
        self.carpeta = tempfile.TemporaryDirectory()
        self.ruta_usuarios = os.path.join(self.carpeta.name, "usuarios.json")
        self.ruta_reservas = os.path.join(self.carpeta.name, "reservas.json")
        self.escribir(self.ruta_usuarios, [])
        self.escribir(self.ruta_reservas, [])

    def tearDown(self):
        self.carpeta.cleanup()

    def escribir(self, ruta, datos):
        archivo = open(ruta, "w", encoding="utf-8")
        json.dump(datos, archivo, ensure_ascii=False)
        archivo.close()

    def leer(self, ruta):
        archivo = open(ruta, encoding="utf-8")
        datos = json.load(archivo)
        archivo.close()
        return datos
