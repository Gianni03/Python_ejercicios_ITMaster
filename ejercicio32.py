""" * Ejercicio 032
Una remisería requiere un sistema que calcule el precio de un viaje a partir de la cantidad de km que desea recorrer el usuario.
Tiene la siguiente tarifa:

    Viaje mínimo $50

    Si recorre entre 0 y 10km: $20/km

    Si recorre 10km o más: $15/km

Escribir un programa que permita ingresar la cantidad de km que desea recorrer el usuario y muestre el precio del viaje.

# Escriba la solución aquí """

TARIFA_BASE = 50
TARIFA_VIAJE_CORTO = 20
TARIFA_VIAJE_LARGO = 15

kilometros = int(input("De cuantos kilometros es el viaje? "))

if (kilometros > 0 and kilometros <= 10):
    valorKms = kilometros * TARIFA_VIAJE_CORTO
    precioViaje = TARIFA_BASE + valorKms
    print(f'Su viaje de {kilometros}Km tiene un valo de ${precioViaje}')
elif kilometros > 10:
    valorKms = kilometros * TARIFA_VIAJE_LARGO
    precioViaje = TARIFA_BASE + valorKms
    print(f'Su viaje de {kilometros}Km tiene un valo de ${precioViaje}')
else:
  print("error en los Km")
    
# estoy repitiendo código dentro del if,  ver para corregir