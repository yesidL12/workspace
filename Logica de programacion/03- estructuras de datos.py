'Estructuras de datos'

'Listas'

''' Es una estructura ordenada donde nosotros
guardamos cada uno de los elementos de forma ordenada'''

myList = ["brais", "Bl4ack", "Wolfy", "Visionos"]
print(myList)
myList.append("Castor") # añade datos(Inserción)
myList.append("Castor") 
print(myList)
myList.remove("brais") # Elimina datos
print(myList)
print(myList[1]) # Acceso - Acceder a uno o varios datos de la lista
myList[1] = "Cuervillo" # Actualización
print(myList)
myList.sort() # Ordenación
print(myList)
print(type(myList))

'Tuplas'

''' Las tuplas no se pueden modificar. Es decir,
como creemos lo tupla inicialmente asi se queda.
Solo podría hacer operaciones de acceso'''

MyTuple = ("Brais", "Moure", "MoureDev", "36")
print(MyTuple[1])
print(MyTuple[3])
MyTuple = tuple(sorted(MyTuple)) #Ordena la tupla, pero hay que indicarle el "tuple", para que no se convierta en una lista
print(type(MyTuple))
print(MyTuple)

'Sets'

'''Es otro tipo de estructura, por definición es
una estructura desordenada. No cuenta con 
operaciones de acceso. No se duplican los datos'''

mySets = {"Brais", "Moure", "MoureDev", "36"}
print(mySets)
mySets.add("mouredev@gmail.com") # Inserción
mySets.add("mouredev@gmail.com") 
mySets.remove("Moure") # Eliminación
mySets.update # Lo que hace es ampliar los datos que tenemnos en el set
mySets = set(sorted(mySets)) # El set no se puede ordenar
print(mySets)
print(type(mySets))

'Diccionario'


myDict: dict = { # La forma en que metemos los datos es: clave - valor
"name":"Brais", 
"subname":"Moure", 
"alias": "MoureDev", 
"edad": "36"
}

myDict["email"] = "mouredev@gmail.com" #inserción
print(myDict["name"]) # Acceso
myDict["edad"] = "37" # Actualización
myDict = dict(sorted(myDict.items())) # Ordenación
# del myDict["subname"] # Eliminación
print(myDict)
print(type(myDict))

'Extra'

def myAgenda():

    agenda = {} # Diccionario vacio donde se guardará la información que de el usuario

    while True: # Bucle infito

        #opciones del usuario
        print("")
        print("1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        option = input("\nSelecciona una opción: ") # El usuario seleciona que desea hacer

        match option: # Hace las veces de Switch
            case "1":# Buscar contacto
                name = input("Introduce el nombre del contacto a buscar: ")
                if name in agenda:
                    print(
                        f"El número del teléfono de {name} es {agenda[name]}.")
                else:
                    print(
                        f" El contacto {name} no existe"
                    )
                #pass # Evita errores ya que impide que se ejhecute todo el bucle
            case "2": #insertar contacto
                name = input("\n Introduce el nombre del contacto: ")
                phone = input("\n Introduce el teléfono del contacto: ")
                #Hacemos la validación de que sea un numnero de telefono valido
                if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
                    agenda[name] = phone
                else:
                    print(
                        "Debes introducir un número de telefono valido")
            case "3": # Actualización de contacto
                name = input("Introduce el nombre del contacto a actualizar: ")
                if name in agenda:
                    phone = input("\nIntroduce el teléfono del contacto: ")
                    if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
                        agenda[name] = phone
                    else:
                        print("Debes introducir un número de teléfono valido")
                else:
                    print(
                        f"El contacto {name} no existe"
                    )
            case "4": # Eliminar contacto
                name = input("Introduce el nombre del contacto a eliminar: ")
                if name in agenda:
                    del agenda[name]
                    print(
                        f"El contacto {name} ha sido eliminado"
                    )
                else:
                    print(
                        f"El contacto {name} no existe"
                    )
            case "5":
                print("Saliendo de la agenda.")
                break # Lo que hace es aslir del bucle que se está ejecutando.
            case _: # Opción por Default
                print("Opción no valida. ELige una opción del 1 al 5.")

myAgenda()