""" * Ejercicio 034
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

Sueldo Neto 999,99 """

# Escriba la solución aquí
JUBILACION = 0.11
OBRA_SOCIAL = 0.03
SINDICATO = 0.03
CASADO = 1.07
SOLTERO = 1.05

sueldoBruto = int(input("ingrese su sueldo bruto: "))
antiguedad = int(input("ingrese su antieguedad: "))
estaCasado = input("Está casado? (S/N)").upper



if estaCasado == "S":
    sueldoBruto *= CASADO
    estadoCivil = "Casado"
else:
    sueldoBruto *= SOLTERO
    estadoCivil = "Soltero"
    
descuentoJubilacion = sueldoBruto * JUBILACION
descuentoObraSocial = sueldoBruto * OBRA_SOCIAL
descuentoSindicato = sueldoBruto * SINDICATO

sueldoNeto = sueldoBruto - descuentoJubilacion - descuentoObraSocial - descuentoSindicato

print(f'Estado Civil: {estadoCivil} Sueldo básico: ${sueldoBruto} Antigüedad: {antiguedad} años \n\n Descuentos: \n\n Jublacion - {descuentoJubilacion} \n\n Obra Social - {descuentoObraSocial} \n\n Sindicato - {descuentoSindicato} \n\n Sueldo neto - {sueldoNeto} \n\n ')
