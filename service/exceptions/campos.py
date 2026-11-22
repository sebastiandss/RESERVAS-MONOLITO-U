def validar_campos_obligatorios(registro, campos_obligatorios):
    # Recibe un diccionario y la lista de claves obligatorias
    for campo in campos_obligatorios:
        if campo not in registro:
            return False
        valor = registro[campo]
        if valor is None or str(valor).strip() == "":
            return False

    return True
