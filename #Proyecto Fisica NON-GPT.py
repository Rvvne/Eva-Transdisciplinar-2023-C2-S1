#Proyecto Fisica NON-GPT

import pygame
import sys

# Configuración de la ventana
WIDTH = 800
HEIGHT = 600
FPS = 60

# Inicialización de Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Insertar Imágenes")
clock = pygame.time.Clock()

# Cargar imagen
image = pygame.image.load("obj.png")
image_rect = image.get_rect()
image_rect.center = (WIDTH // 2, HEIGHT // 2)

# Bucle principal del juego
running = True
while running:
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    # Dibujado en pantalla
    screen.fill((255, 255, 255))
    screen.blit(image, image_rect)

    # Actualización de la ventana
    pygame.display.flip()
    clock.tick(FPS)