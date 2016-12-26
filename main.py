import pygame, tablero
from ficha import Ficha
from tablero import Tablero
from casilla import Casilla

display_width = 800
display_heigth = 800

mx = 0
my = 0

conf_click_area = False

board = Tablero()

matriz = board.inicializar_tablero()

pygame.init()                                                             # Inicializando pygame

chip = Ficha('f_marron.png')

gameSurface = pygame.display.set_mode((display_width, display_heigth))     # Dimenciones del surface (ventana)
sup_tablero = pygame.image.load('tablero.png').convert()


pygame.display.set_caption('Checkers')                                    # titulo de la ventana
                                                                          # reloj de juego
gana_empate = False                                                       # Control main loop del juego, cambiando este valor, a True, # Se acaba el juego

gameSurface.blit(sup_tablero, (0, 0))

cas = None          # La casilla que contiene la ficha que se va a a cambiar de posicion


# Determinado donde se encuentra la ficha a mover
for f in range(len(matriz)):
    for c in range(len(matriz[f])):
        casb = matriz[f][c]
        if casb.ficha != None:
            cas_pintar = casb          # Almacenando la casilla que contiene la ficha
            gameSurface.blit(cas_pintar.ficha.sup_ficha, cas_pintar.ficha.rect)         # chip.sup_ficha, chip.rect)


while not gana_empate:                                                    # Game Loop

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            gana_empate = True

        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] == 1:         # Si se clickeo con el boton izq
            mx, my = pygame.mouse.get_pos()
            mxg = mx                                                                            # Para almacenar la posicion donde se clickeo la ficha para moverla
            myg = my
            cas = board.casilla_activa(mx, my)

            if cas.ficha != None:
                cas_mov = cas                                                                   # La casilla donde se almacena la ficha a cambiar de lugar
                conf_click_area = cas.ficha.click_area(mx, my)                                  # Para validar si se esta clickeando una ficha
                #print(conf_click_area)

        if event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_pressed()[0] == 0:           # Para determinar si se levanto el boton izq.

            mx, my = pygame.mouse.get_pos()
            if board.movimiento_valido(mx, my):                                                 # Determinado si donde el usuario pretende mover la ficha, es un movimiento valido.

                board.cop_ficha(mx, my, cas_mov.ficha)                                          # Copiando la ficha en el tablero
                cas_mov.ficha = None                                                            # Borrando la ficha de la casilla donde estaba ubicada
                #print('Se ejecuto')
                conf_click_area = False

            else:                                                                               # En caso de que el movimiento no sea valido, redibujar la ficha en la casilla donde estaba
                conf_click_area = False
                cas = board.casilla_activa(mxg, myg)
                cas.ficha.rect.centerx = mxg
                cas.ficha.rect.centery = myg

                gameSurface.blit(sup_tablero, (0, 0))  # Redibujando para dar la ilucion de movimiento
                gameSurface.blit(cas.ficha.sup_ficha, cas.ficha.rect)


        if event.type == pygame.MOUSEMOTION and conf_click_area:   # Si el mouse se esta moviendo y no se ha levantado
            mx2, my2 = pygame.mouse.get_pos()                      # El boton por arriba de la ficha, obtener posicion del mouse

            cas.ficha.rect.centerx = mx2
            cas.ficha.rect.centery = my2

            gameSurface.blit(sup_tablero, (0, 0))                  # Redibujando para dar la ilucion de movimiento
            gameSurface.blit(cas.ficha.sup_ficha, cas.ficha.rect)

        pygame.display.update()                                    # Si se coloca un parametro solo va a refrescar ese parametro

pygame.quit()                                                      # Cerrando todos los modulos de pygame
quit()                                                             # Cerrando Python