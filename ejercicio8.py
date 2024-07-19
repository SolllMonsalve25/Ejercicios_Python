# Programa que solicite al usuario los datos para llevar Grados Farenheit a Grados Celcius.

# convertir Fahrenheit a Celsius
def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9  # Fórmula de conversión


try:
    fahrenheit = float(input("Introduce la temperatura en grados Fahrenheit: "))
    
    # para convertir a Celsius
    celsius = fahrenheit_a_celsius(fahrenheit)
    print(f"{fahrenheit} grados Fahrenheit son {celsius:.2f} grados Celsius.")

except ValueError:
    print("Entrada no válida. Por favor, introduce un número.")