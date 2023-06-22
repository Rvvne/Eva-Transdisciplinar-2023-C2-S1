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

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 10
        self.weight = 1.0
        self.velocity = 0.0

    def update(self, dt):
        self.y += self.velocity * dt + 0.5 * GRAVITY * dt**2
        self.velocity += GRAVITY * dt

    def draw(self):
        pygame.draw.circle(screen, RED, (self.x, int(self.y)), self.radius)

def caida_libre():
    ball = Ball(WIDTH // 2, HEIGHT // 20)

    font = pygame.font.Font(None, 24)  # Fuente para mostrar los datos

    tiempo = 0.0  # Tiempo transcurrido

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        dt = clock.tick(60) / 1000.0  # Tiempo transcurrido en segundos

        ball.update(dt)

        if ball.y >= HEIGHT - ball.radius:
            ball.y = HEIGHT - ball.radius
            ball.velocity = 0.0

        screen.fill(BLACK)
        ball.draw()

        tiempo_texto = font.render("Tiempo: {:.1f}".format(tiempo), True, WHITE)
        altura_texto = font.render("Altura: {:.1f}".format(ball.y), True, WHITE)
        velocidad_texto = font.render("Velocidad: {:.1f}".format(ball.velocity), True, WHITE)
        screen.blit(tiempo_texto, (10, 10))
        screen.blit(altura_texto, (10, 40))
        screen.blit(velocidad_texto, (10, 70))

        pygame.display.flip()

        tiempo += dt

caida_libre()

