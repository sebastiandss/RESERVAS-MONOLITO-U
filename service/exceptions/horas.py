from .excepciones import ErrorReserva


def validar_hora(hora):
    # Verifica formato HH:MM en 24 horas
    if type(hora) != str or len(hora) != 5 or hora[2] != ":":
        raise ErrorReserva("La hora debe tener formato HH:MM.")

    horas_txt = hora[0:2]
    minutos_txt = hora[3:5]
    if not (horas_txt.isdigit() and minutos_txt.isdigit()):
        raise ErrorReserva("La hora debe tener formato HH:MM.")

    horas = int(horas_txt)
    minutos = int(minutos_txt)
    if horas < 0 or horas > 23 or minutos < 0 or minutos > 59:
        raise ErrorReserva("La hora no es válida.")

    return True


def validar_rango_horas(hora_inicio, hora_fin):
    # Verifica que ambas horas sean válidas y que inicio sea menor que fin
    validar_hora(hora_inicio)
    validar_hora(hora_fin)

    inicio_min = int(hora_inicio[0:2]) * 60 + int(hora_inicio[3:5])
    fin_min = int(hora_fin[0:2]) * 60 + int(hora_fin[3:5])
    if inicio_min >= fin_min:
        raise ErrorReserva("La hora de inicio debe ser menor que la hora de fin.")

    return True
