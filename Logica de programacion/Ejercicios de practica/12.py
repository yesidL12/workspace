'''
Escribí un programa que solicite al usuario dos números
y los almacene en dos variables. En otra variable, almacená
el resultado de la suma de esos dos números y luego mostrá ese
resultado en pantalla.
A continuación, el programa debe solicitar al usuario que ingrese
un tercer número, el cual se debe almacenar en una nueva variable.
Por último, mostrá en pantalla el resultado de la multiplicación de este
nuevo número por el resultado de la suma anterior.
'''
num1 = int(input("ingresa un número, por favor..."))
num2 = int(input("ingresa otro número, por favor..."))
suma = (num1 + num2 )
print(f"suman: {suma}")
num3 = int(input("Ingresa otro número, por favor..."))
print(f"Multiplicación de la suma por el último número: {suma * num3}")