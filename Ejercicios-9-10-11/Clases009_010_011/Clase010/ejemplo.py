import random

def obtener_fecha_random(anio):
  m = random.randint(1,12)
  d = random.randint(1,obtener_cantidad_de_dias_del_mes(m, anio))
  return anio*10000 + m*100 + d # aaaammdd

def es_bisiesto(anio:int):
  return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)
  
def obtener_cantidad_de_dias_del_mes(m, anio):
  cantidad = 31
  if m in (4,6,9,11):
    cantidad = 30
  elif m == 2:
    if es_bisiesto(anio):
      cantidad = 29
    else:
      cantidad = 28
  return cantidad

def el_anio(f):
  """ 
  Retorna el año de una fecha \n
  aaaa <= mmdd
  """
  return f//10000 # aaaa <= mmdd

def el_mes(f):
  return (f//100)%100  # mm <= dd

def el_dia(f):
  return f%100 # dd <= mm

def str_fecha(f):
  anio = el_anio(f)
  dia = el_dia(f)
  mes = el_mes(f)
  return f"{dia:02}/{mes:02}/{anio:04}"

"""
Progrma principal  
"""
def main():
  fecha =  obtener_fecha_random(2023)# aaaammdd
  print(str_fecha(fecha))
  



main() # Call the main function, funcion principal



