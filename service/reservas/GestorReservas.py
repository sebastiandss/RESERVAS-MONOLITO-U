from modelos.reserva import crear_reserva, ESTADOS_RESERVA
from service.datos.almacen_json import cargar_datos, guardar_datos
from service.exceptions.excepciones import ErrorReserva
from service.exceptions.fechas import validar_fecha
from service.exceptions.horas import validar_rango_horas
from service.GeracionIdUnicos import generar_id, existe_id

RUTA_USUARIOS = "data/usuarios.json"
RUTA_ESPACIOS = "data/espacios.json"
RUTA_RESERVAS = "data/reservas.json"

def registrar_reserva(espacio_id, usuario_id, fecha, hora_inicio, hora_fin, actividad, fecha_actual):
    if actividad == "" or actividad is None:
        raise ErrorReserva("Escribe cuál es la actividad de la reserva.")

    usuarios = cargar_datos(RUTA_USUARIOS)
    usuario_encontrado = False

    for usuario in usuarios:
        if usuario["id"] == usuario_id:
            usuario_encontrado = True

    if usuario_encontrado == False:
        raise ErrorReserva("Ese usuario no está registrado.")

    espacios = cargar_datos(RUTA_ESPACIOS)
    espacio_encontrado = False

    for espacio in espacios:
        if espacio["id"] == espacio_id:
            espacio_encontrado = True

    if espacio_encontrado == False:
        raise ErrorReserva("Ese espacio no está registrado.")

    validar_fecha(fecha)
    validar_fecha(fecha_actual)
    validar_rango_horas(hora_inicio, hora_fin)

    if fecha < fecha_actual:
        raise ErrorReserva("No puedes reservar en una fecha que ya pasó.")

    reservas = cargar_datos(RUTA_RESERVAS)

    for reserva in reservas:
        if reserva["espacio_id"] == espacio_id and reserva["fecha"] == fecha:
            if reserva["estado"] == "Aprobada":
                if hora_inicio < reserva["hora_fin"] and hora_fin > reserva["hora_inicio"]:
                    raise ErrorReserva("Ese espacio ya está ocupado en ese horario.")

    nuevo_id = generar_id()
    while existe_id(nuevo_id, reservas, "id"):
        nuevo_id = generar_id()

    nueva_reserva = crear_reserva(
        nuevo_id,
        espacio_id,
        usuario_id,
        fecha,
        hora_inicio,
        hora_fin,
        actividad,
        "Pendiente"
    )

    reservas.append(nueva_reserva)
    guardar_datos(RUTA_RESERVAS, reservas)
    return nueva_reserva

def cambiar_estado_reserva(id_reserva, nuevo_estado):
    if nuevo_estado not in ESTADOS_RESERVA:
        raise ErrorReserva("Estado no válido. Solo se permite: Pendiente, Aprobada, Rechazada o Cancelada.")

    reservas = cargar_datos(RUTA_RESERVAS)
    reserva_encontrada = None

    for reserva in reservas:
        if reserva["id"] == id_reserva:
            reserva_encontrada = reserva

    if reserva_encontrada is None:
        raise ErrorReserva("No existe ninguna reserva con ese ID.")

    if nuevo_estado == "Aprobada":
        for otra in reservas:
                if otra["espacio_id"] == reserva_encontrada["espacio_id"] and otra["fecha"] == reserva_encontrada["fecha"]:
                    if otra["estado"] == "Aprobada":
                        if reserva_encontrada["hora_inicio"] < otra["hora_fin"] and reserva_encontrada["hora_fin"] > otra["hora_inicio"]:
                            raise ErrorReserva("No se puede aprobar porque se cruza con otra reserva aprobada.")
                        
    reserva_encontrada["estado"] = nuevo_estado
    guardar_datos(RUTA_RESERVAS, reservas)

    return reserva_encontrada