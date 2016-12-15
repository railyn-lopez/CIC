import pygame, tablero, ficha

board = tablero.Tablero()
chip = ficha.Ficha()
pygame.init()                                        # Inicializando pygame

display_width = 800
display_heigth = 800

gameDisplay = pygame.display.set_mode((display_width, display_heigth))    # Dimenciones del frame (ventana)
pygame.display.set_caption('Checkers')                                    # titulo de la ventana
clock = pygame.time.Clock()                                               # reloj de juego
gana_empate = False                                                       # Control main loop del juego, cambiando este valor, a True,                                                       # Se acaba el juego

ficha = chip.cargar_imagen()           # 60 x 60
background = board.cargar_imagen()                # 800 x 800

gameDisplay.blit(background, (0, 0))
gameDisplay.blit(ficha, (20, 20))

while not gana_empate:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gana_empate = True


        pygame.display.update()                     # Si se coloca un parametro solo va a refrescar ese parametro

pygame.quit()                                       # Cerrando pygame
quit()