"""Controles simples reutilizables por las vistas."""
import tkinter as tk
from tkinter import ttk


def campo(master, texto, variable, fila, columna=0):
    """Crea etiqueta + entry y los coloca en la cuadrícula."""
    tk.Label(master, text=texto).grid(row=fila, column=columna, sticky="w")
    tk.Entry(master, textvariable=variable).grid(row=fila, column=columna + 1)


def combo(master, texto, variable, fila, valores, columna=0):
    """Crea etiqueta + combobox y devuelve el combobox."""
    tk.Label(master, text=texto).grid(row=fila, column=columna, sticky="w")
    caja = ttk.Combobox(master, textvariable=variable, values=valores,
                        state="readonly")
    caja.grid(row=fila, column=columna + 1)
    return caja


def boton(master, texto, comando, fila, columna=0):
    """Crea un botón simple en la cuadrícula."""
    tk.Button(master, text=texto, command=comando).grid(row=fila, column=columna)
