#print("en un lugar de la mancha")

#Esto es un comentario de una linea

"""
Esto es un comentario de varias linea

"""

a= "uno"
b= "dos"
c = a +b
print(c)
c = a*3
print(c)

lenguaje = "Superpython"

print(lenguaje[0])
print(lenguaje[1])

"""
ACCESO A ARRAYS
las cadenas de texto son arrays de caracteres puedes acceder a cualquier caracter como si fuese un array.
"""
print(lenguaje[-1])
print(lenguaje[-10])
print(lenguaje[-5])
"""
si seleccionas con numeros negativos se empieza a contar desde el final
"""

"""
METODO DE ACCESO A TIPOS DE VARIABLE
podemos acceder al tipo de la variable con el metodo type()
"""
print(type(c))

numero = 3500
print(type(numero))
"""
METODO DE CONVERSION A ABSOLUTO(NUMEROS)
sirve para sacar el numero absoluto de un numero
"""
d = -3
print(d)
print(abs(d))

"""
METODO para saber
"""

e=15746.435
print(e)
print(float(e))
print(type(float(e)))

"""
METODO DE CONVERSION A ENTERO
"""
print(int(e))
print(int(2.45))
print(int(-4.56))

"""
METODO DE CONVERSION A CADENAS
"""
print(str(2.1))
print(str(235E48))

"""
METODOD DE CONVERSION A BINARIO
"""
print(bin(3))
print(bin(10))
print(bin(254))
"""
METODOD DE CONVERSION A OCTAL
"""
print(oct(3))
print(oct(10))
print(oct(254))
"""
METODOD DE CONVERSION A HEXADECIMAL
"""
print(hex(3))
print(hex(10))
print(hex(254))
"""
METODOD PARA REDONDEAR NUMEROS
puedees meter dos parametros indicando en el primero el numero y en el segundo la longitud de decimales que deseamos
"""
print(round(3.45))
print(round(10.55))
print(round(254.1))
print(round(3.43445,2))
print(round(10.54355,1))
print(round(254.15343,1))

"""
COMPARACION DE CADENAS
la comparacion de cadenas en python se hace caracter por caracter segun su valor en la tabla ascii 
hay que tener en cuenta letras acentuadas porque ocupan una posicion diferente en la tabla ascii
"""
print('barco'>'ancla')
print('árbol'<'ancla')
print('abecedario'<'abadorio')
print('abecedario'<='abecedario')
print('123'<'14')
print('_árbol'<'ancla')

"""
METODO PARA SABER POSICION EN TABLA ASCII
existe un metodo para saber cual es el valor en la tabla ascii del caracter que desees
"""
print(ord('a'))
print(ord('A'))

"""
MODULOS E IMPORTACION DE FUNCIONES Y VARIABLES 
En python hay metodos que no estan disponibles directamente debemos importarlas arriba del codigo
"""
from math import sin 
print(sin(0))
print(sin(1))

import math
#importa todas las funciones del metodo

print(math.floor(3.99))
#metodo para redondear hacia abajo

print(math.ceil(3.01))
#metodo para redondear hacia arriba

numeros=[0.9999,1,2,3,65,89]
print(math.fsum(numeros))
#metodo para sumar todos los elemetos de un array

print(math.trunc(123.456))
#metodo para truncar(hace como el int)

print(math.pow(2,3))
#metodo para elevar un numero se piden dos parametros el numero y la potencia

print(math.sqrt(25))
#metodo para hacer la raiz cuadrada de un numero 

print(math.pi)
#metodo para sacar el nuemro pi con 15 decimales

print(math.e)
#metodo para sacar el nuemro e con 15 decimales

print(dir(math))
#metodo para acceder a todos los metodo de un tipo ej math

print(int(math.exp(2*math.log(3))))
print(round(4*sin(3*math.pi/2)))
print(abs(math.log10(.01)*math.sqrt(25)))
print(round(3.21123*math.log10(1000),3))

"""
MODULOS CURIOSOS

-modulo sys 
    +metodo version(te dice la version de phyton que estas corriendo en el momento)

    +metodo platform (te dice saber la estructura de los directorios estos sirve porque
    las rutas son diferentes en linux y en windows)

    +sys.exit (se corta la ejecucion del codigo)

-modulo os (te devuelve informacion del sistema operativo)
    +getcwd te dice la rutas en la que estas
"""
from sys import version 
print(version)

