from service.datos.almacen_json import cargar_datos
from service.exceptions.excepciones import ErrorReserva
from service.exceptions.fechas import validar_fecha
from service.exceptions.horas import validar_rango_horas

RUTA_USUARIOS = "data/usuarios.json"
RUTA_ESPACIOS = "data/espacios.json"
RUTA_RESERVAS = "data/reservas.json"



def consultar_quien_tiene_espacios(fecha):

    validar_fecha(fecha)

    reservas = cargar_datos(RUTA_RESERVAS)
    espacios = cargar_datos(RUTA_ESPACIOS)
    usuarios = cargar_datos(RUTA_USUARIOS)

    lista_resultados = []

   
    for reserva in reservas:
        if reserva["fecha"] == fecha:
     
            nombre_espacio = "Espacio no encontrado"
            for espacio in espacios:
                if espacio["id"] == reserva["espacio_id"]:
                    nombre_espacio = espacio["nombre"]

    
            nombre_usuario = "Usuario no encontrado"
            for usuario in usuarios:
                if usuario["id"] == reserva["usuario_id"]:
                    nombre_usuario = usuario["nombre"]


            dato = {
                "espacio": nombre_espacio,
                "usuario": nombre_usuario,
                "hora_inicio": reserva["hora_inicio"],
                "hora_fin": reserva["hora_fin"],
                "estado": reserva["estado"]
            }
            lista_resultados.append(dato)

    if len(lista_resultados) == 0:
        raise ErrorReserva("No hay espacios reservados para esa fecha.")

    return lista_resultados


def consultar_espacios_disponibles(fecha, hora_inicio, hora_fin):
    validar_fecha(fecha)
    validar_rango_horas(hora_inicio, hora_fin)

    espacios = cargar_datos(RUTA_ESPACIOS)
    reservas = cargar_datos(RUTA_RESERVAS)

    espacios_libres = []

    for espacio in espacios:
        ocupado = False

        for reserva in reservas:
            if reserva["espacio_id"] == espacio["id"] and reserva["fecha"] == fecha:
                if reserva["estado"] == "Aprobada":
                    if hora_inicio < reserva["hora_fin"] and hora_fin > reserva["hora_inicio"]:
                        ocupado = True

        if ocupado == False:
            espacios_libres.append(espacio)

    if len(espacios_libres) == 0:
        raise ErrorReserva("No hay espacios disponibles en esa fecha y horario.")

    return espacios_libres


def consultar_reservas_coincidentes(espacio_id, fecha, hora_inicio, hora_fin):

    validar_fecha(fecha)
    validar_rango_horas(hora_inicio, hora_fin)

    reservas = cargar_datos(RUTA_RESERVAS)
    coincidentes = []

    for reserva in reservas:
        if reserva["espacio_id"] == espacio_id and reserva["fecha"] == fecha:
            if hora_inicio < reserva["hora_fin"] and hora_fin > reserva["hora_inicio"]:
                coincidentes.append(reserva)

    if len(coincidentes) == 0:
        raise ErrorReserva("No se encontraron reservas coincidentes en ese horario.")

    return coincidentes