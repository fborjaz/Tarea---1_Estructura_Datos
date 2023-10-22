# Ejercicio 1; Crea una lista de números enteros y calcula su suma.

List_num = [1, 2, 3, 4, 5]
sum = 0
for i in List_num:
    sum += i
print(sum)

# Ejercicio 2: Encuentra el número más grande en una lista de números.

List_num = [1, 2, 3, 4, 5]
max = 0
for i in List_num:
    if i > max:
        max = i
print(max)

# Ejercicio 3: Encuentra el número más pequeño en una lista de números.

List_num = [1, 2, 3, 4, 5]
min = List_num[0]
for i in List_num:
    if i < min:
        min = i
print(min)

# Ejercicio 4: Elimina los elementos duplicados de una lista.

List_num = [1, 2, 3, 4, 5]
List_num_new = []
for i in List_num:
    if i not in List_num_new:
        List_num_new.append(i)
print(List_num_new)

# Ejercicio 5: Dada una lista, invierte su orden.

List_num = [1, 2, 3, 4, 5]
List_num_new = []
for i in List_num:
    List_num_new.insert(0, i)
print(List_num_new)

# Ejercicio 6: Escribe un programa que cuente cuántas veces aparece un elemento en una lista.

List_num = [1, 2, 3, 4, 5]
num = 3
count = 0
for i in List_num:
    if i == num:
        count += 1
print(count)

# Ejercicio 7: Crea una lista de números pares del 1 al 20.

List_num = []
for i in range(1, 21):
    if i % 2 == 0:
        List_num.append(i)
print(List_num)

# Ejercicio 8: Dada una lista de nombres, ordénalos alfabéticamente.

List_name = ['Juan', 'Pedro', 'Maria', 'Ana', 'José']
List_name_new = []
for i in List_name:
    List_name_new.append(i)
List_name_new.sort()
print(List_name_new)

# Ejercicio 9: Crea una lista de los cuadrados de los números del 1 al 10.

List_num = []
for i in range(1, 11):
    List_num.append(i ** 2)
print(List_num)

# Ejercicio 10: Dada una lista de números, encuentra el segundo número más grande.

List_num = [1, 2, 3, 4, 5]
max = 0
for i in List_num:
    if i > max:
        max = i
max_2 = 0
for i in List_num:
    if i > max_2 and i < max:
        max_2 = i
print(max_2)

# Ejercicio 11: Crea un diccionario con nombres de personas como claves y sus edades como valores.

Dcc_Person = {"Juan": 25, "Pedro": 30, "Maria": 35, "Ana": 40, "José": 45}

# Ejercicio 12: Agrega un nuevo elemento a un diccionario.

Dcc_Person["Carlos"] = 50
print(Dcc_Person)

# Ejercicio 13: Elimina un elemento de un diccionario por clave.

Dcc_Person.pop("Carlos")
print(Dcc_Person)

# Ejercicio 14: Itera a través de las claves de un diccionario e imprime sus valores.

for key in Dcc_Person:
    print(Dcc_Person[key])

# Ejercicio 15: Verifica si una clave existe en un diccionario.

if "Juan" in Dcc_Person:
    print("Existe")
else:
    print("No existe")

# Ejercicio 16: Dada una lista de diccionarios (personas), encuentra la persona más joven. Sacado Chat GPT

List_person = [{"name": "Juan", "age": 25}, {"name": "Pedro", "age": 30}, {"name": "Maria", "age": 35},
               {"name": "Ana", "age": 40}, {"name": "José", "age": 45}]
min = List_person[0]["age"]
for i in List_person:
    if i["age"] < min:
        min = i["age"]
print(min)

# Ejercicio 17: Dada una lista de diccionarios (libros), busca un libro por título.

List_book = [{"title": "El principito", "author": "Antoine de Saint-Exupéry"},
             {"title": "El cisne negro", "author": "F. Scott Fitzgerald"},
             {"title": "La divina comedia", "author": "Dante Alighieri"}]
title = "El principito"
for i in List_book:
    if i["title"] == title:
        print(i)

# Ejercicio 18: Crea un diccionario que cuente cuántas veces aparece cada palabra en una cadena de texto.

text = "Esto es una prueba de palabras"
List_text = text.split()
Dcc_text = {}
for i in List_text:
    if i in Dcc_text:
        Dcc_text[i] += 1
    else:
        Dcc_text[i] = 1
print(Dcc_text)

# Ejercicio 19:  Dado un diccionario de productos y sus precios, calcula el precio total de una lista de compras.

Dcc_Product = {"Producto 1": 20, "Producto 2": 30, "Producto 3": 40, "Producto 4": 50}
List_Product = ["Producto 1", "Producto 2", "Producto 3"]
total = 0
for i in List_Product:
    total += Dcc_Product[i]
print(total)

# Ejercicio 20: Combina dos diccionarios en uno solo.

