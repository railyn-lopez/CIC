import pygame

class Ficha:
    def __init__(self, nom_archivo, fila_inicial, x, y):

        gameSurface = pygame.display.set_mode((800, 800))
        self.sup_ficha = pygame.image.load(nom_archivo).convert_alpha()       # 60 x 60
        self.nom_archivo = nom_archivo
        self.rect = self.sup_ficha.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.fila_inicial = fila_inicial

    def click_area(self, mx, my):
        """Para determinar si se esta clickeando dentro de una ficha"""

        if (self.rect.x <= mx <= self.rect.topright[0]) and (self.rect.y <= my <= self.rect.bottomleft[1]) and pygame.mouse.get_pressed()[0] == 1:
            #print('si')
            return True

        else:
            return False


