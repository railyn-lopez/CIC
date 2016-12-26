class Casilla:

    def __init__(self, ficha, cor_tablero, cor_pixeles, color):

        self.ficha = ficha                  # none significa que la casilla esta vacia
        self.cor_tablero = cor_tablero      # En la matriz
        self.cor_pixeles = cor_pixeles      # En pixels
        self.color = color                  # color de la casilla

    def __str__(self):
        return ('contenido: {}, cor_tablero: {}, cor_pixeles: {}, color: {}'.format(self.ficha, self.cor_tablero, self.cor_pixeles, self.color))