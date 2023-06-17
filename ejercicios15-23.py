"""
* Ejercicio 015
Definición del problema: Una inmobiliaria paga a sus vendedores un salario base, más una comisión fija por cada venta realizada, más el 5% del valor de esas ventas. Realizar un programa que imprima el nombre del vendedor y el salario que le corresponde en un determinado mes.
Se leen por teclado el nombre del vendedor, la cantidad de ventas que realizó y el valor total de las mismas.
¿Sobran datos? ¿Qué datos sobran?
"""
# falta info sobre sueldo fijo, comision por venta,
#el nombre cantidad de veentas y valores de ventas se piden al usuario

nombre = input("Nombre: ")
ventas = int(input("cantida de ventas: ")) # este dato es irrelevante al programa
valor = int(input("valor total de ventas: "))

SALARIO_BASE = 120000 # sueldo fijo establecido por mi
COMISION_VENTA = 0.1 # comision de ventas
COMISION_EXTRA = 0.5 # %5 del valor de ventas


sueldo = SALARIO_BASE + ( valor * COMISION_VENTA) + (valor * COMISION_EXTRA)
print(f'{nombre} tiene un sueldo de: {sueldo} ')



"""
* Ejercicio 016
Escribir un programa que permita al usuario ingresar un período de tiempo en segundos. Luego, el programa debe convertir ese período de tiempo a una forma más legible y comprensible para el usuario, expresando el resultado en días, horas, minutos y segundos. El resultado se mostrará en pantalla en un mensaje que indique la cantidad de segundos ingresados y su equivalente en días, horas, minutos y segundos.

Ejemplo: 200000 segundos equivalen a 2 días, 7 horas, 33 minutos y 20 segundos.
Usar en el programa las siguientes instrucciones:

dias = segundos // 86400 # 86400 segundos = 1 día

horas = (segundos % 86400) // 3600 # 3600 segundos = 1 hora

minutos = (segundos % 3600) // 60 # 60 segundos = 1 minuto

segundos_restantes = segundos % 60 # segundos restantes
"""
segundos = int(input("Ingrese la cantidad de segundos:   "))

dias = segundos // 86400 # 86400 segundos = 1 día

horas = (segundos % 86400) // 3600 # 3600 segundos = 1 hora

minutos = (segundos % 3600) // 60 # 60 segundos = 1 minuto

segundos_restantes = segundos % 60 # segundos restantes

print(f'{segundos} equivalen a {dias} días, {horas} horas, {minutos} minutos, {segundos_restantes} segundos')
print(f'{dias}:{horas}:{minutos}:{segundos_restantes}')


"""
* Ejercicio 017
¡Ayuda! Se me rompió el programa que convierte una cantidad de dinero en la cantidad mínima de billetes y monedas necesarios. Tengo todas las instrucciones necesarias, pero están todas mezcladas. ¿Podrías ayudarme a ordenarlas de manera correcta para que funcione el programa como debería? A lo mejor se me perdieron algunas instrucciones, ¿podrías agregarlas?

resto = cantidad_total
billetes_cien = resto // 100
resto = resto % 100
billetes_cinco = resto // 5
billetes_mil = resto // 1000
billetes_cincuenta = resto // 50
billetes_doscientos = resto // 200
billetes_diez = resto // 10
billetes_docientos = resto // 200
resto = resto % 10
cantidad_total = int(input("Ingrese la cantidad de dinero a convertir: "))
billetes_uno = resto // 1
print("Para la cantidad de ",cantidadtotal,"senecesitan:")print(billetesmil,"billetesde1000")
print(billetes_doscientos, "billetes de 200")print(billetescien,"billetesde100")
print(billetes_cincuenta, "billetes de 50")print(billetesdiez,"billetesde10")
print(billetes_cinco, "billetes de 5")print(billetesuno,"billetesde1")
"""
cantidad_total = int(input("Ingrese la cantidad de dinero a convertir: "))
resto = cantidad_total
billetes_mil = resto // 1000
resto = resto % 1000
billetes_doscientos = resto // 200
resto = resto % 200
billetes_cien = resto // 100
resto = resto % 100
billetes_cincuenta = resto // 50
resto = resto % 50
billetes_diez = resto // 10
resto = resto % 10
billetes_cinco = resto // 5
resto = resto % 5
billetes_uno = resto

print("Para la cantidad de ",cantidad_total,"senecesitan:")
print(billetes_mil,"billetesde1000")
print(billetes_doscientos, "billetes de 200")
print(billetes_cien,"billetesde100")
print(billetes_cincuenta, "billetes de 50")
print(billetes_diez,"billetesde10")
print(billetes_cinco, "billetes de 5")
print(billetes_uno,"billetes de 1")



