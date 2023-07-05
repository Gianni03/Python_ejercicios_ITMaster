""" *Ejercicio 059
Escribir un programa para un negocio de venta de granos que desea controlar las ventas realizadas. De cada venta ingresa el importe total y un código que indica la forma de pago. Los códigos puede ser:

    C: cheque, 20% de recargo.
    E: efectivo, 10% de descuento.
    T: con tarjeta, 12% de recargo.
    Se debe ingresar una F para finalizar el día de venta y arrojar los siguientes totales.
    
    | Forma de Pago | Total |
    | ---------------- | --------- | 
    | Efectivo en Caja | xxxx.xx|
    |Tarjeta/Crédito| xxxx.xx |
    | Cheques | xxxx.xx|
    |TotaldeVenta| xxxx.xx |

"""

RECARGO_CHEQUE = 0.2
DESCUENTO_EFECTIVO = 0.1
RECARGO_TARJETA = 0.12

tot_efec = 0
tot_tarj = 0
tot_che = 0
tot_gen = 0

codigo = input("ingrese el codigo de pago: << C,E,T,F(FIN) >>").upper()
while codigo != "F":
  importe = float(input("ingrese el importe de la venta: "))
  if codigo == "C":
    
    








str_totales = f"""
    | Forma de Pago    |  Total      |
    | ---------------- | ----------- | 
    | Efectivo en Caja | $ {tot_efec}|
    | Tarjeta/Crédito  | $ {tot_tarj}|
    | Cheques          | $ {tot_che} |
    | TotaldeVenta     | $ {tot_gen}   |
"""