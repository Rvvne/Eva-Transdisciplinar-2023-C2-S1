import tkinter as tk
import time
import matplotlib.pyplot as plt

# Dimensiones de la ventana
ANCHO = 800
ALTO = 600

# Aceleración debido a la gravedad
GRAVEDAD = 9.8

class Pelota:
    def __init__(self, lienzo, velocidad, alturas, vel_inicial, tiempos):
        self.lienzo = lienzo
        self.radio = 20
        self.x = ANCHO // 2
        self.y = 0
        self.velocidad = velocidad
        self.tiempo_inicio = None
        self.alturas = alturas
        self.vel_inicial = vel_inicial
        self.tiempos = tiempos
        self.dibujar()

    def dibujar(self):
        self.lienzo.create_oval(self.x - self.radio, self.y - self.radio, self.x + self.radio, self.y + self.radio, fill="red", outline="white", width=2)

    def actualizar(self):
        if self.tiempo_inicio is None:
            self.tiempo_inicio = time.time()

        tiempo_actual = time.time()
        tiempo_transcurrido = tiempo_actual - self.tiempo_inicio

        self.y = -1 * (self.vel_inicial * tiempo_transcurrido - 0.5 * GRAVEDAD * tiempo_transcurrido ** 2)
        self.alturas.append(self.y)
        self.velocidad = -(self.vel_inicial - GRAVEDAD * tiempo_transcurrido)
        self.tiempos.append(tiempo_transcurrido)

        if self.y >= ALTO - self.radio:
            self.y = ALTO - self.radio
            self.detener()

        self.lienzo.delete("all")
        self.dibujar()

    def detener(self):
        app.en_ejecucion = False
        app.actualizar_botones()
        plt.figure()
        plt.plot(self.tiempos, self.alturas, label="Altura")
        plt.xlabel("Tiempo (s)")
        plt.ylabel("Altura (m)")
        plt.title("Caída Libre")
        plt.legend()
        plt.gca().invert_yaxis()  # Invertir eje Y para mostrar caída libre hacia abajo
        plt.show()


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Caída Libre")

        self.lienzo = tk.Canvas(self.root, width=ANCHO, height=ALTO, bg="#0D47A1")
        self.lienzo.pack(side=tk.LEFT)

        self.marco = tk.Frame(self.root, bg="#E3F2FD", padx=20, pady=20)
        self.marco.pack(side=tk.LEFT)

        self.velocidad = 0
        self.pelota = None
        self.alturas = []
        self.vel_inicial = 0
        self.tiempos = []

        self.etiqueta_velocidad = tk.Label(self.marco, text="Velocidad: 0 m/s", font=("Arial", 12), bg="#E3F2FD", fg="#1A237E")
        self.etiqueta_velocidad.pack()

        self.etiqueta_altura = tk.Label(self.marco, text="Altura: 0 m", font=("Arial", 12), bg="#E3F2FD", fg="#1A237E")
        self.etiqueta_altura.pack()

        self.etiqueta_tiempo = tk.Label(self.marco, text="Tiempo: 0 s", font=("Arial", 12), bg="#E3F2FD", fg="#1A237E")
        self.etiqueta_tiempo.pack()

        self.entrada_velocidad = tk.Entry(self.marco, font=("Arial", 12))
        self.entrada_velocidad.pack()
        self.boton_velocidad = tk.Button(self.marco, text="Ajustar Velocidad", command=self.ajustar_velocidad, bg="#1565C0", fg="white")
        self.boton_velocidad.pack()

        self.entrada_altura = tk.Entry(self.marco, font=("Arial", 12))
        self.entrada_altura.pack()
        self.boton_altura = tk.Button(self.marco, text="Ajustar Altura", command=self.ajustar_altura, bg="#1565C0", fg="white")
        self.boton_altura.pack()

        self.entrada_tiempo = tk.Entry(self.marco, font=("Arial", 12))
        self.entrada_tiempo.pack()
        self.boton_tiempo = tk.Button(self.marco, text="Ajustar Tiempo", command=self.ajustar_tiempo, bg="#1565C0", fg="white")
        self.boton_tiempo.pack()

        self.boton_inicio = tk.Button(self.marco, text="Iniciar", command=self.iniciar, bg="#4CAF50", fg="white")
        self.boton_inicio.pack(side=tk.LEFT)

        self.boton_detener = tk.Button(self.marco, text="Detener", command=self.detener, bg="#F44336", fg="white", state=tk.DISABLED)
        self.boton_detener.pack(side=tk.LEFT)

    def ajustar_velocidad(self):
        self.vel_inicial = -1 * float(self.entrada_velocidad.get())
        if self.pelota is not None:
            self.pelota.vel_inicial = self.vel_inicial
        self.etiqueta_velocidad.config(text="Velocidad: {:.2f} m/s".format(self.vel_inicial))

    def ajustar_altura(self):
        altura = -1 * float(self.entrada_altura.get())
        if self.pelota is not None:
            self.pelota.y = altura
        self.etiqueta_altura.config(text="Altura: {:.2f} m".format(altura))

    def ajustar_tiempo(self):
        self.tiempo_inicio = time.time() - float(self.entrada_tiempo.get())
        self.etiqueta_tiempo.config(text="Tiempo: {:.2f} s".format(float(self.entrada_tiempo.get())))

    def iniciar(self):
        if self.pelota is None:
            self.pelota = Pelota(self.lienzo, self.velocidad, self.alturas, self.vel_inicial, self.tiempos)
        self.en_ejecucion = True
        self.actualizar_botones()
        self.actualizar()

    def detener(self):
        if self.pelota is not None:
            self.pelota.detener()
        self.en_ejecucion = False
        self.actualizar_botones()

    def actualizar_botones(self):
        if self.en_ejecucion:
            self.boton_inicio.config(state=tk.DISABLED)
            self.boton_detener.config(state=tk.NORMAL)
        else:
            self.boton_inicio.config(state=tk.NORMAL)
            self.boton_detener.config(state=tk.DISABLED)

    def actualizar(self):
        if self.en_ejecucion:
            self.pelota.actualizar()
            self.actualizar_etiquetas()
            self.root.after(10, self.actualizar)

    def actualizar_etiquetas(self):
        if self.pelota is not None:
            self.etiqueta_velocidad.config(text="Velocidad: {:.2f} m/s".format(self.pelota.velocidad))
            self.etiqueta_altura.config(text="Altura: {:.2f} m".format(self.pelota.y))
            tiempo_actual = time.time()
            tiempo_transcurrido = tiempo_actual - self.pelota.tiempo_inicio
            self.etiqueta_tiempo.config(text="Tiempo: {:.2f} s".format(tiempo_transcurrido))

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()


