"""
* Ejercicio 024
Para acceder a cierta atracción, es necesario cumplir con dos requisitos: tener al menos 10 años de edad y medir más de 1,60 metros.
(Ojo, tener en cuenta las palabras: más,al menos y sobre todo la letra y)
Escribir un programa en Python que solicite al usuario su edad y estatura, y que determine si cumple con los requisitos para subir a la atracción. Si cumple con ambos requisitos, el programa debe imprimir "¡Puede acceder!" en la pantalla. Si no cumple con alguno de los requisitos, el programa debe imprimir un mensaje que indique el motivo por el cual no puede subir. Por ejemplo, si no cumple con el requisito de la edad, el programa debe imprimir "Lo siento, eres demasiado joven para acceder." Si no cumple con el requisito de la estatura, el programa debe imprimir "Lo siento, eres demasiado bajo para acceder"

Los conectores lógicos "and" y "or" son operadores booleanos utilizados en programación y en lógica matemática para combinar o unir dos o más expresiones lógicas.

El conector "and" se utiliza para combinar dos o más expresiones lógicas y evaluarlas en conjunto. La expresión completa es verdadera sólo si todas las expresiones individuales son verdaderas. Por ejemplo, la expresión lógica "A and B" será verdadera sólo si tanto A como B son verdaderos. Si alguna de las expresiones es falsa, la expresión completa será falsa.

La tabla de verdad del operador "and" se utiliza en lógica proposicional para determinar el valor de verdad de una proposición compuesta formada por dos proposiciones simples unidas por "and". La tabla de verdad del "and" se construye evaluando todas las posibles combinaciones de valores de verdad de las proposiciones simples, y determinando el valor de verdad de la proposición compuesta para cada combinación.

La tabla de verdad del "and" es la siguiente:
P 	Q 	P and Q
V 	V 	V
V 	F 	F
F 	V 	F
F 	F 	F

En resumen, el conector "and" se utiliza para crear expresiones lógicas que requieren que todas las condiciones sean verdaderas para que la expresión sea verdadera.
"""
edad = int(input("ingrese su edad: "))
altura = float(input("ingrese su altura: "))

EDAD_MINIMA = 10
ALTURA_MINIMA = 1.60

entraPorEdad = edad > EDAD_MINIMA
entraPorAltura = altura > ALTURA_MINIMA
entra = entraPorEdad and entraPorAltura

if entra:
    print("puedes ingresar")
else:
    if not entraPorEdad:
        print("eres menor de 10 añor, no puede entrar")
    if not entraPorAltura:
        print("eres menor de 1.60, no puede entrar")
        



"""
* Ejercicio 025
Para acceder a cierta atracción, alcanza con que se cumpla solamente una de las siguientes condiciones: ser mayor de 6 años o medir más de 1,50 metros.
Escribir un programa en Python que solicite al usuario su edad y estatura, y que determine si cumple con los requisitos para subir a la atracción. Si cumple con al menos una de las condiciones, el programa debe imprimir "¡Puede acceder!" en la pantalla. Si no cumple con ninguna de las condiciones, el programa debe imprimir un mensaje que lo indique.
(Ojo, tener en cuenta las palabras: más, mayor y sobre todo la letra o)

El conector "or" se utiliza para combinar dos o más expresiones lógicas y evaluarlas en conjunto. La expresión completa es verdadera si al menos una de las expresiones individuales es verdadera. Por ejemplo, la expresión lógica "A or B" será verdadera si al menos una de las variables A o B es verdadera. Solo si ambas variables son falsas, entonces la expresión completa será falsa.

La tabla de verdad del "or" es la siguiente:
P 	Q 	P or Q
V 	V 	V
V 	F 	V
F 	V 	V
F 	F 	F

El conector "or" se utiliza para crear expresiones lógicas que requieren que al menos una condición sea verdadera para ser verdadera.
"""
edad = int(input("ingrese su edad: "))
altura = float(input("ingrese su altura: "))

MIN_EDAD = 10
MIN_ALTURA = 1.50

porEdad = edad > MIN_EDAD
porAltura = altura > MIN_ALTURA
cumple = porEdad or porAltura

if cumple:
  print("cumples con al menos un requisito")
else:
  print("no cumples con los requisitos")
  


"""
Ejercicio 026
Escribir un programa que permita ingresar la cantidad de invitados a una fiesta y la cantidad de asientos disponibles en el salon. Debes indicar si alcanzan los asientos, Si los asientos no alcanzaran indicar cuántos faltan para que todos los invitados puedan sentarse.
"""
invitados = int(input("Cuantos invitados son? "))
asientos = int(input("cuantos asientos hay disponibles? "))

