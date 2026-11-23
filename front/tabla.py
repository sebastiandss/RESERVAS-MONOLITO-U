"""Tabla sencilla con columnas y barra de desplazamiento."""
from tkinter import ttk


def crear_tabla(master, columnas, anchos=None):
    """Devuelve un Treeview listo para mostrar filas."""
    tabla = ttk.Treeview(master, columns=columnas, show="headings", height=8)
    for indice, nombre in enumerate(columnas):
        ancho = anchos[indice] if anchos else 110
        tabla.heading(nombre, text=nombre)
        tabla.column(nombre, width=ancho, anchor="w")
    barra = ttk.Scrollbar(master, orient="vertical", command=tabla.yview)
    tabla.configure(yscrollcommand=barra.set)
    barra.pack(side="right", fill="y")
    tabla.pack(side="left", fill="both", expand=True)
    return tabla
