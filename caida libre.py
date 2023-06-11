# Formula para la distancia en caida libre
def caida_libre(t,v): #tiempo y velocidad inicial
    g = 9.8  #gravedad
    d = v * g * t**2 # formula
    return d #distancia recorrida en metros

# datos
t = float(input("Ingrese el tiempo (En segundos): "))
v = float(input("Ingrese la Velocidad inical: "))
d = caida_libre(t,v)
print("La distancia recorrida en caída libre es:", d, "metros") # resultado final



