from casilla import Casilla
from ficha import Ficha


class Tablero:

    def __init__(self):

        self._matriz = [[None for f in range(8)] for c in range(8)]
        self.filas_ini_sup = [0, 1, 2]                                # Filas iniciales en la parte superior del tablero.
        self.filas_ini_inf = [5, 6, 7]                                # Filas iniciales en la parte inferior del tablero.


    def inicializar_tablero(self):
        """Metetodo utilizado para inicializar el tablero, con la posicion de juego inicial"""

        cont_pixels_x = 0        # Para contar los pixeles en x, y tenerlos como referencia en la casilla correspondiente
        cont_pixels_y = 0        # Para contar los pixeles en y, y tenerlos como referencia en la casilla correspondiente
        cont_pixels_ficha_x = -80
        cont_pixels_ficha_y = -80
        pixels_cuadro = 100

        for f in range(len(self._matriz)):      # Inicializando la matriz del tablero que va a contener los objetos casilla
            cont_pixels_y += pixels_cuadro
            cont_pixels_ficha_y += pixels_cuadro

            for c in range(len(self._matriz[f])):
                cont_pixels_x += pixels_cuadro
                cont_pixels_ficha_x += pixels_cuadro

                color = False                   # El color de la casilla
                if (f % 2 == 0 and c % 2 != 0) or (f % 2 != 0 and c % 2 == 0):     # Para determinar si el color de la casilla es solido
                    color = True                # Color solido

                # Por el momento solo se estara utilizando una ficha para pruebas.
                if f == 2 and c == 1:                                             #(x_izq, x_der, y_arriba, y_abajo )
                    self._matriz[f][c] = Casilla (Ficha('f_blanca.png', f, cont_pixels_ficha_x, cont_pixels_ficha_y), (f, c), (cont_pixels_x - pixels_cuadro, cont_pixels_x, cont_pixels_y - pixels_cuadro, cont_pixels_y), color)


                elif f == 5 and c == 2:                                             #(x_izq, x_der, y_arriba, y_abajo )
                    self._matriz[f][c] = Casilla (Ficha('f_marron.png', f, cont_pixels_ficha_x, cont_pixels_ficha_y), (f, c), (cont_pixels_x - pixels_cuadro, cont_pixels_x, cont_pixels_y - pixels_cuadro, cont_pixels_y), color)

                else:
                    self._matriz[f][c] = Casilla(None, (f, c), (cont_pixels_x - pixels_cuadro, cont_pixels_x, cont_pixels_y - pixels_cuadro, cont_pixels_y), color)


            cont_pixels_x = 0           # Bajar la columna
            cont_pixels_ficha_x = -80   # Reiniciar el contador de pixeles para acomodar la ficha.

        # for f in range(len(self._matriz)):
        #     for c in range(len(self._matriz[f])):
        #
        #         print(self._matriz[f][c])
        #
        #     print()
        #
        return self._matriz

    def getMatriz(self):
        return self._matriz

    def det_casilla(self, x, y):
        """Para determinar la casilla sobre la que se ha clickeado"""

        for f in range(len(self._matriz)):
            for c in range(len(self._matriz[f])):
                casilla = self._matriz[f][c]

                if (casilla.cor_pixeles[0] <= x < casilla.cor_pixeles[1]) and (casilla.cor_pixeles[2] <= y < casilla.cor_pixeles[3]):

                    return f, c

    def movimiento_valido(self, x, y, x_vieja, y_vieja):
        """Para determinar si la ficha se ha movido a una casilla valida"""

        f_vieja, c_vieja = self.det_casilla(x_vieja, y_vieja)                       # Para determinar, la casilla de arrancada de moviemiento.

        casilla_vieja = self._matriz[f_vieja][c_vieja]

        f, c = self.det_casilla(x, y)                                               # Para determinar, la casilla donde se pienza realizar el movimiento.

        casilla = self._matriz[f][c]

        if casilla_vieja.ficha.nom_archivo == 'f_blanca.png' or casilla_vieja.ficha.nom_archivo == 'f_marron.png':      # Logica mov. fichas simpoles

            if casilla_vieja.ficha.fila_inicial in self.filas_ini_sup:                                                                                              # Para fichas inicializadas en la filas superiores, solo pueden descender diagonalmente.

                if casilla.ficha == None and casilla.color == True and (f - 1) == f_vieja and (c + 1 == c_vieja or c - 1 == c_vieja):      # El mov. es valido si la ficha a sido movida a una casilla solida, ha decendido una fila,
                    return True                                                                                                            # y a aumentado una columna o disminuido una columna (ficha_normal).

            if casilla_vieja.ficha.fila_inicial in self.filas_ini_inf:                                                                     # El mov. es valido si la ficha a sido movida a una casilla solida, ha ascendido una fila,
                                                                                                                                           # y a aumentado una columna o disminuido una columna (ficha_normal).
                if casilla.ficha == None and casilla.color == True and (f + 1) == f_vieja and (c + 1 == c_vieja or c - 1 == c_vieja):      # El mov. es valido si la ficha a sido movida a una casilla solida y ha ascendido una fila (ficha_normal).
                    return True


        if casilla_vieja.ficha.nom_archivo == 'f_blanca_rey.png' or casilla_vieja.ficha.nom_archivo == 'f_marron_rey.png':

            if casilla.ficha == None and casilla.color == True and ((f - 1) == f_vieja or (f + 1) == f_vieja) and (c + 1 == c_vieja or c - 1 == c_vieja):  # El mov. es valido si la ficha a sido movida a una casilla solida, ha decendido una fila.
                                                                                                                                                           # ,subido una fila, aumentado una columna o aumentado una fila (ficha rey).
                return True


    def cop_ficha(self, x, y, ficha):
        """Para copiar una ficha de una casilla a otra y coronar fichas"""

        f, c = self.det_casilla(x, y)

        if f == 0 or f == 7:                            # En caso de que se llege a kings row

            if ficha.nom_archivo == 'f_marron.png':     # Coronando la ficha marron
                ficha = Ficha('f_marron_rey.png', f, x, y)
                ficha.rect.x = x
                ficha.rect.y = y

            if ficha.nom_archivo == 'f_blanca.png':     # Coronando la ficha blanca
                ficha = Ficha('f_blanca_rey.png', f, x, y)
                ficha.rect.x = x
                ficha.rect.y = y

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



