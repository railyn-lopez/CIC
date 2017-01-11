
def prueba(a, cont):

    if a < 10:
        a += 1
        cont += 1
        print(a, cont)
        return prueba(a, cont)

    else:
        return (a, cont)



print(prueba(5, 0))

