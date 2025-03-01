'''
Tenemos la pantalla movil boloqueada. Partiendo
de un PIN_SECRETO, intenatmos desbloquear la pantalla.
Tenemos hasta 3 intentos. SImula el proceso. En caso
de acceder, lanza al usuaario 'login correcto', sino,
'llamando a la policía'
'''

pinSecreto = "CualquierMaricada*"

intentos = 3
while intentos > 0:
    contraseña = str(input("Ingresa tu contraseña: "))
    if contraseña == pinSecreto:
        print("Login correcto")
        break
    else:
        intentos -= 1
        print(f"Contraseña incorrecta. Te quedan {intentos} intentos.")
    
if intentos == 0:
    print("Llamando a la policía")