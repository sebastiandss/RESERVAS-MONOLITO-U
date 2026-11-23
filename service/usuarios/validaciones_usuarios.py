from service.exceptions.excepciones import ErrorReserva


def normalizar_nombre(nombre):
    if not isinstance(nombre, str):
        raise ErrorReserva("El nombre del usuario es obligatorio.")
    nombre = " ".join(nombre.split())
    if not nombre:
        raise ErrorReserva("El nombre del usuario es obligatorio.")
    return nombre


def normalizar_documento(documento):
    if documento is None:
        raise ErrorReserva("El documento del usuario es obligatorio.")
    documento = str(documento).strip()
    if not documento:
        raise ErrorReserva("El documento del usuario es obligatorio.")
    if not documento.isdigit():
        raise ErrorReserva("El documento debe contener solo números.")
    return documento


def normalizar_telefono(telefono):
    if telefono is None:
        raise ErrorReserva("El teléfono del usuario es obligatorio.")
    telefono = str(telefono).strip()
    if not telefono:
        raise ErrorReserva("El teléfono del usuario es obligatorio.")
    return telefono


def validar_documento_unico(documento, usuarios):
    for usuario in usuarios:
        otro = str(usuario.get("documento", "")).strip()
        if otro == documento:
            raise ErrorReserva("Ya existe un usuario con ese documento.")
