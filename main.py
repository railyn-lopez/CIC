import pygame, tablero
from ficha import Ficha
from tablero import Tablero
from casilla import Casilla

display_width = 800
display_heigth = 800
archivo_tablero = 'tablero_coordenado.png'                                              # Variable global para el nombre del archivo tablero.

mx = 0
my = 0

conf_click_area = False

board = Tablero()

matriz = board.inicializar_tablero()

pygame.init()                                                                           # Inicializando pygame

gameSurface = pygame.display.set_mode((display_width, display_heigth))                  # Dimenciones del surface (ventana)
sup_tablero = pygame.image.load(archivo_tablero).convert()

pygame.display.set_caption('Checkers')                                                  # titulo de la ventana
                                                                                        # reloj de juego
gana_empate = False                                                                     # Control main loop del juego, cambiando este valor, a True, # Se acaba el juego

gameSurface.blit(sup_tablero, (0, 0))

cas = None          # La casilla que contiene la ficha que se va a a cambiar de posicion


# Determinado donde se encuentra la ficha a mover
for f in range(len(matriz)):
    for c in range(len(matriz[f])):
        casb = matriz[f][c]
        #print(casb)
        if casb.ficha != None:
            cas_pintar = casb                                                           # Almacenando la casilla que contiene la ficha
            gameSurface.blit(cas_pintar.ficha.sup_ficha, cas_pintar.ficha.rect)         # chip.sup_ficha, chip.rect)

def dibujarFicha (x, y):
    """Para dibujar una ficha determinada en el tablero"""

    cas.ficha.rect.centerx = x
    cas.ficha.rect.centery = y

    #gameSurface.blit(sup_tablero, (0, 0))                                               # Redibujando para dar la ilucion de movimiento
    gameSurface.blit(cas.ficha.sup_ficha, cas.ficha.rect)


def dibujarFichaCentrada(x, y):
    """Para dibujar la ficha centrada en la casilla despues de moverla"""

    casilla = board.casilla_activa(x, y)                                                                            # Para determinar la casilla donde se encentra ubicada la ficha
    casilla.ficha.rect.centerx = casilla.cor_pixeles[0] + (casilla.cor_pixeles[1] - casilla.cor_pixeles[0]) / 2     # Colocando la ficha centralizada
    casilla.ficha.rect.centery = casilla.cor_pixeles[2] + (casilla.cor_pixeles[3] - casilla.cor_pixeles[2]) / 2

    #gameSurface.blit(sup_tablero, (0, 0))                                                                           # Redibujando la ficha centralizada
    gameSurface.blit(casilla.ficha.sup_ficha, casilla.ficha.rect)

def dibujarTodasFichas():
   """Para dibujar toads las fichas luego del mov. de una ficha"""
   tablero = board.getMatriz()

   for f in range(len(tablero)):
       for c in range(len(tablero[f])):

           casilla = tablero[f][c]
           mx, my = pygame.mouse.get_pos()

           if casilla.ficha != None and casilla.ficha != Ficha.activa:#casilla.ficha.click_area(mx, my) == False:                                          # La ficha solo se dibujara si no esta en movimiento
               casilla.ficha.rect.centerx = casilla.cor_pixeles[0] + (casilla.cor_pixeles[1] - casilla.cor_pixeles[0]) /2  # Colocando la ficha centralizada
               casilla.ficha.rect.centery = casilla.cor_pixeles[2] + (casilla.cor_pixeles[3] - casilla.cor_pixeles[2]) /2

               #gameSurface.blit(sup_tablero, (0, 0))  # Redibujando la ficha centralizada
               gameSurface.blit(casilla.ficha.sup_ficha, casilla.ficha.rect)


while not gana_empate:                                                                           # Game Loop

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            gana_empate = True

        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] == 1:         # Si se clickeo con el boton izq

            mx, my = pygame.mouse.get_pos()
            mxg, myg = mx, my                                                                   # Para almacenar la posicion donde se clickeo la ficha para moverla
            cas = board.casilla_activa(mx, my)

            #nada  = board.saltos_posibles_men(cas, [], [], [], [])
            #board.enemigos_proximo(cas)
            #board.saltos_posibles(cas, [])
            #board.movidas_posibles(cas)

            if cas.ficha != None:

                cas_mov = cas                                                                       # La casilla donde se almacena la ficha a cambiar de lugar
                conf_click_area = cas.ficha.click_area(mx, my)                                      # Para validar si se esta clickeando una ficha
                #print(conf_click_area)

                #board.movidas_posibles_men(cas.ficha)                                               # Movimientos validos fichas men
                #board.movidas_posibles_king(cas.ficha)                                              # Movimientos validos fichas king



        if event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_pressed()[0] == 0:               # Para determinar si se levanto el boton izq del mouse.

            mx, my = pygame.mouse.get_pos()

            cas_vieja = board.casilla_activa(mxg, myg)

            if cas_vieja.ficha != None:                                                             # Si se clickeo una casilla con ficha, para empezar el movimiento

                if board.movimiento_valido(mx, my, mxg, myg) == True:                               # Determinado si donde el usuario pretende mover la ficha, es un movimiento valido.

                    board.cop_ficha(mx, my, cas_mov.ficha)                                          # Copiando la ficha en el tablero
                    cas_mov.ficha = None                                                            # Borrando la ficha de la casilla donde estaba ubicada
                    #print('Se ejecuto')

                    gameSurface.blit(sup_tablero, (0, 0))
                    dibujarFichaCentrada(mx, my)                                                    # Dibujar la ficha centrada
                    dibujarTodasFichas()
                    conf_click_area = False                                                         # Para evitar segir dibujando, cuando el mouse se mueva

                elif board.salto_valido(mx, my, mxg, myg) == True:                                  # Para determinar si se esta comiendo validamente

                    board.cop_ficha(mx, my, cas_mov.ficha)                                          # Copiando la ficha en el tablero
                    cas_mov.ficha = None                                                            # Borrando la ficha de la casilla donde estaba ubicada
                    #print('Se ejecuto')

                    gameSurface.blit(sup_tablero, (0, 0))
                    dibujarFichaCentrada(mx, my)                                                    # Dibujar la ficha centrada
                    dibujarTodasFichas()
                    conf_click_area = False                                                         # Para evitar segir dibujando, cuando el mouse se mueva

                else:                                                                               # En caso de que el movimiento no sea valido, redibujar la ficha en la casilla donde estaba
                    conf_click_area = False                                                         # Para evitar segir dibujando, cuando el mouse se mueva
                    cas = board.casilla_activa(mxg, myg)

                    gameSurface.blit(sup_tablero, (0, 0))

                    dibujarFichaCentrada(mxg, myg)                                                  # Dibujar la ficha centrada en la casilla si el movimiento fue invalido
                    dibujarTodasFichas()


        if event.type == pygame.MOUSEMOTION and conf_click_area:                                # Si el mouse se esta moviendo y no se ha levantado
            mx2, my2 = pygame.mouse.get_pos()                                                   # El boton por arriba de la ficha, obtener posicion del mouse

            gameSurface.blit(sup_tablero, (0, 0))
            dibujarTodasFichas()
            dibujarFicha(mx2, my2)                                                              # Dibujando la ficha para dar la ilucion de movimiento
            #dibujarTodasFichas()


    pygame.display.update()                                    # Si se coloca un parametro solo va a refrescar ese parametro


pygame.quit()                                                      # Cerrando todos los modulos de pygame
quit()                                                             # Cerrando Python