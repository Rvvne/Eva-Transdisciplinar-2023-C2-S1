import pygame

# Dimensiones de la ventana
WIDTH = 800
HEIGHT = 600

# Constantes de la física
GRAVITY = 9.8  # Aceleración debido a la gravedad en m/s^2

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Caida Libre")

clock = pygame.time.Clock()

def caida_libre():
    # Parámetros de la pelota
    peso = 1.0  # Peso de la pelota en kg
    altura = 50  # Altura inicial de la pelota
    tiempo = 0.0  # Tiempo transcurrido
    velocidad = 0.0  # Velocidad inicial de la pelota

    font = pygame.font.Font(None, 24)  # Fuente para mostrar los datos

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Calcular la posición y velocidad de la pelota
        altura += velocidad * 0.1  # Actualizar la altura según la velocidad
        velocidad += GRAVITY * 0.1  # Actualizar la velocidad según la aceleración

        # Limpiar la pantalla
        screen.fill(BLACK)

        # Dibujar la pelota en su posición actual
        pygame.draw.circle(screen, RED, (WIDTH // 2, int(altura)), 10)

        # Mostrar los datos en la ventana
        tiempo_texto = font.render("Tiempo: {:.1f}".format(tiempo), True, WHITE)
        altura_texto = font.render("Altura: {:.1f}".format(altura), True, WHITE)
        velocidad_texto = font.render("Velocidad: {:.1f}".format(velocidad), True, WHITE)
        screen.blit(tiempo_texto, (10, 10))
        screen.blit(altura_texto, (10, 40))
        screen.blit(velocidad_texto, (10, 70))

        # Actualizar la ventana
        pygame.display.flip()

        # Actualizar el tiempo
        tiempo += 0.1

        clock.tick(60)  # Limitar el número de frames por segundo

        # Si la pelota toca el suelo, detener la simulación
        if altura >= HEIGHT - 10:
            break

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Mostrar los datos finales en la ventana
        tiempo_texto = font.render("Tiempo: {:.1f}".format(tiempo), True, WHITE)
        altura_texto = font.render("Altura: {:.1f}".format(altura), True, WHITE)
        velocidad_texto = font.render("Velocidad: {:.1f}".format(velocidad), True, WHITE)
        screen.blit(tiempo_texto, (10, 10))
        screen.blit(altura_texto, (10, 40))
        screen.blit(velocidad_texto, (10, 70))

        # Actualizar la ventana
        pygame.display.flip()

        clock.tick(60)  # Limitar el número de frames por segundo

# Ejecutar la función caida_libre()
caida_libre()


