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