import json
from service.reservas.EntradaDeDatosReservas import pedir_datos_reserva
from service.usuarios.usuarios_unicos import generar_id, existe_id

def guardar_reserva(nueva_reserva, ruta="data/reservas.json"):
    if nueva_reserva is None:
        return

    archivo = open(ruta, "r", encoding="utf-8")
    reservas = json.load(archivo)
    archivo.close()

    codigo = generar_id()
    while existe_id(codigo, reservas, "id_reserva"):
        codigo = generar_id()
    nueva_reserva["id_reserva"] = codigo

    reservas.append(nueva_reserva)

    archivo = open(ruta, "w", encoding="utf-8")
    json.dump(reservas, archivo, indent=4, ensure_ascii=False)
    archivo.close()

    print("Reserva guardada correctamente con ID:", codigo)

if __name__ == "__main__":
    datos = pedir_datos_reserva()
    guardar_reserva(datos)