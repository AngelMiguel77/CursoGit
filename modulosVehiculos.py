class Vehiculos():
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        self.arranca=False
        self.acelera=False
        self.frena=False
    def arrancar(self):
        self.arranca=True
    def acelerar(self):
        self.acelera=True
    def frenar(self):
        self.frena=True
    def estado(self):#\n para hacer salto de linea
        print ("marca: ", self.marca, "\nmodelo: ", self.modelo, "\nArranca: ", 
                self.arranca, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)
class Furgoneta(Vehiculos):
    def carga(self,cargar):
        self.cargado=cargar
        if(self.cargado):
            return "la furgoneta esta cargada"
        else:
            return "la furgoneta no esta cargada"
class VElectricos():
    def __init__(self):
        self.autonomia=100
        self.carga=True
class BElectrica(Vehiculos,VElectricos):#la primera herencia que se ponga es la que va a primar
    pass
class Moto(Vehiculos):#asi esta clase hereda a la superclase
    hcaballito=""
    def caballito(self):
        self.hcaballito="voy haciendo el caballito"
    def estado(self):#cuando se modifica una funcion de una herencia se sobreescribe y se añade lo nuevo
        print ("marca: ", self.marca, "\nmodelo: ", self.modelo, "\nArranca: ", 
                self.arranca, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena,"\n",self.hcaballito)
