from casilla import Casilla
from ficha import Ficha


class Tablero:

    def __init__(self):

        self._matriz = [[None for f in range(8)] for c in range(8)]   # Matriz del tablero
        self.filas_ini_sup = [0, 1, 2]                                # Filas iniciales en la parte superior del tablero.
        self.filas_ini_inf = [5, 6, 7]                                # Filas iniciales en la parte inferior del tablero.
        self.ficha_1 = 'f_blanca_.png'                                # Variable global para hacer el juego independiente de la ficha
        self.ficha_1_rey = 'f_blanca_rey_.png'
        self.ficha_2 = 'f_marron_.png'                                # Variable global para hacer el juego independiente de la ficha
        self.ficha_2_rey = 'f_marron_rey_.png'

        self.cont_f1 = 0                                              # Para contar las fichas comidas
        self.cont_f2 = 0                                              # Para contar las fichas comidas

        self.cont_turno = 0                                           # Utilizado para determinar el color al que le toca mover, aumentara en uno con cada movimiento valido.

        self.orden_fichas = 'b'                                       # Por defecto, las fichas oscuras estaran debajo

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

                # Llenando las casillas

                if self.orden_fichas == 'b':

                    if f < 3 and color == True:                         # Llenando las primeras 3 filas
                        self._matriz[f][c] = Casilla(Ficha(self.ficha_1, f, cont_pixels_ficha_x, cont_pixels_ficha_y), (f, c), (cont_pixels_x - pixels_cuadro, cont_pixels_x, cont_pixels_y - pixels_cuadro, cont_pixels_y), color)

                    elif f > 4 and color == True:                       # Llenando las ultimas 3 filas
                        self._matriz[f][c] = Casilla(Ficha(self.ficha_2, f, cont_pixels_ficha_x, cont_pixels_ficha_y), (f, c), (cont_pixels_x - pixels_cuadro, cont_pixels_x, cont_pixels_y - pixels_cuadro, cont_pixels_y), color)

                    else:
                        self._matriz[f][c] = Casilla(None, (f, c), ( cont_pixels_x - pixels_cuadro, cont_pixels_x, cont_pixels_y - pixels_cuadro, cont_pixels_y), color)

                if self.orden_fichas == 'a':

                    if f < 3 and color == True:  # Llenando las primeras 3 filas
                        self._matriz[f][c] = Casilla(Ficha(self.ficha_2, f, cont_pixels_ficha_x, cont_pixels_ficha_y), (f, c), (cont_pixels_x - pixels_cuadro, cont_pixels_x, cont_pixels_y - pixels_cuadro, cont_pixels_y), color)

                    elif f > 4 and color == True:  # Llenando las ultimas 3 fila
                        self._matriz[f][c] = Casilla(Ficha(self.ficha_1, f, cont_pixels_ficha_x, cont_pixels_ficha_y), (f, c), (cont_pixels_x - pixels_cuadro, cont_pixels_x, cont_pixels_y - pixels_cuadro, cont_pixels_y), color)

                    else:
                        self._matriz[f][c] = Casilla(None, (f, c), (cont_pixels_x - pixels_cuadro, cont_pixels_x, cont_pixels_y - pixels_cuadro, cont_pixels_y), color)


                # Por el momento solo se estara utilizando una ficha para pruebas.
                # if (f == 0 and c == 1) or (f == 0 and c == 3) or (f == 0 and c == 5) or (f == 0 and c == 7) or (f == 1 and c == 0) or (f == 1 and c == 2) or (f == 1 and c == 4) or (f == 1 and c == 6) or (f == 2 and c == 1) or (f == 2 and c == 3) or (f == 2 and c == 5) or (f == 2 and c == 7):                                              #(x_izq, x_der, y_arriba, y_abajo )
                #     self._matriz[f][c] = Casilla (Ficha(self.ficha_1, f, cont_pixels_ficha_x, cont_pixels_ficha_y), (f, c), (cont_pixels_x - pixels_cuadro, cont_pixels_x, cont_pixels_y - pixels_cuadro, cont_pixels_y), color)
                #
                # elif (f == 7 and c == 0) or (f == 7 and c == 2) or (f == 7 and c == 4) or (f == 7 and c == 6) or (f == 6 and c == 1) or (f == 6 and c == 3) or (f == 6 and c == 3) or (f == 6 and c == 5) or (f == 6 and c == 7) or (f == 5 and c == 0) or (f == 5 and c == 2) or (f == 5 and c == 4) or (f == 5 and c == 6):                                             #(x_izq, x_der, y_arriba, y_abajo )
                #     self._matriz[f][c] = Casilla (Ficha(self.ficha_2, f, cont_pixels_ficha_x, cont_pixels_ficha_y), (f, c), (cont_pixels_x - pixels_cuadro, cont_pixels_x, cont_pixels_y - pixels_cuadro, cont_pixels_y), color)
                #
                # else:
                #     self._matriz[f][c] = Casilla(None, (f, c), (cont_pixels_x - pixels_cuadro, cont_pixels_x, cont_pixels_y - pixels_cuadro, cont_pixels_y), color)


            cont_pixels_x = 0           # Bajar la columna
            cont_pixels_ficha_x = -80   # Reiniciar el contador de pixeles para acomodar la ficha.

        # for f in range(len(self._matriz)):
        #     for c in range(len(self._matriz[f])):
        #
        #         print(self._matriz[f][c])
        #
        #     print()

        return self._matriz

    def getMatriz(self):
        return self._matriz

    def det_casilla(self, x, y):
        """Para sacar las coordenadas de la casilla a traves de la posicion del raton"""

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

        if casilla_vieja.ficha.nom_archivo == self.ficha_1 or casilla_vieja.ficha.nom_archivo == self.ficha_2:      # Logica mov. fichas simpoles

            if casilla_vieja.ficha.fila_inicial in self.filas_ini_sup:                                                                                              # Para fichas inicializadas en la filas superiores, solo pueden descender diagonalmente.

                if casilla.ficha == None and casilla.color == True and (f - 1) == f_vieja and (c + 1 == c_vieja or c - 1 == c_vieja):      # El mov. es valido si la ficha a sido movida a una casilla solida, ha decendido una fila,
                    return True                                                                                                            # y a aumentado una columna o disminuido una columna (ficha_normal).

            if casilla_vieja.ficha.fila_inicial in self.filas_ini_inf:                                                                     # El mov. es valido si la ficha a sido movida a una casilla solida, ha ascendido una fila,
                                                                                                                                           # y a aumentado una columna o disminuido una columna (ficha_normal).
                if casilla.ficha == None and casilla.color == True and (f + 1) == f_vieja and (c + 1 == c_vieja or c - 1 == c_vieja):      # El mov. es valido si la ficha a sido movida a una casilla solida y ha ascendido una fila (ficha_normal).
                    return True


        if casilla_vieja.ficha.nom_archivo == self.ficha_1_rey or casilla_vieja.ficha.nom_archivo == self.ficha_2_rey:

            if casilla.ficha == None and casilla.color == True and ((f - 1) == f_vieja or (f + 1) == f_vieja) and (c + 1 == c_vieja or c - 1 == c_vieja):  # El mov. es valido si la ficha a sido movida a una casilla solida, ha decendido una fila.
                                                                                                                                                           # ,subido una fila, aumentado una columna o aumentado una fila (ficha rey).
                return True
                                                                               #(f_nueva, c_nueva, f_vieja, c_vieja)

    def salto_valido(self, x = None, y = None, x_vieja = None, y_vieja = None, coor_fichas = None):
        """Para determinar si la ficha ha saltado validamente"""

        if coor_fichas == None:                                                         # En caso de que se tengan que determinar la posicion de las casillas, a traves del mouse

            f_vieja, c_vieja = self.det_casilla(x_vieja, y_vieja)                       # Para determinar, la casilla de arrancada de moviemiento
            casilla_vieja = self._matriz[f_vieja][c_vieja]

            f, c = self.det_casilla(x, y)                                               # Para determinar, la casilla donde se pienza realizar el movimiento.
            casilla = self._matriz[f][c]


        else:                                                                           # En caso de que se tengan las coordenadas de las casillas

            f_vieja, c_vieja = coor_fichas[2], coor_fichas[3]                           # Para determinar, la casilla de arrancada de moviemiento
            casilla_vieja = self._matriz[f_vieja][c_vieja]

            f, c = coor_fichas[0], coor_fichas[1]                                       # Para determinar, la casilla donde se pienza realizar el movimiento.
            casilla = self._matriz[f][c]




        if casilla_vieja.ficha.nom_archivo == self.ficha_1 or casilla_vieja.ficha.nom_archivo == self.ficha_2:                       # Logica salto men

            if casilla_vieja.ficha.fila_inicial in self.filas_ini_sup:                                                                     # Para fichas inicializadas en la filas superiores, solo pueden descender diagonalmente.
                                                                                                                                           # El salto es valido si la ficha a sido movida a una casilla solida, ha asendido una fila,
                if casilla.ficha == None and casilla.color == True and (f - 2) == f_vieja and (c + 2 == c_vieja or c - 2 == c_vieja):      # Para movimientos hacia abajo

                    if c - 2 == c_vieja:                                                                                                   # Para determinar si la ficha se ha desplazado hacia la izquierda
                        casilla_int = self._matriz[f - 1][c - 1]

                        if casilla_int.ficha != None:
                            if casilla_int.ficha.tipo_color != casilla_vieja.ficha.tipo_color:
                                if coor_fichas == None:                                                                                     # Si se utilizan las coordenadas de tablero, no eliminar la ficha ya que es una comprobacion
                                    self.remover_ficha(casilla_int)
                                return True

                    if c + 2 == c_vieja:                                                                                                   # Para determinar si la ficha se ha desplazado hacia la derecha
                        casilla_int = self._matriz[f - 1][c + 1]

                        if casilla_int.ficha != None:
                            if casilla_int.ficha.tipo_color != casilla_vieja.ficha.tipo_color:
                                if coor_fichas == None:                                                                                    # Si se utilizan las coordenadas de tablero, no eliminar la ficha ya que es una comprobacion
                                    self.remover_ficha(casilla_int)
                                return True


            if casilla_vieja.ficha.fila_inicial in self.filas_ini_inf:                                                                     # El salto es valido si la ficha a sido movida a una casilla solida, ha desendido una fila,
                                                                                                                                           # y a aumentado una columna o disminuido una columna (izq. derecha) ficha men.
                if casilla.ficha == None and casilla.color == True and (f + 2) == f_vieja and (c + 2 == c_vieja or c - 2 == c_vieja):      # El salto es valido si la ficha a sido movida a una casilla solida y ha desendido una fila (men).

                    if c - 2 == c_vieja:                                                                                                   # Para determinar si la ficha se ha desplazado hacia la izquierda
                        casilla_int = self._matriz[f + 1][c - 1]

                        if casilla_int.ficha != None:
                            if casilla_int.ficha.tipo_color != casilla_vieja.ficha.tipo_color:
                                if coor_fichas == None:                                                                                     # Si se utilizan las coordenadas de tablero, no eliminar la ficha ya que es una comprobacion
                                    self.remover_ficha(casilla_int)
                                return True

                    if c + 2 == c_vieja:                                                                                                   # Para determinar si la ficha se ha desplazado hacia la derecha
                        casilla_int = self._matriz[f + 1][c + 1]

                        if casilla_int.ficha != None:
                            if casilla_int.ficha.tipo_color != casilla_vieja.ficha.tipo_color:
                                if coor_fichas == None:                                                                                     # Si se utilizan las coordenadas de tablero, no eliminar la ficha ya que es una comprobacion
                                    self.remover_ficha(casilla_int)
                                return True

                    #return True

        if casilla_vieja.ficha.nom_archivo == self.ficha_1_rey or casilla_vieja.ficha.nom_archivo == self.ficha_2_rey:                               # Para determinar saltos validos, reyes

            if casilla.ficha == None and casilla.color == True and ((f - 2) == f_vieja or (f + 2) == f_vieja) and (c + 2 == c_vieja or c - 2 == c_vieja):  # El mov. es valido si la ficha a sido movida a una casilla solida, ha decendido una fila.
                                                                                                                                                            # ,subido una fila, aumentado una columna o aumentado una fila (ficha rey).

                if f - 2 == f_vieja:                                                                                                                       # En caso de que el salto ascienda

                    if c + 2 == c_vieja:                                                                                                                   # En caso de que el salto ascienda hacia la derecha
                        casilla_int = self._matriz[f - 1][c + 1]

                        if casilla_int.ficha != None:
                            if casilla_int.ficha.tipo_color != casilla_vieja.ficha.tipo_color:
                                if coor_fichas == None:                                                                                                     # Si se utilizan las coordenadas de tablero, no eliminar la ficha ya que es una comprobacion
                                    self.remover_ficha(casilla_int)
                                return True

                    if c - 2 == c_vieja:                                                                                                                    # En caso de que el salto ascienda hacia la izquierda
                        casilla_int = self._matriz[f - 1][c - 1]

                        if casilla_int.ficha != None:
                            if casilla_int.ficha.tipo_color != casilla_vieja.ficha.tipo_color:
                                if coor_fichas == None:                                                                                                     # Si se utilizan las coordenadas de tablero, no eliminar la ficha ya que es una comprobacion
                                    self.remover_ficha(casilla_int)
                                return True

                if f + 2 == f_vieja:                                                                                                                        # En caso de que el salto descienda

                    if c + 2 == c_vieja:
                        casilla_int = self._matriz[f + 1][c + 1]

                        if casilla_int.ficha != None:                                                                                                       # En caso de que el salto desienda hacia la derecha
                            if casilla_int.ficha.tipo_color != casilla_vieja.ficha.tipo_color:
                                if coor_fichas == None:
                                    self.remover_ficha(casilla_int)                                                                                         # Si se utilizan las coordenadas de tablero, no eliminar la ficha ya que es una comprobacion
                                return True

                    elif c - 2 == c_vieja:                                                                                                                  # En caso de que el salto desienda hacia la izquierda
                        casilla_int = self._matriz[f + 1][c - 1]

                        if casilla_int.ficha != None:
                            if casilla_int.ficha.tipo_color != casilla_vieja.ficha.tipo_color:
                                if coor_fichas == None:                                                                                                     # Si se utilizan las coordenadas de tablero, no eliminar la ficha ya que es una comprobacion
                                    self.remover_ficha(casilla_int)
                                return True

    def cop_ficha(self, x, y, ficha):
        """Para copiar una ficha de una casilla a otra"""

        f, c = self.det_casilla(x, y)

        if f > 0 and f < 7:                                  # Copiando una ficha de una casilla normal a otra

            casilla = self._matriz[f][c]
            casilla.ficha = ficha

        else:                                               # En caso de que se llegue a kings row, es necesario coronarla
            self.coronar_ficha(x, y, ficha)

    def coronar_ficha(self, x, y, ficha):
        """Para coronar las fichas"""

        f, c = self.det_casilla(x, y)

        if f == 0 or f == 7:                                # En caso de que se llegue a kings row

            if ficha.nom_archivo == self.ficha_2:           # Coronando la ficha marron
                ficha = Ficha(self.ficha_2_rey, f, x, y)
                ficha.rect.centerx = x
                ficha.rect.centery = y

            if ficha.nom_archivo == self.ficha_1:           # Coronando la ficha blanca
                ficha = Ficha(self.ficha_1_rey, f, x, y)
                ficha.rect.centerx = x
                ficha.rect.centery = y

        casilla = self._matriz[f][c]
        casilla.ficha = ficha
        pass

    def casilla_activa(self, x, y):
        """Para mover una ficha de casilla"""

        f, c = self.det_casilla(x, y)
        return self._matriz[f][c]

    def remover_ficha(self, casilla):
        """Para remover una ficha del tablero """
        
        if casilla.ficha.tipo_color in self.ficha_1:            # Para contabilizar las fichas 1 comidas
            self.cont_f1 += 1
            casilla.ficha = None

        elif casilla.ficha.tipo_color in self.ficha_2:          # Para contabilizar las fichas 2 comidas.
            self.cont_f2 += 1
            casilla.ficha = None

        print(self.cont_f1, self.cont_f2)

    def movidas_posibles_men(self, ficha, vervose=None):
        """Para determinar las movidas posibles de una ficha, men"""

        f, c = (self.det_casilla(ficha.rect.centerx, ficha.rect.centery))

        casilla = self._matriz[f][c]

        if casilla.ficha != None:

            #f, c = casilla.cor_tablero
            casillas_vacias = []                        # Para almacenar las casillas que rodean la ficha en cuestion

            if casilla.ficha.tipo_men() == True:         # En caso de que la ficha seleccionada sea un men

                if casilla.ficha.fila_inicial in self.filas_ini_sup:    # Si el men va bajando

                    if f < 7:  # Revisando las 2 casillas inferiores

                        if c >= 1:
                            cas_prox = self._matriz[f + 1][c - 1]

                            if cas_prox.ficha == None:
                                casillas_vacias.append(cas_prox)

                        if c < 7:
                            cas_prox = self._matriz[f + 1][c + 1]

                            if cas_prox.ficha == None:
                                casillas_vacias.append(cas_prox)

                elif casilla.ficha.fila_inicial in self.filas_ini_inf:  # Si el men va subiendo

                    if f > 1:  # Revisando las 2 casillas superiores

                        if c >= 1:
                            cas_prox = self._matriz[f - 1][c - 1]

                            if cas_prox.ficha == None:
                                casillas_vacias.append(cas_prox)

                        if c < 7:
                            cas_prox = self._matriz[f - 1][c + 1]

                            if cas_prox.ficha == None:
                                casillas_vacias.append(cas_prox)

            else:

                if vervose == True:

                    print('La ficha introducida no es men')

            if vervose == True:

                print('Moves posibles: ', len(casillas_vacias))

                for ele in casillas_vacias:
                    print(ele.cor_tablero)

            return (casillas_vacias)

    def movidas_posibles_king(self, ficha, vervose=None):
        """Para determinar las movidas posibles de una ficha, king"""

        f, c = (self.det_casilla(ficha.rect.centerx, ficha.rect.centery))

        casilla = self._matriz[f][c]

        if casilla.ficha != None:

            #f, c = casilla.cor_tablero
            casillas_vacias = []                          # Para almacenar las casillas que rodean la ficha en cuestion

            if casilla.ficha.tipo_men() == False:         # En caso de que la ficha seleccionada sea un men

                if f >= 1:                                # Revisando las 2 casillas superiores

                    if c >= 1:
                        cas_prox = self._matriz[f - 1][c - 1]

                        if cas_prox.ficha == None:
                            casillas_vacias.append(cas_prox)

                    if c < 7:
                        cas_prox = self._matriz[f - 1][c + 1]

                        if cas_prox.ficha == None:
                            casillas_vacias.append(cas_prox)

                if f < 7:                               # Revisando las 2 casillas inferiores

                    if c >= 1:
                        cas_prox = self._matriz[f + 1][c - 1]

                        if cas_prox.ficha == None:
                            casillas_vacias.append(cas_prox)

                    if c < 7:
                        cas_prox = self._matriz[f + 1][c + 1]

                        if cas_prox.ficha == None:
                            casillas_vacias.append(cas_prox)
            else:

                print('La ficha introducida no es king')

            if vervose == True:                                 # Para imprimir cuando el usuario lo desee

                print('Moves posibles: ', len(casillas_vacias))
                for ele in casillas_vacias:
                    print(ele.cor_tablero)

            return (casillas_vacias)

    def saltos_posibles_men_2(self, ficha, vervose=None):
        """Imprime todos los posibles jumps de una ficha"""

        f, c = self.det_casilla(ficha.rect.centerx, ficha.rect.centery)

        casilla = self._matriz[f][c]

        if casilla.ficha != None and casilla.ficha.tipo_men() == True:

            enemigos = self.enemigos_proximo(casilla)

            posiciones = self.comidas_posibles(casilla, enemigos)

            if len(posiciones[0]) > 0:  # En caso de que se alla saltos realizables.

                if vervose == True:  # Para imprimir cuando el usuario lo desee

                    for cas in posiciones[0]:
                       print(cas)

                return(posiciones)

            else:

                return []                                   # En caso de que no alla saltos realizables.

        else:

            if vervose == True:
                print("La casilla no esta vacia, o la ficha no es men")

    def saltos_posibles_king(self, ficha, vervose=None):
        """Imprime todos los posibles jumps de una ficha"""

        f, c = self.det_casilla(ficha.rect.centerx, ficha.rect.centery)

        casilla = self._matriz[f][c]

        if casilla.ficha != None and casilla.ficha.tipo_men() == False:

            enemigos = self.enemigos_proximo(casilla)

            posiciones = self.comidas_posibles(casilla, enemigos)


            if len(posiciones[0]) > 0:                  # En caso de que se alla saltos realizables.

                if vervose == True:  # Para imprimir cuando el usuario lo desee

                    for cas in posiciones[0]:
                       print(cas)

                return(posiciones)

            else:
                return []                               # En caso de que no alla saltos realizables.

        else:

            if vervose == True:

                print("La casilla no esta vacia, o la ficha no es men")

    def movidas_validos_por_color(self, color, vervose=None):
        """Imprime la posicion de las fichas, que pueden tener movimientos validos para ese color
        y retona la cantidad de fichas que pueden hacer movimientos validos, para dicho color"""

        cant_fichas_mov = 0                             # Para contar las fichas que pueden realizar movimientos
        cont_fichas = 0                                 # Para contar fichas disponibles para un color determinado

        for f in range(len(self._matriz)):              # Inicializando la matriz del tablero que va a contener los objetos casilla

            for c in range(len(self._matriz[f])):

                casilla = self._matriz[f][c]

                if casilla.ficha != None:

                    ficha = casilla.ficha

                    if ficha.tipo_color == color:

                        if ficha.tipo_men() == True:

                            cont_fichas += 1            # Para contar las fichas disponibles en el tablero

                            movimientos = self.movidas_posibles_men(ficha)

                            if len(movimientos) > 0:

                                cant_fichas_mov += 1

                                if vervose == True:    # Para imprimir cuando el usuario lo deseee

                                    print(casilla.cor_tablero, "\n")

                        else:           # En caso de que sea una king

                            cont_fichas += 1            # Para contar las fichas disponibles en el tablero

                            movimientos = self.movidas_posibles_king(ficha)

                            if len(movimientos) > 0:
                                cant_fichas_mov += 1

                                if vervose == True:    # Para imprimir cuando el usuario lo deseee

                                    print(casilla.cor_tablero, "\n")

        if cont_fichas > 0:

            return cant_fichas_mov

        else:

            return None

    def saltos_posibles_men(self, casilla, enemigos_proximos, lista_saltos, casillas_saltadas, casillas_imposible_saltar):

        if len(lista_saltos) == 0:                      # Almacenando la pos inicial como 1er salto

            lista_saltos.append(casilla)

        if casilla.ficha.tipo_men() == True:            # Asegurando que la ficha sea men

            enemigos = self.enemigos_proximo(casilla)   # Determinando si la ficha tiene enemigos proximos

            print(enemigos)

            for cas in enemigos:                        # En enemigos_proximos no pueden estar las fichas saltadas o las imposibles de saltar.

                if cas not in casillas_saltadas and cas not in casillas_imposible_saltar and cas not in enemigos_proximos:      # Para serciorarse de que esa casilla no fue revisada

                    enemigos_proximos.insert(0, cas)

            #print('Enemigos proximos')
            # for cas in enemigos_proximos:
            #     print(cas)

            if len(enemigos_proximos) == 0 and lista_saltos[0] == casilla:         # condicion de salida de la funcion

                for x in range(len(lista_saltos)):

                    if x > 0:
                        lista_saltos[x].ficha = None
                        print(lista_saltos[x])

                return lista_saltos


            enemigos_proximos_vol = list(enemigos_proximos)
            enemigos_proximos_vol.reverse()

            intentos_saltos = self.comidas_posibles(casilla, enemigos_proximos_vol)     # Determinando donde la ficha puede saltar
            saltos_posibles = intentos_saltos[0]

            for cas in intentos_saltos[1]:                                              # Para introducir en casillas_imposible_saltar las casillas que no se pudieron saltar

                if cas not in casillas_imposible_saltar:
                    casillas_imposible_saltar.append(cas)



            if len(saltos_posibles) > 0:    # Determinando si es posible realizar el salto.

                #print('Saltos posibles')
                for x in range(len(saltos_posibles)):
                    # print(saltos_posibles[x])

                    if enemigos_proximos_vol[x] not in casillas_saltadas and enemigos_proximos_vol[x] not in casillas_imposible_saltar:
                    #if saltos_posibles[x] not in lista_saltos:  # Si no se ha saltado previamente

                        lista_saltos.append(saltos_posibles[x])
                        saltos_posibles[x].ficha = casilla.ficha
                        casilla.ficha = None
                        casillas_saltadas.append(enemigos_proximos_vol[x])
                        enemigos_proximos = []
                        #enemigos_proximos.remove(enemigos_proximos[x])
                        casilla = saltos_posibles[x]

                        break


                enemigos = self.enemigos_proximo(casilla)   # Determinando si la ficha tiene enemigos proximos

                #print(enemigos)

                for cas in enemigos:                        # En enemigos_proximos no pueden estar las fichas saltadas o las imposibles de saltar.

                    if cas not in casillas_saltadas and cas not in casillas_imposible_saltar:

                        enemigos_proximos.insert(0, cas)

                enemigos_proximos_vol = list(enemigos_proximos)
                enemigos_proximos_vol.reverse()

                #saltos_posibles = self.comidas_posibles(casilla, enemigos_proximos_vol)  # Determinando donde la ficha puede saltar

                intentos_saltos = self.comidas_posibles(casilla, enemigos_proximos_vol)  # Determinando donde la ficha puede saltar
                saltos_posibles = intentos_saltos[0]

                for cas in intentos_saltos[1]:  # Para introducir en casillas_imposible_saltar las casillas que no se pudieron saltar

                    if cas not in casillas_imposible_saltar:
                        casillas_imposible_saltar.append(cas)



                if len(saltos_posibles) == 0 and casilla != lista_saltos[0]:      # En caso de que no se produzcan saltos, volver atras una ficha

                    for cas in enemigos_proximos:
                        casillas_imposible_saltar.append(cas)

                    enemigos_proximos = []  # Ya que dicha casilla no se puede saltar, se remueve.


                    #indice_pos_anterior = lista_saltos.index(casilla) - 1
                    indice_pos_anterior = len(lista_saltos) - 2
                    pos_anterior = lista_saltos[indice_pos_anterior]
                    pos_anterior.ficha = casilla.ficha
                    casilla.ficha = None
                    casilla = pos_anterior
                    # pos = self.saltos_posibles_men(casilla, enemigos_proximos, lista_saltos, casillas_saltadas, [])
                    self.saltos_posibles_men(casilla, enemigos_proximos, lista_saltos, casillas_saltadas,casillas_imposible_saltar)
                    return lista_saltos[1:]

                # pos = self.saltos_posibles_men(casilla, enemigos_proximos, lista_saltos, casillas_saltadas, [])
                self.saltos_posibles_men(casilla, enemigos_proximos, lista_saltos, casillas_saltadas, casillas_imposible_saltar)
                return lista_saltos[1:]

            else:       # En caso de que no se puedan realizar saltos

                #return lista_saltos
                for cas in enemigos_proximos:

                    if cas not in casillas_imposible_saltar:

                        casillas_imposible_saltar.append(cas)

                enemigos_proximos = []              # Ya que dicha casilla no se puede saltar, se remueve.

                if len(saltos_posibles) == 0 and casilla != lista_saltos[0]:      # En caso de que no se produzcan saltos, volver atras una ficha

                    indice_pos_anterior = lista_saltos.index(casilla) - 1
                    pos_anterior = lista_saltos[indice_pos_anterior]
                    pos_anterior.ficha = casilla.ficha
                    casilla.ficha = None
                    casilla = pos_anterior

                    self.saltos_posibles_men(casilla, enemigos_proximos, lista_saltos, casillas_saltadas, casillas_imposible_saltar)
                    return lista_saltos[1:]

                else:

                    self.saltos_posibles_men(casilla, enemigos_proximos, lista_saltos, casillas_saltadas, casillas_imposible_saltar)
                    return lista_saltos[1:]


        else:
            print('Solo para fichas men')

    def enemigos_proximo(self, casilla):
        """Para determinar los enemigos que una ficha (king o men) tiene alrededor"""

        casillas_alrededor_enemigos = []  # Para almacenar las casillas que rodean la ficha en cuestion

        if casilla.ficha != None:

            f, c = casilla.cor_tablero

            # Determinando las fichas enemigas que una ficha tiene a su arrededor
            if casilla.ficha.tipo_men() == True:    # En caso de que la ficha seleccionada sea un men

                if casilla.ficha.fila_inicial in self.filas_ini_sup:    # Si el men va bajando

                    if f < 7:   # Revisando las 2 casillas inferiores

                        if c >= 1:
                            cas_prox = self._matriz[f + 1][c - 1]

                            if cas_prox.ficha != None and casilla.ficha.tipo_color != cas_prox.ficha.tipo_color:
                                casillas_alrededor_enemigos.append(cas_prox)

                        if c < 7:
                            cas_prox = self._matriz[f + 1][c + 1]

                            if cas_prox.ficha != None and casilla.ficha.tipo_color != cas_prox.ficha.tipo_color:
                                casillas_alrededor_enemigos.append(cas_prox)

                elif casilla.ficha.fila_inicial in self.filas_ini_inf:  # Si el men va subiendo

                    if f > 0:  # Revisando las 2 casillas superiores

                        if c >= 1:
                            cas_prox = self._matriz[f - 1][c - 1]

                            if cas_prox.ficha != None and casilla.ficha.tipo_color != cas_prox.ficha.tipo_color:
                                casillas_alrededor_enemigos.append(cas_prox)

                        if c < 7:
                            cas_prox = self._matriz[f - 1][c + 1]

                            if cas_prox.ficha != None and casilla.ficha.tipo_color != cas_prox.ficha.tipo_color:
                                casillas_alrededor_enemigos.append(cas_prox)

            else:                                       # En caso de que la ficha seleccionada sea un king

                if f >= 1:                               # Revisando las 2 casillas superiores

                    if c >= 1:
                        cas_prox = self._matriz[f-1][c-1]

                        if cas_prox.ficha != None and  casilla.ficha.tipo_color != cas_prox.ficha.tipo_color:
                            casillas_alrededor_enemigos.append(cas_prox)

                    if c < 7:
                        cas_prox = self._matriz[f - 1][c + 1]

                        if cas_prox.ficha != None and casilla.ficha.tipo_color != cas_prox.ficha.tipo_color:
                            casillas_alrededor_enemigos.append(cas_prox)

                if f < 7:                               # Revisando las 2 casillas inferiores

                    if c >= 1:
                        cas_prox = self._matriz[f + 1][c - 1]

                        if cas_prox.ficha != None and casilla.ficha.tipo_color != cas_prox.ficha.tipo_color:

                            casillas_alrededor_enemigos.append(cas_prox)

                    if c < 7:
                        cas_prox = self._matriz[f + 1][c + 1]

                        if cas_prox.ficha != None and casilla.ficha.tipo_color != cas_prox.ficha.tipo_color:

                            casillas_alrededor_enemigos.append(cas_prox)

            #print(casillas_alrededor_enemigos)
            return (casillas_alrededor_enemigos)

        elif casilla.ficha == None:

            raise ValueError('La casilla no tiene ficha dentro')

    def comidas_posibles(self, casilla, casillas_alrededor_enemigos):
        """Para determinar hacia donde una ficha (men o king) puede realizar un salto valido, en caso de que no se pueda realizar saltos validos devuelve una lista vacia"""

        lista_saltos = []       # Para almacenar las coordenadas a donde puede ser posible saltar validamente
        lista_no_saltos = []    # Para almacenar las coordenadas de las fichas que no se pueden saltar

        for cas in casillas_alrededor_enemigos:  # Para saber cuales de las fichas se pueden comer##########################3

            if casilla.ficha.tipo_men() == True:  # Si la ficha seleccionada es un men######################################

                if casilla.ficha.fila_inicial in self.filas_ini_inf:  # Si el men va subiendo

                    if cas.cor_tablero[1] < casilla.cor_tablero[1]:  # Si el men esta a la izquierda
                        #print('Izquierda')
                        f_nueva, c_nueva = cas.cor_tablero  # El salto se realizara a la casilla superior izquierda inmediata

                        f_nueva -= 1
                        c_nueva -= 1

                        f_vieja, c_vieja = casilla.cor_tablero

                        if self._com_coordenadas(f_nueva, c_nueva) and self._matriz[f_nueva][c_nueva].ficha == None:  # Para que solo sea posible introducir valores validos en la funcion
                            # (f_nueva, c_nueva, f_vieja, c_vieja)
                            #print(self.salto_valido(None, None, None, None, (f_nueva, c_nueva, f_vieja, c_vieja)))
                            lista_saltos.append(self._matriz[f_nueva][c_nueva])

                        else:
                            #continue
                            lista_no_saltos.append(cas)

                    if cas.cor_tablero[1] > casilla.cor_tablero[1]:  # Si el men esta a la derecha
                        #print('Derecha')
                        f_nueva, c_nueva = cas.cor_tablero  # El salto se realizara a la casilla superior Derecha inmediata

                        f_nueva -= 1
                        c_nueva += 1

                        f_vieja, c_vieja = casilla.cor_tablero

                        # (f_nueva, c_nueva, f_vieja, c_vieja)
                        if self._com_coordenadas(f_nueva, c_nueva) and self._matriz[f_nueva][c_nueva].ficha == None:  # Para que solo sea posible introducir valores validos en la funcion
                            # (f_nueva, c_nueva, f_vieja, c_vieja)
                            #print(self.salto_valido(None, None, None, None, (f_nueva, c_nueva, f_vieja, c_vieja)))
                            lista_saltos.append(self._matriz[f_nueva][c_nueva])

                        else:
                            #continue
                            lista_no_saltos.append(cas)

                if casilla.ficha.fila_inicial in self.filas_ini_sup:  # Si el men va bajando

                    if cas.cor_tablero[1] < casilla.cor_tablero[1]:  # Si el men esta a la izquierda
                        #print('Izquierda')
                        f_nueva, c_nueva = cas.cor_tablero  # El salto se realizara a la casilla superior izquierda inmediata

                        f_nueva += 1
                        c_nueva -= 1

                        f_vieja, c_vieja = casilla.cor_tablero

                        # (f_nueva, c_nueva, f_vieja, c_vieja)
                        if self._com_coordenadas(f_nueva, c_nueva) and self._matriz[f_nueva][c_nueva].ficha == None:  # Para que solo sea posible introducir valores validos en la funcion y la casilla proxima este vacia
                            # (f_nueva, c_nueva, f_vieja, c_vieja)
                            #print(self.salto_valido(None, None, None, None, (f_nueva, c_nueva, f_vieja, c_vieja)))
                            lista_saltos.append(self._matriz[f_nueva][c_nueva])

                        else:
                            #continue
                            lista_no_saltos.append(cas)

                    if cas.cor_tablero[1] > casilla.cor_tablero[1]:  # Si el men esta a la Derecha
                        #print('Derecha')
                        f_nueva, c_nueva = cas.cor_tablero  # El salto se realizara a la casilla superior derecha inmediata

                        f_nueva += 1
                        c_nueva += 1

                        f_vieja, c_vieja = casilla.cor_tablero

                        # (f_nueva, c_nueva, f_vieja, c_vieja)
                        if self._com_coordenadas(f_nueva,c_nueva) and self._matriz[f_nueva][c_nueva].ficha == None:  # Para que solo sea posible introducir valores validos en la funcion y la casilla proxima este vacia
                            # (f_nueva, c_nueva, f_vieja, c_vieja)
                            #print(self.salto_valido(None, None, None, None, (f_nueva, c_nueva, f_vieja, c_vieja)))
                            lista_saltos.append(self._matriz[f_nueva][c_nueva])

                        else:
                           #continue
                           lista_no_saltos.append(cas)

            if casilla.ficha.tipo_men() == False:  # En caso de que la ficha seleccionada sea un king###########################

                if cas.cor_tablero[0] < casilla.cor_tablero[0]:  # Si la ficha  esta a la arriba
                    #print('Arriba')

                    if cas.cor_tablero[1] < casilla.cor_tablero[1]:  # Si la ficha esta a la izq
                        #print('Izq')

                        f_nueva, c_nueva = cas.cor_tablero  # El salto se realizara a la casilla superior izquierda inmediata

                        f_nueva -= 1
                        c_nueva -= 1

                        f_vieja, c_vieja = casilla.cor_tablero

                        if self._com_coordenadas(f_nueva, c_nueva) and self._matriz[f_nueva][c_nueva].ficha == None:  # Para que solo sea posible introducir valores validos en la funcion
                            # (f_nueva, c_nueva, f_vieja, c_vieja)
                            #print(self.salto_valido(None, None, None, None, (f_nueva, c_nueva, f_vieja, c_vieja)))
                            lista_saltos.append(self._matriz[f_nueva][c_nueva])

                        else:
                            #continue
                            lista_no_saltos.append(cas)

                    if cas.cor_tablero[1] > casilla.cor_tablero[1]:  # Si la ficha esta a la Der
                        #print('Der')

                        if cas.cor_tablero[1] > casilla.cor_tablero[1]:  # Si el men esta a la derecha

                            f_nueva, c_nueva = cas.cor_tablero  # El salto se realizara a la casilla superior derecha inmediata

                            f_nueva -= 1
                            c_nueva += 1

                            f_vieja, c_vieja = casilla.cor_tablero

                            # (f_nueva, c_nueva, f_vieja, c_vieja)
                            if self._com_coordenadas(f_nueva, c_nueva) and self._matriz[f_nueva][c_nueva].ficha == None:  # Para que solo sea posible introducir valores validos en la funcion
                                # (f_nueva, c_nueva, f_vieja, c_vieja)
                                #print(self.salto_valido(None, None, None, None, (f_nueva, c_nueva, f_vieja, c_vieja)))
                                lista_saltos.append(self._matriz[f_nueva][c_nueva])

                            else:
                                #continue
                                lista_no_saltos.append(cas)

                if cas.cor_tablero[0] > casilla.cor_tablero[0]:  # Si la ficha  esta a la abajo
                    #print('Abajo')

                    if cas.cor_tablero[1] < casilla.cor_tablero[1]:  # Si la ficha esta a la izq
                        #print('Izq')

                        f_nueva, c_nueva = cas.cor_tablero  # El salto se realizara a la casilla superior izquierda inmediata

                        f_nueva += 1
                        c_nueva -= 1

                        f_vieja, c_vieja = casilla.cor_tablero

                        # (f_nueva, c_nueva, f_vieja, c_vieja)
                        if self._com_coordenadas(f_nueva, c_nueva) and self._matriz[f_nueva][c_nueva].ficha == None:  # Para que solo sea posible introducir valores validos en la funcion
                            # (f_nueva, c_nueva, f_vieja, c_vieja)
                            #print(self.salto_valido(None, None, None, None, (f_nueva, c_nueva, f_vieja, c_vieja)))
                            lista_saltos.append(self._matriz[f_nueva][c_nueva])

                        else:
                            #continue
                            lista_no_saltos.append(cas)

                    if cas.cor_tablero[1] > casilla.cor_tablero[1]:  # Si la ficha esta a la Der
                        #print('Der')

                        f_nueva, c_nueva = cas.cor_tablero  # El salto se realizara a la casilla superior izquierda inmediata

                        f_nueva += 1
                        c_nueva += 1

                        f_vieja, c_vieja = casilla.cor_tablero

                        # (f_nueva, c_nueva, f_vieja, c_vieja)
                        if self._com_coordenadas(f_nueva, c_nueva) and self._matriz[f_nueva][c_nueva].ficha == None:  # Para que solo sea posible introducir valores validos en la funcion
                            # (f_nueva, c_nueva, f_vieja, c_vieja)
                            #print(self.salto_valido(None, None, None, None, (f_nueva, c_nueva, f_vieja, c_vieja)))
                            lista_saltos.append(self._matriz[f_nueva][c_nueva])

                        else:
                            #continue
                            lista_no_saltos.append(cas)

        return lista_saltos, lista_no_saltos

    def saltos_posibles(self, casilla, casillas_alrededor_enemigos, lista_saltos = None, cas_inicial=None):
        """Determina los posibles saltos de una ficha y las fichas sobre las cuales no se puede saltar"""

        if cas_inicial != None:
            casilla_inicial = cas_inicial

        if casilla.ficha != None:

            f, c = casilla.cor_tablero
            casillas_alrededor_enemigos = casillas_alrededor_enemigos             # Para almacenar las casillas que rodean la ficha en cuestion

            # Determinando las fichas enemigas que una ficha tiene a su arrededor
            if casilla.ficha.tipo_men() == True:         # En caso de que la ficha seleccionada sea un men

                if casilla.ficha.fila_inicial in self.filas_ini_sup:    # Si el men va bajando

                    if f < 7:  # Revisando las 2 casillas inferiores

                        if c >= 1:
                            cas_prox = self._matriz[f + 1][c - 1]

                            if cas_prox.ficha != None and casilla.ficha.tipo_color != cas_prox.ficha.tipo_color:
                                casillas_alrededor_enemigos.append(cas_prox)

                        if c < 7:
                            cas_prox = self._matriz[f + 1][c + 1]

                            if cas_prox.ficha != None and casilla.ficha.tipo_color != cas_prox.ficha.tipo_color:
                                casillas_alrededor_enemigos.append(cas_prox)

                elif casilla.ficha.fila_inicial in self.filas_ini_inf:  # Si el men va subiendo

                    if f > 0:  # Revisando las 2 casillas superiores

                        if c >= 1:
                            cas_prox = self._matriz[f - 1][c - 1]

                            if cas_prox.ficha != None and casilla.ficha.tipo_color != cas_prox.ficha.tipo_color:
                                casillas_alrededor_enemigos.append(cas_prox)

                        if c < 7:
                            cas_prox = self._matriz[f - 1][c + 1]

                            if cas_prox.ficha != None and casilla.ficha.tipo_color != cas_prox.ficha.tipo_color:
                                casillas_alrededor_enemigos.append(cas_prox)

            else:                                       # En caso de que la ficha seleccionada sea un king

                if f >= 1:                               # Revisando las 2 casillas superiores

                    if c >= 1:
                        cas_prox = self._matriz[f-1][c-1]

                        if cas_prox.ficha != None and  casilla.ficha.tipo_color != cas_prox.ficha.tipo_color:
                            casillas_alrededor_enemigos.append(cas_prox)

                    if c < 7:
                        cas_prox = self._matriz[f - 1][c + 1]

                        if cas_prox.ficha != None and casilla.ficha.tipo_color != cas_prox.ficha.tipo_color:
                            casillas_alrededor_enemigos.append(cas_prox)

                if f < 7:                               # Revisando las 2 casillas inferiores

                    if c >= 1:
                        cas_prox = self._matriz[f + 1][c - 1]

                        if cas_prox.ficha != None and casilla.ficha.tipo_color != cas_prox.ficha.tipo_color:

                            casillas_alrededor_enemigos.append(cas_prox)

                    if c < 7:
                        cas_prox = self._matriz[f + 1][c + 1]

                        if cas_prox.ficha != None and casilla.ficha.tipo_color != cas_prox.ficha.tipo_color:

                            casillas_alrededor_enemigos.append(cas_prox)

            print(casillas_alrededor_enemigos)

            for cas in casillas_alrededor_enemigos:                         # Para saber cuales de las fichas se pueden comer##########################3

                if casilla.ficha.tipo_men() == True:                        # Si la ficha seleccionada es un men######################################

                    if casilla.ficha.fila_inicial in self.filas_ini_inf:    # Si el men va subiendo

                        if cas.cor_tablero[1] < casilla.cor_tablero[1]:     # Si el men esta a la izquierda
                            print('Izquierda')
                            f_nueva, c_nueva = cas.cor_tablero              # El salto se realizara a la casilla superior izquierda inmediata

                            f_nueva -= 1
                            c_nueva -= 1

                            f_vieja, c_vieja = casilla.cor_tablero

                            if self._com_coordenadas(f_nueva, c_nueva):         # Para que solo sea posible introducir valores validos en la funcion
                                # (f_nueva, c_nueva, f_vieja, c_vieja)
                                print(self.salto_valido(None, None, None, None, (f_nueva, c_nueva, f_vieja, c_vieja)))

                            else:
                                print(False)

                        if cas.cor_tablero[1] > casilla.cor_tablero[1]:  # Si el men esta a la derecha
                            print('Derecha')
                            f_nueva, c_nueva = cas.cor_tablero  # El salto se realizara a la casilla superior Derecha inmediata

                            f_nueva -= 1
                            c_nueva += 1

                            f_vieja, c_vieja = casilla.cor_tablero

                            # (f_nueva, c_nueva, f_vieja, c_vieja)
                            if self._com_coordenadas(f_nueva,c_nueva):  # Para que solo sea posible introducir valores validos en la funcion
                                # (f_nueva, c_nueva, f_vieja, c_vieja)
                                print(self.salto_valido(None, None, None, None, (f_nueva, c_nueva, f_vieja, c_vieja)))

                            else:
                                print(False)

                    if casilla.ficha.fila_inicial in self.filas_ini_sup:  # Si el men va bajando

                        if cas.cor_tablero[1] < casilla.cor_tablero[1]:  # Si el men esta a la izquierda
                            print('Izquierda')
                            f_nueva, c_nueva = cas.cor_tablero  # El salto se realizara a la casilla superior izquierda inmediata

                            f_nueva += 1
                            c_nueva -= 1

                            f_vieja, c_vieja = casilla.cor_tablero

                            # (f_nueva, c_nueva, f_vieja, c_vieja)
                            if self._com_coordenadas(f_nueva, c_nueva):  # Para que solo sea posible introducir valores validos en la funcion
                                # (f_nueva, c_nueva, f_vieja, c_vieja)
                                print(self.salto_valido(None, None, None, None, (f_nueva, c_nueva, f_vieja, c_vieja)))

                            else:
                                print(False)

                        if cas.cor_tablero[1] > casilla.cor_tablero[1]:  # Si el men esta a la Derecha
                            print('Derecha')
                            f_nueva, c_nueva = cas.cor_tablero  # El salto se realizara a la casilla superior izquierda inmediata

                            f_nueva += 1
                            c_nueva += 1

                            f_vieja, c_vieja = casilla.cor_tablero

                            # (f_nueva, c_nueva, f_vieja, c_vieja)
                            if self._com_coordenadas(f_nueva, c_nueva):  # Para que solo sea posible introducir valores validos en la funcion
                                # (f_nueva, c_nueva, f_vieja, c_vieja)
                                print(self.salto_valido(None, None, None, None, (f_nueva, c_nueva, f_vieja, c_vieja)))

                            else:
                                print(False)


                if casilla.ficha.tipo_men() == False:                       # En caso de que la ficha seleccionada sea un king###########################

                    if cas.cor_tablero[0] < casilla.cor_tablero[0]:         # Si la ficha  esta a la arriba
                        print('Arriba')

                        if cas.cor_tablero[1] < casilla.cor_tablero[1]:     # Si la ficha esta a la izq
                            print('Izq')

                            f_nueva, c_nueva = cas.cor_tablero              # El salto se realizara a la casilla superior izquierda inmediata

                            f_nueva -= 1
                            c_nueva -= 1

                            f_vieja, c_vieja = casilla.cor_tablero

                            if self._com_coordenadas(f_nueva, c_nueva):  # Para que solo sea posible introducir valores validos en la funcion
                                # (f_nueva, c_nueva, f_vieja, c_vieja)
                                print(self.salto_valido(None, None, None, None, (f_nueva, c_nueva, f_vieja, c_vieja)))

                            else:
                                print(False)

                        if cas.cor_tablero[1] > casilla.cor_tablero[1]:  # Si la ficha esta a la Der
                            print('Der')

                            if cas.cor_tablero[1] > casilla.cor_tablero[1]:  # Si el men esta a la derecha

                                f_nueva, c_nueva = cas.cor_tablero  # El salto se realizara a la casilla superior derecha inmediata

                                f_nueva -= 1
                                c_nueva += 1

                                f_vieja, c_vieja = casilla.cor_tablero

                                # (f_nueva, c_nueva, f_vieja, c_vieja)
                                if self._com_coordenadas(f_nueva,
                                                         c_nueva):  # Para que solo sea posible introducir valores validos en la funcion
                                    # (f_nueva, c_nueva, f_vieja, c_vieja)
                                    print(
                                        self.salto_valido(None, None, None, None, (f_nueva, c_nueva, f_vieja, c_vieja)))

                                else:
                                    print(False)

                    if cas.cor_tablero[0] > casilla.cor_tablero[0]:  # Si la ficha  esta a la abajo
                        print('Abajo')

                        if cas.cor_tablero[1] < casilla.cor_tablero[1]: # Si la ficha esta a la izq
                            print('Izq')

                            f_nueva, c_nueva = cas.cor_tablero  # El salto se realizara a la casilla superior izquierda inmediata

                            f_nueva += 1
                            c_nueva -= 1

                            f_vieja, c_vieja = casilla.cor_tablero

                            # (f_nueva, c_nueva, f_vieja, c_vieja)
                            if self._com_coordenadas(f_nueva,
                                                     c_nueva):  # Para que solo sea posible introducir valores validos en la funcion
                                # (f_nueva, c_nueva, f_vieja, c_vieja)
                                print(self.salto_valido(None, None, None, None, (f_nueva, c_nueva, f_vieja, c_vieja)))

                            else:
                                print(False)

                        if cas.cor_tablero[1] > casilla.cor_tablero[1]:  # Si la ficha esta a la Der
                            print('Der')

                            f_nueva, c_nueva = cas.cor_tablero  # El salto se realizara a la casilla superior izquierda inmediata

                            f_nueva += 1
                            c_nueva += 1

                            f_vieja, c_vieja = casilla.cor_tablero

                            # (f_nueva, c_nueva, f_vieja, c_vieja)
                            if self._com_coordenadas(f_nueva, c_nueva):  # Para que solo sea posible introducir valores validos en la funcion
                                # (f_nueva, c_nueva, f_vieja, c_vieja)
                                print(self.salto_valido(None, None, None, None, (f_nueva, c_nueva, f_vieja, c_vieja)))

                            else:
                                print(False)

    def _com_coordenadas(self, f, c):
        """Para comprobar si unas coordenadas de matriz son validas"""

        if (f >= 0 and f <= 7) and (c >= 0 and c <= 7):
            return True

        else:

            return False

    def game_over(self):
        """Utilizada para monitoriar el tablero, revisara si el juego esta acabado por captura de fichas"""

        if self.cont_f1 == 12 or self.cont_f2 == 12:                        # Game over por comer todas las fichas

            if self.cont_f1 == 12:
                print('El jugador de las fichas claras gano 1')

            else:
                print('El jugador de las oscuras gano 1')

            return True

        else:
            return False

    def game_over2(self):
        """Para determinar si el juego ha acabado por trancar las fichas"""

        if self.movidas_validos_por_color('blanca') == 0 or self.movidas_validos_por_color('marron') == 0:

            if self.movidas_validos_por_color('blanca') == 0:
                print('El jugador de las oscuras gano 2')
                input()
                return True

            if self.movidas_validos_por_color('marron') == 0:
                print('El jugador de las fichas claras gano 2')
                input()
                return True

        else:
            return False

    def limpiar_marcador(self):
        """Para resetear los contadores a 0 luego de que una partida acabe y se desida seguir jugando"""

        self.cont_f1 = 0
        self.cont_f2 = 0

    def turno_oscuras(self):
        """Para determinar a que color de ficha le toca mover"""

        if self.cont_turno % 2 == 0:

            return True

        else:

            return False

    def contador_turno(self, control=1):
        """Manipula la variable que lleva el turno del juego"""

        self.cont_turno += control

    def saltos_posibles_universal(self, ficha):
        """Para retornar los saltos que una ficha, puede dar independientemente del tipo que sea (men o king)"""

        if ficha.tipo_men() == True:                # Si la ficha es un men

            saltos = self.saltos_posibles_men_2(ficha)
            return saltos

        else:                                       # Si la ficha es un king

            saltos = self.saltos_posibles_king(ficha)
            return saltos

    def saltos_validos_por_color(self, color, vervose=None):
        '''Retorna un lista con las casillas que pueden realizar saltos posibles, por color & en caso de que
        se desee imprime las coordenadas de las casillas que tienen la posibilidad de saltar'''

        cant_fichas_sal = []                              # Para almacenar las casillas que pueden saltar

        if vervose == True:                               # Para imprimir una linea en blanco y que se note la diferencia entre un resultado y otro

            print('')

        for f in range(len(self._matriz)):

            for c in range(len(self._matriz[f])):

                casilla = self._matriz[f][c]

                if casilla.ficha != None:

                    ficha = casilla.ficha

                    if ficha.tipo_color == color:

                        saltos = self.saltos_posibles_universal(ficha)  # Independientemente si es men o king

                        if len(saltos) > 0:                             # Si hay saltos disponibles, a realizar, se almacena en la lista
                            cant_fichas_sal.append(casilla)

                            if vervose == True:          # En caso de que se deseen imprimir las coordenadas por consola
                                print(casilla.cor_tablero)

        return cant_fichas_sal                           # En caso de que no haya casillas disponibles para saltar, se devolvera una lista vacia
                        




#a = Tablero()
#
# ma = a.inicializar_tablero()
#
# ma[0][0] = Casilla (Ficha(self.ficha_2), (0, 0), (100, 0))



