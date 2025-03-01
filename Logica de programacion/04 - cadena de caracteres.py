'Cadena de Caráteres'

'Operaciones'

# Operación de concatenación

s1 = "Hola"
s2 = "phython"

print(s1 + " " + s2)

# Repetición
print(s1 * 3)

# Indexación
# Básicamente es acceder a un carácter de una cadena de texto
print(s1[0])

# Longitud

print(len(s2))

#Slicing (porción)

print(s2[2:6])
print(s2[2:]) # Se va hasta el final
print(s2[:2]) # va desde el principio hasta el indice 2

#Busqueda
print("Ho" in s1) # para buscar si una cadena de carácteres está contenida en otra cadena de carácteres.

#Reemplazo
print(s1.replace("0", "a")) # "o", es el carácter a reemplazar, y "a", es el carácter que reemplaza.

# División

print(s2.split("t")) # divide la cadena de caracteres desde el carácter mencionado, sin incluir el carácter.

# Mayúsculas y minúsculas y primera letra en mayúsculas
print(s1.upper())
print(s1.lower())
print("yesid londoño".title())# Pone la primera letra de cada palabra en mayúscula.
print("yesid londoño".capitalize()) #Pone la primera letra de la cadena de texto en mayúscula

# Eliminación de espacios al principio y al final

print("yesid londoño".strip() + "@gmail.com") # Elimina espacios al inicio y al final

#Búsqueda al principio y al final
print(s1.startswith("Ho")) # Busca al inicio de la cadena de texto
print(s1.startswith("py"))
print(s1.endswith("la"))# Busca al final de la cadena de texto
print(s1.endswith("thon"))


s3 = "Brais Mpure @moredev"

#Búsqueda de posición
print("Brais Mpure @moredev".find("moure")) #Nos da la posición donde está empezando la cadena que se está búscando

#búsqueda de ocurrencias
#nos dice cuantas veces aparece un criterio de búsqueda
print(s3.lower().count("m"))

#Formateo
print("saludo: {}, lenguaje: {}!".format(s1, s2))

# Interpolacion
print(f"saludo: {s1}, lenguaje: {s2}!")

# Transformación en lista de carácteres
print(list(s3))

# Transformación de lista a cadena
l1 = [s1, ", ", s2, "!"]
print("".join(l1)) # para concatenar resultados de una lista.

# Transformaciones númericas
s4 = "123456"
s4 = int(s4) #Convierte la cadena de texto a números enteros
print(s4)

s5 = "123.456"
s5 = float(s5) # Convierte la cadena de texto a número decimal
print(s5)

# Comprobaciones varias
print(s1.isalnum()) # Comprueba si la cadena tiene letras y números
print(s1.isalpha()) # Comprueba si la cadena es solo letras
print(s1.isnumeric()) # Comprueba si la cadena es solo números

'Extra'

def check(word1, word2):

    # Palíndromos
    print(f"¿{word1} es un palíondromo?: {word1 == word1[::-1]}")
    print(f"¿{word2} es un palíondromo?: {word2 == word2[::-1]}")

    #Anagramas
    print(f"¿{word1} es anagrama de {word2}: {sorted(word1) == sorted(word2)}")
    print(sorted(word1) == sorted(word2))

    # Isogramas
    print(f"¿{word1} es un isograma?: {len(word1) == len(set(word1))}")
    print(f"¿{word2} es un isograma?: {len(word2) == len(set(word2))}")

    word_dict = dict()
    for word in word2:
        word_dict[word] = word_dict.get(word, 0) + 1

    isograma = True
    values = list(word_dict.values())
    isogram_len = values[0]
    for word_count in values:
        if word_count != isogram_len:
            isograma = False
            break
    
    print(isograma)
    print(word_dict)
    

check("radar", "phyton") # Palindromos
check("amor", "roma") # Anagramas
check("radar", "phhytonphytonhytonphyton") # Isogramas