'''
EScribir una función que calcule el total de 
una factura tras aplicarle el IVA. La función 
debe recibir la cantidad sin IVA y el procentaje
de IVA a aplicar, y devolver el total de la factura. 
Si se invoca la función sin pasarle el porcentajeje de
IVa, deberá aplicar un 21%
'''

def calculaIva(precioNeto, iva) -> int:

    if precioNeto > 0 and iva > 0:
        print( (precioNeto * iva) + precioNeto)
    else:
        print ( (precioNeto * 0.21) + precioNeto)
    
calculaIva(1000,0)
calculaIva(1000, 0.16)
