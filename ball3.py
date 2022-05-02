import sys, pygame
# Inicializamos pygame
pygame.init()
# Muestro una ventana de 800x600
size = 800, 600
screen = pygame.display.set_mode(size)
# Cambio el título de la ventana
pygame.display.set_caption("Juego BALL")
# Inicializamos variables
width, height = size
speed = [1, 1]
white = 255, 255, 255
black = 0, 0, 0
fondo = pygame.image.load("fondo.png").convert()
# Crea un objeto imagen pelota y obtengo su rectángulo
ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()
# Crea un objeto imagen bate y obtengo su rectángulo
bate1 = pygame.image.load("bate.png")
bate = pygame.image.load("bate.png")
baterect = bate.get_rect()
baterect1 = bate1.get_rect()
# Pongo el bate en el centro de la pantalla
ballrect.move_ip(size[0]/2,size[1]/2)
baterect.move_ip(200, 300)
baterect1.move_ip(600, 300)
# Comenzamos el bucle del juego
run=True
while run:
    # Espero un tiempo (milisegundos) para que la pelota no vaya muy rápida
    pygame.time.delay(3)
    # Capturamos los eventos que se han producido
    for event in pygame.event.get():
        #Si el evento es salir de la ventana, terminamos
        if event.type == pygame.QUIT: run = False
    # Compruebo si se ha pulsado alguna tecla
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        baterect1=baterect1.move(0, -1)
    if keys[pygame.K_s]:
        baterect1=baterect1.move(0, 1)
    # Compruebo si hay colisión
    if baterect.colliderect(ballrect) or baterect1.colliderect(ballrect):
        speed[0] = - speed[0]
    if keys[pygame.K_UP]:
        baterect=baterect.move(0, -1)
    if keys[pygame.K_DOWN]:
        baterect=baterect.move(0, 1)
    # Muevo la pelota
    ballrect = ballrect.move(speed)
    # Compruebo si la pelota llega a los límites de la ventana
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    # Pinto el fondo de blanco, dibujo la pelota y actualizo la pantalla
    screen.fill(black)
    screen.blit(fondo, [0, 40])
    screen.blit(ball, ballrect)
    screen.blit(bate1, baterect1)
    screen.blit(bate, baterect)

    pygame.display.flip()
# Salgo de pygame
pygame.quit()