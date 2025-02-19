'''
Escribí un programa que le solicite al usuario su
edad y la guarde en una variable. Que luego solicite
la cantidad de artículos comprados en una tienda y
la guarde en otra variable. Finalmente, mostrar en
pantalla un valor de verdad (True o False) que
indique si el usuario es mayor de 18 años de edad y
además compró más de 1 artículo.
'''

edad = int(input("Ingresa tu edad: "))
articulos = int(input("Ingresa la cantidad de articúlos que compraste: "))

if edad > 18 and articulos > 1:
    print(True)
else:
    print(False)