"""Vista para ver coincidencias y cambiar estados."""
import tkinter as tk

from models.reserva import ESTADOS_RESERVA
from service.exceptions import ErrorReserva

from .apoyo_ui import (
    agregar_fila, avisar_error, id_de, id_reserva_json, limpiar, seleccion,
)
from .formulario import boton, campo, combo
from .tabla import crear_tabla


class VistaEstados(tk.Frame):
    """Consulta reservas activas y permite cambiar su estado."""

    def __init__(self, master, gestor, consultas):
        super().__init__(master)
        self.gestor = gestor
        self.consultas = consultas
        self.espacio = tk.StringVar()
        self.fecha = tk.StringVar()
        self.inicio = tk.StringVar()
        self.fin = tk.StringVar()
        self.id_reserva = tk.StringVar()
        self._reservas = []
        self.estado = tk.StringVar(value=ESTADOS_RESERVA[0])
        self.caja_espacio = combo(self, "Espacio", self.espacio, 0, [])
        campo(self, "Fecha", self.fecha, 1)
        campo(self, "Inicio", self.inicio, 2)
        campo(self, "Fin", self.fin, 3)
        boton(self, "Buscar", self.buscar, 4)
        marco = tk.Frame(self)
        marco.grid(row=5, column=0, columnspan=2, sticky="nsew")
        self.tabla = crear_tabla(marco, (
            "ID", "Espacio", "Usuario", "Fecha", "Inicio", "Fin",
            "Actividad", "Estado",
        ))
        self.tabla.bind("<<TreeviewSelect>>", self._elegir)
        campo(self, "ID reserva", self.id_reserva, 6)
        combo(self, "Nuevo estado", self.estado, 7, ESTADOS_RESERVA)
        boton(self, "Cambiar estado", self.cambiar, 8)
        self.rowconfigure(5, weight=1)
        self.actualizar()

    def actualizar(self):
        """Recarga el combo de espacios."""
        espacios = [f"{e['id']} - {e['nombre']}"
                    for e in self.gestor.listar_espacios()]
        self.caja_espacio["values"] = espacios
        if espacios and not self.espacio.get():
            self.espacio.set(espacios[0])

    def _elegir(self, event):
        fila = seleccion(self.tabla)
        if fila:
            self.id_reserva.set(fila[0])

    def buscar(self):
        """Muestra las reservas activas que se cruzan."""
        limpiar(self.tabla)
        self._reservas = []
        if not self.espacio.get():
            return
        try:
            reservas = self.consultas.consultar_coincidentes(
                id_de(self.espacio.get()), self.fecha.get(),
                self.inicio.get(), self.fin.get())
        except ErrorReserva as error:
            avisar_error(error)
            return
        self._reservas = reservas
        for reserva in reservas:
            agregar_fila(self.tabla, (
                reserva["id"], reserva["espacio_id"], reserva["usuario_id"],
                reserva["fecha"], reserva["hora_inicio"], reserva["hora_fin"],
                reserva["actividad"], reserva["estado"],
            ))

    def cambiar(self):
        """Cambia el estado de la reserva indicada."""
        if not self.id_reserva.get():
            return
        id_elegido = id_reserva_json(self.id_reserva.get(), self._reservas)
        try:
            self.gestor.cambiar_estado(id_elegido, self.estado.get())
        except ErrorReserva as error:
            avisar_error(error)
        else:
            self.buscar()
