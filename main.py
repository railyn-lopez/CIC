import pygame, time
from ficha import Ficha
from tablero import Tablero
from casilla import Casilla

display_width = 800
display_heigth = 800
archivo_tablero = 'tablero_coordenado.png'                                              # Variable global para el nombre del archivo tablero.
black = (0, 0, 0,)
white = (255, 255, 255)
brown = (51, 25, 0)
red = (255, 0, 0)
mx = 0
my = 0


board = Tablero()

pygame.init()                                                                           # Inicializando pygame
pygame.font.init()                                                                      # Inicializar el modulo font de pygame
smallfont = pygame.font.SysFont(None, 25)                                                    # Creando el objeto font
medfont = pygame.font.SysFont(None, 50)
largefont = pygame.font.SysFont(None, 75)


gameSurface = pygame.display.set_mode((display_width, display_heigth))                  # Dimenciones del surface (ventana)
sup_tablero = pygame.image.load(archivo_tablero).convert()

pygame.display.set_caption('Checkers')                                                  # titulo de la ventana
                                                                                        # reloj de juego

def inicializar_juego():

    matriz = board.inicializar_tablero()
    gameSurface.blit(sup_tablero, (0, 0))
    cas = None                                                                              # La casilla que contiene la ficha que se va a a cambiar de posicion


    # Determinado donde se encuentra la ficha a mover
    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            casb = matriz[f][c]
            #print(casb)
            if casb.ficha != None:
                cas_pintar = casb                                                           # Almacenando la casilla que contiene la ficha
                gameSurface.blit(cas_pintar.ficha.sup_ficha, cas_pintar.ficha.rect)         # chip.sup_ficha, chip.rect)


def dibujarFicha (cas):#(x, y):
    """Para dibujar una ficha determinada en el tablero"""

    # cas.ficha.rect.centerx = x
    # cas.ficha.rect.centery = y

    #gameSurface.blit(sup_tablero, (0, 0))                                               # Redibujando para dar la ilucion de movimiento
    gameSurface.blit(cas.ficha.sup_ficha, cas.ficha.rect)


def dibujarFichaCentrada(x, y):
    """Para dibujar la ficha centrada en la casilla despues de moverla"""

    casilla = board.casilla_activa(x, y)                                                                            # Para determinar la casilla donde se encentra ubicada la ficha
    casilla.ficha.rect.centerx = casilla.cor_pixeles[0] + (casilla.cor_pixeles[1] - casilla.cor_pixeles[0]) / 2     # Colocando la ficha centralizada
    casilla.ficha.rect.centery = casilla.cor_pixeles[2] + (casilla.cor_pixeles[3] - casilla.cor_pixeles[2]) / 2

    #gameSurface.blit(sup_tablero, (0, 0))                                                                           # Redibujando la ficha centralizada
    gameSurface.blit(casilla.ficha.sup_ficha, casilla.ficha.rect)

def dibujarTodasFichas(tablero1):
   """Para dibujar toads las fichas luego del mov. de una ficha"""
   tablero = tablero1
   #tablero = board.getMatriz()

   for f in range(len(tablero)):
       for c in range(len(tablero[f])):

           casilla = tablero[f][c]
           mx, my = pygame.mouse.get_pos()

           if casilla.ficha != None and casilla.ficha != Ficha.activa:#casilla.ficha.click_area(mx, my) == False:                                          # La ficha solo se dibujara si no esta en movimiento
               casilla.ficha.rect.centerx = casilla.cor_pixeles[0] + (casilla.cor_pixeles[1] - casilla.cor_pixeles[0]) /2  # Colocando la ficha centralizada
               casilla.ficha.rect.centery = casilla.cor_pixeles[2] + (casilla.cor_pixeles[3] - casilla.cor_pixeles[2]) /2

               #gameSurface.blit(sup_tablero, (0, 0))  # Redibujando la ficha centralizada
               gameSurface.blit(casilla.ficha.sup_ficha, casilla.ficha.rect)

def make_rect_text(text, dis_y):
    """Para crear rectangulo, para manipular el texto """
    rect_text = text.get_rect()                                                     # Sacando rectangulo del texto, para su manupulacion
    rect_text.center = (display_width / 2, ((display_heigth / 2) + dis_y))          # Para que el mensaje quede centralizado
    return rect_text

def message_to_screen(msg, color, size='small', dis_y=0):
                                                                                    # y_dis, para mover el texto a lo largo de y (arriba y abajo).
    if size == 'small':
        screen_text = smallfont.render(msg, True, color)                            # Creando el surface que contiene de acuerdo al tamano
        rect_text = make_rect_text(screen_text, dis_y)

    elif size == 'medium':
        screen_text = medfont.render(msg, True, color)
        rect_text = make_rect_text(screen_text, dis_y)

    elif size == 'large':
        screen_text = largefont.render(msg, True, color)                            # Obteniendo el Rectangulo, para la centralizacion
        rect_text = make_rect_text(screen_text, dis_y)

    else:
        print('Condicion indeterminada, no deberias estar aqui')

    gameSurface.blit(screen_text, rect_text)  # Dibujando el mensaje en la pantalla

