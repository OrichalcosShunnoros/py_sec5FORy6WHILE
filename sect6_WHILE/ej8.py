"""
Programa que muestra la suma de los cuadrados de los números entre 1 y n.
Autor: Christian Zambrano
Fecha: Diciembre 9 de 2023
"""

#Cree un programa que calcule la suma de los cuadrados de los números entre 1 y n

n = int(input("Ingrese un número entero positivo n: "))

sum_cuad = 0

i = 1
while i <= n:
    sum_cuad += i**2
    i += 1

print("La suma de los cuadrados de los números entre 1 y", n, "es:", sum_cuad)
