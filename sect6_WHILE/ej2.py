"""
Programa que muestra la su,a de los primeros n N.
Autor: Christian Zambrano
Fecha: Diciembre 9 de 2023
"""


#Cree un programa que calcula la suma de los primeros n números naturales


n = int(input("Ingrese un número entero positivo n: "))

sum = 0
i = 1

while i <= n:
    sum += i
    i += 1

print("La suma de los primeros", n, "números naturales es:", sum)
