"""Selección de estado de reserva por consola."""

from modelos.reserva import ESTADOS_RESERVA


def pedir_estado():
    """Muestra los estados disponibles y devuelve el seleccionado."""
    print("Seleccione el estado de la reserva:")
    for numero, estado in enumerate(ESTADOS_RESERVA, start=1):
        print(f"{numero}. {estado}")

    opcion = input("Ingrese el número del estado: ").strip()
    if not opcion.isdigit():
        print("Debe ingresar un número válido.")
        return None

    indice = int(opcion) - 1
    if indice < 0 or indice >= len(ESTADOS_RESERVA):
        print("Opción fuera de rango.")
        return None

    return ESTADOS_RESERVA[indice]
