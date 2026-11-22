from service.exceptions.excepciones import ErrorReserva


def normalizar_nombre(nombre):
    if not isinstance(nombre, str):
        raise ErrorReserva("El nombre del espacio es obligatorio.")
    nombre = " ".join(nombre.split())
    if not nombre:
        raise ErrorReserva("El nombre del espacio es obligatorio.")
    return nombre


def validar_capacidad(capacidad):
    if isinstance(capacidad, bool):
        raise ErrorReserva("La capacidad debe ser un número entero mayor a 0.")
    if isinstance(capacidad, str):
        capacidad = capacidad.strip()
        if not capacidad.isdigit():
            raise ErrorReserva("La capacidad debe ser un número entero mayor a 0.")
        capacidad = int(capacidad)
    if not isinstance(capacidad, int) or capacidad <= 0:
        raise ErrorReserva("La capacidad debe ser un número entero mayor a 0.")
    return capacidad


def validar_nombre_unico(nombre, espacios):
    clave = nombre.casefold()
    for espacio in espacios:
        otro = " ".join(str(espacio.get("nombre", "")).split()).casefold()
        if otro == clave:
            raise ErrorReserva(f"Ya existe un espacio con el nombre '{nombre}'.")
