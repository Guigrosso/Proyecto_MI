import sys, pygame
# Inicializamos pygame
pygame.init()
# Muestro una ventana de 800x600
tamanio = 800, 600
pantalla = pygame.display.set_mode(tamanio)
# Cambio el título de la ventana
pygame.display.set_caption("Juego pelota")
# Inicializamos variables
ancho, altura = tamanio
velocidad = [1, 1]
blanco = 255, 255, 255
negro = 0, 0, 0
#fondo = pygame.image.load("fondo.png").convert()
# Crea un objeto imagen pelota y obtengo su rectángulo
pelotaPng="pelota.png"
pelota = pygame.image.load(pelotaPng)
pelotaRectangulo = pelota.get_rect()
# Crea un objeto imagen bate y obtengo su rectángulo
batePic="bate.png"
bate = pygame.image.load(batePic)
bate1 = pygame.image.load(batePic)
bateRectangulo = bate.get_rect()
bateRectangulo1 = bate1.get_rect()
# Pongo el bate en el centro de la pantalla
pelotaRectangulo.move_ip(tamanio[0]/2,tamanio[1]/2)
bateRectangulo.move_ip(tamanio[0]/5,tamanio[1]/2)
bateRectangulo1.move_ip(tamanio[0]*4/5,tamanio[1]/2)
# Comenzamos el bucle del juego
corriendo=True
while corriendo:
    # Espero un tiempo (milisegundos) para que la pelota no vaya muy rápida
    pygame.time.delay(3)
    # Capturamos los eventoos que se han producido
    for evento in pygame.event.get():
        #Si el eventoo es salir de la ventana, terminamos
        if evento.type == pygame.QUIT: corriendo = False
    # Compruebo si se ha pulsado alguna tecla
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w]:
        bateRectangulo = bateRectangulo.move(0, -1)
    if teclas[pygame.K_s]:
        bateRectangulo = bateRectangulo.move(0, 1)
    # Compruebo si hay colisión
    if bateRectangulo.colliderect(pelotaRectangulo) or bateRectangulo1.colliderect(pelotaRectangulo):
        velocidad[0] = - velocidad[0]
    if teclas[pygame.K_UP]:
        bateRectangulo1=bateRectangulo1.move(0, -1)
    if teclas[pygame.K_DOWN]:
        bateRectangulo1=bateRectangulo1.move(0, 1)
    # Muevo la pelota
    pelotaRectangulo = pelotaRectangulo.move(velocidad)
    # Compruebo si la pelota llega a los límites de la ventana
    if pelotaRectangulo.left < 0 or pelotaRectangulo.right > ancho:
        velocidad[0] = -velocidad[0]
    if pelotaRectangulo.top < 0 or pelotaRectangulo.bottom > altura:
        velocidad[1] = -velocidad[1]
    # Pinto el fondo de blanco, dibujo la pelota y actualizo la pantalla
    pantalla.fill(negro)
    #pantalla.blit(fondo, [0, 40])
    pantalla.blit(pelota, pelotaRectangulo)
    pantalla.blit(bate1, bateRectangulo1)
    pantalla.blit(bate, bateRectangulo)

    pygame.display.flip()
# Salgo de pygame
pygame.quit()
