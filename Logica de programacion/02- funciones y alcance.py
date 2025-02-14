'Funciones'

'''
Es un  bloque de codigo que lo creamos en forma de funcion
para poder reutilizar una acción especifica. proporcionan una
forma de organizar el código en bloques lógicos, para hacer que
el código sea más legible, más limpio y se comentan menos bugs,
sea más fácil de escalar y de mantener.
'''

'Funnciones definidas por el usuario'

# Funciones simple

def greet():
    print("Hola, phyton!")

greet()

# Funciones con retorno
# Son funcones que va a ejecutar una lógica y va a devolver algo

def returnGreet():
    return "Hola, mundo!"

# Puedo guardar el retorno en una variable o no hacerlo
greet = returnGreet()
print(greet)

print(returnGreet())

# Función con un argumento

def argGreet(name):
    print(f"hola,{name}!")

argGreet("yesid")

# Función con argumentos

def argGreet(great,name):
    print(f"{great},{name}!")

argGreet("Hola", "Londoño")
argGreet(name="YesidL", great="Hola") # Esto para que no afecte la posición de los argumentos

# Con un argumento predeterminado

def defaultArgGreet(name="YesidF"):
    print(f"Hola, {name}!")

defaultArgGreet("Yesid")
defaultArgGreet()

# Funciones con argumentos y retorno

def returnArgsGreet(greet, name):
    return f"{greet}, {name}!"

print(returnArgsGreet("Hi", "Yesid"))

# Funciones con returno de varios valores

def multipleReturnGret():
    return "Hola", "phyton"

greet, name = multipleReturnGret()

print(greet)
print(name)

# Funciones con un número variable de argumentos

def variableArgGreet(*names):
    for name in names:
        print(f"Hola,{name}!")

variableArgGreet("Phyton"," Yesid", "Londoño")

# Funciones con un número variable de argumentos con palabra clave

def variableKeyArgGreet(**names):
    for key, value in names.items():
        print(f"Hola,{value} ({key})!")

variableKeyArgGreet(
    Lenguaje="Phyton", 
    name=" Yesid",
    apellido= "Londoño",
    edad= 26
    )

'Funcones dentro de funciones'

def outerFunction():
    def innerFunction():
        print("Función interna: Hello, world!")
    innerFunction()

outerFunction()

'Funciones definidas por el lenguaje (Built-in)'

print(len("MoureDev")) # Len lo que hace es contar
print(type("Yesid")) # Nos dice el tipo de dato
print("MoureDev".upper())


'Variables locales y globales'

globalVariable = "Phyton" # Variable global

print(globalVariable)

def helloPhyton():
    localVar = "Hola" # Variable local. Solo puedo acceder a ella dentro de la función.
    print(f"{localVar}, {globalVariable}")

helloPhyton()

'''
Extra
'''

def ejercicio(str1, str2):
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(str1 + str2)
        elif i % 3 == 0:
            print(str1)
        elif i % 5 == 0:
            print(str2)
        else:
            print(i)
        
ejercicio("yesid", "Londoño")