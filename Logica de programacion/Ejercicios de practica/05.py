'''
Escribe un programa que pide 
al usuario un número del 1 al 7
y determine el día de la semana correspondiente
'''
dia = int(input("Ingrese un número del 1 al 7: "))

if dia == 1:
    print("Lunes")
elif dia == 2:
    print(" Martes")
elif dia == 3:
    print(" Miercoles")
elif dia == 4:
    print(" Jueves")
elif dia == 5:
    print(" Viernes")
elif dia == 6:
    print(" Sábado")
elif dia == 7:
    print(" Domingo")
else:
    print("No es un día de la semana")