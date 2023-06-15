"""
* Ejercicio 008
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

valor_hora = int(input("Valor de la hora de trabajo: "))
horas_trabajadas_por_dia = int(input("horas de trabajo por día: "))
salario_diario = valor_hora * horas_trabajadas_por_dia
DIAS_HABILES = 5
salario_semanal = salario_diario * DIAS_HABILES
horas_sabado = horas_trabajadas_por_dia / 2
salario_sabado = horas_sabado * valor_hora
salario_total = salario_semanal + salario_sabado

print("El salario por semana es: ", salario_total)


"""
* Ejercicio 009
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
num1 = int(input("Ingrese un valor:   "))
num2 = int(input("Ingrese un valor:   "))
print("Valores: ", num1,num2)

aux = num1
num1 = num2
num2 = aux
print("intercambiados",num1,num2)

num1,num2 = num2,num1
print("intercambiados otra forma: ",num1,num2)

a=10
b=20
print(a,b)
a = a + b;
b = a - b;
a = a - b;
print(a,b)


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
"""
inversion_persona1 = float(input("Ingrese la cantidad invertida por la persona 1: $"))
inversion_persona2 = float(input("Ingrese la cantidad invertida por la persona 2: $"))
inversion_persona3 = float(input("Ingrese la cantidad invertida por la persona 3: $"))

total = inversion_persona1 + inversion_persona2 + inversion_persona3
porcentaje_inversion_persona1 = round((inversion_persona1 / total) * 100, 2)
porcentaje_inversion_persona2 = round((inversion_persona2 / total) * 100, 2)
porcentaje_inversion_persona3 = round((inversion_persona3 / total) * 100, 2)

print(f'El porcentaje invertido por cada persona es: \n persona 1 = {porcentaje_inversion_persona1}% \n persona 2 = {porcentaje_inversion_persona2}% \n persona 3 = {porcentaje_inversion_persona3}%')

"""
Ejercicio 011
Escribir un programa que permita resolver el siguiente problema:
Tres personas aportan diferente capital a una sociedad y desean saber el valor total aportado y qué porcentaje aportó cada una (indicando nombre y porcentaje).
Solicitar la carga por teclado del nombre de cada socio y su capital aportado, a partir de esto calcular e informar lo requerido previamente.

"""
persona1 = input("nombre del inversor 1: ")
persona2 = input("nombre del inversor 2: ")
persona3 = input("nombre del inversor 3: ")

print(f'El porcentaje invertido por cada persona es: \n {persona1} - invertido ${inversion_persona1} - {porcentaje_inversion_persona1}% \n {persona2} - invertido ${inversion_persona2} -  {porcentaje_inversion_persona2}% \n {persona3} - invertido ${inversion_persona3} - {porcentaje_inversion_persona3}%')


"""
Ejercicio 012
Escribir un programa en Python que solicite al usuario ingresar dos valores que representen las medidas en grados de dos ángulos interiores de un triángulo. Luego, calcular y mostrar por pantalla el valor en grados del ángulo restante.
Es importante recordar que la suma de los ángulos interiores de todo triángulo es de 180 grados. Es decir, la suma de los ángulos internos de un triángulo siempre es igual a 180 grados. Por lo tanto, para calcular el ángulo restante es necesario restar la suma de los dos ángulos interiores ingresados al valor 180."
Para pensar:

¿Qué pasaría si se ingresan valores negativos como medidas de ángulos?

¿Qué sucedería si la suma de los dos ángulos ingresados es mayor o igual a 180 grados?
"""
print("Calcular los angulos de un triangulo")
angulo1 = float(input("ingrese el valor del angulo: "))
angulo2 = float(input("ingrese el valor del angulo: "))
TOTAL_ANGULOS = 180

if angulo1 < 1  or angulo2 < 1:
    print("el valor no puede ser negativo")
    
if (angulo1 + angulo2 >=180):
    print("loa angulos dados no son de un triangulo")
    
angulo3 = TOTAL_ANGULOS - (angulo1 + angulo2)

print("El angulo restante tiene un valor de ", angulo3, "°")    



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
SUELDO_FIJO = 20000
ventas_mes = float(input("Total de ventes en el mes: "))
comision = 0.16
comision_mes = ventas_mes * comision
sueldo_total = SUELDO_FIJO + comision_mes
print(f'En el mes de vendio${ventas_mes} lo que deja una comision de ${comision_mes}. \n El sueldo total del mes es ${sueldo_total}')

"""
Ejercicio 014
Escribir un programa que permita al usuario ingresar el ancho y largo de un terreno en metros, junto con el valor del metro cuadrado de tierra. El programa debe calcular y mostrar el valor total del terreno. Además, debe calcular la cantidad de metros de alambre necesarios para cercar completamente el terreno a tres alturas distintas.
Pensando los pasos para resolver el problema:

Solicitar al usuario que ingrese el ancho del terreno en metros y almacenarlo en una variable. Solicitar al usuario que ingrese el largo del terreno en metros y almacenarlo en otra variable. Solicitar al usuario que ingrese el valor del metro cuadrado de tierra y almacenarlo en otra variable. 
Calcular el valor total del terreno multiplicando el ancho por el largo y luego multiplicando el resultado por el valor del metro cuadrado de tierra. Mostrar el valor total del terreno al usuario. Calcular la cantidad de metros de alambre necesarios para cercar el terreno a tres alturas distintas. Por ejemplo, se puede calcular la cantidad de alambre necesaria para cercar a 1 metro de altura, a 2 metros de altura y a 3 metros de altura. Para hacerlo, se debe sumar el perímetro del terreno (2 veces el ancho más 2 veces el largo) y luego multiplicarlo por la cantidad de alturas. Mostrar la cantidad de metros de alambre necesarios para cercar el terreno a las tres alturas distintas al usuario.
"""
ancho = float(input("ingrese el ancho del terreno: "))
largo = float(input("ingrese el largo del terreno: "))
valor_m2 = float(input("ingrese el valor del metro cuadrado: $"))
superficie = ancho * largo
perimetro = (ancho * 2) + (largo * 2)

valor_terreno = superficie * valor_m2

alambre = int(input("altura del alambrado 1, 2, 3: "))
metros_alambre = ""
if (alambre >= 1 or alambre <=3):
    metros_alambre = perimetro * alambre
else:
    print("valor no aceptado")
    
print(f'El terreno tiene un valor de ${valor_terreno}, y para una altura de {alambre}mts de alambrado se necesita un total de {metros_alambre}mts de alambre')

