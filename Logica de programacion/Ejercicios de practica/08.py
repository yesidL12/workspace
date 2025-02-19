'''
Escribe un programa que almacene
un número y pida al usuario adivinarlo.
'''
import random
numSecreto = random.randint(1, 20) # GEnera un número aleatorio

numUsuario = int(input("Ingresa un número del 1 al 20: "))

if numUsuario == numSecreto:
    print("Acertaste!")
else:
    print( f"EL número es: {numSecreto} \n Sigue intentando")