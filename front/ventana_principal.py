"""Ventana principal con botones sencillos para cambiar de sección."""
import tkinter as tk

from service.gestor import Gestor
from service.gestor_consultas import GestorConsultas

from .vista_consultas import VistaConsultas
from .vista_espacios import VistaEspacios
from .vista_estados import VistaEstados
from .vista_reservas import VistaReservas
from .vista_usuarios import VistaUsuarios


class VentanaPrincipal(tk.Tk):
    """Muestra una sección a la vez; solo se cambia con un clic."""

    def __init__(self):
        super().__init__()
        self.title("Monolito de reservas")
        self.geometry("900x600")
        self.gestor = Gestor()
        self.consultas = GestorConsultas()

        barra = tk.Frame(self)
        barra.pack(fill="x")
        self.contenedor = tk.Frame(self)
        self.contenedor.pack(fill="both", expand=True)

        self.vistas = (
            VistaEspacios(self.contenedor, self.gestor),
            VistaUsuarios(self.contenedor, self.gestor),
            VistaReservas(self.contenedor, self.gestor),
            VistaEstados(self.contenedor, self.gestor, self.consultas),
            VistaConsultas(self.contenedor, self.consultas),
        )
        nombres = ("Espacios", "Usuarios", "Reservas", "Estados", "Consultas")
        for indice, (vista, nombre) in enumerate(zip(self.vistas, nombres)):
            tk.Button(barra, text=nombre,
                      command=lambda v=vista: self.mostrar(v)).grid(
                          row=0, column=indice, sticky="ew")
            barra.columnconfigure(indice, weight=1)
            vista.place(in_=self.contenedor, x=0, y=0,
                        relwidth=1, relheight=1)
        self.mostrar(self.vistas[0])

    def mostrar(self, vista):
        """Trae la sección al frente y refresca sus datos."""
        vista.tkraise()
        if hasattr(vista, "actualizar"):
            vista.actualizar()