Dcc_1 = {"Producto 1": 20, "Producto 2": 30, "Producto 3": 40, "Producto 4": 50}
Dcc_2 = {"Producto 5": 60, "Producto 6": 70, "Producto 7": 80, "Producto 8": 90}
Dcc_3 = {**Dcc_1, **Dcc_2}
print(Dcc_3)

# Ejercicio 21: Usa un bucle while para contar del 1 al 10.

i = 1
while i <= 10:
    print(i)
    i += 1

# Ejercicio 22: Usa un bucle for para imprimir los números pares del 1 al 20.

for i in range(1, 21, 2):
    print(i)

# Ejercicio 23: Escribe un programa que imprima los elementos de una lista utilizando un bucle for.

list = ["Elemento 1", "Elemento 2", "Elemento 3"]
for i in list:
    print(i)

# Ejercicio 24: Usa un bucle while para sumar los números del 1 al 100.

sum = 0
i = 1
while i <= 100:
    sum += i
    i += 1
print(sum)

# Ejercicios 25: Escribe un programa que cuente cuántas veces aparece una letra en una cadena de texto utilizando un bucle for.

text = "Esto es una prueba de palabras"
count = 0
for i in text:
    if i == "e":
        count += 1
print(count)

# Ejercicio 26: Utiliza un bucle for para imprimir los números del 10 al 1 en orden decreciente.

for i in range(10, 0, -1):
    print(i)

# Ejercicio 27: Escribe un programa que imprima los números impares del 1 al 30 usando un bucle for

for i in range(1, 31, 2):
    print(i)

# Ejercicio 28: Usa un bucle while para encontrar el primer número divisible por 7 y 11.

i = 1
while i % 7 != 0 or i % 11 != 0:
    i += 1
print(i)

# Ejercicio 29: Escribe un programa que genere los primeros 10 números de la secuencia Fibonacci.

first = 0
second = 1
for i in range(10):
    print(first)
    first, second = second, first + second

# Ejercicio 30: Utiliza un bucle for para imprimir los elementos de una lista en reversa.

list = ["Elemento 1", "Elemento 2", "Elemento 3"]
for i in range(len(list) - 1, -1, -1):
    print(list[i])

# Ejercicio 31: Escribe un programa que determine si un número es positivo, negativo o cero.

number = int(input("Ingrese un número: "))
if number > 0:
    print("El número es positivo")
elif number < 0:
    print("El número es negativo")
else:
    print("El número es cero")

# Ejercicio 32: Dado un número, verifica si es par o impar.

number = int(input("Ingrese un número: "))
if number % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

# Ejercicio 33: Escribe un programa que determine si un año es bisiesto.

