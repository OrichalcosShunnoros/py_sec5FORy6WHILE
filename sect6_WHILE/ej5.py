"""
Programa que pregunta al usuario si desea salir con las opciones S/N.
Autor: Christian Zambrano
Fecha: Diciembre 9 de 2023
"""

#Cree un programa que pregunte al usuario si desea salir, si o no “S/N”, si el usuario teclea la letra S el
#programa se detendrá, de lo contrario continuará ejecutándose.

while True:
    respuesta = input("¿Desea salir? (S/N): ")
    
    if respuesta.upper() == "S":
        print("¡Vuelva pronto!")
        break 
    elif respuesta.upper() == "N":
        print("Continuando...")
    else:
        print("Respuesta no válida. Por favor, ingrese S o N.")
