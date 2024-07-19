# Escribir un programa que lea un entero positivo, introducido por el usuario y después
# muestre en pantalla la suma de todos los enteros desde 1. 

def suma_enteros(n):
    return n * (n + 1) // 2  # "//" para asegurar que el resultado sea un entero

# introduzca un entero positivo
try:
    numero = int(input("Introduce un entero positivo: "))
    
    if numero <= 0:
        print("Por favor, introduce un número entero positivo.")
    else:
        resultado = suma_enteros(numero)
        print(f"La suma de todos los enteros desde 1 hasta {numero} es: {resultado}")

except ValueError:
    print("Entrada no válida. Por favor, introduce un número entero.")