def menu_loop():
    """Para que el usuario seleccione el modo de juego"""
    modo_juego = True                                                      # Para controlar el loop que le permitira al usuario seleccionar el modo de juego
    modo_juego2 = True                                                     # Para controlar el loop que le permitira al usuario seleccionar el modo el lugar de las fichas
    while modo_juego:

        gameSurface.fill(brown)
        message_to_screen('Welcome to chechers', red, 'large', -40)
        message_to_screen('Press S to single player (Against the machine)', white, 'small', 0)
        message_to_screen('Press M to multiplayer', white, 'small', 40)
        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                modo_juego = False
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:                 # Si se presiona la s, se jugara contra la maquina
                    gameSurface.fill(brown)
                    message_to_screen('Single player mode is a work in progress', red, 'medium', 0)
                    pygame.display.update()
                    time.sleep(4)
                    modo_juego = False
                    return True

                if event.key == pygame.K_m:                 # Si se presiona la m, Se jugara contra otro jugador

                    while modo_juego2:

                        gameSurface.fill(brown)
                        message_to_screen('Select location for the darkers chips (1st move)', red, 'medium', -40)
                        message_to_screen('Press A to above', white, 'small', 0)
                        message_to_screen('Press B to bellow', white, 'small', 40)
                        pygame.display.update()

                        for event2 in pygame.event.get():

                            if event2.type == pygame.QUIT:
                                return False

                            if event2.type == pygame.KEYDOWN:
                                if event2.key == pygame.K_a:  # Si se presiona la a, las fichas oscuras estaran arriba
                                    board.orden_fichas = 'a'
                                    return True               # Para entrar al gameloop en el main program

                                if event2.key == pygame.K_b:  # Si se presiona la s, las fichas oscuras estaran abajo
                                    board.orden_fichas = 'b'
                                    return True               # Para entrar al gameloop en el main program



