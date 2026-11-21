def pedir_datos_espacio():
    nombre = input("Ingrese el nombre del espacio: ")
    if not nombre:
        print("El nombre no puede estar vacío.")
        return None

    tipo = input("Ingrese el tipo de espacio (ej. Salón, Cancha, Auditorio): ")
    if not tipo:
        print("El tipo no puede estar vacío.")
        return None

    ubicacion = input("Ingrese la ubicación del espacio: ")
    if not ubicacion:
        print("La ubicación no puede estar vacía.")
        return None

    return {
        "nombre": nombre,
        "tipo": tipo,
        "ubicacion": ubicacion
    }