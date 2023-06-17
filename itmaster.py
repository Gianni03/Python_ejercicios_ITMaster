""" 
* Ejercicio 001
Escribir un programa que permita que el usuario ingrese su nombre. El programa debe emitir una salida con un mensaje de bienvenida que incluya el nombre ingresado.

Ejemplo de ejecución
Ingrese su nombre: Juan
Bienvenido Juan
"""
"""
* Ejercicio 002
Escribir un programa que solicite al usuario su nombre y su edad, y luego muestre por pantalla un mensaje que diga "Hola, [nombre]. Tu Hedad es [edad] años."

Ejemplo de ejecución:

Ingrese su nombre: Juan
Ingrese su edad: 30
Hola, Juan. Tu edad es 30 años.
"""
"""
Ejercicio 003
Escribir un programa que solicite al usuario su nombre y su edad, después pida una cantidad de años y muestre por pantalla un mensaje que indique cuántos años tendrá la persona después de sumarle a su edad la cantidad de años ingresada. El mensaje debe tener el siguiente formato: 'Hola, [nombre]. Dentro de [cantidad] años tendrás [edad + cantidad] años'".

Ejemplo: Si el usuario ingresa "Juan" y "20" y luego ingresa "5", el programa debe mostrar por pantalla "Hola, Juan. Dentro de 5 años tendrás 25 años".
Ejercicio 004
Escribir un programa que solicite al usuario ingresar tres numeros enteros.El programa debe mostrar por pantalla el resultado de sumar los tres numeros de la siguiente manera: "[numero1] + [numero2] + [numero3] = [suma]".

Ejemplo: Si el usuario ingresa 1, 2 y 3, el programa debe mostrar por pantalla: "1 + 2 + 3 = 6".
"""
"""
Ejercicio 005
Escribir un programa que solicite al usuario ingresar dos notas de un alumno. El programa debe mostrar por pantalla el promedio de las notas de la siguiente manera: "Notas: [nota1] , [nota2] ==> promedio: [(nota1+nota2)/2]".

Ejemplo: Si el usuario ingresa 7 y 8, el programa debe mostrar por pantalla: "Notas: 7 , 8 ==> promedio: 7.5".
"""
"""
Ejercicio 006
Escribir un programa que solicite al usuario ingresar tres notas de un alumno. El programa debe mostrar por pantalla las notas separadas por comas en un renglón y el promedio de las notas en el siguiente renglon.

Ejemplo de ejecución:

    Ingrese la nota 1: 7
    Ingrese la nota 2: 8
    Ingrese la nota 3: 9
    Notas: 7, 8, 9
    Promedio: 8.0
"""
"""
Ejercicio 007
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
"""
Ejercicio 008
Escribir un programa que permita ingresar el valor monetario de una hora de trabajo y la cantidad de horas trabajadas por día, para calcular el salario semanal de un trabajador que trabaja todos los días hábiles y la mitad de las horas del día hábil los sábados, suponiendo que todas las horas tienen el mismo valor."
Como pensarlo:

1- Pedir al usuario que ingrese el valor monetario de una hora de trabajo y almacenarlo en una variable valor_hora.

2- Pedir al usuario que ingrese la cantidad de horas trabajadas por día por el trabajador y almacenarla en una variable horas_trabajadas_por_dia.

3- Calcular el salario diario del trabajador multiplicando valor_hora por horas_trabajadas_por_dia.

4- Calcular el salario semanal del trabajador multiplicando el salario diario por la cantidad de días hábiles de la semana. Para esto, puedes utilizar la constante dias_habiles definida como 5.

5- Calcular la cantidad de horas trabajadas por el trabajador el sábado, que es la mitad de la cantidad de horas trabajadas por día hábil. Para esto, se puede utilizar la vaiable horas_sabado definida como horas_trabajadas_por_dia / 2.

6- Calcular el salario del trabajador por las horas trabajadas el sábado multiplicando valor_hora por horas_sabado.

7- Sumar el salario semanal con el salario del sábado para obtener el salario total semanal del trabajador.

8- Mostrar el resultado del salario semanal en la pantalla.
"""
"""
Ejercicio 009
Escribir un programa que permita ingresar valores del mismo tipo para las variables num1 y num2. Una vez cargadas, mostrar ambas variables por pantalla, intercambiá sus valores (que lo cargado en num1 quede en num2, y viceversa) y volvé a mostrarlas actualizadas.
Como pensarlo:

1- Pedir al usuario que ingrese un valor para la variable num1.

2- Pedir al usuario que ingrese un valor para la variable num2.

3- Mostrar por pantalla el valor de las variables num1 y num2.

4- Intercambiar los valores de las variables num1 y num2.

