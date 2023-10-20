# menu.py
import os
import time
import function

while True:
    os.system('clear' if os.name == 'posix' else 'cls')  # Limpiar la pantalla (funciona en sistemas Unix y Windows)
    print("Elija un ejercicio:")
    print("1. Calcular suma de una lista de números")
    print("2. Encontrar el número más grande en una lista de números")
    print("0. Salir")

    try:
        option = int(input("Ingrese el número del ejercicio (0 para salir): "))

        if option == 0:
            break
        elif option == 1:
            lista = [int(x) for x in input("Ingrese la lista de números separados por espacios: ").split()]
            resultado = function.calcular_suma(lista)
            print("El resultado es:", resultado)
        elif option == 2:
            lista = [int(x) for x in input("Ingrese la lista de números separados por espacios: ").split()]
            resultado = function.encontrar_maximo(lista)
            print("El número más grande es:", resultado)
        else:
            print("Opción no válida. Por favor, elija una opción válida.")

        time.sleep(5)  # Espera 5 segundos
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número válido.")
        time.sleep(5)  # Espera 5 segundos
