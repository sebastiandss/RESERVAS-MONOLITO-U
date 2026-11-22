from service.datos.almacen_json import cargar_datos


def siguiente_id(usuarios):
    mayor = 0
    for usuario in usuarios:
        id_actual = str(usuario.get("id", ""))
        if id_actual.isdigit():
            numero = int(id_actual)
            if numero > mayor:
                mayor = numero
    return mayor + 1


def reservas_del_usuario(id_usuario, ruta_reservas):
    reservas = cargar_datos(ruta_reservas)
    clave = str(id_usuario)
    encontradas = []
    for reserva in reservas:
        if str(reserva.get("usuario_id", "")) == clave:
            encontradas.append(reserva)
        elif str(reserva.get("id_usuario", "")) == clave:
            encontradas.append(reserva)
    return encontradas


def clave_orden(usuario):
    return str(usuario.get("nombre", "")).lower()
