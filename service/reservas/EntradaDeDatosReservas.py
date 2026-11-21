def pedir_datos_reserva():
    id_usuario = input("Ingrese el ID del usuario: ")
    if not id_usuario:
        print("El ID del usuario no puede estar vacío.")
        return None

    id_espacio = input("Ingrese el ID del espacio: ")
    if not id_espacio:
        print("El ID del espacio no puede estar vacío.")
        return None

    fecha = input("Ingrese la fecha (AAAA-MM-DD): ")
    if not fecha:
        print("La fecha no puede estar vacía.")
        return None

    inicio = input("Ingrese la hora de inicio (HH:MM): ")
    if not inicio:
        print("La hora de inicio no puede estar vacía.")
        return None

    fin = input("Ingrese la hora de fin (HH:MM): ")
    if not fin:
        print("La hora de fin no puede estar vacía.")
        return None

    return {
        "id_usuario": id_usuario,
        "id_espacio": id_espacio,
        "fecha": fecha,
        "inicio": inicio,
        "fin": fin,
        "estado": "Vigente"
    }