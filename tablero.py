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

                color = False                   # El color de la casilla

                if (f % 2 == 0 and c % 2 != 0) or (f % 2 != 0 and c % 2 == 0):     # Para determinar si el color de la casilla es solido

                    color = True

                # Por el momento solo se estara utilizando una ficha para pruebas.
                if f == 0 and c == 1:                                             #(x_izq, x_der, y_arriba, y_abajo )

                    self._matriz[f][c] = Casilla (Ficha('f_marron.png'), (f, c), (cont_pixels_x - pixels_cuadro, cont_pixels_x, cont_pixels_y - pixels_cuadro, cont_pixels_y), color)

                else:
                    self._matriz[f][c] = Casilla(None, (f, c), (cont_pixels_x - pixels_cuadro, cont_pixels_x, cont_pixels_y - pixels_cuadro, cont_pixels_y), color)

            cont_pixels_x = 0           # Bajar la columna

        # for f in range(len(self._matriz)):
        #     for c in range(len(self._matriz[f])):
        #
        #         print(self._matriz[f][c])
        #
        #     print()
        #
        return self._matriz

    def det_casilla(self, x, y):
        """Para determinar la casilla sobre la que se ha clickeado"""

        for f in range(len(self._matriz)):
            for c in range(len(self._matriz[f])):
                casilla = self._matriz[f][c]

                if (casilla.cor_pixeles[0] < x < casilla.cor_pixeles[1]) and (casilla.cor_pixeles[2] < y < casilla.cor_pixeles[3]):

                    return f, c

    def movimiento_valido(self, x, y, x_vieja, y_vieja):
        """Para determinar si la ficha se ha movido a una casilla valida"""

        f_vieja, c_vieja = self.det_casilla(x_vieja, y_vieja)                       # Para determinar, la casilla de arrancada de moviemiento.

        f, c = self.det_casilla(x, y)                                               # Para determinar, la casilla de actual

        casilla = self._matriz[f][c]

        if casilla.ficha == None and casilla.color == True and  (f - 1) == f_vieja: # El mov. es valido si la ficha a sido movida a una casilla solida y ha decendido una fila.

            return True

    def cop_ficha(self, x, y, ficha):
        """Para copiar una ficha de una casilla a otra"""

        f, c = self.det_casilla(x, y)
        casilla = self._matriz[f][c]
        casilla.ficha = ficha


    def casilla_activa(self, x, y):
        """Para mover una ficha de casilla"""

        f, c = self.det_casilla(x, y)
        return self._matriz[f][c]



#a = Tablero()
#
# ma = a.inicializar_tablero()
#
# ma[0][0] = Casilla (Ficha('f_marron.png'), (0, 0), (100, 0))



