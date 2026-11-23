"""Punto de entrada de la interfaz gráfica."""
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if RAIZ not in sys.path:
    sys.path.insert(0, RAIZ)
os.chdir(RAIZ)  # los JSON de data/ son relativos a la raíz

from front.ventana_principal import VentanaPrincipal  # noqa: E402


def main():
    """Abre la ventana principal."""
    VentanaPrincipal().mainloop()


if __name__ == "__main__":
    main()
