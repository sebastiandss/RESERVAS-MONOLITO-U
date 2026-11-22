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
