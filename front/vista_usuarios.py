"""Vista para dar de alta y listar usuarios."""
import tkinter as tk

from service.exceptions import ErrorReserva

from .apoyo_ui import agregar_fila, avisar_error, limpiar, limpiar_campos, seleccion
from .formulario import boton, campo
from .tabla import crear_tabla


class VistaUsuarios(tk.Frame):
    """Formulario y tabla de usuarios."""

    def __init__(self, master, gestor):
        super().__init__(master)
        self.gestor = gestor
        self.nombre = tk.StringVar()
        self.documento = tk.StringVar()
        self.telefono = tk.StringVar()
        campo(self, "Nombre", self.nombre, 0)
        campo(self, "Documento", self.documento, 1)
        campo(self, "Teléfono", self.telefono, 2)
        boton(self, "Agregar", self.agregar, 3)
        boton(self, "Eliminar", self.eliminar, 3, 1)
        marco = tk.Frame(self)
        marco.grid(row=4, column=0, columnspan=2, sticky="nsew")
        self.tabla = crear_tabla(
            marco, ("ID", "Nombre", "Documento", "Teléfono"))
        self.rowconfigure(4, weight=1)
        self.actualizar()

    def actualizar(self):
        """Vuelve a cargar la tabla desde la fachada."""
        limpiar(self.tabla)
        for usuario in self.gestor.listar_usuarios():
            agregar_fila(self.tabla, (
                usuario["id"], usuario["nombre"],
                usuario["documento"], usuario["telefono"],
            ))

    def agregar(self):
        """Da de alta un usuario con los datos del formulario."""
        try:
            self.gestor.agregar_usuario(
                self.nombre.get(), self.documento.get(), self.telefono.get())
        except ErrorReserva as error:
            avisar_error(error)
        else:
            limpiar_campos(self.nombre, self.documento, self.telefono)
            self.actualizar()

    def eliminar(self):
        """Elimina el usuario seleccionado en la tabla."""
        fila = seleccion(self.tabla)
        if not fila:
            return
        try:
            self.gestor.eliminar_usuario(int(fila[0]))
        except ErrorReserva as error:
            avisar_error(error)
        else:
            self.actualizar()
