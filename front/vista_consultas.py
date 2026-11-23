"""Vista con las consultas de disponibilidad y asignaciones."""
import tkinter as tk

from service.exceptions import ErrorReserva

from .apoyo_ui import agregar_fila, avisar_error, limpiar
from .formulario import boton, campo
from .tabla import crear_tabla


class VistaConsultas(tk.Frame):
    """Muestra espacios libres y reservas aprobadas por fecha."""

    def __init__(self, master, consultas):
        super().__init__(master)
        self.consultas = consultas
        self.fecha = tk.StringVar()
        self.inicio = tk.StringVar()
        self.fin = tk.StringVar()
        campo(self, "Fecha", self.fecha, 0)
        campo(self, "Inicio (HH:MM)", self.inicio, 1)
        campo(self, "Fin (HH:MM)", self.fin, 2)
        boton(self, "Disponibles", self.disponibles, 3)
        boton(self, "Asignaciones", self.asignaciones, 3, 1)
        self.tabla_libres = self._tabla(4, (
            "ID", "Nombre", "Capacidad", "Descripción"))
        self.tabla_asignadas = self._tabla(6, (
            "Espacio", "Usuario", "Inicio", "Fin", "Estado"))

    def _tabla(self, fila, columnas):
        marco = tk.Frame(self)
        marco.grid(row=fila, column=0, columnspan=2, sticky="nsew")
        self.rowconfigure(fila, weight=1)
        return crear_tabla(marco, columnas)

    def disponibles(self):
        """Consulta los espacios libres en la fecha y franja dadas."""
        limpiar(self.tabla_libres)
        try:
            espacios = self.consultas.consultar_disponibles(
                self.fecha.get(), self.inicio.get(), self.fin.get())
        except ErrorReserva as error:
            avisar_error(error)
            return
        for espacio in espacios:
            agregar_fila(self.tabla_libres, (
                espacio["id"], espacio["nombre"],
                espacio["capacidad"], espacio["descripcion"]))

    def asignaciones(self):
        """Consulta quién tiene los espacios en una fecha."""
        limpiar(self.tabla_asignadas)
        try:
            filas = self.consultas.consultar_asignaciones(self.fecha.get())
        except ErrorReserva as error:
            avisar_error(error)
            return
        for fila in filas:
            agregar_fila(self.tabla_asignadas, (
                fila["espacio"], fila["usuario"], fila["hora_inicio"],
                fila["hora_fin"], fila["estado"]))
