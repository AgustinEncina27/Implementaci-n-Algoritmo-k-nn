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
        
    def obtenerGraficoKnnConK(self,k):
        return self.algoritmo.algoritmoKnn(k)
    
    def obtenerGraficoPonderadoConK(self,k):
        return self.algoritmo.algoritmoKnnPonderado(k)

    def limpiarDatosAlgoritmo(self):
        self.algoritmo.limpiarDatos()
    
    def limpiarDatos(self):
        self.direccion=''
        self.k=0
        self.coordenadaX=0
        self.coordenadaY=0
    
    def mostrarResultadoAlgoritmo(self):
        return self.algoritmo.algoritmoKnn(33)
    
    def mostrarResultadoAlgoritmoPonderado(self):
        return self.algoritmo.algoritmoKnnPonderado(33)
