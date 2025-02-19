'''
Esribe un programa que solicite un
número con decimales en una variable.
A continuación, el programa debe solicitar
al usuario que ingrese un número entero y
guardarlo en otra variable. En una tercera 
variable se deberá guardar el resultado de la
suma de los dos números ingresados por el usuario.
Por último, se debe mostrar en pantalla el texto
"El resultado de la suma es [sumna]"
'''

num1 = float(input("Ingresa un número decimal, por favor..."))
num2 = int(input("Ingresa un número entero, por favor..."))
resultado = (num1 + num2) # Resutado de los dos números
print(f"EL resultado de la suma es: {resultado}")
