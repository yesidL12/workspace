'''
Escribí un programa que solicite al usuario que
ingrese cuántos shows musicales ha visto en el
último año y almacene ese número en una variable. A
continuación mostrar en pantalla un valor de verdad
(True o False) que indique si el usuario ha visto
más de 3 shows.
'''

showsVistos = int(input("Ingresa la cantidad de shows visto en el último año: "))

if showsVistos > 3:
    print(True)
else:
    print(False)