def game_loop():
    """Logica del juego, interaccion del usuario y las fichas"""

    gana_empate = False                                                     # Control main loop del juego, cambiando este valor, a True, # Se acaba el juego
    conf_click_area = False
    game_over = False
    tablero = board.getMatriz()
    inicializar_juego()
    ficha_selec = False                                                     # Controla el turno
    casilla_en_salto = None                                                 # Para que la ficha realice todos los saltos posibles, en una secuencia determinada y no se puedan mover las demas fichas
    saltos_posibles = []                                                    # Utilizada para contabilizar si una casilla tiene, saltos disponibles luego de realizar un salto.

    while not gana_empate:                                                                           # Game Loop

        game_over_loop = board.game_over()                                                           # Para determinar si el juego termino
        while game_over_loop:                                                                        # En caso de que el juego terminara entrara al game over loop
            time.sleep(2)                                                                            # Para no borrar la pantalla del juego inmediatamente.
            gameSurface.fill(brown)
            message_to_screen('Game Over', red, 'large', 0)
            message_to_screen('Press C to continue or Q to quit', white, 'small', 40)
            pygame.display.update()

            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:                 # Si se presiona la q, el juego termina
                        gana_empate = True
                        game_over_loop = False

                    if event.key == pygame.K_c:
                        board.limpiar_marcador()                # Si se presiona la c, el juego continua
                        game_over_loop = False
                        game_loop()                             # Jugar nuevamente
                        gana_empate = True                      # Para que el programa termine cuando salga de la llamada recursiva (no darle 2 veces a la x)


        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gana_empate = True
                return

            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] == 1:         # Si se clickeo con el boton izq

                mx, my = pygame.mouse.get_pos()
                mxg, myg = mx, my                                                                   # Para almacenar la posicion donde se clickeo la ficha para moverla
                cas = board.casilla_activa(mx, my)

                #nada  = board.saltos_posibles_men(cas, [], [], [], [])
                #board.enemigos_proximo(cas)
                #board.movidas_posibles(cas)
                #board.saltos_posibles(cas, [])
                #board.movidas_validos_por_color('marron')


                if cas.ficha != None:

                    # Para jugar sin turno
                    # cas_mov = cas  # La casilla donde se almacena la ficha a cambiar de lugar
                    # conf_click_area = cas.ficha.click_area(mx, my)  # Para validar si se esta clickeando una ficha
                    # ficha_selec = True
                    ####################################################################################################
                    # Para jugar con turno

                    if casilla_en_salto == None:                                                                    # Si no hay una casilla en medio de una secuencia de salto.

                        if board.turno_oscuras() == True and cas.ficha.tipo_color == 'marron':

                            cas_mov = cas                                                                           # La casilla donde se almacena la ficha a cambiar de lugar
                            conf_click_area = cas.ficha.click_area(mx, my)                                          # Para validar si se esta clickeando una ficha
                            ficha_selec = True

                        if board.turno_oscuras() == False and cas.ficha.tipo_color == 'blanca':

                            cas_mov = cas                                                                           # La casilla donde se almacena la ficha a cambiar de lugar
                            conf_click_area = cas.ficha.click_area(mx, my)                                          # Para validar si se esta clickeando una ficha
                            ficha_selec = True

                    else:                                                                                           # Si hay una casilla en medio de una secuencia de salto,

                        if cas == casilla_en_salto:

                            cas_mov = cas                                                                           # La casilla donde se almacena la ficha a cambiar de lugar
                            conf_click_area = cas.ficha.click_area(mx, my)                                          # Para validar si se esta clickeando una ficha
                            ficha_selec = True


                    #print(conf_click_area)

                    #board.movidas_posibles_men(cas.ficha)                                               # Movimientos validos fichas men
                    #board.movidas_posibles_king(cas.ficha)                                              # Movimientos validos fichas king
                    #board.saltos_posibles_men_2(cas.ficha)
                    #board.saltos_posibles_king(cas.ficha)

            if event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_pressed()[0] == 0 and ficha_selec == True:               # Para determinar si se levanto el boton izq del mouse.

                ficha_selec = False                                                                     # Reseteando, la variable que controla el turno
                mx, my = pygame.mouse.get_pos()

                cas_vieja = board.casilla_activa(mxg, myg)

                if cas_vieja.ficha != None:                                                             # Si se clickeo una casilla con ficha, para empezar el movimiento

                    if board.movimiento_valido(mx, my, mxg, myg) == True:                               # Determinado si donde el usuario pretende mover la ficha, es un movimiento valido.

                        board.cop_ficha(mx, my, cas_mov.ficha)                                          # Copiando la ficha en el tablero
                        cas_mov.ficha = None                                                            # Borrando la ficha de la casilla donde estaba ubicada
                        #print('Se ejecuto')
                        gameSurface.blit(sup_tablero, (0, 0))
                        dibujarFichaCentrada(mx, my)                                                    # Dibujar la ficha centrada
                        dibujarTodasFichas(tablero)
                        board.contador_turno()
                        conf_click_area = False                                                         # Para evitar segir dibujando, cuando el mouse se mueva

                    elif board.salto_valido(mx, my, mxg, myg) == True:                                  # Para determinar si se esta comiendo validamente

                        board.cop_ficha(mx, my, cas_mov.ficha)                                          # Copiando la ficha en el tablero
                        cas_mov.ficha = None                                                            # Borrando la ficha de la casilla donde estaba ubicada

                        f, c = board.det_casilla(mx, my)                                                # Para averiguar si la casilla esta en medio de una secuencia de salto
                        cas_ver = board._matriz[f][c]

                        if len(saltos_posibles) > 0 and [cas_ver] in saltos_posibles:                   # En caso de que se este en una secuencia de salto y el salto realizado este en los saltos posibles que se puedem realizar
                            casilla_en_salto = None  ###########                                        # Para indicar que no se esta en medio de una secuencia de salto
                            #board.contador_turno()

                        saltos_posibles = board.saltos_posibles_universal(cas_ver.ficha)                # Para verificar despues del salto si es necesario seguir saltando

                        if len(saltos_posibles) == 0:                                                   # En caso de que no sea necesario seguir saltando
                            casilla_en_salto = None  ###########
                            board.contador_turno()

                        else:
                            casilla_en_salto = cas_ver                                                  # Para solo poder mover la ficha que empezo una secuencia de salto.

                        #print('Se ejecuto')

                        gameSurface.blit(sup_tablero, (0, 0))
                        dibujarFichaCentrada(mx, my)                                                    # Dibujar la ficha centrada
                        dibujarTodasFichas(tablero)
                        conf_click_area = False                                                         # Para evitar segir dibujando, cuando el mouse se mueva

                    else:                                                                               # En caso de que el movimiento no sea valido, redibujar la ficha en la casilla donde estaba
                        conf_click_area = False                                                         # Para evitar segir dibujando, cuando el mouse se mueva
                        cas = board.casilla_activa(mxg, myg)
                        gameSurface.blit(sup_tablero, (0, 0))
                        dibujarFichaCentrada(mxg, myg)                                                  # Dibujar la ficha centrada en la casilla si el movimiento fue invalido
                        dibujarTodasFichas(tablero)

            if event.type == pygame.MOUSEMOTION and conf_click_area:                                # Si el mouse se esta moviendo y no se ha levantado
                mx2, my2 = pygame.mouse.get_pos()                                                   # El boton por arriba de la ficha, obtener posicion del mouse

                gameSurface.blit(sup_tablero, (0, 0))
                tablero = board.getMatriz()                                                         # Pasandole la matriz a la funcion
                dibujarTodasFichas(tablero)

                cas.ficha.rect.centerx = mx2
                cas.ficha.rect.centery = my2

                dibujarFicha(cas)                                                                   # Dibujando la ficha para dar la ilucion de movimiento
                #dibujarTodasFichas()

        pygame.display.update()                                                                     # Si se coloca un parametro solo va a refrescar ese parametro

if menu_loop():                                                                                     # Despues que se tome la accion pertinente en el menu
    game_loop()
#message_to_screen('Game Over', (0, 0, 0))
#pygame.display.update()
#time.sleep(2)
pygame.quit()                                                      # Cerrando todos los modulos de pygame
quit()                                                             # Cerrando Python