"""Fachada orientada a objetos sobre la lógica del sistema."""

from service.espacios.GestionarEspacios import agregar_espacio, eliminar_espacio, listar_espacios
from service.usuarios.GestionUsuarios import agregar_usuario, eliminar_usuario, listar_usuarios
from service.reservas.gestion import cambiar_estado_reserva, registrar_reserva


class Gestor:
    """Agrupa las operaciones principales del sistema de reservas."""

    def agregar_espacio(self, nombre, capacidad, descripcion=""):
        return agregar_espacio(nombre, capacidad, descripcion)

    def listar_espacios(self):
        return listar_espacios()

    def eliminar_espacio(self, id_espacio):
        return eliminar_espacio(id_espacio)

    def agregar_usuario(self, nombre, documento, telefono):
        return agregar_usuario(nombre, documento, telefono)

    def listar_usuarios(self):
        return listar_usuarios()

    def eliminar_usuario(self, id_usuario):
        return eliminar_usuario(id_usuario)

    def registrar_reserva(self, espacio_id, usuario_id, fecha,
                          hora_inicio, hora_fin, actividad, fecha_actual):
        return registrar_reserva(espacio_id, usuario_id, fecha,
                                 hora_inicio, hora_fin, actividad, fecha_actual)

    def cambiar_estado(self, id_reserva, nuevo_estado):
        return cambiar_estado_reserva(id_reserva, nuevo_estado)
