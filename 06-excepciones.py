#sirve para captar errores y dar mensajes personalizado es obligatorio cuando se usan parametro
#o entradas de datos
#TRY ejecucion del codigo donde se controlan los errores
#EXCEPT captacion del error y codigo que se ejecuta cuando da el error
#FINALLY sirve para mostrar mensaje en cualquier error o aunque se ejecute bien
"""
try:
    print(3/0)
except: 
    print("Error: Division por cero")
finally:
    print("El programa ha finalizado")

try:
    print(3/1)
except: 
    print("Error: Division por cero")
finally:
    print("El programa ha finalizado")

#MANEJOS DE ERRORES
try:
        print("hola")
except NameError:
    print("variale no esta definida")

try:
    while True:
        print("hola")
except KeyboardInterrupt:
    print("se ha salido forzosamente del programa")
"""
try:
    while True:
        print("hola")
except KeyboardInterrupt:
    print("se ha salido forzosamente del programa")
finally:
    print("se ha terminado la ejecucion del programa")

#generar errores propios
try:
    raise IOError#devuelve un error provocado, cuando nos interese
except IOError:
    print("Ocurrio un error")