5- Mostrar por pantalla el valor de las variables num1 y num2.
Otra forma de resolverlo:

a=10
b=20
print(a,b)
a = a + b;
b = a - b;
a = a - b;
print(a,b)

# Escriba la solución aquí respetando los pasos descriptos en el enunciado
"""
"""
Ejercicio 010
Escribir un programa para resolver el siguiente problema:
Tres personas invierten dinero para fundar una empresa (no necesariamente en partes iguales).
Calcular qué porcentaje invirtió cada una.
Como pensarlo:

    1 Solicitar al usuario que ingrese las cantidades invertidas por cada persona en tres variables numéricas.

    inversion_persona1 = float(input("Ingrese la cantidad invertida por la persona 1: "))

    inversion_persona2 = float(input("Ingrese la cantidad invertida por la persona 2: "))

    inversion_persona3 = float(input("Ingrese la cantidad invertida por la persona 3: "))

    2 Calcular el total de la inversión sumando las cantidades de las tres personas.

    total = inversion_persona1 + inversion_persona2 + inversion_persona3

    3 Calcular el porcentaje que representa la inversión de cada persona en relación al total de la inversión.

        3 - 1 Dividir la cantidad invertida por cada persona entre el total de la inversión y multiplicar por 100 para obtener el porcentaje. Almacenar el resultado en una variable correspondiente a cada persona. Opcionalmente, se puede redondear el resultado a un número determinado de decimales utilizando la función round().

        Ejemplo:

        porcentaje_inversion_persona1 = round((inversion_persona1 / total) * 100, 2)
        porcentaje_inversion_persona2 = round((inversion_persona2 / total) * 100, 2)
        porcentaje_inversion_persona3 = round((inversion_persona3 / total) * 100, 2)

    4 Mostrar por pantalla el porcentaje de inversión de cada persona.

# Escriba la solución aquí respetando los pasos descriptos en el enunciado
"""
"""
Ejercicio 011
Escribir un programa que permita resolver el siguiente problema:
Tres personas aportan diferente capital a una sociedad y desean saber el valor total aportado y qué porcentaje aportó cada una (indicando nombre y porcentaje).
Solicitar la carga por teclado del nombre de cada socio y su capital aportado, a partir de esto calcular e informar lo requerido previamente.

"""
"""
Ejercicio 012
Escribir un programa en Python que solicite al usuario ingresar dos valores que representen las medidas en grados de dos ángulos interiores de un triángulo. Luego, calcular y mostrar por pantalla el valor en grados del ángulo restante.
Es importante recordar que la suma de los ángulos interiores de todo triángulo es de 180 grados. Es decir, la suma de los ángulos internos de un triángulo siempre es igual a 180 grados. Por lo tanto, para calcular el ángulo restante es necesario restar la suma de los dos ángulos interiores ingresados al valor 180."
Para pensar:

¿Qué pasaría si se ingresan valores negativos como medidas de ángulos?

¿Qué sucedería si la suma de los dos ángulos ingresados es mayor o igual a 180 grados?
"""
"""
Ejercicio 013
Escribir un programa para calcular el importe a cobrar por un vendedor, considerando su sueldo fijo de $200000 pesos más el 16% del monto total de ventas realizadas durante un mes.
Pensando los pasos para resolver el problema:

    1 Solicitar al usuario que ingrese el monto total de ventas realizadas por el vendedor durante el mes en una variable correspondiente.

    2 Calcular el 16% del monto total de ventas realizadas y almacenar el resultado en una variable.

    3 Sumar el resultado del cálculo anterior al sueldo fijo del vendedor.

    4 Mostrar el importe a cobrar por el vendedor.

Para pensar:

¿Qué pasaría si se modificara el sueldo fijo del vendedor?

Si se modifica el sueldo fijo del vendedor, entonces la fórmula utilizada para calcular el salario total debería ser actualizada para reflejar el nuevo sueldo fijo. En este caso, si el sueldo fijo aumenta, entonces el salario total también aumentaría. De igual manera, si el sueldo fijo disminuye, entonces el salario total también disminuiría. Es importante actualizar la fórmula en el programa para asegurarse de que el cálculo del salario total sea preciso y refleje el cambio en el importe a cobrar por del vendedor.

¿Hay que modificar el programa cada vez? ¿Cómo lo soluciono?
"""
"""
Ejercicio 014
Escribir un programa que permita al usuario ingresar el ancho y largo de un terreno en metros, junto con el valor del metro cuadrado de tierra. El programa debe calcular y mostrar el valor total del terreno. Además, debe calcular la cantidad de metros de alambre necesarios para cercar completamente el terreno a tres alturas distintas.
Pensando los pasos para resolver el problema:

