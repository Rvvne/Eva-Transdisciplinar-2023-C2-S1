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

# colores
color1= 100, 100, 100
color2= 250, 250, 250
color3= 210, 180, 140
color4= 0, 0, 0

# Color de la venatana
ventana.fill(color2)

# Ventana de Tkinter oculta para los botones
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

# Crear objeto de fuente
titulo = pygame.font.Font(None, 60)
velocidad= pygame.font.Font(None, 20)
tiempo= pygame.font.Font(None, 20)

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Cambiar el color de fondo de las secciones
    lado_iz.fill(color3)
    lado_der.fill(color3)
    
    # Crea fondo del titulo
    fondo = pygame.Rect(30, 90, 290, 300)
    pygame.draw.rect(lado_iz, (0, 0, 0), fondo)
    
    # Crear un rectángulo para el botón en la sección 1
    boton1= pygame.Rect(50, 200, 100, 50)
    pygame.draw.rect(lado_iz, (225, 225, 225), boton1)

        
    boton2= pygame.Rect(200, 300, 100, 50)
    pygame.draw.rect(lado_iz, (225, 225, 225), boton2)
    
    # Obtener las coordenadas del ratón
    mouse_pos = pygame.mouse.get_pos()


    # Verificar si el ratón está sobre el botón en la sección 1 y si se hace clic
    if boton1.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
        # Crear una ventana de Tkinter
        ventana_tk1 = tk.Toplevel()
        
        # Función para obtener el texto ingresado
        def obtener_texto1():
            texto1 = cuadro_texto1.get()
            print("Texto ingresado:", texto1)
            ventana_tk1.destroy()
        
        # Crear un cuadro de texto
        cuadro_texto1 = tk.Entry(ventana_tk1)
        cuadro_texto1.pack()

        # Crear un botón para obtener el texto ingresado
        boton_tk1 = tk.Button(ventana_tk1, text="Ingrese Velocidad", command=obtener_texto1)
        boton_tk1.pack()

        # Ejecutar el bucle principal de Tkinter
        ventana_tk1.mainloop()
    
    if boton2.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
        # Crear una ventana de Tkinter
        ventana_tk2 = tk.Toplevel()
        
        # Función para obtener el texto ingresado
        def obtener_texto2():
            texto2 = cuadro_texto2.get()
            print("Texto ingresado:", texto2)
            ventana_tk2.destroy()
        
        # Crear un cuadro de texto
        cuadro_texto2 = tk.Entry(ventana_tk2)
        cuadro_texto2.pack()

        # Crear un botón para obtener el texto ingresado
        boton_tk2 = tk.Button(ventana_tk2, text="Ingrese tiempo", command=obtener_texto2)
        boton_tk2.pack()

        # Ejecutar el bucle principal de Tkinter
        ventana_tk2.mainloop()

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

    # Dibujar texto en la subsuperficie
    texto = titulo.render("CAIDA LIBRE", True, (color2))
    ventana.blit(texto, (40, 110)) 
    texto = velocidad.render("Velocidad", True, (color4))
    ventana.blit(texto, (70, 216)) 
    texto = tiempo.render("Tiempo", True, (color4))
    ventana.blit(texto, (205, 310)) 
    
    # Actualizar la pantalla
    pygame.display.flip()

# Cerrar pygame y Tkinter al finalizar
pygame.quit()
root.destroy()