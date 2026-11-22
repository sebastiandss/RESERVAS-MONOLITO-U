from modelos.reserva import crear_reserva
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
        mismo_espacio = reserva["espacio_id"] == espacio_id
        mismo_dia = reserva["fecha"] == fecha
        esta_aprobada = reserva["estado"] == "Aprobada"

        if mismo_espacio and mismo_dia and esta_aprobada:
            
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