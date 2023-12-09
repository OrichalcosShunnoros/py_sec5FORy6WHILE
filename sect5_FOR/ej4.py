"""
Programa que calcula la factorial de un número.
Autor: Christian Zambrano
Fecha: Diciembre 6 de 2023
"""


#Cree un programa que dado un número entero n, calcule su factorial(n!).

n = int(input("Ingrese un número entero para calcular su factorial: "))

fact = 1

for i in range(1, n + 1):
    fact *= i

print(f"El factorial de {n} es: {fact}")
