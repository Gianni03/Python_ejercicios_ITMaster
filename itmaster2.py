""" 
Entrada y salida de datos
Ejercicio 031
Una editorial determina el precio de un libro según la cantidad de páginas que contiene. El costo básico del libro es de 1000,más35,10 por página con encuadernación rústica. Si el número de páginas supera las 300 la encuadernación debe ser especial, lo que incrementa el costo en 1200.Además,sielnúmerodepáginassobrepasalas600sehacenecesariootroprocedimientodeencuadernaciónqueincrementaelcostoen880. Desarrollar un programa que calcule el costo de un libro dado el número de páginas.

En Python no existen constantes como tal, pero se utiliza una convención de nomenclatura en mayúsculas para indicar que una variable no debe ser modificada. Esto se conoce como "constante simbólica" o "constante convencional". Para definir una constante convencional, simplemente se define una variable con un nombre en mayúsculas.

Por ejemplo, para el problema anterior, se pueden definir las constantes:

COSTO_BASICO con valor 1000

COSTO_POR_PAGINA con valor 35.10

COSTO_ENC_RUSTICA con valor 1200

COSTO_ENC_ESPECIAL con valor 880.

Es una buena práctica utilizar constantes para almacenar valores fijos en un programa, ya que facilita la lectura del código y su mantenimiento, evita errores por la modificación accidental de valores y permite un fácil ajuste de los valores fijos en caso de ser necesario.


# constantes simbólicas
COSTO_BASICO = 1000
COSTO_POR_PAGINA = 35.10
COSTO_ENC_RUSTICA = 1200
COSTO_ENC_ESPECIAL = 880

num_paginas = int(input("Ingrese el número de páginas del libro: "))
costo = COSTO_BASICO + (COSTO_POR_PAGINA * num_paginas)

# Escriba lo que falta de la solución aquí

print("El costo del libro es: $", costo)

Ejercicio 032
Una remisería requiere un sistema que calcule el precio de un viaje a partir de la cantidad de km que desea recorrer el usuario.
Tiene la siguiente tarifa:

    Viaje mínimo $50

    Si recorre entre 0 y 10km: $20/km

    Si recorre 10km o más: $15/km

Escribir un programa que permita ingresar la cantidad de km que desea recorrer el usuario y muestre el precio del viaje.

# Escriba la solución aquí

Ejercicio 033
La farmacia Sindical efectúa descuentos a sus afiliados según el importe de la compra con la siguiente escala:

    Menor de 5500.0 el descuento es del 4.5%  
    - ### Entre5500.0 y 10000.0 el descuento es del 8%  
    - ### Más de10000.0 el descuento es del 10.5%

Escribir un programa que reciba un importe e informe: el descuento y el precio neto a cobrar, con mensajes aclaratorios.

# Escriba la solución aquí

Ejercicio 034
Escribir un programa que calcule y muestre el sueldo neto de un empleado en base a su sueldo básico y su antigüedad en años. Si es soltero se le incrementa el sueldo en 5% del salario bruto por cada año de antigüedad, mientras que si es casado se le incrementa el sueldo en 7% del salario bruto por cada año de antigüedad. También se le realizan los siguientes descuentos:

    Jubilación: 11%

    Obra Social: 3%

    Sindicato: 3%

Como datos de entrada se ingresa por teclado el sueldo básico, antigüedad y estado civil (S: Soltero / C: Casado). Se debe informar: (reemplazando los 9 por los valores que correspondan)

Estado Civil: Soltero/Casado Sueldo básico: $ 999.99 Antigüedad: 99 años

Descuentos:

    Jubilación - 999,99

    Obra Social - 999,99

    Sindicato - 999,99

Sueldo Neto 999,99

# Escriba la solución aquí

Ejercicio 035
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

# Escriba la solución aquí


esDeUnSoloDigito: True
esImpar: True
estaEnAmbos: True
noEstaEnNinguno: False

Ejercicio 036
Escribir un programa que permita ingresar dos números enteros y la operación a realizar('+', '-', '*', '/'). Debe mostrarse el resultado para la operación ingresada. Considerar que no se puede dividir por cero (en ese caso mostrar el texto 'ERROR').

# Escriba la solución aquí

Flujo de repetición.
Ejercicio 037
Escribir un programa que muestre todos los números enteros del 1 al 5, y luego los mismos números pero en orden inverso.

# Escriba la solución aquí

Ejercicio 038
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
n x 10 = 50

# Escriba la solución aquí

Ejercicio 039
Escribir un programa para calcular e imprimir la suma de los números comprendidos entre 42 y 176

# Escriba la solución aquí

Ejercicio 040
Escribir un programa que permita ingresar dos numeros enteros a y b. El programa debe mostrar:

    La suma de los numeros pares entre a y b.
    El producto de los numeros impares entre a y b.

# Escriba la solución aquí

Ejercicio 041
Escribir un programa que lea números enteros hasta que se ingrese un 0, y muestre el máximo.

# Escriba la solución aquí

Ejercicio 042
Escribir un programa que lea números enteros hasta que se ingrese un 0, y muestre el promedio de los números ingresados.

# Escriba la solución aquí

Ejercicio 043
Escribir un programa que lea números enteros hasta que se la suma de éstos sea mayor que 100, y muestre la cantidad de números ingresados.

# Escriba la solución aquí

Ejercicio 044
Escribir un programa que permita leer dos números A y B (enteros positivos). Calcular el producto A * B por sumas sucesivas e imprimir el resultado.
Ejemplo:

    4*3 = 4 + 4 + 4 (4 sumado 3 veces).
    3*4 = 3 + 3 + 3 + 3 (3 sumado 4 veces).

# Escriba la solución aquí

Ejercicio 045
Escribir un programa que permita leer dos números naturales A y B. Calcular A elevado a la B mediante productos sucesivos y mostrar el resultado.
Ejemplo:

    4^3 = 4 * 4 * 4 (4 multiplicado 3 veces).
    3^4 = 3 * 3 * 3 * 3 (3 multiplicado 4 veces).

# Escriba la solución aquí

Ejercicio 046
Escribir un programa que a partir de un número entero cant ingresado por el usuario permita cargar por teclado cant números enteros. La computadora debe mostrar cuál fue el mayor número y en qué posición apareció.

# Escriba la solución aquí

Ejercicio 047
Escribir un programa que permita validar la nota de un examen. Se espera que la nota que el usuario ingrese sea un número comprendido entre 0 y 10.
La misma debe ser ingresada tantas veces como sea necesario hasta que quede comprendida dentro del rango indicado.

# Escriba la solución aquí

Ejercicio 048
Escribir un programa que permita realizar varias operaciones matemáticas ingresando un caracter por cada una la operación a realizar (‘+’, ‘-’, ‘*’, ‘/’, ‘F’) y dos números enteros en el caso que no haya elegido ‘F’. La computadora debe mostrar el resultado para la operación ingresada. Considerar que no se puede dividir por cero. Cuando la operación ingresada sea ‘F’ nos indicará que no se desean calcular más operaciones.

# Escriba la solución aquí

Ejercicio 049
Escribir un programa que permita validar una opción ingresada. Se le preguntará al usuario si desea continuar con alguna operación de la forma "¿Deseás continuar? [S/N]". Se espera que el usuario ingrese una 'S' o una 'N' (incluir las minúsculas). La opción debe ser ingresada tanto como sea necesario hasta que quede comprendida dentro de las posibilidades esperadas.

# Escriba la solución aquí

Ejercicio 050
Escribir un programa que permita validar la nota de un examen. Se espera que la nota que el usuario ingrese sea un número comprendido entre 0 y 10.
La misma debe ser ingresada tantas veces como sea necesario hasta que quede comprendida dentro del rango indicado.

    Las notas 1 y 3 no usan nunca.
    La nota 0 se reserva para los ausentes.
    Las notas válidas pueden ser un 2 o un valor entre 4 y 10.

# Escriba la solución aquí

Ejercicio 051
Escribir un programa que permita al usuario ingresar números hasta que se introduzca un 0.
La computadora debe mostrar el número máximo y el número mínimo.

# Escriba la solución aquí

Ejercicio 052
Escribir un programa que permita un programa que permita ingresar la estatura (en metros con decimales) de cada jugador de un equipo de baloncesto. La carga finalizará al ingresar cero. Calcular y mostrar la estatura promedio del equipo.

# Escriba la solución aquí

Ejercicio 053
Escribir un programa que permita ingresar nombre y edad de un grupo de personas (para cada una, nombre y edad). La carga termina cuando en el nombre de la persona se ingresa un asterisco ('*'). Mostrar al final cómo se llama la persona más joven.

# Escriba la solución aquí

Ejercicio 054
Escribir un programa que permita controlar con validación el ingreso a un sitio web. Teniendo dos constantes con un nombre de usuario ("admin") y una contraseña ("123456"), el programa debe permitir al usuario ingresar sus credenciales. Si las mismas son erróneas, se volverán a pedir hasta un máximo de 3 intentos. Finalmente, la computadora debe mostrar alguno de los siguientes mensajes según sea el caso: "Acceso concedido" o "Se ha bloqueado la cuenta"

# Escriba la solución aquí
USUARIO = "admin"
CONTRASENA = "1234"

Ejercicio 055
Escribir un programa que permita para cada cliente que va al banco "Express".
Cada cliente indica su número de documento y aguarda a ser atendido, cuando finaliza la atención del día se ingresa -1 para indicar que no hay más clientes para ser atendidos. El banco desea saber quién fue el primer cliente atendido y quién fue el último.

# Escriba la solución aquí

Ejercicio 056
Escribir un programa que permita Leer números que representan edades de un grupo de personas, finalizando la lectura cuando se ingrese el número 999. Imprimir cuántos son menores de 18 años, cuántos tienen 18 años o más y el promedio de edad de ambos grupos. Descartar valores que no representan una edad válida. (Se considera válido una edad entre 0 y 100)

# Escriba la solución aquí

Ejercicio 057
Escribir un programa que permita ingresar los números de legajo de los alumnos de un curso y su nota de examen final. El fin de la carga se determina ingresando un -1 en el legajo.
Informar para cada alumno si aprobó o no el examen considerando que se aprueba con nota mayor o igual a 4. Se debe validar que la nota ingresada sea entre 1 y 10. Terminada la carga de datos, informar:

    Cantidad de alumnos que aprobaron (nota >= 4).
    Cantidad de alumnos que desaprobaron el examen (nota < 4).
    Porcentaje de alumnos que están aplazados (nota == 1).

# Escriba la solución aquí

Ejercicio 058
Una empresa aplica el siguiente procedimiento en la comercialización de sus productos:

    Aplica el precio base a la primera docena de unidades.
    Aplica un 10% de descuento a todas las unidades entre 13 y 100.
    Aplica un 25% de descuento a todas las unidades por encima de las 100.
    Por ejemplo, supongamos que vende 230 unidades de un producto cuyo precio base es 100. El cálculo resultante sería:
    100 * 12 + 90 * 88 + 75 * 130 = 18870, y el precio promedio será 18870 / 230 = 82,04
    Escribir un programa que lea la cantidad solicitada de un producto y su precio base, y muestre el valor total de la venta y el precio promedio por unidad. El fin de carga se determina ingresando -1 como cantidad solicitada.
    Al finalizar informar:
    a) Cantidad de ventas realizadas total.
    b) Cantidad de ventas que se aplicaron un 10% de descuento.
    c) Cantidad de ventas que SOLO se aplicó el precio base, no se le realizaron descuentos

# Escriba la solución aquí

Ejercicio 059
Escribir un programa para un negocio de venta de granos que desea controlar las ventas realizadas. De cada venta ingresa el importe total y un código que indica la forma de pago. Los códigos puede ser:

    C: cheque, 20% de recargo.
    E: efectivo, 10% de descuento.
    T: con tarjeta, 12% de recargo.
    Se debe ingresar una F para finalizar el día de venta y arrojar los siguientes totales.
    | Forma de Pago | Total |
    | ---------------- | --------- | | Efectivo en Caja | xxxx.xx||Tarjeta/Crédito| xxxx.xx |
    | Cheques | xxxx.xx||TotaldeVenta| xxxx.xx |
    | Importe del IVA | $ xxxx.xx |

# Escriba la solución aquí

Ejercicio 060
Escribir un programa para calcular el sueldo final a pagar a cada empleado de una empresa. De cada uno se tiene, sueldo básico, antigüedad, cantidad de hijos y estudios superiores (‘S’ o ‘N’). Además, se conocen los porcentajes de aumento del sueldo que dependen de los siguientes factores:

    Si el empleado tiene más de 10 años de antigüedad: aumento del 10%
    Si el empleado tiene más de 2 hijos: aumento del 10%, si solo tiene uno 5%
    Si el empleado posee estudios superiores: aumento del 5%

Luego de ingresar los datos de un empleado se debe preguntar si se desea ingresar otro empleado o no. Se termina la carga cuando no se deseen ingresar más empleados.

    Determinar:
        a. Por cada empleado: número de empleado, el sueldo básico y el nuevo sueldo.
        b. Sueldo nuevo promedio de la empresa.

# Escriba la solución aquí

Ejercicio 061
Escribir un programa que permita ingresar un número entero positivo y mostrar su factorial. El factorial de un número es el producto de todos los números enteros desde 1 hasta el número ingresado. Por ejemplo, el factorial de 5 es 1 * 2 * 3 * 4 * 5 = 120.

# Escriba la solución aquí

Ejercicio 062
Un entrenador le ha propuesto a un atleta recorrer una ruta de cinco kilómetros durante 10 días para determinar si es apto para la prueba de 5 kilómetros que se desarrollará en el Parque. No se sabe si está apto y para eso nos piden que hagamos el siguiente programa.
Nos ingresan por cada día de entrenamiento tiempo de la prueba en minutos (entero mayor que 0 y menor a 100)
Para considerarlo apto debe cumplir las siguientes condiciones:

    Que en ninguna de las pruebas haga un tiempo mayor a 20 minutos.
    Que al menos en una de las pruebas realice un tiempo menor de 15 minutos.
    Que su promedio sea menor o igual a 18 minutos.
    Se pide:
    Diseñar un algoritmo para registrar los datos y decidir si es apto para la competencia.
    Sólo en caso de estar apto, informar el promedio y el número de día en el que realizó el menor tiempo

# Escriba la solución aquí

Ejercicio 063
Escribir un programa para registrar y obtener información sobre los viajes diarios de un conductor de Uber.
Cada vez que comienza un viaje se debe ingresar la distancia recorrida, indicando si el viaje fue corto (‘C’), mediano (‘M’), largo (‘L’) o si es el fin de los datos (‘Z’).
El día finaliza cuando se llega a los 30 viajes o cuando se ingresa distancia ‘Z’ (fin de los datos).
Por cada viaje se debe ingresar la siguiente información:

    Cantidad de pasajeros (mayor a 0 y menor a 4).
    Importe a cobrar, incluyendo la el costo básico ($180).
    Por cada pasajero de ese viaje se debe ingresar:
        Nombre.
        Edad (mayor a 18 y menor a 120 años).

Se desea saber, para cada viaje, cuál es la persona más grande y su nombre.
Al finalizar el día de trabajo, el programa debe informar:

    Cantidad de viajes por cada categoría (‘C’, ‘M’, ‘L’).
    Recaudación total.
    Valor promedio del viaje.
    Porcentaje de viajes cortos.

Todos los datos ingresados deben ser validados.

# Escriba la solución aquí

Ejercicio 064
Un animal en rehabilitación después de una cirugía requiere ser alimentado y monitoreado en un zoológico. Se alimenta al animal 3 veces al día y se le da de comer hasta que ya no tenga ganas de comer.
Por cada tanda de comida, se debe ingresar la cantidad de alimento en kg (número entero) que se le dio y se le debe preguntar al animal si quiere seguir comiendo ('S', 'N').
Se desea conocer:

    Cuál de las 3 comidas fue la que el animal comió más cantidad de alimento y cuánto fue esa cantidad.
    El total en kg de alimento recibido.
    Promedio de alimento por tanda.

# Escriba la solución aquí

Ejercicio 065
Una cadena de comida rápida solicita el desarrollo de una aplicación para sus terminales de autoservicio que permita a los clientes armar su propio menú. Los clientes pueden elegir entre diferentes opciones de combos o pedir por separado la comida, bebida y postre.
Al iniciar la aplicación, se debe mostrar el siguiente menú de opciones:

    1) Combo 1: Hamburguesa, papas fritas y gaseosa - 1550
    2) Combo 2: Hamburguesa con queso, papas fritas y gaseosa - 1650
    3) Hamburguesa sola - 1300
    4) Hamburguesa con queso - 1400
    5) Gaseosa - 700
    6) Postre - 600
    7) Agregar aderezo - 100
    8) Terminar

Luego de seleccionar cada ítem, se debe mostrar el subtotal para que el cliente pueda decidir si desea agregar más productos a su pedido antes de terminar.
El valor mínimo del pedido debe ser de $1550. Si el cliente elige un combo, se debe sumar el importe total al subtotal. Si el cliente selecciona opciones 3 a 7, se le debe preguntar la cantidad deseada y calcular el valor total antes de sumarlo al subtotal.
Al finalizar el pedido, se debe mostrar el monto total a pagar, el ítem más caro y, si no se han seleccionado productos, mostrar un mensaje que diga "Pedido cancelado".

# Escriba su solución aquí

Ejercicio 066a
La biblioteca de la ciudad necesita organizar y hacer un recuento de los libros que tiene en sus 5 estantes. Para cada uno de los 5 estantes, se deben ingresar los libros, y para cada libro, se debe ingresar su nombre (usando 'FIN' si no hay más libros para ese estante), género (usando 'I' para Infantil, 'N' para Novela, o 'H' para Historia), y cantidad de páginas (mayor a 0). Una vez que se han ingresado los datos de 1 estante, se debe mostrar por pantalla el nombre del libro con la mayor cantidad de páginas y su cantidad correspondiente. Al finalizar el ingreso de datos de todos los estantes, se deben mostrar la cantidad de libros por género y el promedio de libros por estante.

# Escriba su solución aquí

Ejercicio 066b
La biblioteca de la ciudad necesita organizar y hacer un recuento de los libros que tiene en sus estantes. Para cada uno de los estantes (usando 'F' para indicar el fin de los estantes), se deben ingresar 15 libros, y para cada libro, se debe ingresar su nombre, género (usando 'I' para Infantil, 'N' para Novela, o 'H' para Historia), y cantidad de páginas (mayor a 0). Una vez que se han ingresado los datos de 1 estante, se debe mostrar por pantalla el nombre del libro con la mayor cantidad de páginas y su cantidad correspondiente. Al finalizar el ingreso de datos de todos los estantes, se deben mostrar la cantidad de libros por género.

# Escriba su solución aquí

Ejercicio 066c
La biblioteca de la ciudad necesita organizar y hacer un recuento de los libros que tiene en sus estantes. Para cada uno de los estantes (usando 'F' para indicar el fin del estante), se deben ingresar los libros, y para cada libro, se debe ingresar su nombre (usando 'FIN' si no hay más libros para ese estante), género (usando 'I' para Infantil, 'N' para Novela, o 'H' para Historia), y cantidad de páginas (mayor a 0). Una vez que se han ingresado los datos de 1 estante, se debe mostrar por pantalla el nombre del libro con la mayor cantidad de páginas y su cantidad correspondiente. Al finalizar el ingreso de datos de todos los estantes, se deben mostrar la cantidad de libros por género y el promedio de libros por estante.

# Escriba su solución aquí

Ejercicio 066d
La biblioteca de la ciudad necesita organizar y hacer un recuento de los libros que tiene en sus estantes. Para cada uno de los 5 estantes, se le pide al usuario que ingrese la cantidad de libros que tendrá ese estante. Para cada libro, se debe ingresar su nombre, género (usando 'I' para Infantil, 'N' para Novela, o 'H' para Historia), y cantidad de páginas (mayor a 0). Una vez que se han ingresado los datos de 1 estante, se debe mostrar por pantalla el nombre del libro con la mayor cantidad de páginas y su cantidad correspondiente. Al finalizar el ingreso de datos de todos los estantes, se deben mostrar la cantidad de libros por género.

# Escriba su solución aquí

Productos pagados de Colab - Cancela los contratos aquí
 """