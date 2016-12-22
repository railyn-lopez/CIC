from casilla import Casilla
from ficha import Ficha


class Tablero:

    def __init__(self):

        self._matriz = [[None for f in range(8)] for c in range(8)]


    def inicializar_tablero(self):
        """Metetodo utilizado para inicializar el tablero, con la posicion de juego inicial"""

        cont_pixels_x = 0        # Para contar los pixeles en x, y tenerlos como referencia en la casilla correspondiente
        cont_pixels_y = 0        # Para contar los pixeles en y, y tenerlos como referencia en la casilla correspondiente
        pixels_cuadro = 100

        for f in range(len(self._matriz)):      # Inicializando la matriz del tablero que va a contener los objetos casilla
            cont_pixels_y += pixels_cuadro
            for c in range(len(self._matriz[f])):
                cont_pixels_x += pixels_cuadro

                # Por el momento solo se estara utilizando una ficha para pruebas.
                if f == 0 and c == 1:                                             #(superior_izq, superior_der, inferior_izq, inferior_der )
                    self._matriz[f][c] = Casilla (Ficha('f_marron.png'), (f, c), (cont_pixels_x - pixels_cuadro, cont_pixels_x, cont_pixels_y - pixels_cuadro, cont_pixels_y))

                else:
                    self._matriz[f][c] = Casilla(None, (f, c), (cont_pixels_x - pixels_cuadro, cont_pixels_x, cont_pixels_y - pixels_cuadro, cont_pixels_y))

            cont_pixels_x = 0           # Bajar la columna


        return self._matriz

    def det_casilla(self, x, y):
        """Para determinar la casilla sobre la que se ha clickeado"""

        for f in range(len(self._matriz)):
            for c in range(len(self._matriz[f])):
                casilla = self._matriz[f][c]

                if (casilla.cor_pixeles[0] < x < casilla.cor_pixeles[1]) and (casilla.cor_pixeles[2] < y < casilla.cor_pixeles[3]):

                    return f, c

    def movimiento_valido(self, x, y):
        """Para determinar si la ficha se ha movido a una casilla valida"""

        f, c = self.det_casilla(x, y)

        casilla = self._matriz[f][c]

        if casilla.ficha == None:

            #self._matriz[f][c] = casilla

            return True

#a = Tablero()
#
# ma = a.inicializar_tablero()
#
# ma[0][0] = Casilla (Ficha('f_marron.png'), (0, 0), (100, 0))



