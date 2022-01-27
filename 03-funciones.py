#COMO SE USAN LAS FUNCIONES EN  PYTHON

def saludar():
    print("hola buenas")
def despedir():
    print("gracias por el empleo")
def main():
    saludar()
    despedir()

#esta comparacion siempre es verda dentro del programa
if __name__ == '__main__':
    main()
       
def saludar (nombrecillo, edad_en_numero):
    print(f'hola, {nombrecillo} tienes {edad_en_numero} años')

def main():
    Nombre = input("intoduce tu nombre")
    Edad = int(input("cuantos años tienes"))
    saludar(Nombre,Edad)

if __name__ == '__main__':
    main()

#CLASES EN PYTHON
class coche:
    def __init__(self, marca,modelo,color):
        self.Marca= marca
        self.Modelo= modelo
        self.Color= color
    def MostrarCoche(self):
        print(f"la marca es {self.Marca}, el modelo es {self.Modelo} y el color {self.Color}")

Automovil1 = coche("Opel","Astra","Gris")
Automovil2 = coche("Mercedes","Clase B","Verde")
Automovil3 = coche("Kia","Carens","Blanco")
Automovil4 = coche("volskwagen","Beattle","Rojo")

Automovil1.MostrarCoche()
Automovil2.MostrarCoche()
Automovil3.MostrarCoche()
Automovil4.MostrarCoche()

#cambiar una propiedad de una clase
Automovil3.Color = "Dorado"
Automovil3.MostrarCoche()
#asignar el valor de una propiedad a la propiedad de otro objeto
Automovil3.Color =Automovil1.Color 
Automovil3.MostrarCoche()

class CochesCasa:
    def __init__(self, coche1,coche2,coche3):
        self.C1= coche1
        self.C2= coche2
        self.C3= coche3
    def MostrarCoches(self):
        #print(f"la marca es {self.Marca}, el modelo es {self.Modelo} y el color {self.Color}")
        self.C1.MostrarCoche()
        self.C2.MostrarCoche()
        self.C3.MostrarCoche()


Coche01 = coche("Opel","Astra","Gris")
Coche02 = coche("Mercedes","Clase B","Verde")
Coche03 = coche("Kia","Carens","Blanco")

CochesFamilia = CochesCasa(Coche01,Coche02,Coche03)
CochesFamilia.MostrarCoches()


#CLASES PUBLICAS Y CLASES PRIVADAS

class PuntoPublico:
    def __init__(self,x,y):
        self.X = x
        self.Y = y

#para indicar que la propiedad es privada se ponen dos guiones bajos detras del self.    
class PuntoPrivado:
    def __init__(self,x,y):
        self.__X = x
        self.__Y = y
    def GetX(self):
        return self.__X
    def GetY(self):
        return self.__Y
    def SetX(self,x):
        self.__X=x
    def SetY(self,y):
        self.__Y=y

publico=PuntoPublico(4,6)
privado=PuntoPrivado(7,4)
print()
print(f"valores punto publico x={publico.X} y={publico.Y}")
print(f"valores punto publico x={privado.GetX()} y={privado.GetY()}")

publico.X=2
privado.SetX(6)

print()
print(f"valores punto publico x={publico.X} y={publico.Y}")
print(f"valores punto publico x={privado.GetX()} y={privado.GetY()}")


class OperarValores:
    def __init__(self,v1,v2):
        self.__V1 = v1
        self.__V2 = v2
    def __Sumar(self):
        return self.__V1+self.__V2
    def __Restar(self):
        return self.__V1-self.__V2
    def Operar(self):
        print(f"El resultado de la suma es: {self.__Sumar()}")
        print(f"El resultado de la resta es: {self.__Restar()}")
operarvalores = OperarValores(7,3)
print(operarvalores.Operar)
"""
