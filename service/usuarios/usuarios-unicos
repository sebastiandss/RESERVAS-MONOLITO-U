import random
import string

def generar_id():
    caracteres = string.ascii_uppercase + string.digits
    return ''.join(random.choices(caracteres, k=5))

def existe_id(codigo, lista_registros, nombre_clave):
    for registro in lista_registros:
        if registro[nombre_clave] == codigo:
            return True
    return False