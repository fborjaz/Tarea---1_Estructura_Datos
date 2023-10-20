# menu.py
import funciones

while True:
    print("Elija un ejercicio:")
    print("1. Calcular suma de una lista de números")
    print("2. Encontrar el número más grande en una lista de números")
    # Agrega las demás opciones aquí...
    print("0. Salir")

    opcion = int(input("Ingrese el número del ejercicio (0 para salir): ")

    if opcion == 0:
        break
    elif opcion == 1:
        lista = [int(x) for x in input("Ingrese la lista de números separados por espacios: ").split()]
        resultado = funciones.calcular_suma(lista)
        print("El resultado es:", resultado)
    elif opcion == 2:
        lista = [int(x) for x in input("Ingrese la lista de números separados por espacios: ").split()]
        resultado = funciones.encontrar_maximo(lista)
        print("El número más grande es:", resultado)
# Agrega el resto de las opciones aquí...