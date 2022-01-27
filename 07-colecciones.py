#COLECCIONES
#Las colecciones de python son muy poderosas se usasn para el bigData junto con R
#El primer tipo de colecciones son las listas
"""
#LISTAS
#coleciones de cualquier tipo de dato
numeros = [1,2,3,4]
datos = [4, "una cadena", -15, 3.14]
print(datos[0])#primer elemento
print(datos[-1])#ultimo elemnto
#slicing
print(datos[-2:])#los dos ultimos
numeros +=[5,6,7,8]
print(numeros)

pares = [0,2,4,5,8]
pares[3]=6
print(pares)

pares.append(12)
print("La longitud de la lista de 'pares' es:",len(pares))
#Slicing coger trozos de una cadena [0:2] cogeria desde cero hasta 1 el numero anterior el dos no se incluye
lenguaje="superphyton"
print(lenguaje[0:2])
print(lenguaje[2:-1])
print(lenguaje[:2])
print(lenguaje[:2]+lenguaje[:2])
print(lenguaje[:5]+"P"+lenguaje[:5])

lenguaje="superphyton"

listaLenguaje = list(lenguaje)
lenguaje2 = "".join(listaLenguaje)
print(lenguaje2)

letras = ["a","b","c","d","e","f"]
print(letras[:3])
print(letras[2:])
letras[:3] = ["A","B","C"]
print(letras)

letras[:3] = []
print("la nueva lista de letras es: ",letras)
letras = []
print("La lista de letras vacia es: ",letras)

a =[1,2,3]
b =[4,5,6]
c =[7,8,9]
r = [a,b,c]
print(r)
print(r[-1])
#como se ha convertido en forma de matriz podriamos hacer:
print(r[0][0])
print(r[1][1])
print(r[-1][-1])

#TUPLAS
#En una tupla no se puede modificar su valor
MiPrimerTupla= (100, "hola", [1,2,3,4], -50)
print("El valor de la tupla es: ", MiPrimerTupla)
print("El primer valor de la tupla es: ", MiPrimerTupla[0])
print("El ultimo valor de la tupla es: ", MiPrimerTupla[-1])
print("Utilizando Slicing, los dos primeros valores son:", MiPrimerTupla[:2])
print("usando la notacion de matrices:", MiPrimerTupla[2][0])
print("Conocer la longuitud de la tupla", len(MiPrimerTupla))
print("Conocer la logitud del 3er valor de la tupla", len(MiPrimerTupla[2]))

print("Cuantas veces aparece el elemento con valor 100", MiPrimerTupla.count(100))
print("Cuantas veces aparece el elemento con valor k", MiPrimerTupla.count("k"))
#redeclaramos la tupla
MiPrimerTupla=(100,100,"hola",100,[1,2,3,4],-50,"b","b")
print("Cuantas veces aparece el elemento con valor 100", MiPrimerTupla.count(100))
#no se puede usar metodos de modificacion de listas porque las tuplas son imutables

#CONJUTOS: SON COLECCIONES DESORDENADAS
conjunto = {1,2,3}
print(conjunto)
conjunto.add(4)
print(conjunto)
conjunto.add(0)
print(conjunto)
conjunto.add("H")
print(conjunto)
conjunto.add("A")
print(conjunto)
conjunto.add("Z")
print(conjunto)

personas = {"ale", "kirzah"}
print("se encuentra ale en el conjunto?","ale"in personas)
print("se encuentra Maria en el conjunto?","Maria"in personas)

#Los conjuntos no perminte elementos duplicados
prueba = {"ale","ale","ale"}
print(prueba)

#Pasar de lista a 
lista = [1,2,3,4,5,1,2,3,4,5]
print(lista)
tonta=set(lista)
print(tonta)
listorra = list(tonta)
print(listorra)

listorra2 = list(set(lista))
print(listorra2)

#DICCIONARIOS
#No siempre estan ordenados y los acentos caen mal
diccionarioVacio={}
print(diccionarioVacio)
print(type(diccionarioVacio))

colores= {"amarillo":"yellow","azul":"blue","verde":"green","rojo":"red"}

print(colores)
print(colores["rojo"])
print(colores["amarillo"])

numeros= {10:"diez",20:"veinte",15:"quince",8:"ocho"}
print(numeros[15])
print(numeros[20])

colores["amarillo"]= "gold"
print(colores)

del(colores["amarillo"])
print(colores)

#recorrer un diccionario
for clave, valor in colores.items():
    print(clave, valor)

#Lo mas interesante es meter los diccionarios dentro de las listas
personajes=[]
p={"nombre":"gandalf","clase":"mago","raza":"humano"}
personajes.append(p)
p={"nombre":"legolas","clase":"arquero","raza":"Elfo"}
personajes.append(p)
p={"nombre":"Gimil","clase":"guerrero","raza":"enano"}
personajes.append(p)

for p in personajes:
    print(p["nombre"],p["clase"],p["raza"])
"""