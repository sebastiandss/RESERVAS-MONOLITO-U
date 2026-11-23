"""Vista para registrar reservas."""
import tkinter as tk

from service.exceptions import ErrorReserva

from .apoyo_ui import avisar, avisar_error, hoy, id_de, limpiar_campos
from .formulario import boton, campo, combo


class VistaReservas(tk.Frame):
    """Formulario sencillo de alta de reservas."""

    def __init__(self, master, gestor):
        super().__init__(master)
        self.gestor = gestor
        self.espacio = tk.StringVar()
        self.usuario = tk.StringVar()
        self.fecha = tk.StringVar(value=hoy())
        self.inicio = tk.StringVar()
        self.fin = tk.StringVar()
        self.actividad = tk.StringVar()
        self.caja_espacio = combo(self, "Espacio", self.espacio, 0, [])
        self.caja_usuario = combo(self, "Usuario", self.usuario, 1, [])
        campo(self, "Fecha (AAAA-MM-DD)", self.fecha, 2)
        campo(self, "Inicio (HH:MM)", self.inicio, 3)
        campo(self, "Fin (HH:MM)", self.fin, 4)
        campo(self, "Actividad", self.actividad, 5)
        boton(self, "Reservar", self.reservar, 6)
        self.actualizar()

    def actualizar(self):
        """Recarga los combos de espacios y usuarios."""
        espacios = [f"{e['id']} - {e['nombre']}"
                    for e in self.gestor.listar_espacios()]
        usuarios = [f"{u['id']} - {u['nombre']}"
                    for u in self.gestor.listar_usuarios()]
        self.caja_espacio["values"] = espacios
        self.caja_usuario["values"] = usuarios
        if espacios and not self.espacio.get():
            self.espacio.set(espacios[0])
        if usuarios and not self.usuario.get():
            self.usuario.set(usuarios[0])

    def reservar(self):
        """Registra la reserva usando hoy como fecha actual."""
        if not self.espacio.get() or not self.usuario.get():
            avisar("Primero agrega espacios y usuarios.")
            return
        try:
            reserva = self.gestor.registrar_reserva(
                id_de(self.espacio.get()), id_de(self.usuario.get()),
                self.fecha.get(), self.inicio.get(), self.fin.get(),
                self.actividad.get(), hoy(),
            )
        except ErrorReserva as error:
            avisar_error(error)
            return
        mensaje = f"Reserva {reserva['id']} registrada como Pendiente."
        if reserva.get("aviso"):
            mensaje += "\n" + reserva["aviso"]
        avisar(mensaje)
        limpiar_campos(self.inicio, self.fin, self.actividad)
