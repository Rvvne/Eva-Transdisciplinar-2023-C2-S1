import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Posición inicial del objeto
x = width // 2
y = 0

# Velocidad y aceleración
speed = 0
acceleration = 0.5

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Actualizar la posición y la velocidad
    y += speed
    speed += acceleration

    # Limpiar la pantalla
    screen.fill((0, 0, 0))

    # Dibujar el objeto
    pygame.draw.circle(screen, (255, 255, 255), (x, int(y)), 20)

    # Actualizar la pantalla
    pygame.display.flip()

    # Establecer la velocidad de fotogramas
    clock.tick(60)
