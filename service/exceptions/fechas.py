from .excepciones import ErrorReserva


def validar_fecha(fecha):
    # Verifica formato AAAA-MM-DD
    if type(fecha) != str or len(fecha) != 10:
        raise ErrorReserva("La fecha debe tener formato AAAA-MM-DD.")

    if fecha[4] != "-" or fecha[7] != "-":
        raise ErrorReserva("La fecha debe tener formato AAAA-MM-DD.")

    year_txt = fecha[0:4]
    month_txt = fecha[5:7]
    day_txt = fecha[8:10]
    if not (year_txt.isdigit() and month_txt.isdigit() and day_txt.isdigit()):
        raise ErrorReserva("La fecha debe tener formato AAAA-MM-DD.")

    year = int(year_txt)
    month = int(month_txt)
    day = int(day_txt)
    if year < 2000 or month < 1 or month > 12 or day < 1:
        raise ErrorReserva("La fecha no es válida.")

    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_per_month[1] = 29

    if day > days_per_month[month - 1]:
        raise ErrorReserva("La fecha no es válida.")

    return True
