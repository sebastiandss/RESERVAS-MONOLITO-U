"""Ayudas pequeñas para las vistas."""
from datetime import date
from tkinter import messagebox


def hoy():
    """Devuelve la fecha actual como AAAA-MM-DD."""
    return date.today().strftime("%Y-%m-%d")


def avisar_error(error):
    """Muestra un error de negocio sin cerrar la ventana."""
    messagebox.showerror("Error", str(error))


def avisar(texto):
    """Muestra un aviso informativo."""
    messagebox.showinfo("Aviso", texto)


def limpiar_campos(*variables):
    """Pone en blanco las variables de entrada recibidas."""
    for variable in variables:
        variable.set("")


def limpiar(tabla):
    """Borra todas las filas del Treeview."""
    for fila in tabla.get_children():
        tabla.delete(fila)


def agregar_fila(tabla, valores):
    """Añade una fila al Treeview."""
    tabla.insert("", "end", values=valores)


def seleccion(tabla):
    """Devuelve los valores de la fila seleccionada o None."""
    item = tabla.focus()
    return tabla.item(item, "values") if item else None


def id_de(valor):
    """Extrae el ID de un texto con forma '1 - Nombre'."""
    return int(str(valor).split(" - ")[0])


def id_reserva_json(texto, reservas):
    """Devuelve el ID con el tipo guardado en el JSON."""
    for reserva in reservas:
        if str(reserva["id"]) == str(texto):
            return reserva["id"]
    return texto
