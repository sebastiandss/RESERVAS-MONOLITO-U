class ErrorReserva(Exception):
    # Excepción para avisar errores de validación o reglas del negocio
    pass

def validar_fecha(fecha):
    # Verifica formato AAAA-MM-DD 
    if type(fecha) != str or len(fecha) != 10:
        return False

    if fecha[4] != "-" or fecha[7] != "-":
        return False

    year_txt = fecha[0:4]
    month_txt = fecha[5:7]
    day_txt = fecha[8:10]

    if not (year_txt.isdigit() and month_txt.isdigit() and day_txt.isdigit()):
        return False

    year = int(year_txt)
    month = int(month_txt)
    day = int(day_txt)

    if year < 2000 or month < 1 or month > 12 or day < 1:
        return False

    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_per_month[1] = 29

    if day > days_per_month[month - 1]:
        return False

    return True


def validar_hora(hora):
    # Verifica formato HH:MM en 24 horas 
    if type(hora) != str or len(hora) != 5:
        return False

    if hora[2] != ":":
        return False

    horas_txt = hora[0:2]
    minutos_txt = hora[3:5]

    if not (horas_txt.isdigit() and minutos_txt.isdigit()):
        return False

    horas = int(horas_txt)
    minutos = int(minutos_txt)

    if horas < 0 or horas > 23 or minutos < 0 or minutos > 59:
        return False

    return True


def validar_rango_horas(hora_inicio, hora_fin):
    # Verifica que ambas horas sean válidas y que inicio sea menor que fin
    if not validar_hora(hora_inicio) or not validar_hora(hora_fin):
        return False

    inicio_min = int(hora_inicio[0:2]) * 60 + int(hora_inicio[3:5])
    fin_min = int(hora_fin[0:2]) * 60 + int(hora_fin[3:5])

    return inicio_min < fin_min


def validar_campos_obligatorios(registro, campos_obligatorios):
    # Recibe un diccionario (espacio, usuario o reserva) y la lista de claves obligatorias
    for campo in campos_obligatorios:
        if campo not in registro:
            return False
        valor = registro[campo]
        if valor is None or str(valor).strip() == "":
            return False

    return True