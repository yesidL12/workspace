'''
Escribí un programa para solicitar al usuario tres
números y mostrar en pantalla al menor de los tres.
'''

n1 = int(input("Ingresa un número: "))
n2 = int(input("Ingresa un número: "))
n3 = int(input("Ingresa un número: "))

if n1 < n2:
    if n1 < n3:
        print(f"Menor: {n1}")
    else:
        print (f"Menor: {n3}")
else:
    if n2 < n3:
        print(f"Menor: {n2}")
    else:
        print(f"Menor: {n3}")