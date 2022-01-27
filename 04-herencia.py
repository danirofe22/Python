
#EJERCICIO DE HERENCIAS DE CLASES CON ELECTRODOMESTICOS
#"""
"""
class Electrodomesticos:

    def __init__(self):
        self.__Encendido = False
        self.__Tension = 0
    def Encender(self):
        self.__Encendido= True
    def Apagar(self):
        self.__Encendido= False
    def Encendido(self):
        return self.__Encendido
    def SetTension(self,tension):
        self.__Tension = tension
    def GetTension(self):
        return self.__Tension

class Lavadora(Electrodomesticos):
    def __init__(self):
        self.__RPM = 0
        self.__Kilos = 0
    def SetRPM(self, rpm):
        self.__RPM=rpm
    def SetKilos(self,kg):
        self.__Kilos=kg
    def MostrarLavadoras(self):
        print()
        print("#########")
        print("LAVADORA:")
        print(f"\tLas RPM son: {self.__RPM}")
        print(f"\tLos Kilos son: {self.__Kilos}")
        print(f"\tLa tension es: {self.GetTension()}")
        if self.Encendido():
            print("\tLa lavadora esta encendida")
        else:
            print("\tLa lavadora no esta encendida")
        print("########")
        print()



lavadora=Lavadora()
lavadora.SetRPM(1200)
lavadora.SetKilos(7)
lavadora.SetTension(220)
lavadora.Encender()

lavadora.MostrarLavadoras()

class Microhondas(Electrodomesticos):
    def __init__(self):
        self.__PotenciaMaxima = 0
        self.__Grill = False
    def SetPotenciaMaxima(self, potenciaMax):
        self.__PotenciaMaxima = potenciaMax
    def SetGrill(self,grill):
        self.__Grill = grill
    def MostrarMicroondas(self):
        #imprimo por pantalla todas las propiedades
        print()
        print("#########")
        print("MICROONDAS: ")
        print(f"\tLa potencia Maxima: {self.__PotenciaMaxima}")
        print(f"\tLa tension es: {self.GetTension()}")

        if self.__Grill == True:
            print("\tEl microondas si tiene grill")
        else:
            print("\tEl microondas no tiene grill")
        
        if self.Encendido():
            print("\tEl microondas esta encendida")
        else:
            print("\tEl microondas no esta encendida")
        print("########")
        print()

#le paso parametros a las funciones para establecer las propiedades
microhondas=Microhondas()
microhondas.SetPotenciaMaxima(1200)
microhondas.SetGrill(True)
microhondas.SetTension(220)
microhondas.Encender()

#ejecuto la funcion mostrarMicroondas del objeto microondas que muestra las propiedades
microhondas.MostrarMicroondas()
"""
#EJERCICIO CON MAS DE UNA HERENCIA
class Hotel:
    def __init__(self):
        self.__NumeroHabitaciones = 0
        self.__Estrellas = 0
    def SetNumeroHabitaciones(self,habs):
        self.__NumeroHabitaciones = habs
    def SetEstrellas(self, estrellas):
        self.__Estrellas = estrellas
    def MostrarHotel(self):
        print("-----------")
        print("hotel: ")
        print(f"\tEstrellas: {self.__Estrellas}")
        print(f"\tNumero de habitaciones:{self.__NumeroHabitaciones}")
        print("-----------")
        
class Restaurante:
    def __init__(self):
        self.__Tenedores = 0
        self.__HoraDeApertura = 0
    def SetTenedores(self, tenedores):
        self.__Tenedores = tenedores
    def SetHoraDeApertura(self, apertura):
        self.__HoraDeApertura = apertura
    def MostrarRestaurante(self):
        print("-----------")
        print("Restaurante: ")
        print(f"\ttenedores: {self.__Tenedores}")
        print(f"\tNumero de habitaciones:{self.__HoraDeApertura}")
        print("-----------")

class Negocio(Hotel,Restaurante):
    def __init__(self):
        self.__Nombre = ""
        self.__Direccion = ""
        self.__Telefono = 0
    def SetNombre(self, nombre):
        self.__Nombre = nombre
    def SetDireccion(self, direccion):
        self.__Direccion = direccion
    def SeTelefono(self, telefono):
        self.__Telefono = telefono
    def MostrarNegocio(self):
        print("-----------")
        print("Negocio: ")
        print(f"\t Nombre: {self.__Nombre}")
        print(f"\t direccion:{self.__Direccion}")
        print(f"\t Telefono:{ self.__Telefono}")
        print("-----------")
        
        self.MostrarRestaurante()
        self.MostrarHotel()

#creo un objeto negocio que herencia de hotel y restaurante
negocio=Negocio()

#Doy valores a las propiedades de los objetos ya que todos heredana negocio
negocio.SetNumeroHabitaciones(200)
negocio.SetEstrellas(4)
negocio.SetTenedores(2)
negocio.SetHoraDeApertura(10)
negocio.SetNombre("negocio")
negocio.SetDireccion("direccion")
negocio.SeTelefono(999999999)

#llamo a la funcion de mostrar datos
negocio.MostrarNegocio()
