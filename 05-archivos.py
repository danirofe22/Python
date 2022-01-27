import os
#con el metodo open abrimos el archivo y le pasamos dos parametros la ruta y como quieres 
#ejecutar el archico w para escribir
archivo= open("PrimerArchivo.txt","w")
#con el metodo write escribimos el archivo
archivo.write("Mi primera linea del archivo\n")
archivo.write("Mi segunda linea del archivo\n")
archivo.write("Mi tercera linea del archivo\n")
#metodo para cerrar el archivo(ahi que cerrarlo siempre para que guarde los cambio)
archivo.close()
#con el metodo getcwd() accedemos a la ruta del directorio actual
#para abrir un archivo ponemos \\ entre comillas para que se añada la barra para acceder al siguiente nivel 
rutaActual = os.getcwd()
print(rutaActual)

archivo2= open("PrimerArchivo.txt","r")
archivoCompleto= archivo2.read()
print(archivoCompleto)
archivo2.close()

archivo= open("PrimerArchivo.txt", "a")
archivo.write("Mi cuarta linea del archivo\n")
archivo.write("Mi quinta linea del archivo\n")
archivo.write("Mi sexta linea del archivo\n")
archivo.close()

archivo3 = open("TercerArchivo.txt", "w", encoding="cp1252")
archivo3.write("mi primera óracion")
archivo3.close()

archivo = open("PrimerArchivo.txt","r")

contador = 0 
while 1: 
    caracter = archivo.read(1)
    if caracter=='':
        break
    contador+=1

archivo.close()
print("Numero Caracteres: ", str(contador))

