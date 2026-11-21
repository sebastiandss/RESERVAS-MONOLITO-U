from datetime import datetime


def pedir_datos_reserva():
    id_usuario = input("Ingrese el ID del usuario: ").strip()
    if not id_usuario:
        print("El ID del usuario no puede estar vacío.")
        return None

    id_espacio = input("Ingrese el ID del espacio: ").strip()
    if not id_espacio:
        print("El ID del espacio no puede estar vacío.")
        return None

    fecha = input("Ingrese la fecha (AAAA-MM-DD): ").strip()
    if not fecha:
        print("La fecha no puede estar vacía.")
        return None

    inicio = input("Ingrese la hora de inicio (HH:MM): ").strip()
    if not inicio:
        print("La hora de inicio no puede estar vacía.")
        return None

    fin = input("Ingrese la hora de fin (HH:MM): ").strip()
    if not fin:
        print("La hora de fin no puede estar vacía.")
        return None

    try:
        fecha = datetime.strptime(fecha, "%Y-%m-%d").strftime("%Y-%m-%d")
        inicio = datetime.strptime(inicio, "%H:%M").strftime("%H:%M")
        fin = datetime.strptime(fin, "%H:%M").strftime("%H:%M")
    except ValueError:
        print("Formato de fecha u hora inválido. Use AAAA-MM-DD y HH:MM.")
        return None

    return {
        "id_usuario": id_usuario,
        "id_espacio": id_espacio,
        "fecha": fecha,
        "inicio": inicio,
        "fin": fin,
        "estado": "Vigente"
    }