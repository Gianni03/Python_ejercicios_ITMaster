""" *Ejercicio 056
Escribir un programa que permita Leer números que representan edades de un grupo de personas, finalizando la lectura cuando se ingrese el número 999. Imprimir cuántos son menores de 18 años, cuántos tienen 18 años o más y el promedio de edad de ambos grupos. Descartar valores que no representan una edad válida. (Se considera válido una edad entre 0 y 100)
"""

terminar = False
cantidad_menores = 0
cantidad_mayores = 0
edades_menores = 0
edades_mayores = 0
print("Ingrese 999 para terminar")

while not terminar:
    edad = int(input("Ingrese la edad: "))
    if edad == 999:
        terminar = True
    else:
      if 0 <= edad <= 100: #Validar
        if edad <= 18:
            cantidad_menores += 1
            edades_menores += edad
        else: 
          cantidad_mayores += 1
          edades_mayores += edad
      else:
        print("Edad no válida")
        
prom_menores = edades_menores / cantidad_menores
prom_mayores = edades_mayores / cantidad_mayores
        
print(f'Cantidad de menores: {cantidad_menores} y el promedio de edad es: {prom_menores}')
print(f'Cantidad de mayores: {cantidad_mayores} y el promedio de edad es: {prom_mayores}')