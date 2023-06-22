import pygame
from tkinter import *
from tkinter import ttk

# Configuración de la ventana Tkinter
root = Tk()
root.title("Simulación de caída libre")

# Variables
velocidad_inicial = 0
tiempo = 0
gravedad = 9.8
altura = 0
movimiento = False

# Función para iniciar la simulación
def iniciar_simulacion():
    global velocidad_inicial, tiempo, gravedad, altura, movimiento
    velocidad_inicial = float(entry_velocidad.get())
    tiempo = 0
    altura = 0
    movimiento = True

# Función para detener la simulación
def detener_simulacion():
    global movimiento
    movimiento = False

# Función para actualizar la altura y el tiempo en cada iteración de la simulación
def actualizar_simulacion():
    global velocidad_inicial, tiempo, gravedad, altura
    tiempo += 0.1
    altura = velocidad_inicial * tiempo - 0.5 * gravedad * tiempo**2

# Función para dibujar la simulación en la ventana de pygame
def dibujar_simulacion():
    pygame.draw.circle(screen, (255, 255, 255), (250, int(250 - altura)), 10)  # Dibujar la bola
    pygame.display.flip()

# Función para manejar los eventos de cierre de la ventana de pygame
def cerrar_ventana():
    pygame.quit()

# Configuración de la ventana de pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Simulación de caída libre")
clock = pygame.time.Clock()

# Configuración de la ventana Tkinter
frame = ttk.Frame(root, padding="20")
frame.grid()

# Etiquetas y campos de entrada
label_velocidad = ttk.Label(frame, text="Velocidad inicial:")
label_velocidad.grid(column=0, row=0)
entry_velocidad = ttk.Entry(frame)
entry_velocidad.grid(column=1, row=0)

# Botón de iniciar simulación
boton_iniciar = ttk.Button(frame, text="Iniciar simulación", command=iniciar_simulacion)
boton_iniciar.grid(column=0, row=1)

# Botón de detener simulación
boton_detener = ttk.Button(frame, text="Detener simulación", command=detener_simulacion)
boton_detener.grid(column=1, row=1)

# Bucle principal
while True:
    root.update()  # Actualizar la ventana Tkinter
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cerrar_ventana()

    if movimiento and tiempo < 2 * velocidad_inicial / gravedad:
        actualizar_simulacion()
        screen.fill((0, 0, 0))  # Limpiar la pantalla antes de dibujar la siguiente posición
        dibujar_simulacion()
        clock.tick(60)  # Limitar el número de fotogramas por segundo


