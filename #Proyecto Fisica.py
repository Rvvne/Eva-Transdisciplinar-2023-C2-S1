#Proyecto Fisica 

import pygame, tkinter
pygame.init()

#Ventana
res = (1200,680)
ventana = pygame.display.set_mode(res)
pygame.display.set_caption("Caida libre")

#Colores
GRAY  = (100, 100, 100)
WHITE = (250, 250, 250)
BEIGE = (210, 180, 140)
BLACK = (0,     0,   0)
BLUE  = (0,   174, 239)

# Velocidad inicial y gravedad
speed = 0
gravity = 0.1

# Posición inicial de la pelota
x = 950
y = 0
clock = pygame.time.Clock()

# Crear objeto de fuente
titulo = pygame.font.Font(None, 60)
calculo1 = pygame.font.Font(None, 25)
calculo12 = pygame.font.Font(None, 25)
tiempo1 = pygame.font.Font(None, 20)
tiempo2 = pygame.font.Font(None, 20)

#Pelota
def update():
    global speed, y
    speed += gravity
    y += speed

def draw_ball():
    pygame.draw.circle(ventana, BLUE, (x, int(y)), 20)

IOK = True
while IOK:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            IOK = False
    ventana.fill(BEIGE)
    
    pygame.draw.line(ventana, BLACK, [700, 0], [700, 680], 2)
    
    fondo1 = pygame.Rect(200, 25, 300, 65)
    pygame.draw.rect(ventana, BLACK, fondo1)
    
    fondo2 = pygame.Rect(50, 100 , 250, 250) #PRIMER CUADRO
    pygame.draw.rect(ventana, BLACK, fondo2)
    
    fondo3 = pygame.Rect(400, 100 , 250, 250) #SEGUNDO CUADRO
    pygame.draw.rect(ventana, BLACK, fondo3)
    
    fondo4 = pygame.Rect(50 ,400 , 250, 250)
    pygame.draw.rect(ventana, BLACK, fondo4)
    
    boton1 = pygame.Rect(130, 193, 100, 50) #PRIMER BOTON
    pygame.draw.rect(ventana, WHITE, boton1)
    
    boton2 = pygame.Rect(480, 193, 100, 50) #SEGUNDO BOTON
    pygame.draw.rect(ventana, WHITE, boton2)
    
    boton3 = pygame.Rect(130, 493, 100, 50)
    pygame.draw.rect(ventana, WHITE, boton3)
    # Dibujar texto en la ventana
    texto1 = titulo.render("CAIDA LIBRE", True, WHITE)
    ventana.blit(texto1, (215, 35)) 
    texto2 = tiempo1.render("Tiempo", True, BLACK) #Texto del Boton 1
    ventana.blit(texto2, (155, 210)) 
    texto3 = tiempo2.render("altura", True, BLACK) #texto del Boton 2
    ventana.blit(texto3, (510, 210)) 
    texto3 = tiempo2.render("Tiempo", True, BLACK) #texto del Boton 3
    ventana.blit(texto3, (155, 510)) 
    texto4 = calculo1.render("CALCULO DE" , True, WHITE) #Texto del cuadro 1
    ventana.blit(texto4, (125, 120))
    texto5 = calculo12.render("VELOCIDAD" , True, WHITE) #Texto del cuadro 1
    ventana.blit(texto5, (130, 143))
    texto4 = calculo1.render("CALCULO DE" , True, WHITE) #Texto del cuadro 2
    ventana.blit(texto4, (125, 420))
    texto5 = calculo12.render("ALTURA" , True, WHITE) #Texto del cuadro 2
    ventana.blit(texto5, (147, 443))
    texto4 = calculo1.render("CALCULO DE" , True, WHITE) #Texto del cuadro 3
    ventana.blit(texto4, (475, 120))
    texto5 = calculo12.render("TIEMPO" , True, WHITE) #Texto del cuadro 3
    ventana.blit(texto5, (495, 143))

    update()
    draw_ball()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()