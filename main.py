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

        #print(event)

        if event.type == pygame.MOUSEBUTTONDOWN:

            mx, my = pygame.mouse.get_pos()

            if mx <= (chip.rect.bottomright[0] - 10)  and (my <= chip.rect.bottomright[1] - 10):
                print(True)




            print(mx, my)

            # print(ficha_rect)
            # ficha_rect.x, ficha_rect.y = mx, my
            # gameSurface.blit(sup_tablero, (0, 0))
            # gameSurface.blit(ficha, ficha_rect)


        pygame.display.update()                     # Si se coloca un parametro solo va a refrescar ese parametro

pygame.quit()                                       # Cerrando todos los modulos de pygame
quit()                                              # Cerrando Python