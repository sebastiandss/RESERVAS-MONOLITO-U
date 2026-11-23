"""Vista para dar de alta y listar espacios."""
import tkinter as tk

from service.exceptions import ErrorReserva

from .apoyo_ui import agregar_fila, avisar_error, limpiar, limpiar_campos, seleccion
from .formulario import boton, campo
from .tabla import crear_tabla


class VistaEspacios(tk.Frame):
    """Formulario y tabla de espacios."""

    def __init__(self, master, gestor):
        super().__init__(master)
        self.gestor = gestor
        self.nombre = tk.StringVar()
        self.capacidad = tk.StringVar()
        self.descripcion = tk.StringVar()
        campo(self, "Nombre", self.nombre, 0)
        campo(self, "Capacidad", self.capacidad, 1)
        campo(self, "Descripción", self.descripcion, 2)
        boton(self, "Agregar", self.agregar, 3)
        boton(self, "Eliminar", self.eliminar, 3, 1)
        marco = tk.Frame(self)
        marco.grid(row=4, column=0, columnspan=2, sticky="nsew")
        self.tabla = crear_tabla(
            marco, ("ID", "Nombre", "Capacidad", "Descripción"))
        self.rowconfigure(4, weight=1)
        self.actualizar()

    def actualizar(self):
        """Vuelve a cargar la tabla desde la fachada."""
        limpiar(self.tabla)
        for espacio in self.gestor.listar_espacios():
            agregar_fila(self.tabla, (
                espacio["id"], espacio["nombre"],
                espacio["capacidad"], espacio["descripcion"],
            ))

    def agregar(self):
        """Da de alta un espacio con los datos del formulario."""
        try:
            self.gestor.agregar_espacio(
                self.nombre.get(), self.capacidad.get(), self.descripcion.get())
        except ErrorReserva as error:
            avisar_error(error)
        else:
            limpiar_campos(self.nombre, self.capacidad, self.descripcion)
            self.actualizar()

    def eliminar(self):
        """Elimina el espacio seleccionado en la tabla."""
        fila = seleccion(self.tabla)
        if not fila:
            return
        try:
            self.gestor.eliminar_espacio(int(fila[0]))
        except ErrorReserva as error:
            avisar_error(error)
        else:
            self.actualizar()
