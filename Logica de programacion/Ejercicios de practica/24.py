'''
Escribí un programa que, dado un número entero,
muestre su valor absoluto. Recordá que, para los
números positivos su valor absoluto es igual al
número (el valor absoluto de 52 es 52), mientras
que, para los negativos, su valor absoluto es el
número multiplicado por -1 (el valor absoluto de -52
es 52).
'''

num1 = int(input("Ingresa un número: "))
if num1 < 0:
    print(num1 * -1)
else:
    print(num1)