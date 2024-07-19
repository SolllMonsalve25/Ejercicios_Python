#Programa que solicite al usuario los datos para calcular el área de un Círculo (●),
#finalmente mostrar el resultado en pantalla.

import math  #  para usar pi

# Función para calcular el área
def calcular_area_circulo(radio):
    return math.pi * (radio ** 2) 

#  radio del círculo
try:
    radio = float(input("Introduce el radio del círculo: "))
    
    if radio <= 0:
        print("Por favor, introduce un número positivo para el radio.")
    else:
        area = calcular_area_circulo(radio)
        print(f"El área del círculo con radio {radio} es: {area:.2f}")  # Mostramos el área con dos decimales

except ValueError:
    print("Entrada no válida. Por favor, introduce un número.")