"""
Flujos de selección
Ejercicio 018
Escribir un programa que permita al usuario ingresar un número entero y luego muestre un mensaje indicando si el número es par o impar.
Pensando los pasos para resolver el problema:

-1 Pedir al usuario que ingrese un número entero.
-2 Almacenar ese número en una variable.

-3 Verificar si el número es par o impar.

    Si el número es par, mostrar un mensaje indicando que es par.
    Si el número es impar, mostrar un mensaje indicando que es impar.

(Para verificar si un número es par o impar, se puede utilizar el operador módulo (%). Si el resto de la división del número por 2 es 0, entonces el número es par. Si el resto de la división del número por 2 es 1, entonces el número es impar.)
"""


numero = int(input("Ingrese un número: "))
print("El número ingresado es:", numero)
if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")


"""
Ejercicio 019
Escribir un programa que permita ingresar dos números enteros e indicar si son iguales o distintos.
"""

numero1 = int(input("Ingrese un número: "))
numero2 = int(input("Ingrese un número: "))
print("Los números ingresados son:", numero1, numero2)
if numero1 == numero2:
    print("Los número son iguales")
else:
    print("Los número son distintos")


"""
* Ejercicio 020
Escribir un programa que permita ingresar dos cadenas de caracteres e indicar si son iguales o distintas.
"""
txt1 = input("Ingrese un texto: ")
txt2 = input("Ingrese un texto: ")

print("Los textos ingresados son:", txt1, txt2)
if txt1 == txt2:
    print("Los textos son iguales")
else:
    print("Los textos son distintos")
    
igual = txt1 is txt2 # el is comprueba si la ubicacion en memoria es la misma
print(igual)   
txt1 = txt2
igual = txt1 is txt2 # el is comprueba si la ubicacion en memoria es la misma
print(igual)   

"""
* Ejercicio 021
Escribir un programa que permita ingresar dos números enteros e indicar si el primero es mayor, menor o igual al segundo.
"""

n1 = int(input("ingrese el primer número: "))
n2 = int(input("ingrese el segundo número: "))

if n1 > n2:
    print(" el mayor es: ", n1)
else:
    if n2 > n1:
        print(" el mayor es: ", n2)
    else:
        print(" son iguales ")
    

"""
* Ejercicio 022
Escribir un programa que permita ingresar tres números enteros e indicar cual es el mayor.
"""
n1 = int(input("ingrese el primer número: "))
n2 = int(input("ingrese el segundo número: "))
n3 = int(input("ingrese el tercer número: "))


# if n1 > n2:
#     if n1 > n3:
#         print(" el mayor es: ", n1)
#     else:
#         print(" el mayor es: ", n3)
# else:
#     if n2 > n1:
#         if n2 > n3:
#             print(" el mayor es: ", n2)
#         else:
#             print(" el mayor es: ", n3)

mayor = n1

if n2 > mayor:
    mayor = n2

if n3 > mayor:
    mayor = n3

print('el mayor es: ', mayor)

mayor = max(n1,n2,n3) # solo funciona con números!!!
print("el numero mayor es: ",mayor)

"""
* Ejercicio 023
Escribir un programa que permita ingresar tres números enteros y mostrar el mayor el menor y el valor que esta en medio.
Ejemplo: Si se ingresan los números 5, 3 y 7, el programa debe mostrar el número 3 como el menor, el número 7 como el mayor y el número 5 como el que esta en medio.
Otra vez se mezclaron las instrucciones, ¿podrías arreglarlas?

numero_uno = int(input("Ingrese el primer número: "))
numero_dos = int(input("Ingrese el segundo número: "))
numero_tres = int(input("Ingrese el tercer número: "))

if medio < menor:
auxiliar = medio
medio = menor
menor = auxiliar

if numero_tres > mayor:
mayor = numero_tres
medio = numero_uno
menor = numero_dos

if numero_dos > mayor:
mayor = numero_dos
medio = numero_uno
menor = numero_tres

mayor = numero_uno
medio = numero_dos
menor = numero_tres

print("El mayor es: ", mayor)
print("El medio es: ", medio)
print("El menor es: ", menor)
"""
numero_uno = int(input("Ingrese el primer número: "))
numero_dos = int(input("Ingrese el segundo número: "))
numero_tres = int(input("Ingrese el tercer número: "))

mayor = numero_uno
medio = numero_dos
menor = numero_tres



if numero_tres > mayor:
    mayor = numero_tres
    medio = numero_uno
    menor = numero_dos

if numero_dos > mayor:
    mayor = numero_dos
    medio = numero_uno
    menor = numero_tres
    
if medio < menor:
    auxiliar = medio
    medio = menor
    menor = auxiliar


print("El mayor es: ", mayor)
print("El medio es: ", medio)
print("El menor es: ", menor)
