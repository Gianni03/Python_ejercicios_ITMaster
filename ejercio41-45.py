""" *Ejercicio 041
Escribir un programa que lea números enteros hasta que se ingrese un 0, y muestre el máximo.
"""
print("Ej 41 muestra el mayor, 0 para salir")
numero = int(input("Ingrese un numero entero: "))
mayor = 0
if numero != 0:
  mayor = numero

while numero != 0:
  numero = int(input("Ingrese un numero entero: "))
  print(numero)
  print(mayor)
  if numero > mayor:
    mayor = numero
    print(mayor)

print(f' Se ingreso un 0, el numero mayor ingresado fué: {mayor}')

"""
*Ejercicio 042
Escribir un programa que lea números enteros hasta que se ingrese un 0, y muestre el promedio de los números ingresados.

"""
import random   
print("Ej 42 promedio de numeros, 0 para salir")

num = random.randint(0, 3)
suma = 0
contador = 0
while num != 0:
    suma += num
    contador += 1
    num = random.randint(0, 3)

if(contador !=  0): 
    promedio = suma / contador
else:
    promedio = None
    print("el primer numero fue el 0")
    
print(f"aparecio un 0, antes se generaron {contador} numeros y el promedio es {promedio}")

"""
*Ejercicio 043
Escribir un programa que lea números enteros hasta que se la suma de éstos sea mayor que 100, y muestre la cantidad de números ingresados.

"""
print("ej 43, suma de números hasta 100")
contador = 0
suma = 0

while suma <= 100:
  entero = int(input("ingrese un numero entero:"))
  contador += 1
  suma += entero
  
print(f'la suma de los numero supero 100, se ingresaropn {contador} numeros')

"""
*Ejercicio 044
Escribir un programa que permita leer dos números A y B (enteros positivos). Calcular el producto A * B por sumas sucesivas e imprimir el resultado.
Ejemplo:

    4*3 = 4 + 4 + 4 (4 sumado 3 veces).
    3*4 = 3 + 3 + 3 + 3 (3 sumado 4 veces).

"""
print("ej 44, producto por sumas sucesivas")

numA = int(input("numero A: "))
numB = int(input("numero B: "))
producto = 0

if numA < 0:
  numA = int(input("numero A, positivo"))
if numB < 0:
  numB = int(input("numero B, positivo"))
  
for i in range(numB):
  producto += numA
  print(numA)
  
print(f'el producto de {numA} * {numB} es {producto}')

"""
*Ejercicio 045
Escribir un programa que permita leer dos números naturales A y B. Calcular A elevado a la B mediante productos sucesivos y mostrar el resultado.
Ejemplo:

    4^3 = 4 * 4 * 4 (4 multiplicado 3 veces).
    3^4 = 3 * 3 * 3 * 3 (3 multiplicado 4 veces).
"""
print("ej 45, potencia por productos sucesivos, utilizando los datos del ejercicio anterior")
potencia = 1

for i in range(numB):
  potencia *= numA
  print(numA)
  
print(f'la potencia de {numA} al {numB} es {potencia}')