'''
EScribir una función que calcule el total de 
una factura tras aplicarle el IVA. La función 
debe recibir la cantidad sin IVA y el procentaje
de IVA a aplicar, y devolver el total de la factura. 
Si se invoca la función sin pasarle el porcentajeje de
IVa, deberá aplicar un 21%
'''

def calculaIva():
    precioNeto = int(input("Ingrese el valor neto a pagar:"))
    iva = float(input("Ingrese el porcentaje de iva a cobrar:"))

    if iva > 0:
        print((precioNeto * iva) + precioNeto)
    else:
        print((precioNeto * 0.21) + precioNeto)

calculaIva()