"""
#abrimos un archivo
archivo=open('mbox.txt','r')
#recoremos el archivo para contar las lineas


contador=0
for linea in archivo:
    contador=contador+1
print(f"lineas contabilizadas {contador}")


#leer el fichero entero
ent=archivo.read()
print(len(ent))

for linea in archivo: 
    if linea.startswith("From:"):
    #startswith para buscar lineas que empiezen por()
        linea = linea.rstrip()
        print(linea)

for linea in archivo:
    linea =linea.rstrip()
    if not linea.startswith("From:"):
        continue
    print(linea)
    

#metodo para buscar cadenas en documentos
for linea in archivo:
    linea =linea.rstrip()
    if linea.find("@uct.ac.za")==-1:
        continue
    print(linea)

NombreFichero = input("introduce el nombre del fichero: ")
archivo= open(NombreFichero)
contador=0
for linea in archivo:
    if linea.startswith("Subject"):
        contador = contador+1
print("hay", contador, "lineas subjects en",NombreFichero)

NombreFichero = input("introduce el nombre del fichero: ")
try:
    archivo= open(NombreFichero)
except:
    print("No se puede abrir el fichero", NombreFichero)
    exit()
    #el exit sirve para detener la ejecucion del archivo
contador=0
for linea in archivo:
    if linea.startswith("Subject"):
        contador = contador+1
print("hay", contador, "lineas subjects en",NombreFichero)
"""
#DIFERENTE USOS DEL PRINT
#print para rutas 
print(r"Cadena de caracteres que no coge caracteres especiales")
#print con tabulacion \t
print("hola \t mundo")
#print de varias lineas
print("""eesfse
efsfsg
dgsgs
dsds""")
#concatenacion de prints
print("hola", end="t")
print("mundo")