from sys import platform
print(platform)

import os
#print(os.getcwd())

import sys
#sys.exit()
print("hola")

"""
METODOS
los metodos son funciones especiales 

METODOS PARA CADENAS DE TEXTO
    +TITLE pone todas los primeros caracteres de caada palabra por una mayuscula
    *REPLACE recibe dos parametros la palabra que quieres cambiar y en segundo lugar la palabra nueva que quieres poner
"""
cadena="un ejemplo de cadena"
print(cadena.lower())
print("OTRO EJEMPLO DE CADENA".lower())
print(cadena.title)
print(cadena.replace("ejemplo","cambiado"))

""""
MOSTRAR MENSAJE POR PANTALLA
"""

mensaje= " el resultado de la division es: {0}".format(54)
print(mensaje)

print("{0}".format(1))
print("{0}_{1}".format(1,2))
print("{0}-{1}".format(1,2))
print("{1},_{0}".format(1,2))
print("{0}_1".format(1,2))

"""
INTRODUCION DE DATOS POR LA CONSOLA

cuando ejecutamos una entrada de datos debemos darle un nuemro a la maquina para que siga ejecutandose
en el codigo debemos meter el tipo de dato que queremos recibir y luego poner un input
con el texto que queremos mostrar en pantalla junto a la peticion de dato
"""

"""
b=int(input("introduce un numero entero"))
print(b)
c=print(input(("introduce un texto")))
print(c)
d=print(float(input("introduce un nuemro decimal: ")))
print(d)
"""

"""
BUCLES FOR
los for tienen que ir tabulados y con dos puntos al final de la declaracion
"""
for nombre in["manzana", "pera","platano"]:
    print("hola,{0}".format(nombre))

print()
print()

print("iniciamos bucle for")
print()
for i in [0,1,2,3,4,5]:
    print("imprimo ")
print()
print("terminamos el bucle for")

print("iniciamos bucle for")
print()
for i in []:
    print("imprimo la lista vacia ")
print()
print("terminamos el bucle for")
#no se imprime nada porque la lista esta vacia

print("iniciamos bucle for")
print()
for _ in [0,1,2,3,4,5]:
    print("imprimo ")
print()
print("terminamos el bucle for")
#si no usamos las variables del bucle for ponemos un gion bajo y deja de haber varible

print("iniciamos bucle con vlores utiles")
print()
for k in [1,2,3,4,5]:
    print("n vale {0} y su cubo  {1}".format(k,k**3))
print()
print("terminamos el bucle con vlores utiles")
#con dos astericos tambien elevamos poniendo numero**potencia

print("iniciamos bucle con valores mezclados")
print()
for j in ["hola","me", "llamo","dani",33]:
    print("n tiene el valor {0} ".format(j))
print()
print("terminamos el bucle con valores mezclados")
#en el array podemos meter los valores que queramos 

print("iniciamos bucle con valores mezclados")
print()
for j in 'python':
    print(f"la letra es {j} ")
print()
print("terminamos el bucle con valores mezclados")
"""
CONCATENACION DE CADENA CON VARIABLES
para concatenar variables con cadenas se usa el .format agregandolo al final de la cadena le pasamos los parametros
que estaran ubicados en una cadena segun donde queramos ubicarlos

se puede hacer mas facil poniendo una f al principio de la cadena y ubicando donde queramos las varibles 
entre llaves.
"""

for n in range(1,10):
    print (f"muestro el numero{n}")
#podemos definir rangos dentro del el bucle for para recoorer la cantidad que queramos

"""
print("programam a resolver raices cuadradas")

a=float(input("introduce un numero"))

if a<0:
    print(f"el numero {a} es negativo no lo puedo resolver")
else:
    b=math.sqrt(a)
    print(f"El resultado de la raiz cuadrada de a es {b}")
"""


"""
BUCLES WHILE
"""

i=0
while i<3:
    print(i)
    i+=1
print("hecho")

g=1
while g<50:
    print(g)
    g=1*3+1
print("hecho")







