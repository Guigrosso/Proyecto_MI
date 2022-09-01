import sys, pygame, time, os, random

#Este comentario solo sirve para hacer doble clic y buscar la palabra para editar 
#png

# Inicializamos pygame
pygame.init()

# Muestro una ventana de 800x600
tamanio = 800, 600
pantalla = pygame.display.set_mode(tamanio)

# Genero el contador

def draw_text(surface, text, size, x,y):
    font = pygame.font.SysFont("serif", size)
    text_surface = font.render(text,True, blanco)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surface.blit(text_surface, text_rect)
    
# Cambio el título de la ventana
pygame.display.set_caption("Juego pelota")

# Inicializamos variables
ancho, altura = tamanio
velocidad = 4
velocidadPelota = [velocidad, velocidad]
velocidadBate = [velocidad, velocidad]
velocidadBate1 = [velocidad, velocidad]
blanco = 255, 255, 255
negro = 0, 0, 0
fondo = pygame.image.load("fondo.png")
contador1 = 0
contador2 = 0

# Crea un objeto imagen pelota y obtengo su rectángulo
pelota = pygame.image.load("pelotaN.png")


pelotaRectangulo = pelota.get_rect()


# Crea un objeto imagen bate y obtengo su rectángulo
bate1 = pygame.image.load("botin.png")
bate = pygame.image.load("botin1.png")
bateRectangulo = bate.get_rect()
bategrande = pygame.image.load("bategrande.png")
bate1Rectangulo = bate1.get_rect() 

#Bloques

# Creo Bloques
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
    
    
#Ubico los bloques en la pantalla
espacio = 50
for i in range(0,int(cantBloques/2)):
    bloqueRect1[i].move_ip(tamanio[0]/16-espacio,tamanio[1]/(cantBloques/2+1)*i+espacio)    
    bloqueRect1[int(i+cantBloques/2)].move_ip(tamanio[0]*2/16-espacio,tamanio[1]/(cantBloques/2+1)*i+espacio)    
    bloqueRect2[i].move_ip(tamanio[0]*15/16,tamanio[1]/(cantBloques/2+1)*i+espacio)    
    bloqueRect2[int(i+cantBloques/2)].move_ip(tamanio[0]*14/16,tamanio[1]/(cantBloques/2+1)*i+espacio)



# Creo poder de bate
batePRect = bategrande.get_rect()



# Pongo el bate en el centro de la pantalla
pelotaRectangulo.move_ip(tamanio[0]/2,tamanio[1]/2)
bateRectangulo.move_ip(tamanio[0]/4,tamanio[1]/2)
bate1Rectangulo.move_ip(tamanio[0]*3/4,tamanio[1]/2)
batePRect.move_ip(tamanio[0]*3/4,tamanio[1]/2)

