"""
Programa que imprima los número enteros entre 0 y 100 de forma ascendente y descendente.
Autor: Christian Zambrano
Fecha: Diciembre 6 de 2023
"""

#CICLO FOR
#Cree un programa que imprima los números enteros entre 0 y 100 en orden ascendente y descendente.

print("Números en orden ascendente:")
for i in range(101):
    print(i, end=' ')

print("\n")

print("Números en orden descendente:")
for i in range(100, -1, -1):
    print(i, end=' ')
