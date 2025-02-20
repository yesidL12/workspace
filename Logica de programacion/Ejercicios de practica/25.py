'''
Escribí un programa que solicite al usuario el
ingreso de dos números diferentes y muestre en
pantalla al mayor de los dos
'''
num1= input("ingresa un número: ")
num2 = input("Ingresa un número: ")
if num1 < num2:
    print(f"{num1} es mayor")
else:
    print(f"{num2} es mayor")