# Comenzamos el bucle del juego
corriendo = True
while corriendo:
    
    # Espero un tiempo (milisegundos) para que la pelota no vaya muy rápida
    pygame.time.delay(2)
    
    # Capturamos los eventos que se han producido
    for evento in pygame.event.get():
        #Si el eventoo es salir de la ventana, terminamos
        if evento.type == pygame.QUIT: corriendo = False
        
    # Compruebo si se ha pulsado alguna tecla
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w]:
        bate1Rectangulo=bate1Rectangulo.move(0, -velocidadBate1[1])
        batePRect=batePRect.move(0, -velocidadBate1[1])
    if teclas[pygame.K_s]:
        bate1Rectangulo=bate1Rectangulo.move(0, velocidadBate1[1])
        batePRect=batePRect.move(0, velocidadBate1[1])
    
    
    #Descomentar lo siguiente para comentar las colisiones
    #'''
    
    # Colisiones
    if bateRectangulo.colliderect(pelotaRectangulo) or bate1Rectangulo.colliderect(pelotaRectangulo):
        velocidadPelota[0] = - velocidadPelota[0]
        
    if teclas[pygame.K_UP]:
        bateRectangulo=bateRectangulo.move(0, -velocidadBate[1])
    
    if teclas[pygame.K_DOWN]:
        bateRectangulo=bateRectangulo.move(0, velocidadBate[1])
    
    for i in range(0,cantBloques):
        if bloqueRect1[i].colliderect(pelotaRectangulo):
            velocidadPelota[0] = - velocidadPelota[0]
            bloqueRect1[i].move_ip(tamanio[0],tamanio[0])
            contador1 += 1
        
        if bloqueRect2[i].colliderect(pelotaRectangulo):
            velocidadPelota[0] = - velocidadPelota[0]
            bloqueRect2[i].move_ip(tamanio[0],tamanio[0])
            contador2 += 1
    
    #'''    
    
    
    
    # Muevo la pelota
    pelotaRectangulo = pelotaRectangulo.move(velocidadPelota)
    
    # Compruebo si la pelota llega a los límites de la ventana
    if pelotaRectangulo.left < 0 or pelotaRectangulo.right > ancho:
        velocidadPelota[0] = -velocidadPelota[0]
    if pelotaRectangulo.top < 0 or pelotaRectangulo.bottom > altura:
        velocidadPelota[1] = -velocidadPelota[1]
    
    # Compruebo si los bates llegan a los límites de la ventana
    if bate1Rectangulo.left < 0 or bate1Rectangulo.right > ancho:
        velocidadBate[0] = -velocidadBate[0]
    if (bate1Rectangulo.top or batePRect.top) < 0:
        bate1Rectangulo.top = velocidadBate1[1]-velocidadBate1[1]
        batePRect.top = velocidadBate1[1]-velocidadBate1[1]
    if (bate1Rectangulo.bottom or batePRect.bottom) > altura:
        bate1Rectangulo.bottom = bate1Rectangulo.bottom - velocidadBate1 [1]
        batePRect.bottom = batePRect.bottom - velocidadBate1 [1]
        
    if bateRectangulo.left < 0 or bateRectangulo.right > ancho:
        velocidadBate[0] = -velocidadBate[0]
    if bateRectangulo.top < 0:
        bateRectangulo.top = velocidadBate[1]-velocidadBate[1]
    if bateRectangulo.bottom > altura:
        bateRectangulo.bottom = bateRectangulo.bottom - velocidadBate [1]
    if contador1 ==1:
        if bate1Rectangulo.colliderect(pelotaRectangulo):
            velocidadPelota = [0,0]
            if teclas[pygame.K_w]:
                pelotaRectangulo=pelotaRectangulo.move(0, -velocidadBate1[1])
            if teclas[pygame.K_s]:
                pelotaRectangulo=pelotaRectangulo.move(0, velocidadBate1[1])
            if teclas [pygame.K_q]:
                velocidadPelota = [velocidad, velocidad]
    if contador1 == 2:
        
        bate1 = bategrande
        bate1Rectangulo = batePRect
        
        velocidadBate = [0,0]
        
        # for i in range(1,6):
          #  time.sleep(1)
           # print(i)
            #if (i==5):
             #   velocidadBate = [velocidad, velocidad]
         
    
            
        
    # Pinto el fondo de blanco, dibujo la pelota y actualizo la pantalla
    pantalla.fill(negro)
    pantalla.blit(fondo, [0, 40])
    pantalla.blit(pelota, pelotaRectangulo)
    pantalla.blit(bate1, bate1Rectangulo)
    pantalla.blit(bate, bateRectangulo)
    for i in range(0,cantBloques):
        pantalla.blit(bloques1[i], bloqueRect1[i])
        pantalla.blit(bloques2[i], bloqueRect2[i])
    
    
            
        
    
    #muestro contadores    
    draw_text(pantalla,str(contador1), 40, tamanio[0]/6*5, 20)
    draw_text(pantalla,str(contador2), 40, tamanio[0]/6, 20)
    
    pygame.display.flip()
    
# Salgo de pygame
pygame.quit()