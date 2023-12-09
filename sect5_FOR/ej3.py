"""
Programa que calcula el promedio de tres notas para n estudiantes.
Autor: Christian Zambrano
Fecha: Diciembre 6 de 2023
"""


#Cree un programa que calcule el promedio de tres notas para n estudiantes.

num_est = int(input("Ingrese el número de estudiantes: "))

for est in range(1, num_est + 1):
    print(f"\nNotas del estudiante {est}:")
    
    nt1 = float(input("Ingrese la primera nota: "))
    nt2 = float(input("Ingrese la segunda nota: "))
    nt3 = float(input("Ingrese la tercera nota: "))
    
    prom = (nt1 + nt2 + nt3) / 3

    print(f"El promedio del estudiante {est} es: {prom}")
