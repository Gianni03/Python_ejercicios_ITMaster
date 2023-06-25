""" *Ejercicio 036
Escribir un programa que permita ingresar dos números enteros y la operación a realizar('+', '-', '*', '/'). Debe mostrarse el resultado para la operación ingresada. Considerar que no se puede dividir por cero (en ese caso mostrar el texto 'ERROR'). """

# Escriba la solución aquí
""" 
Flujo de repetición.
*Ejercicio 037
Escribir un programa que muestre todos los números enteros del 1 al 5, y luego los mismos números pero en orden inverso. """

# Escriba la solución aquí

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

# Escriba la solución aquí

""" *Ejercicio 039
Escribir un programa para calcular e imprimir la suma de los números comprendidos entre 42 y 176 """

# Escriba la solución aquí

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