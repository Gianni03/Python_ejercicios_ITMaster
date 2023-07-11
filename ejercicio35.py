"""
* Ejercicio 035
Existen dos reglas que identifican dos conjuntos de valores:

    a) El número es de un solo dígito.
    b) El número es impar.

A partir de estas reglas, escribir un programa que permita ingresar un número entero.
Debe asignar el valor que corresponda a las variables booleanas:

    esDeUnSoloDigito
    esImpar
    estaEnAmbos
    noEstaEnNinguno

el valor Verdadero o Falso, según corresponda, para indicar si el valor número ingresado pertenece o no a cada conjunto. Definir un lote de prueba de varios números y probr el algoritmo, escribiendo los resultados.
"""



esDeUnSoloDigito: True
esImpar: True
estaEnAmbos: True
noEstaEnNinguno: False 

numero = int(input("Ingrese un numero: "))
print("El numero ingresado es: ", numero)

if numero >= 0 and numero <= 9:
    esDeUnSoloDigito = True
else:
    esDeUnSoloDigito = False
print("El numero es de un solo digito: ", esDeUnSoloDigito)
    
if numero % 2 != 0:
    esImpar = True
else:
    esImpar = False
print("El numero es impar: ", esImpar)  

if esDeUnSoloDigito and esImpar:
    estaEnAmbos = True
else:
    estaEnAmbos = False
print("El numero esta en ambos: ", estaEnAmbos) 

if not esDeUnSoloDigito and not esImpar:
    noEstaEnNinguno = True
    estaEnAmbos = False
else:
    noEstaEnNinguno = False
print("El numero no esta en ninguno: ", noEstaEnNinguno)        

    
print(f'El número {numero} tiene las siguientes caracteristicas: \n esDeUnSoloDigito: {esDeUnSoloDigito} \n esImpar: {esImpar} \n estaEnAmbos: {estaEnAmbos} \n noEstaEnNinguno: {noEstaEnNinguno}')
