from leer_archivo import Algoritmo

class Controlador():
    def __init__(self):
        self.direccion=''
        self.k=0
        self.coordenadaX=0
        self.coordenadaY=0
        self.algoritmo=None

    def obtenerDatos(self,direccion):
        self.algoritmo=Algoritmo()
        self.algoritmo.leerArchivo(direccion)
        self.algoritmo.calcularMatrizDistancias()
    
    def obtenerK(self,k):
        self.k=k
    
    def limpiarDatos(self):
        self.direccion=''
        self.k=0
        self.coordenadaX=0
        self.coordenadaY=0
    
    def mostrarResultadoAlgoritmo(self):
        return self.algoritmo.algoritmoKnn(33)
    
    def mostrarResultadoAlgoritmoPonderado(self):
        return self.algoritmo.algoritmoKnnPonderado(33)
