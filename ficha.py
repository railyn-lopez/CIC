import pygame

class Ficha:
    def __init__(self, nom_archivo):

        gameSurface = pygame.display.set_mode((800, 800))
        self.sup_ficha = pygame.image.load(nom_archivo).convert_alpha()       # 60 x 60
        self.rect = self.sup_ficha.get_rect()
        self.rect.x = 10
        self.rect.y = 10


