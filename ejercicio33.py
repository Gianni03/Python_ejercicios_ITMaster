""" 
* Ejercicio 033
La farmacia Sindical efectúa descuentos a sus afiliados según el importe de la compra con la siguiente escala:

    Menor de 5500.0 el descuento es del 4.5%  
    - ### Entre5500.0 y 10000.0 el descuento es del 8%  
    - ### Más de10000.0 el descuento es del 10.5%

Escribir un programa que reciba un importe e informe: el descuento y el precio neto a cobrar, con mensajes aclaratorios.

# Escriba la solución aquí """

DESCUENTO_MENOR = 0.045
DESCUENTO_MEDIO = 0.08
DESCUENTO_MAYOR = 0.105

importe = int(input("Ingrese el valor de la compra: "))


if importe < 5500:
    descuento = importe * DESCUENTO_MENOR
    precio = importe - descuento
    print(f'Tuvo un descuento de {descuento}. El monto total es {precio}')
elif importe >= 5500 and importe <= 10000:
    descuento = importe * DESCUENTO_MEDIO
    precio = importe - descuento    
    print(f'Tuvo un descuento de {descuento}. El monto total es {precio}') 
else:
    descuento = importe * DESCUENTO_MAYOR
    precio = importe - descuento
    print(f'Tuvo un descuento de {descuento}. El monto total es {precio}')