import pygame
class Ficha:
    def __init__(self):
        #self.nom_imagenes = ['f_marron.png']
        pass

    def cargar_imagen(self):
        return  pygame.image.load('f_marron.png').convert_alpha()       # 60 x 60