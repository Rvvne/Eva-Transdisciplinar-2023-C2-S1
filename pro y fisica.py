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
color1= 100, 100, 100
color2= 0, 0, 0
color3= 210, 180, 140

# Crear una ventana de Tkinter oculta para los botones
root = tk.Tk()
root.withdraw()

# Función para mostrar un mensaje con Tkinter
def show_message_box():
    messagebox.showinfo("INSERTE DATOS", "DATOS ANOTADOS")

# Definir las dimensiones de las secciones
seccion1_ancho = ancho // 2
seccion2_ancho = 350
alto1= 350

# Crear superficies para las secciones
lado_iz = pygame.Surface((seccion1_ancho, alto))
lado_der = pygame.Surface((seccion2_ancho, alto1))

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Cambiar el color de fondo de las secciones
    lado_iz.fill(color3)
    lado_der.fill(color3)

    # Crear un rectángulo para el botón en la sección 1
    boton1= pygame.Rect(50, 150, 100, 50)
    pygame.draw.rect(lado_iz, (255, 255, 255), boton1)

        
    boton2= pygame.Rect(200,150 , 100, 50)
    pygame.draw.rect(lado_iz, (255, 255, 255), boton2)
    
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

    # Obtener las coordenadas del ratón
    mouse_pos = pygame.mouse.get_pos()

    # Verificar si el ratón está sobre el botón en la sección 1 y si se hace clic
    if boton1.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
        show_message_box()
    if boton2.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
        show_message_box()

    # Copiar las superficies de las secciones en la ventana principal
    ventana.blit(lado_iz, (0, 0))
    ventana.blit(lado_der,(seccion1_ancho, alto1))

    # Actualizar la pantalla
    pygame.display.flip()

# Cerrar pygame y Tkinter al finalizar
pygame.quit()
root.destroy()