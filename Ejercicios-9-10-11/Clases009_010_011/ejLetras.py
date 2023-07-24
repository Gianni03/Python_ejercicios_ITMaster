FILAS = 9
COLUMNAS = 9

PFILA = 0 # primera fila
PCOLU = 0 # primera columna
UFILA = FILAS - 1 # ultima fila
UCOLU = COLUMNAS - 1 # ultima columna
MFILA = FILAS//2 # mitad de filas
MCOLU = COLUMNAS//2 # mitad de columnas

print("Letra O")
print()
for f in range(FILAS):
  for c in range(COLUMNAS):
    # print(f'{f},{c }')
    if f == 0 or f == FILAS - 1 or c == 0 or c == COLUMNAS - 1:
      print('*',end='')
    else:
      print(' ',end='')
  print()
  
print()

print("Letra L") 
print() 
for f in range(FILAS):
  for c in range(COLUMNAS):
    if f == FILAS - 1 or c == 0:
      print('*',end='')
    else:
      print(' ',end='')
  print()
  
print()

print("Letra S")
print()  
for f in range(FILAS):
  for c in range(COLUMNAS):
    if f == PFILA or f == UFILA or f == MFILA or \
      (f >= MFILA and c == UCOLU) or (f<= MFILA and c == PCOLU): 
      print('*',end='')
    else:
      print(' ',end='')
  print()
  
print()

print("Letra N")
print()  
for f in range(FILAS):
  for c in range(COLUMNAS):
    if f == c or c == PCOLU or c == UCOLU: 
      print('*',end='')
    else:
      print(' ',end='')
  print()
  
print()

