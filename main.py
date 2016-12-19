import pygame, tablero
from ficha import Ficha
from tablero import Tablero

display_width = 800
display_heigth = 800

mx = 0
my = 0

board = Tablero()

pygame.init()                                                             # Inicializando pygame

chip = Ficha('f_marron.png')

gameSurface = pygame.display.set_mode((display_width, display_heigth))     # Dimenciones del surface (ventana)
sup_tablero = pygame.image.load('tablero.png').convert()


pygame.display.set_caption('Checkers')                                    # titulo de la ventana
                                                                          # reloj de juego
gana_empate = False                                                       # Control main loop del juego, cambiando este valor, a True,                                                       # Se acaba el juego

gameSurface.blit(sup_tablero, (0, 0))
gameSurface.blit(chip.sup_ficha, chip.rect)

while not gana_empate:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gana_empate = True

        if event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0] == 1:

            mx, my = pygame.mouse.get_pos()
            #print(mx, my)

            if mx <= (chip.rect.x + chip.rect.width) and (my <= (chip.rect.y) + chip.rect.height) and pygame.mouse.get_pressed()[0] == 1:

                print('TRUE')
                mx, my = 0, 0
                chip.rect.x, chip.rect.y = pygame.mouse.get_pos()

                #print('True Presionado')
                #print(chip.rect.x, (mx, my))

                gameSurface.blit(sup_tablero, (0, 0))
                gameSurface.blit(chip.sup_ficha, chip.rect)


    pygame.display.update()                         # Si se coloca un parametro solo va a refrescar ese parametro

pygame.quit()                                       # Cerrando todos los modulos de pygame
quit()                                              # Cerrando Python