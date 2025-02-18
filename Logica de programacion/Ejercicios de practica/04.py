'''
Escribe un programa que pida al usuario una nota
y determine  si es aprobatoria (mayor o igual a 7)
'''

nota = float(input("Ingrese su nota:"))
if nota >= 7:
    print(f"Aprobó el curso con una nota de : {nota}")
else:
    print("No aprobó el curso")