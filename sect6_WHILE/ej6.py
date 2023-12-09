"""
Programa que calcua el promedio de 10 números.
Autor: Christian Zambrano
Fecha: Diciembre 9 de 2023
"""

#Cree un programa que calcule el promedio de 10 números

sum = 0
cont = 0

while cont < 10:
    n = float(input("Ingrese un número: "))
    sum += n
    cont += 1

prom = sum / 10

print(f"El promedio de los 10 números es: {prom}")
