# Programa que solicite al usuario los datos para calcular el área de un Triángulo (▲), 
# finalmente mostrar el resultado en pantalla

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2  # área del triángulo

# la base y la altura del triángulo
try:
    base = float(input("Introduce la longitud de la base del triángulo: "))
    altura = float(input("Introduce la altura del triángulo: "))
    
    if base <= 0 or altura <= 0:
        print("Por favor, introduce números positivos para la base y la altura.")
    else:
        area = calcular_area_triangulo(base, altura)
        print(f"El área del triángulo con base {base} y altura {altura} es: {area}")

except ValueError:
    print("Entrada no válida. Por favor, introduce números.")