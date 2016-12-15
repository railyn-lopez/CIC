import pygame
class Tablero:

    def __init__(self):
        # self.nom_imagen = 'tablero.png'
        pass

    def cargar_imagen(self):
        return pygame.image.load('tablero.png').convert_alpha()         # 60 x 60

