from socket import NI_NUMERICHOST
import sys, pygame, time, os, random

def draw_text(surface, text, size, x, y):
    font = pygame.font.SysFont("serif", size)
    text_surface = font.render(text,True, blanco)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surface.blit(text_surface, text_rect)

#Este comentario solo sirve para hacer doble clic y buscar la palabra para editar 
#png

# Inicializamos pygame
pygame.init()



# Pantalla

# Muestro una ventana de 800x600
tamanio = 800, 600
ancho, altura = tamanio
pantalla = pygame.display.set_mode(tamanio)
fondo = pygame.image.load("fondo.png")
    
# Cambio el título de la ventana
pygame.display.set_caption("LOS ROMPE-PELOTAS")

# Inicializamos variables de velocidades
velocidad = 4
velocidadPelota = [velocidad, velocidad]
velocidadBate1 = [velocidad, velocidad]
velocidadBate2 = [velocidad, velocidad]

# Atajo de colores
blanco = 255, 255, 255
negro = 0, 0, 0

# Contadores
contador1 = 0
contador2 = 0

# Pelota
pelota = pygame.image.load("pelotaN.png")
pelotaRectangulo = pelota.get_rect()

# Bates
bate1 = pygame.image.load("botin1.png")
bate2 = pygame.image.load("botin.png")
bate1Rectangulo = bate1.get_rect()
bate2Rectangulo = bate2.get_rect() 
bategrande = pygame.image.load("bategrande.png")
batePRect = bategrande.get_rect()

# Bloques
cantBloques = 10
bloques1 = []
bloqueRect1 = []
bloques2 = []
bloqueRect2 = []
for i in range(0,cantBloques):
    bloques1.append(pygame.image.load("bloquemediano.png"))
    bloqueRect1.append(bloques1[i].get_rect())
    bloques2.append(pygame.image.load("bloquemediano.png"))
    bloqueRect2.append(bloques2[i].get_rect())
    
    
    
# UBICACION DE OBJETOS EN PANTALLA


# Pelota
pelotaRectangulo.move_ip(tamanio[0]/2,tamanio[1]/2)

# Bates
bate1Rectangulo.move_ip(tamanio[0]/4,tamanio[1]/2)
bate2Rectangulo.move_ip(tamanio[0]*3/4,tamanio[1]/2)
batePRect.move_ip(tamanio[0]*3/4,tamanio[1]/2)

# Bloques
espacio = 50
for i in range(0,int(cantBloques/2)):
    bloqueRect1[i].move_ip(tamanio[0]/16-espacio,tamanio[1]/(cantBloques/2+1)*i+espacio)    
    bloqueRect1[int(i+cantBloques/2)].move_ip(tamanio[0]*2/16-espacio,tamanio[1]/(cantBloques/2+1)*i+espacio)    
    bloqueRect2[i].move_ip(tamanio[0]*15/16,tamanio[1]/(cantBloques/2+1)*i+espacio)    
    bloqueRect2[int(i+cantBloques/2)].move_ip(tamanio[0]*14/16,tamanio[1]/(cantBloques/2+1)*i+espacio)


# JUEGO

corriendo = True

