def pedir_datos():
    nombre = input("Ingrese su nombre: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío.")
        return None

    edad = input("Ingrese su edad: ").strip()
    if not edad.isdigit():
        print("La edad debe ser un número entero.")
        return None

    telefono = input("Ingrese su número de teléfono: ").strip()
    if not telefono.isdigit():
        print("El número de teléfono debe ser un número entero.")
        return None

    return {
        "nombre": nombre,
        "edad": int(edad),
        "telefono": int(telefono)
    }