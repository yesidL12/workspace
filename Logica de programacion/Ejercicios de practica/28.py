'''
Escribí un programa que solicite ingresar un nombre de usuario y una contraseña. Si el nombre es “Gwenevere” y la contraseña es “excalibur”, mostrar en pantalla “Usuario y contraseña correctos. Puede ingresar a Camelot”. Si el nombre o la contraseña no coinciden, mostrar “Acceso denegado”
'''

usuario = "Gwenevere"
contraseña = "excalibur"

nombreUsuario = input("Ingresa tu nombre de usuario: ")
ContraseñaUsuario = input("Ingresa tu contraseña: ")

if nombreUsuario == usuario and contraseña == ContraseñaUsuario:
    print("Usuario y contraseña correcto. Puede ingresar a Camelot.")
else:
    print("Acceso denegado.")
