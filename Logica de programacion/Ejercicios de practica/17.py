'''
Escribí un programa que solicite al usuario el
ingreso de un texto y almacene ese texto en una
variable. A continuación, mostrar en pantalla la
primera letra del texto ingresado. Luego, solicitar
al usuario que ingrese un número positivo menor a la
cantidad de caracteres que tiene el texto que
ingresó (por ejemplo, si escribió la palabra “HOLA”,
tendrá que ser un número entre 0 y 4) y almacenar
este número en una variable llamada indice. 
Mostrar en pantalla el carácter del texto ubicado en la posición dada por indice.
'''

str1 = str(input("Ingresa un texto: "))
print (f"Tu texto tiene", len(str1), "carácteres")
print(str1[0])
index = int(input("Ingresa un número entero menor a la cantidad de carácteres de tu texto: "))
print(str1[index])