Solicitar al usuario que ingrese el ancho del terreno en metros y almacenarlo en una variable. Solicitar al usuario que ingrese el largo del terreno en metros y almacenarlo en otra variable. Solicitar al usuario que ingrese el valor del metro cuadrado de tierra y almacenarlo en otra variable. Calcular el valor total del terreno multiplicando el ancho por el largo y luego multiplicando el resultado por el valor del metro cuadrado de tierra. Mostrar el valor total del terreno al usuario. Calcular la cantidad de metros de alambre necesarios para cercar el terreno a tres alturas distintas. Por ejemplo, se puede calcular la cantidad de alambre necesaria para cercar a 1 metro de altura, a 2 metros de altura y a 3 metros de altura. Para hacerlo, se debe sumar el perímetro del terreno (2 veces el ancho más 2 veces el largo) y luego multiplicarlo por la cantidad de alturas. Mostrar la cantidad de metros de alambre necesarios para cercar el terreno a las tres alturas distintas al usuario.
"""
"""
* Ejercicio 015
Definición del problema: Una inmobiliaria paga a sus vendedores un salario base, más una comisión fija por cada venta realizada, más el 5% del valor de esas ventas. Realizar un programa que imprima el nombre del vendedor y el salario que le corresponde en un determinado mes.
Se leen por teclado el nombre del vendedor, la cantidad de ventas que realizó y el valor total de las mismas.
¿Sobran datos? ¿Qué datos sobran?
"""
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
"""
Ejercicio 019
Escribir un programa que permita ingresar dos números enteros e indicar si son iguales o distintos.
"""
"""
Ejercicio 020
Escribir un programa que permita ingresar dos cadenas de caracteres e indicar si son iguales o distintas.
"""
"""
* Ejercicio 021
Escribir un programa que permita ingresar dos números enteros e indicar si el primero es mayor, menor o igual al segundo.
"""
"""
* Ejercicio 022
Escribir un programa que permita ingresar tres números enteros e indicar cual es el mayor.
"""
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


"""
Ejercicio 024
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
""" edad = int(input("ongrese su edad: "))
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


"""
Ejercicio 025
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
# Escriba la solución aquí
"""
Ejercicio 026
Escribir un programa que permita ingresar la cantidad de invitados a una fiesta y la cantidad de asientos disponibles en el salon. Debes indicar si alcanzan los asientos, Si los asientos no alcanzaran indicar cuántos faltan para que todos los invitados puedan sentarse.
"""
# Escriba la solución aquí
"""
* Ejercicio 027
Escribir un programa que permita ingresar una edad (entre 1 y 120 años), un género ('F'para mujeres, 'M' para hombres) y un nombre. En caso de haber ingresado valores erróneos (edad fuera de rango o género inválido), informar tal situación indicando el nombre de la persona. Si los datos están bien ingresados el programa debe indicar, sabiendo que las mujeres se jubilan con 60 años o más y los hombres con 65 años o más, si la persona está en edad de jubilarse.
"""
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
    print(f'{edad} No es una edad válida') """

    
"""
Ejercicio 028
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
Ejercicio 029
Escribir un programa que permita Ingresar las notas de los dos parciales de un alumno e indicar si promocionó, aprobó o debe recuperar. Si el valor de la nota no esta entre 0 y 10, debe informar un error.

    Se promociona cuando las notas de ambos parciales son mayores o iguales a 7.
    Se aprueba cuando las notas de ambos parciales son mayores o iguales a 4.
    Se debe recuperar cuando al menos una de las dos notas es menor a 4.
"""
# Escriba la solución aquí
"""
Ejercicio 030
Escribir un programa que permita al usuario ingresar dos números enteros. La computadora debe indicar si el mayor es divisible por el menor.

(Un número entero a es divisible por un número entero b cuando el resto de la división entre a y b es 0)
"""
# Escriba la solución aquí

"""
# constantes simbólicas
COSTO_BASICO = 1000
COSTO_POR_PAGINA = 35.10
COSTO_ENC_RUSTICA = 1200
COSTO_ENC_ESPECIAL = 880

num_paginas = int(input("Ingrese el número de páginas del libro: "))
costo = COSTO_BASICO + (COSTO_POR_PAGINA * num_paginas)

# Escriba lo que falta de la solución aquí

print("El costo del libro es: $", costo)

Productos pagados de Colab - Cancela los contratos aquí
*values: object, print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False) Prints the values to a stream, or to sys.stdout by default. Optional keyword arguments: file: a file-like object (stream); defaults to the current sys.stdout. sep: string inserted between values, default a space. end: string appended after the last value, default a newline. flush: whether to forcibly flush the stream., hint
"""