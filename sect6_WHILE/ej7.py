"""
Programa que muestra el promedio de n números con brake 0
Autor: Christian Zambrano
Fecha: Diciembre 9 de 2023
"""

#Cree un programa que muestre el promedio de n números, dejándose de solicitar números cuando se
#introduzca el cero.

sum = 0
cont = 0

while True:
    n = float(input("Ingrese un número (0 para terminar): "))
    
    if n == 0:
        break 
    sum += n
    cont += 1

if cont == 0:
    print("No se ingresaron números.")
else:
    prom = sum / cont
    print(f"El promedio de los números ingresados es: {prom}")
