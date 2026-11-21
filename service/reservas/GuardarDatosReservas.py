import json
from service.reservas.EntradaDeDatosReservas import pedir_datos_reserva

def guardar_reserva(nueva_reserva, ruta="data/reservas.json"):
    if nueva_reserva is None:
        return

    archivo = open(ruta, "r", encoding="utf-8")
    reservas = json.load(archivo)
    archivo.close()

    reservas.append(nueva_reserva)

    archivo = open(ruta, "w", encoding="utf-8")
    json.dump(reservas, archivo, indent=4, ensure_ascii=False)
    archivo.close()

    print("Reserva guardada correctamente.")

if __name__ == "__main__":
    datos = pedir_datos_reserva()
    guardar_reserva(datos)