if invitados <= asientos:
  print("La cantidad de asientos alcanza para los invitados")
else:
  faltan = invitados - asientos
  print(f"Invitaste a mucha gente, te faltan {faltan} asientos")


"""
* Ejercicio 027
Escribir un programa que permita ingresar una edad (entre 1 y 120 años), un género ('F'para mujeres, 'M' para hombres) y un nombre. En caso de haber ingresado valores erróneos (edad fuera de rango o género inválido), informar tal situación indicando el nombre de la persona. Si los datos están bien ingresados el programa debe indicar, sabiendo que las mujeres se jubilan con 60 años o más y los hombres con 65 años o más, si la persona está en edad de jubilarse.
"""

JUBILACION_HOMBRE = 65
JUBILACION_MUJER = 60

edad = int(input("edad: "))
genero = input("Género: ").upper()
nombre = input("Nombre: ").title()

if edad >= 1 and edad <= 120:
    if genero == "M" or genero == "F":
        if genero == "M":
            se_jubila = edad >= JUBILACION_HOMBRE
        else:
            se_jubila = edad >= JUBILACION_MUJER
    
        if se_jubila:
            print(f'{nombre} Género: {genero} se jubila')
        else:
            print(f'{nombre} Género: {genero} no se jubila')
    else:
        print(f'{genero} No es un género válido')
else:
    print(f'{edad} No es una edad válida')

    
"""
* Ejercicio 028
Crear un programa que pida un número de mes (ejemplo 4) y escriba el nombre del mes en letras ("abril"). Verificar que el mes sea válido e informar en caso que no lo sea.
"""

import random
# numero_mes = int(input("Número de mes: "))
numero_mes = random.randint(1,12)

if numero_mes == 1:
    nombre = "Enero"
elif numero_mes == 2:
    nombre = "Febrero"
elif numero_mes == 3:
    nombre = "Marzo"
elif numero_mes == 4:
    nombre = "Abril"
elif numero_mes == 5:
    nombre = "Mayo"
elif numero_mes == 6:
    nombre = "Junio"
elif numero_mes == 7:
    nombre = "Julio"
elif numero_mes == 8:
    nombre = "Agosto"
elif numero_mes == 9:
    nombre = "Septiembre"
elif numero_mes == 10:
    nombre = "Octubre"
elif numero_mes == 11:
    nombre = "Noviembre"
elif numero_mes == 12:
    nombre = "Diciembre"
else:
    nombre = "error"

print(f'El mes {numero_mes} es: {nombre}')

"""
* Ejercicio 029
Escribir un programa que permita Ingresar las notas de los dos parciales de un alumno e indicar si promocionó, aprobó o debe recuperar. Si el valor de la nota no esta entre 0 y 10, debe informar un error.

    Se promociona cuando las notas de ambos parciales son mayores o iguales a 7.
    Se aprueba cuando las notas de ambos parciales son mayores o iguales a 4.
    Se debe recuperar cuando al menos una de las dos notas es menor a 4.
"""
nota1 = int(input("ingresa la nota de tu parcial: "))
nota2 = int(input("ingresa la segunda nota de tu parcial: "))

while nota1 > 10 or nota1 < 0:
    nota1 = int(input("ERROR: ingresa la nota correcta de tu parcial 1: "))
while nota2 > 10 or nota2 < 0:
    nota2 = int(input("ERROR: ingresa la nota correcta de tu parcial 2: "))


if nota1 >= 7 and nota2 >= 7:
    print("Felicitaciones, promocionaste")
elif nota1 >= 4 and nota2 >= 4:
    print("Felicitaciones, aporbaste")
else:
    print("Debes recuperar")

"""
Ejercicio 030
Escribir un programa que permita al usuario ingresar dos números enteros. La computadora debe indicar si el mayor es divisible por el menor.

(Un número entero a es divisible por un número entero b cuando el resto de la división entre a y b es 0)
"""
num1 = int(input("ingresa un número: "))
num2 = int(input("ingresa otro un número: "))

if num1 > num2:
  if num1 % num2 == 0:
    print(f'ingresaste {num1} y {num2} donde {num1} es el mayor y es divisible por {num2}')
  else:
    print(f'ingresaste {num1} y {num2} donde {num1} es el mayor y no es divisible por {num2}')
elif num1 < num2:
  if num2 % num1 == 0:
    print(f'ingresaste {num1} y {num2} donde {num2} es el mayor y es divisible por {num1}')
  else:
    print(f'ingresaste {num1} y {num2} donde {num2} es el mayor y no es divisible por {num1}')
else:
    print(f'ingresaste {num1} y {num2} y son iguales')

