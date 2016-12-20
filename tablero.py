class Tablero:

    def __init__(self):

        self.matriz = 8 * [ 8 * [None]]

        pass

a = Tablero()

for a in (a.matriz):
    for b in a:
        print(b)

    print(a)


