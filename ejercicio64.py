""" *Ejercicio 064
Un animal en rehabilitación después de una cirugía requiere ser alimentado y monitoreado en un zoológico. Se alimenta al animal 3 veces al día y se le da de comer hasta que ya no tenga ganas de comer.
Por cada tanda de comida, se debe ingresar la cantidad de alimento en kg (número entero) que se le dio y se le debe preguntar al animal si quiere seguir comiendo ('S', 'N').
Se desea conocer:

    Cuál de las 3 comidas fue la que el animal comió más cantidad de alimento y cuánto fue esa cantidad.
    El total en kg de alimento recibido.
    Promedio de alimento por tanda.

# Escriba la solución aquí 
"""
TANDA = 3
mayor_kg = -float('inf')
total = 0
for comida in range(TANDA):
  print(f' comida {comida +1} de {TANDA}')
  terminar = False
  while not terminar:
    kg = int(input('Ingrese la cantidad de alimento en kg: '))
    if kg > mayor_kg:
      mayor_kg = kg
      comida_mayor_kg = comida +1
    total += kg
    terminar = input('¿Quiere seguir comiendo? (S/N) ').upper() == 'N'
    
print(f'Luego de {TANDA} comidas, el animal comió {total} kg de alimento')
print(f'El promedio de alimento por tanda es {total/TANDA} kg')
print(f'La tanda en la que comió más fue la {comida_mayor_kg} con {mayor_kg} kg')