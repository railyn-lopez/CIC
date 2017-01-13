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
                if f == 0 and c == 1 or f == 0 and c == 3:                                             #(x_izq, x_der, y_arriba, y_abajo )
                    self._matriz[f][c] = Casilla (Ficha(self.ficha_1, f, cont_pixels_ficha_x, cont_pixels_ficha_y), (f, c), (cont_pixels_x - pixels_cuadro, cont_pixels_x, cont_pixels_y - pixels_cuadro, cont_pixels_y), color)


                elif f == 7 and c == 0 or f == 7 and c == 2 or f == 7 and c == 4 or f == 7 and c == 6:                                             #(x_izq, x_der, y_arriba, y_abajo )
                    self._matriz[f][c] = Casilla (Ficha(self.ficha_2, f, cont_pixels_ficha_x, cont_pixels_ficha_y), (f, c), (cont_pixels_x - pixels_cuadro, cont_pixels_x, cont_pixels_y - pixels_cuadro, cont_pixels_y), color)

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
        """Para copiar una ficha de una casilla a otra y coronar fichas"""

        f, c = self.det_casilla(x, y)

        if f == 0 or f == 7:                            # En caso de que se llege a kings row

            if ficha.nom_archivo == self.ficha_2:     # Coronando la ficha marron
                ficha = Ficha(self.ficha_2_rey, f, x, y)
                ficha.rect.x = x
                ficha.rect.y = y

            if ficha.nom_archivo == self.ficha_1:     # Coronando la ficha blanca
                ficha = Ficha(self.ficha_1_rey, f, x, y)
                ficha.rect.x = x
                ficha.rect.y = y

        casilla = self._matriz[f][c]
        casilla.ficha = ficha

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

    def movidas_posibles(self, casilla):
        """Para determinar las movidas posibles que tiene una ficha"""


        if casilla.ficha != None:

            f, c = casilla.cor_tablero
            casillas_vacias = []             # Para almacenar las casillas que rodean la ficha en cuestion


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

            elif casilla.ficha.tipo_men() == False:                                       # En caso de que la ficha seleccionada sea un king

                if f >= 1:                               # Revisando las 2 casillas superiores

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

            print('Moves posibles: ', len(casillas_vacias))

            for ele in casillas_vacias:
                print(ele.cor_tablero)

            return (casillas_vacias)

    def saltos_posibles(self, casilla, casillas_alrededor_enemigos, lista_saltos = None, cas_inicial = None):
        """Determina los posibles saltos de una ficha"""

        if cas_inicial != None:
            casilla_inicial = cas_inicial

        if casilla.ficha != None:

            f, c = casilla.cor_tablero
            casillas_alrededor_enemigos = casillas_alrededor_enemigos             # Para almacenar las casillas que rodean la ficha en cuestion


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

            for cas in casillas_alrededor_enemigos:

                if casilla.ficha.tipo_men() == True:                        # Si la ficha seleccionada es un men

                    if casilla.ficha.fila_inicial in self.filas_ini_inf:    # Si el men va subiendo

                        if cas.cor_tablero[1] < casilla.cor_tablero[1]:     # Si el men esta a la izquierda
                            print('Izquierda')
                            f_nueva, c_nueva = cas.cor_tablero              # El salto se realizara a la casilla superior izquierda inmediata

                            f_nueva -= 1
                            c_nueva -= 1

                            f_vieja, c_vieja = casilla.cor_tablero

                            #x = self._matriz[f_vieja][c_vieja]
                            #print(x.ficha.nom_archivo)

                            if self._com_coordenadas(f_nueva, c_nueva):         # Para que solo sea posible introducir valores validos en la funcion
                                # (f_nueva, c_nueva, f_vieja, c_vieja)
                                print(self.salto_valido(None, None, None, None, (f_nueva, c_nueva, f_vieja, c_vieja)))

                            else:
                                print(False)

                        if cas.cor_tablero[1] > casilla.cor_tablero[1]:  # Si el men esta a la izquierda
                            print('Derecha')
                            f_nueva, c_nueva = cas.cor_tablero  # El salto se realizara a la casilla superior izquierda inmediata

                            f_nueva -= 1
                            c_nueva += 1

                            f_vieja, c_vieja = casilla.cor_tablero

                            # x = self._matriz[f_vieja][c_vieja]
                            # print(x.ficha.nom_archivo)

                            # (f_nueva, c_nueva, f_vieja, c_vieja)

                            if self._com_coordenadas(f_nueva,c_nueva):  # Para que solo sea posible introducir valores validos en la funcion
                                # (f_nueva, c_nueva, f_vieja, c_vieja)
                                print(self.salto_valido(None, None, None, None, (f_nueva, c_nueva, f_vieja, c_vieja)))

                            else:
                                print(False)
                    if casilla.ficha.fila_inicial in self.filas_ini_sup:  # Si el men va subiendo

                        if cas.cor_tablero[1] < casilla.cor_tablero[1]:  # Si el men esta a la izquierda
                            print('Izquierda')
                            f_nueva, c_nueva = cas.cor_tablero  # El salto se realizara a la casilla superior izquierda inmediata

                            f_nueva += 1
                            c_nueva -= 1

                            f_vieja, c_vieja = casilla.cor_tablero

                            # x = self._matriz[f_vieja][c_vieja]
                            # print(x.ficha.nom_archivo)

                            # (f_nueva, c_nueva, f_vieja, c_vieja)
                            if self._com_coordenadas(f_nueva, c_nueva):  # Para que solo sea posible introducir valores validos en la funcion
                                # (f_nueva, c_nueva, f_vieja, c_vieja)
                                print(self.salto_valido(None, None, None, None, (f_nueva, c_nueva, f_vieja, c_vieja)))

                            else:
                                print(False)

                        if cas.cor_tablero[1] > casilla.cor_tablero[1]:  # Si el men esta a la izquierda
                            print('Derecha')
                            f_nueva, c_nueva = cas.cor_tablero  # El salto se realizara a la casilla superior izquierda inmediata

                            f_nueva += 1
                            c_nueva += 1

                            f_vieja, c_vieja = casilla.cor_tablero

                            # x = self._matriz[f_vieja][c_vieja]
                            # print(x.ficha.nom_archivo)

                            # (f_nueva, c_nueva, f_vieja, c_vieja)
                            if self._com_coordenadas(f_nueva, c_nueva):  # Para que solo sea posible introducir valores validos en la funcion
                                # (f_nueva, c_nueva, f_vieja, c_vieja)
                                print(self.salto_valido(None, None, None, None, (f_nueva, c_nueva, f_vieja, c_vieja)))

                            else:
                                print(False)


                if casilla.ficha.tipo_men() == False:           # En caso de que la ficha seleccionada sea un king

                    if cas.cor_tablero[0] < casilla.cor_tablero[0]:  # Si la ficha  esta a la arriba
                        print('Arriba')

                    pass

    def _com_coordenadas(self, f, c):
        """Para comprobar si unas coordenadas de matriz son validas"""

        if (f > 0 and f < 7) and (c > 0 and c < 7):
            return True

        else:

            return False





#a = Tablero()
#
# ma = a.inicializar_tablero()
#
# ma[0][0] = Casilla (Ficha(self.ficha_2), (0, 0), (100, 0))



