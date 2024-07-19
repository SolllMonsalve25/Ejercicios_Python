#Un Freelancer desea saber cuánto puede cobrar por su trabajo semanal y mensualmente, para ello 
# solo necesita establecer el precio de su trabajo por hora. Se estiman 40 horas de trabajo a la semana.

# Función para calcular el salario semanal y mensual
def calcular_salario(precio_por_hora):
    horas_semanales = 40  # Horas de trabajo a la semana
    semanas_mensuales = 4  # Aproximación de semanas en un mes

    salario_semanal = precio_por_hora * horas_semanales
    salario_mensual = salario_semanal * semanas_mensuales
    
    return salario_semanal, salario_mensual

try:
    precio_por_hora = float(input("Introduzca el precio por hora: "))
    
    if precio_por_hora < 0:
        print("Por favor, introduzca un número positivo para el precio por hora.")
    else:
        salario_semanal, salario_mensual = calcular_salario(precio_por_hora)
        print(f"Su salario semanal es: ${salario_semanal:.2f}")
        print(f"Su salario mensual es: ${salario_mensual:.2f}")

except ValueError:
    print("Entrada no válida. Digite un numero")