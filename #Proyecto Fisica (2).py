import pygame
from pygame.locals import *
import tkinter as tk
from tkinter import messagebox

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
ancho = 1200
alto = 700
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Caida libre")

# colores
color1 = (100, 100, 100)  # gris
color2 = (250, 250, 250)  # blanco
color3 = (210, 180, 140)  # beige
color4 = (0, 0, 0)  # negro

# Velocidad inicial y gravedad
speed = 0
gravity = 0.1

# Posición inicial de la pelota
x = 950
y = 0
clock = pygame.time.Clock()

# Ventana de Tkinter oculta para los botones
root = tk.Tk()
root.withdraw()

# Función para mostrar un mensaje con Tkinter
def show_message_box():
    messagebox.showinfo("INSERTE DATOS", "DATOS ANOTADOS")

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
    pygame.draw.circle(ventana, color1, (x, int(y)), 20)

# Bucle principal de la ventana
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    # Color de la ventana
    ventana.fill(color3)
    pygame.draw.line(ventana, color4, [720, 0], [720, 680], 2)
    # Objetos
    fondo1 = pygame.Rect(10, 25, 300, 65)
    pygame.draw.rect(ventana, color4, fondo1)
    
    fondo2 = pygame.Rect(50, 100 , 250, 250) #PRIMER CUADRO
    pygame.draw.rect(ventana, color4, fondo2)
    
    fondo3 = pygame.Rect(400, 25 , 250, 250) #SEGUNDO CUADRO
    pygame.draw.rect(ventana, color4, fondo3)
    
    fondo4 = pygame.Rect(50 ,400 , 250, 250) # TERCER CUADRO
    pygame.draw.rect(ventana, color4, fondo4)
    
    fondo5 = pygame.Rect(350, 330, 350, 350) # CUARTO CUCADRO
    pygame.draw.rect(ventana, color4, fondo5)
    
    boton1 = pygame.Rect(130, 193, 100, 50) #PRIMER BOTON
    pygame.draw.rect(ventana, color2, boton1)
    
    boton2 = pygame.Rect(480, 145, 100, 50) #SEGUNDO BOTON
    pygame.draw.rect(ventana, color2, boton2)
    
    boton3 = pygame.Rect(130, 493, 100, 50) #TERCER BOTON
    pygame.draw.rect(ventana, color2, boton3) 
    
    # Obtener las coordenadas del ratón
    mouse_pos = pygame.mouse.get_pos()

    # Verificar si el ratón está sobre el botón en la sección 1 y si se hace clic
    if boton1.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
        # Crear una ventana de Tkinter
        ventana_tk1 = tk.Toplevel()
        
        # Función para obtener el texto ingresado
        def obtener_texto1():
            texto1 = cuadro_texto1.get()
            print("Tiempo Ingresado:", texto1)
            ventana_tk1.destroy()
        
        # Crear un cuadro de texto
        cuadro_texto1 = tk.Entry(ventana_tk1)
        cuadro_texto1.pack()

        # Crear un botón para obtener el texto ingresado
        boton_tk1 = tk.Button(ventana_tk1, text="Ingresar Tiempo", command=obtener_texto1)
        boton_tk1.pack()

        # Ejecutar el bucle principal de Tkinter
        ventana_tk1.mainloop()
    
    if boton2.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
        # Crear una ventana de Tkinter
        ventana_tk2 = tk.Toplevel()
        
        # Función para obtener el texto ingresado
        def obtener_texto2():
            texto2 = cuadro_texto2.get()
            print("Altura ingresada:", texto2)
            ventana_tk2.destroy()
        
        # Crear un cuadro de texto
        cuadro_texto2 = tk.Entry(ventana_tk2)
        cuadro_texto2.pack()

        # Crear un botón para obtener el texto ingresado
        boton_tk2 = tk.Button(ventana_tk2, text="Ingrese Altura", command=obtener_texto2)
        boton_tk2.pack()

        # Ejecutar el bucle principal de Tkinter
        ventana_tk2.mainloop()
        
    if boton3.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
        # Crear una ventana de Tkinter
        ventana_tk3 = tk.Toplevel()
        
        # Función para obtener el texto ingresado
        def obtener_texto3():
            texto3 = cuadro_texto3.get()
            print("Tiempo ingresado:", texto3)
            ventana_tk3.destroy()
        
        # Crear un cuadro de texto
        cuadro_texto3 = tk.Entry(ventana_tk3)
        cuadro_texto3.pack()

        # Crear un botón para obtener el texto ingresado
        boton_tk3 = tk.Button(ventana_tk3, text="Ingrese Tiempo", command=obtener_texto3)
        boton_tk3.pack()

        # Ejecutar el bucle principal de Tkinter
        ventana_tk3.mainloop()

    # Obtener las coordenadas del ratón
    mouse_pos = pygame.mouse.get_pos()

    # Verificar si el ratón está sobre el botón en la sección 1 y si se hace clic
    if boton1.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
        show_message_box()
    if boton2.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
        show_message_box()
    if boton3.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
        show_message_box()

    # Dibujar texto en la ventana
    texto1 = titulo.render("CAIDA LIBRE", True, color2)
    ventana.blit(texto1, (10, 35)) 
    texto2 = tiempo1.render("Tiempo", True, color4) #Texto del Boton 1
    ventana.blit(texto2, (155, 210)) 
    texto3 = tiempo2.render("Altura", True, color4) #texto del Boton 2
    ventana.blit(texto3, (510, 168)) 
    texto3 = tiempo2.render("Tiempo", True, color4) #texto del Boton 3
    ventana.blit(texto3, (155, 510)) 
    texto4 = calculo1.render("CALCULO DE" , True, color2) #Texto del cuadro 1
    ventana.blit(texto4, (125, 120))
    texto44= calculo1.render('V = G * T', True, color2) # formula de la velocidad
    ventana.blit(texto44, (135,260))
    texto5 = calculo12.render("VELOCIDAD" , True, color2) #Texto del cuadro 1
    ventana.blit(texto5, (130, 143))
    texto4 = calculo1.render("CALCULO DE" , True, color2) #Texto del cuadro 2
    ventana.blit(texto4, (125, 420))
    texto55= calculo1.render('H = G * T² / 2', True, color2)#formula de la altura
    ventana.blit(texto55, (125,560))
    texto5 = calculo12.render("ALTURA" , True, color2) #Texto del cuadro 2
    ventana.blit(texto5, (147, 443))
    texto4 = calculo1.render("CALCULO DE" , True, color2) #Texto del cuadro 3
    ventana.blit(texto4, (475, 70))
    texto6=  calculo1.render('T = V * 2 * H / G', True, color2)# formula del tiempo
    ventana.blit(texto6, (475,210))
    texto5 = calculo12.render("TIEMPO" , True, color2) #Texto del cuadro 3
    ventana.blit(texto5, (495, 90))

    # Actualizar la pantalla
    update()
    draw_ball()
    pygame.display.flip()
    clock.tick(60)

# Cerrar pygame y Tkinter al finalizar
pygame.quit()
root.destroy()