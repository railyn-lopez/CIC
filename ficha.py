import pygame

class Ficha:

    activa = None                               # Para determinar si la ficha esta en movimiento

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
            Ficha.activa = self                  # Para determinar si la ficha esta en movimiento
            return True

        else:
            Ficha.activa = None
            return False

    @property
    def tipo_color(self):
        """Para determinar el color de la ficha"""

        nombre = self.nom_archivo               # Extrayendo el color de la ficha teniendo en cuenta que esta en '_'
        end = nombre.find("_", 2)
        color = nombre[2:end]

        return color


    def tipo_men(self):
        """Para determinar si la ficha es un men o un king"""

        if 'rey' not in self.nom_archivo:

            return True

        else:

            return False

