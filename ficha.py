import pygame

class Ficha:
    def __init__(self, nom_archivo):

        gameSurface = pygame.display.set_mode((800, 800))
        self.sup_ficha =  pygame.image.load(nom_archivo).convert_alpha()       # 60 x 60
        self.ficha_rect = self.sup_ficha.get_rect()

        pass
