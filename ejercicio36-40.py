"""
*Ejercicio 036
Escribir un programa que permita ingresar dos números enteros y la operación a realizar('+', '-', '*', '/'). Debe mostrarse el resultado para la operación ingresada. Considerar que no se puede dividir por cero (en ese caso mostrar el texto 'ERROR'). """

num1 = int(input("ingrese el primer número: "))
num2 = int(input("ingrese el segundo número: "))
signo = input("ingrese la operacion a realizar ( + , - , * , / ):")



if signo == "+":
    print(f'la suma de {num1} y {num2} es = a {num1 + num2}')
elif signo == "-":
    print(f'la resta de {num1} y {num2} es = a {num1 - num2}')
elif signo == "*":
    print(f'la multiplicación de {num1} y {num2} es = a {num1 * num2}')
elif signo == "/":
    if num2 == 0:
        print("ERROR")
    print(f'la division de {num1} y {num2} es = a {num1 / num2}')
    


""" 

Flujo de repetición.
*Ejercicio 037
Escribir un programa que muestre todos los números enteros del 1 al 5, y luego los mismos números pero en orden inverso. """

numeros = [1,2,3,4,5]

for numero in numeros:
    print(numero)
    
numeros.reverse()
for numero in numeros:
    print(numero)

""" *Ejercicio 038
Escribir un programa que permita ingresar un número entero n. Debe mostrar los primeros 10 múltiplos de n.
Ejemplo

n = 5

n x 1 = 5
n x 2 = 10
n x 3 = 15
n x 4 = 20
n x 5 = 25
n x 6 = 30
n x 7 = 35
n x 8 = 40
n x 9 = 45
n x 10 = 50 """

entero = int(input("ingrese un número entero: "))
multiplo = 1
while multiplo <= 10:
    resultado = entero * multiplo
    print(f'{entero} x {multiplo} = {resultado}')
    multiplo += 1
    

""" *Ejercicio 039
Escribir un programa para calcular e imprimir la suma de los números comprendidos entre 42 y 176 """

comienzo = 42
final = 176
sumaRango = 0 

while comienzo != final +1:
    sumaRango += comienzo
    comienzo += 1
print(f'La suma total de los numeros entre 42 y 176 es {sumaRango}')

""" *Ejercicio 040
Escribir un programa que permita ingresar dos numeros enteros a y b. El programa debe mostrar:

    La suma de los numeros pares entre a y b.
    El producto de los numeros impares entre a y b. 
    
"""
a = int(input("Número a: "))
b = int(input("Número b: "))


suma = 0
suma_pares = 0
producto_impares = 1
if a > b:
    a,b = b,a

for numero in range(a,b+1):
    print(numero)
    suma += numero
    
    if numero % 2 == 0:
        suma_pares += numero
    else:
        producto_impares *= numero
        
print(f'la suma es {suma}')
print(f'la suma de los pares es {suma_pares}')
print(f'el producto de los impares es {producto_impares}')