year = int(input("Ingrese un año: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")

# ejercicio 34: Dada la edad de una persona, clasifícala como niño, adolescente, adulto o anciano.

age = int(input("Ingrese su edad: "))
if age < 13:
    print("Es un niño")
elif age < 20:
    print("Es un adolescente")
elif age < 65:
    print("Es un adulto")
else:
    print("Es un anciano")

# Ejercicio 35: Escribe un programa que determine si un triángulo es equilátero, isósceles o escaleno.

a = int(input("Ingrese la medida del lado a: "))
b = int(input("Ingrese la medida del lado b: "))
c = int(input("Ingrese la medida del lado c: "))
if a == b and b == c:
    print("El triángulo es equilátero")
elif a == b or b == c or a == c:
    print("El triángulo es isósceles")
else:
    print("El triángulo es escaleno")

# Ejercicio 36: Dado un número, verifica si es primo o no.

number = int(input("Ingrese un número: "))
if number < 2:
    print("El número no es primo")
else:
    for i in range(2, number):
        if number % i == 0:
            print("El número no es primo")
            break
    else:
        print("El número es primo")

# Ejercicio 37: Escribe un programa que clasifique a un estudiante según su calificación (A, B, C, D, F).

score = int(input("Ingrese su calificación: "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

# Ejercicio 38: Dada una cadena de texto, verifica si es un palíndromo.

text = input("Ingrese una cadena de texto: ")
if text == text[::-1]:
    print("La cadena es un palíndromo")
else:
    print("La cadena no es un palíndromo")

# Ejercicio 39: Escribe un programa que determine si un número es divisible por 3 y 5.

number = int(input("Ingrese un número: "))
if number % 3 == 0 and number % 5 == 0:
    print("El número es divisible por 3 y 5")
else:
    print("El número no es divisible por 3 y 5")

# Ejercicio 40: Dado un número, verifica si es positivo y múltiplo de 4.

number = int(input("Ingrese un número: "))
if number > 0 and number % 4 == 0:
    print("El número es positivo y múltiplo de 4")
else:
    print("El número no es positivo y múltiplo de 4")


# Ejercicio 41: Crea una función que calcule el área de un triángulo.

def area_triangle(base, height):
    return (base * height) / 2


base = int(input("Ingrese la base del triángulo: "))
height = int(input("Ingrese la altura del triángulo: "))
print(f"El área del triángulo es {area_triangle(base, height)}")


# Ejercicio 42: Escribe una función que devuelva la longitud de una lista.

def list_length(list):
    return len(list)


list = [1, 2, 3, 4, 5]
print(f"La longitud de la lista es {list_length(list)}")


# Ejercicio 43: Crea una función que convierta grados Celsius a Fahrenheit.

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


celsius = int(input("Ingrese los grados Celsius: "))
print(f"{celsius} grados Celsius son {celsius_to_fahrenheit(celsius)} grados Fahrenheit")


# Ejercicio 44: Escribe una función que genere una lista de números primos.

def generate_prime_list(n):
    prime_list = []
    for i in range(2, n + 1):
        if is_prime(i):
            prime_list.append(i)
    return prime_list


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


n = int(input("Ingrese un número: "))
print(f"Los números primos menores que {n} son {generate_prime_list(n)}")


# Ejercicio 45: Crea una función que calcule el factorial de un número.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


n = int(input("Ingrese un número: "))
print(f"El factorial de {n} es {factorial(n)}")


# Ejercicio 46: Escribe una función que verifique si una cadena de texto es un pangrama (contiene todas las letras del alfabeto).

def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabet:
        if letter not in sentence.lower():
            return False
    return True


sentence = input("Ingrese una cadena de texto: ")
if is_pangram(sentence):
    print("La cadena de texto es un pangrama")
else:
    print("La cadena de texto no es un pangrama")


# Ejercicio 47: Crea una función que devuelva el número de vocales en una cadena de texto.

def count_vowels(sentence):
    vowels = "aeiouAEIOU"
    count = 0
    for letter in sentence:
        if letter in vowels:
            count += 1
    return count


sentence = input("Ingrese una cadena de texto: ")
print(f"La cadena de texto tiene {count_vowels(sentence)} vocales")


# Ejercicio 48: Crea una función que devuelva el número de vocales en una cadena de texto.

def count_vowels(sentence):
    vowels = "aeiouAEIOU"
    count = 0
    for letter in sentence:
        if letter in vowels:
            count += 1
    return count


sentence = input("Ingrese una cadena de texto: ")
print(f"La cadena de texto tiene {count_vowels(sentence)} vocales")


# Ejercicio 49: Crea una función que verifique si una cadena de texto es un palíndromo.

def is_palindrome(sentence):
    reversed_sentence = sentence[::-1]
    return sentence == reversed_sentence


sentence = input("Ingrese una cadena de texto: ")
if is_palindrome(sentence):
    print("La cadena de texto es un palíndromo")
else:
    print("La cadena de texto no es un palíndromo")


# Ejercicio 50: Escribe una función que determine si un número es par o impar

def is_even(n):
    return n % 2 == 0


n = int(input("Ingrese un número: "))
if is_even(n):
    print(f"{n} es un número par")
else:
    print(f"{n} es un número impar")


# Ejercicio 51: Crea una clase llamada "Persona" con atributos nombre y edad.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hola, mi nombre es {self.name} y tengo {self.age} años")


# Ejercicio 52: Crea un objeto de la clase "Persona" e imprime sus atributos.

person = Person("Juan", 30)
print(f"Nombre: {person.name}")
print(f"Edad: {person.age}")


# Ejercicio 53: Agrega un método a la clase "Persona" para saludar

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hola, mi nombre es {self.name} y tengo {self.age} años")

    def greet_with_name(self, name):
        print(f"Hola, {name}, mi nombre es {self.name} y tengo {self.age} años")


# Ejercicio 54: Crea una clase llamada "Rectángulo" con atributos largo y ancho

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length + self.width)


# Ejercicio 55: Agrega un método a la clase "Rectángulo" para calcular el área.

rectangle = Rectangle(5, 10)
print(f"El área del rectángulo es: {rectangle.get_area()}")


# Ejercicio 56: Crea una clase llamada "CuentaBancaria" con atributos saldo y titular. // Echo en clases

class BankAccount:
    def __init__(self, balance, titular):
        self.balance = balance
        self.titular = titular

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def get_balance(self):
        return self.balance

    def get_titular(self):
        return self.titular


# Ejercicio 57: Agrega métodos para depositar y retirar dinero de la cuenta bancaria.

account = BankAccount(1000, "Juan")
account.deposit(500)
account.withdraw(200)
print(f"El saldo actual de la cuenta es: {account.get_balance()}")


# Ejercicio 58: Crea una clase llamada "Coche" con atributos marca, modelo y año.

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_details(self):
        return f"{self.brand} {self.model} ({self.year})"

    def accelerate(self):
        print(f"{self.brand} {self.model} está acelerando.")


# Ejercicio 59: Agrega un método para acelerar el coche.

car = Car("Toyota", "Camry", 2020)
print(f"El coche es un {car.get_details()}")
car.accelerate()

# Ejercicio 60: Escribe un programa que cree una lista de objetos "Coche" y acelere cada uno de ellos.

cars = [Car("Toyota", "Camry", 2020), Car("Ford", "Mustang", 2021), Car("Chevrolet", "Corvette", 2022)]
for car in cars:
    print(f"El coche es un {car.get_details()}")
    car.accelerate()


