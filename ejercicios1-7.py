""" 
* Ejercicio 001
Escribir un programa que permita que el usuario ingrese su nombre. El programa debe emitir una salida con un mensaje de bienvenida que incluya el nombre ingresado.
Ejemplo de ejecución
Ingrese su nombre: Juan
Bienvenido Juan
"""

nombre = input("Ingrese su nombre: ")
print("Bienvenido", nombre)



"""
* Ejercicio 002
Escribir un programa que solicite al usuario su nombre y su edad, y luego muestre por pantalla un mensaje que diga "Hola, [nombre]. Tu Hedad es [edad] años."
Ejemplo de ejecución:
Ingrese su nombre: Juan
Ingrese su edad: 30
Hola, Juan. Tu edad es 30 años.
"""

nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
print("Hola,",nombre, "te edad es ",edad) 

"""
* Ejercicio 003
Escribir un programa que solicite al usuario su nombre y su edad, después pida una cantidad de años y muestre por pantalla un mensaje que indique cuántos años tendrá la persona después de sumarle a su edad la cantidad de años ingresada. El mensaje debe tener el siguiente formato: 'Hola, [nombre]. Dentro de [cantidad] años tendrás [edad + cantidad] años'".

Ejemplo: Si el usuario ingresa "Juan" y "20" y luego ingresa "5", el programa debe mostrar por pantalla "Hola, Juan. Dentro de 5 años tendrás 25 años".
"""
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
anios = int(input("ingrese un numero mas: "))
sumarAnios = edad + anios
print(f'Hola, {nombre}. Dentro de {anios} años tendrás {sumarAnios} años')

"""
* Ejercicio 004
Escribir un programa que solicite al usuario ingresar tres numeros enteros.El programa debe mostrar por pantalla el resultado de sumar los tres numeros de la siguiente manera: "[numero1] + [numero2] + [numero3] = [suma]".

Ejemplo: Si el usuario ingresa 1, 2 y 3, el programa debe mostrar por pantalla: "1 + 2 + 3 = 6".
"""
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese un número: "))
num3 = int(input("Ingrese un número: "))
suma = num1 + num2 + num3
print(f'{num1} + {num2} + {num3} = {suma}')

"""
* Ejercicio 005
Escribir un programa que solicite al usuario ingresar dos notas de un alumno. El programa debe mostrar por pantalla el promedio de las notas de la siguiente manera: "Notas: [nota1] , [nota2] ==> promedio: [(nota1+nota2)/2]".

Ejemplo: Si el usuario ingresa 7 y 8, el programa debe mostrar por pantalla: "Notas: 7 , 8 ==> promedio: 7.5".
"""
nota1 = float(input("Ingrese la nota: "))
nota2 = float(input("Ingrese la nota: "))
promedio = (nota1 + nota2) / 2
print(f'Notas: {nota1} - {nota2} ==> Promedio: {promedio}')

"""
* Ejercicio 006
Escribir un programa que solicite al usuario ingresar tres notas de un alumno. El programa debe mostrar por pantalla las notas separadas por comas en un renglón y el promedio de las notas en el siguiente renglon.

Ejemplo de ejecución:
    Ingrese la nota 1: 7
    Ingrese la nota 2: 8
    Ingrese la nota 3: 9
    Notas: 7, 8, 9
    Promedio: 8.0
"""
nota1 = float(input("Ingrese la nota: "))
nota2 = float(input("Ingrese la nota: "))
nota3 = float(input("Ingrese la nota: "))
promedio = (nota1 + nota2 + nota3) / 3

print("Notas:", nota1, nota2, nota3, sep=", ")
print(f'Promedio: {promedio}')

"""
* Ejercicio 007
Escribir un programa que permita ingresar un número entero. Debe mostrarse el número ingresado:
a. Multiplicado por 10. (utilizar el operador *)
b. Dividido por 10. (utilizar el operador /)
c. Elevado al cuadrado. (utilizar el operador **)
Cada resultado debe mostrarse en una línea distinta.

Ejemplo de ejecución:
Ingrese un número entero: 5
5 * 10 = 50
5 / 10 = 0.5
5 ** 2 = 25
"""
valor1 = int(input("ingrese un numero:"))

print("el nḿero que ingresaste es: ", valor1)

mult = valor1 * 10
div = valor1 / 10
pot = valor1 ** 2
print("se realizaron alguna operaciones")
print("multiplicacion x 10 = ", mult )
print("division x 10 = ", div )
print("potencia 2 = ", pot )