'Operadores'

# Operadores aritméticos
print(f"suma: 10 + 3 = {10 + 3}")
print(f"resta: 10 - 3 = {10 - 3}")
print(f"multlipicación: 10 * 3 = {10 * 3}")
print(f"Divisicón: 10 / 3 = {10 / 3}")
print(f"modúlo: 10 % 3 = {10 % 3}")
print(f"Exponente: 10 ** 3 = {10 ** 3}")
print(f"División entera: 10 // 3 = {10 // 3}")

# Operadores de comparación
print(f"Igualdad: 10 == 3 es {10 ==3 }")
print(f"Desigualdad: 10 != 3 es {10 != 3}")
print(f"Mayor que: 10 > 3 es {10 > 3}")
print(f"Menor que: 10 < 3 es {10 < 3}")
print(f"Mayor o igual que: 10 < 3 es {10 >= 3}")
print(f"Menor o igual  que: 10 <= 3 es {10 <= 3}")

# Operadores lógicos
print(f"AND: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}") # Evalúa que dos condiciones se cumplan
print (f"OR: 10 + 3 == 14 or 5 - 1 == 4 es {10 + 3 == 14 or 5 - 1 == 4}") # Evalua que una de las condiciones se cumplan
print (f"NOT: 10 + 3 == 14 es {not 10 + 3 == 14}") # Es una negación

# Operadores de asignación
myNumber = 11 # asignación
print(myNumber)
myNumber += 1 # Suma y asignación
print(myNumber)
myNumber -= 1 # Resta y asignación
print(myNumber)
myNumber *= 1 # Multiplicación y asignación
print(myNumber)
myNumber /= 1 # División y asignación
print(myNumber)
myNumber %= 1 # Modúlo y asignación
print(myNumber)
myNumber **= 1 # Exponente y asignación
print(myNumber)
myNumber //= 1 # División entera y asignación
print(myNumber)

# Operadores de identidad
'''Nos sirven para comparar el valor no de la variable sino el valor de la posición de la variable
'''
myNewNumber = 1.0
print(f"myNumber is myNewNumber es {myNumber is myNewNumber}" )

# Operadoers de pertenencia
'''Nos ayuda a saber  si algo pertenece a algo
'''
print(f"'u' in 'moure' = {'u' in 'moure'}")
print(f"'b' not in 'moure' = {'b' not in 'moure'}")


"""
Estructuras de control
"""

# Condicionales
myStr = "MoureDev"

if myStr == "MoureDev":
    print("MyStr es 'MoureDev'")
elif  myStr == "Brais":
    print("myStr es 'Brais'")
else:
    print("myStr no es  'MoureDev'")

 # Iterativas

for i in range(11):
    print(i)

i = 0
while i <= 10:
    print(i)
    i +=1

# Manejo de excepciones
try:
    print(10 / 0)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")

''' Extra'''

for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)


for num in range (1, 10):
    if num % 2 == 0 and num % 3 == 0:
        print("FizzBuzz")
    elif num % 2 == 0:
        print("Fizz")
    elif num % 3 == 0:
        print("Buzz")
    else:
        print("No coincide")