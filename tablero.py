from casilla import Casilla
from ficha import Ficha


class Tablero:

    def __init__(self):

        self.matriz = [[None for f in range(8)] for c in range(8)]
        self.matriz[0][0] = Casilla (Ficha('f_marron.png'), (0, 0), (100, 0))

        

    # def inicializar_tablero(self):
    #     """Metetodo utilizado para inicializar el tablero, con la posicion de juego inicial"""
    #
    #     x_pixels = 0        # Para contar los pixeles en x, y tenerlos como referencia en la casilla correspondiente
    #     y_pixels = 0        # Para contar los pixeles en y, y tenerlos como referencia en la casilla correspondiente
    #
    #     for f in range(len(self._matriz)):
    #         y_pixels += 100
    #         for c in range(len(self._matriz[f])):
    #             x_pixels += 100
    #             self._matriz[f][c] = None
    #
    #     return self._matriz

# a = Tablero()
#
# ma = a.inicializar_tablero()
#
# ma[0][0] = Casilla (Ficha('f_marron.png'), (0, 0), (100, 0))



