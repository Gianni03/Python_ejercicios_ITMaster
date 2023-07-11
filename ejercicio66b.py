""" 
*Ejercicio 066b
La biblioteca de la ciudad necesita organizar y hacer un recuento de los libros que tiene en sus estantes. Para cada uno de los estantes (usando 'F' para indicar el fin de los estantes), se deben ingresar 15 libros, y para cada libro, se debe ingresar su nombre, género (usando 'I' para Infantil, 'N' para Novela, o 'H' para Historia), y cantidad de páginas (mayor a 0). Una vez que se han ingresado los datos de 1 estante, se debe mostrar por pantalla el nombre del libro con la mayor cantidad de páginas y su cantidad correspondiente. Al finalizar el ingreso de datos de todos los estantes, se deben mostrar la cantidad de libros por género.
"""

CANTEIDAD_DE_LIBROS_POR_ESTANTES = 2
tot_h = 0
tot_i = 0
tot_n = 0

estante = input("Estante: ").upper()
masPaginas = 0

while estante != "F":
  print(f'Proceso de estante {estante}')
  for num_libro in range(CANTEIDAD_DE_LIBROS_POR_ESTANTES):
    nombre = input("Título de libro: ")
    
    genero = input("Géner de libro, novela, infantil, historia (N,I,H): ").upper()
    while genero not in "NIH":
      print("error en el género")
      genero = input("Géner de libro, novela, infantil, historia (N,I,H): ").upper()
    
    paginas = int(input("Cantida de páginas del libro: "))
    
    if genero == "I":
      tot_i += 1
    elif genero == "H":
      tot_h += 1
    else:
      tot_n += 1
    
    if paginas > masPaginas:
      masPaginas = paginas
      nombreLibroMayor = nombre
    # fin for
  print(f'El libro con as páginas es {nombreLibroMayor} con {masPaginas}')
  estante = input("Estante: ").upper()
# fin while

print(f'Total de libros de Historia: {tot_h}')
print(f'Total de libros infantiles: {tot_i}')
print(f'Total de libros de novelas: {tot_n}')