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
            cas = casb          # Almacenando la casilla que contiene la ficha
            gameSurface.blit(cas.ficha.sup_ficha, cas.ficha.rect)         # chip.sup_ficha, chip.rect)


while not gana_empate:                                                    # Game Loop

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            gana_empate = True

        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] == 1:         # Si se clickeo con el boton izq
            mx, my = pygame.mouse.get_pos()

            if cas.ficha != None:
                ficha_mover = cas.ficha             # Almacenando la ficha que se cambiara de lugar
                conf_click_area = cas.ficha.click_area(mx, my)


        if event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_pressed()[0] == 0:           # Para determinar si se levanto el boton izq.

            mx, my = pygame.mouse.get_pos()
            if board.movimiento_valido(mx, my):                     # Determinado si donde el usuario pretende mover la ficha, es un movimiento valido.
                #print('Se ejecuto')
                conf_click_area = False

        if event.type == pygame.MOUSEMOTION and conf_click_area:   # Si el mouse se esta moviendo y no se ha levantado
            mx2, my2 = pygame.mouse.get_pos()                      # el boton por arriba de la ficha, obtener posicion del mouse

            cas.ficha.rect.centerx = mx2
            cas.ficha.rect.centery = my2

        if cas.ficha != None:
            gameSurface.blit(sup_tablero, (0, 0))                      # Redibujando para dar la ilucion de movimiento
            gameSurface.blit(cas.ficha.sup_ficha, cas.ficha.rect)

        pygame.display.update()                                    # Si se coloca un parametro solo va a refrescar ese parametro

pygame.quit()                                                      # Cerrando todos los modulos de pygame
quit()                                                             # Cerrando Python