while corriendo:    
    # Espero un tiempo (milisegundos) para que no crashee
    pygame.time.delay(2)
    
    # Salida del juego
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: corriendo = False
    
    # MOVIMIENTOS
    
    # Movimiento de la pelota
    pelotaRectangulo = pelotaRectangulo.move(velocidadPelota)
    
    # Movimiento de los bates
    teclas = pygame.key.get_pressed()
    
    # Bate 1
    if teclas[pygame.K_w]:
        bate1Rectangulo = bate1Rectangulo.move(0, -velocidadBate1[1])
    if teclas[pygame.K_s]:
        bate1Rectangulo = bate1Rectangulo.move(0, velocidadBate1[1])
        
    # Bate 2
    if teclas[pygame.K_UP]:
        batePRect = batePRect.move(0, -velocidadBate2[1])
        bate2Rectangulo = bate2Rectangulo.move(0, -velocidadBate2[1])    
    if teclas[pygame.K_DOWN]:
        batePRect = batePRect.move(0, velocidadBate2[1])
        bate2Rectangulo = bate2Rectangulo.move(0, velocidadBate2[1])
    
    # Límites de movimiento
    
    # Compruebo si la pelota llega a los límites de la ventana
    if pelotaRectangulo.left <= 0 or pelotaRectangulo.right >= ancho:
        velocidadPelota[0] = -velocidadPelota[0]
    if pelotaRectangulo.top <= 0 or pelotaRectangulo.bottom >= altura:
        velocidadPelota[1] = -velocidadPelota[1]
    
    # Compruebo si los bates llegan a los límites de la ventana
    if bate1Rectangulo.top <= 0:
        bate1Rectangulo.top = 0
    if bate1Rectangulo.bottom >= altura:
        bate1Rectangulo.bottom = altura
    
    if bate2Rectangulo.top <= 0:
        bate2Rectangulo.top = 0
    if bate2Rectangulo.bottom >= altura:
        bate2Rectangulo.bottom = altura
    
    if batePRect.top <= 0:
        batePRect.top = 0
    if batePRect.bottom >= altura:
        batePRect.bottom = altura
    
    
    
    # Descomentar lo siguiente para comentar las colisiones
    #'''
    
    # Colisiones
    
    # Colisiones de los bates
    if bate1Rectangulo.colliderect(pelotaRectangulo):
        velocidadPelota[0] = - velocidadPelota[0]
    
    if bate2Rectangulo.colliderect(pelotaRectangulo):
        velocidadPelota[0] = - velocidadPelota[0]

    
    # Colisiones con los bloques
    # ESTA ROTO ARREGLAR PARA QUE REBOTE BIEN
    for i in range(0,cantBloques):
        if bloqueRect1[i].colliderect(pelotaRectangulo):
            pygame.time.delay(2)
            if (bloqueRect1[i].top <= pelotaRectangulo.bottom) or (bloqueRect1[i].bottom >= pelotaRectangulo.top):
                velocidadPelota[1] = - velocidadPelota[1]
            if (bloqueRect1[i].left >= pelotaRectangulo.right) or (bloqueRect1[i].right <= pelotaRectangulo.left):
                velocidadPelota[0] = - velocidadPelota[0]
            bloqueRect1[i].move_ip(tamanio[0],tamanio[0])
            contador1 += 1
        
        if bloqueRect2[i].colliderect(pelotaRectangulo):
            pygame.time.delay(2)
            if (bloqueRect2[i].top <= pelotaRectangulo.bottom) or (bloqueRect2[i].bottom >= pelotaRectangulo.top):
                velocidadPelota[1] = - velocidadPelota[1]
            if (bloqueRect2[i].left >= pelotaRectangulo.right) or (bloqueRect2[i].right <= pelotaRectangulo.left):
                velocidadPelota[0] = - velocidadPelota[0]
            bloqueRect2[i].move_ip(tamanio[0],tamanio[0])
            contador2 += 1
    
    #'''    
    
    
    
    
    
    
    
    #Poderes
    
    '''
    if contador1 ==1:
        if bate2Rectangulo.colliderect(pelotaRectangulo):
            velocidadPelota = [0,0]
            if (pelotaRectangulo.top) < 0:
                pelotaRectangulo.top = 0
            if pelotaRectangulo.bottom >= altura:
                pelotaRectangulo.bottom = altura
            if teclas[pygame.K_w]:
                pelotaRectangulo=pelotaRectangulo.move(0, -velocidadBate1[1])
            if teclas[pygame.K_s]:
                pelotaRectangulo=pelotaRectangulo.move(0, velocidadBate1[1])
            if teclas [pygame.K_q]:
                velocidadPelota = [velocidad, velocidad]
    '''
    
    if contador1 >= 2:
        
        
        def temporizador():
            numero = 5
            for i in range (1,numero):
                time.sleep(1)
                numero -= 1
                if (numero == 1):
                    numero =1
            return numero
    
        bate2 = bategrande
        bate2Rectangulo = batePRect
        
        velocidadBate1 = [0,0]
        if temporizador() == 1:
            velocidadBate1 = [velocidad, velocidad]
    
            
        
    # Pinto el fondo de blanco, dibujo la pelota y actualizo la pantalla
    pantalla.fill(negro)
    pantalla.blit(fondo, [0, 40])
    pantalla.blit(pelota, pelotaRectangulo)
    pantalla.blit(bate1, bate1Rectangulo)
    pantalla.blit(bate2, bate2Rectangulo)
    for i in range(0,cantBloques):
        pantalla.blit(bloques1[i], bloqueRect1[i])
        pantalla.blit(bloques2[i], bloqueRect2[i])
        
    # Muestro contadores    
    draw_text(pantalla,str(contador1), 40, tamanio[0]/6*5, 20)
    draw_text(pantalla,str(contador2), 40, tamanio[0]/6, 20)
    
    pygame.display.flip()
    
# Salgo de pygame
pygame.quit()