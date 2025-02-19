'''
Escribí un programa que le pida al usuario ingresar
dos palabras y las guarde en dos variables, y que
luego imprima True si la primera palabra es menor
que la segunda o False si no lo es.
'''

str1 = str(input("Ingresa una palabra: "))
str2 = str(input("Ingresa otra palabra"))

if str1 < str2:
    print(True)
else:
    print(False)