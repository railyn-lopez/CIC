class Casilla:

    def __init__(self, ficha, cor_tablero, cor_pixeles):

        self.ficha = ficha
        self.cor_tablero = cor_tablero
        self.cor_pixeles = cor_pixeles

    def __str__(self):
        return ('contenido: {}, cor_tablero: {}, cor_pixeles: {}'.format(self.ficha, self.cor_tablero, self.cor_pixeles))