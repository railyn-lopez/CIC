import pygame, tablero
from ficha import Ficha
from tablero import Tablero

display_width = 800
display_heigth = 800

mx = 0
my = 0

conf_click_area = False

board = Tablero()

pygame.init()                                                             # Inicializando pygame

chip = Ficha('f_marron.png')

gameSurface = pygame.display.set_mode((display_width, display_heigth))     # Dimenciones del surface (ventana)
sup_tablero = pygame.image.load('tablero.png').convert()


pygame.display.set_caption('Checkers')                                    # titulo de la ventana
                                                                          # reloj de juego
gana_empate = False                                                       # Control main loop del juego, cambiando este valor, a True, # Se acaba el juego

gameSurface.blit(sup_tablero, (0, 0))
gameSurface.blit(chip.sup_ficha, chip.rect)


while not gana_empate:                                                    # Game Loop

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            gana_empate = True

        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] == 1:         # Si se clickeo con el
            mx, my = pygame.mouse.get_pos()                                                     # boton izq
            conf_click_area = chip.click_area(mx, my)


        if event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_pressed()[0] == 0:           # Para determinar
            conf_click_area = False                                                             # Si se levanto el
                                                                                                # boton izq

        if event.type == pygame.MOUSEMOTION and conf_click_area:   # Si el mouse se esta moviendo y no se ha levantado
            mx2, my2 = pygame.mouse.get_pos()                      # el boton por arriba de la ficha, obtener posicion del mouse

            chip.rect.centerx = mx2
            chip.rect.centery = my2

        gameSurface.blit(sup_tablero, (0, 0))                      # Redibujando para dar la ilucion de movimiento
        gameSurface.blit(chip.sup_ficha, chip.rect)
        pygame.display.update()                                    # Si se coloca un parametro solo va a refrescar ese parametro

pygame.quit()                                                      # Cerrando todos los modulos de pygame
quit()                                                             # Cerrando Python