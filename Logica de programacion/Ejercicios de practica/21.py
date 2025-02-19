'''
Escribí un programa que, dada una cadena de texto 
 el usuario, imprima True si la cantidad de
 caracteres en la cadena es un número par, o False
 si no lo es.
'''

str1 = str(input("Ingresa un texto: "))
print(len(str1))

if len(str1) % 2 == 0:
    print(True)
else:
    print(False)