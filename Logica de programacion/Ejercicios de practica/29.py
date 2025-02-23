'''
Escribí un programa que permita saber si un año es bisiesto. Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.
'''

año = int(input("Ingresa un año: "))

if año % 4 ==0:
    if año % 100 != 0 or año % 400 == 0:
        print(f"Año {año} es Bisiesto")
    else:
        print("No bisiesto")
else:
    print("No es Bisiesto")