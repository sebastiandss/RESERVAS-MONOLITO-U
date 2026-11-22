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
