import pygame
from pygame.locals import *
import tkinter as tk
from tkinter import messagebox

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
ancho = 700
alto = 700
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Caida libre")

# Cambia el color de la ventana
color1 = 100, 100, 100
color2 = 0, 0, 0

# Crear una ventana de Tkinter oculta para los botones
root = tk.Tk()
root.withdraw()

# Función para mostrar un mensaje con Tkinter
def show_message_box():
    messagebox.showinfo("INSERTE DATOS", "DATOS ANOTADOS")

# Definir las dimensiones de las secciones
seccion1_ancho = ancho // 2
seccion2_ancho = ancho // 2
seccion_alto = alto

# Crear superficies para las secciones
lado_iz = pygame.Surface((seccion1_ancho, seccion_alto))
lado_der = pygame.Surface((seccion2_ancho, seccion_alto))

# Función para dibujar los botones en la sección 1
def dibujar_botones1():
    # Crear un rectángulo para el botón en la sección 1
    boton1 = pygame.Rect(100, 100, 200, 50)
    pygame.draw.rect(lado_iz, (255, 255, 255), boton1)
    
    boton2 = pygame.Rect(100, 200, 200, 50)
    pygame.draw.rect(lado_iz, (255, 255, 255), boton2)
    if boton2.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        show_message_box()

    
    # Obtener las coordenadas del ratón
    mouse_pos = pygame.mouse.get_pos()

    # Verificar si el ratón está sobre el botón en la sección 1 y si se hace clic
    if boton1.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
        # Crear una ventana de Tkinter
        ventana_tk = tk.Toplevel()
        
        # Función para obtener el texto ingresado
        def obtener_texto():
            texto_ingresado = cuadro_texto.get()
            print("Texto ingresado:", texto_ingresado)
            ventana_tk.destroy()
        
        # Crear un cuadro de texto
        cuadro_texto = tk.Entry(ventana_tk)
        cuadro_texto.pack()

        # Crear un botón para obtener el texto ingresado
        boton_tk = tk.Button(ventana_tk, text="Ingrese aceleracion", command=obtener_texto)
        boton_tk.pack()

        # Ejecutar el bucle principal de Tkinter
        ventana_tk.mainloop()

# Función para actualizar la pantalla
def actualizar_pantalla():
    ventana.blit(lado_iz, (0, 0))
    ventana.blit(lado_der, (seccion1_ancho, 0))
    pygame.display.flip()

# Bucle principal del juego
def main_loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        # Cambiar el color de fondo de las secciones
        lado_iz.fill(color1)
        lado_der.fill(color2)

        # Dibujar los botones en cada sección
        dibujar_botones1()

        # Actualizar la pantalla
        actualizar_pantalla()

    # Cerrar pygame y Tkinter al finalizar
    pygame.quit()
    root.destroy()

# Ejecutar el bucle principal
if __name__ == "__main__":
    main_loop()