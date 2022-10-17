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
    
    def mostrarResultadoAlgoritmo(self,k):
        x, y, colormap = self.algoritmo.algoritmoKnn(k)
        return (x,y,colormap)
    
    def mostrarResultadoAlgoritmoPonderado(self,k):
        xPonderado, yPonderado, colormapPonderado = self.algoritmo.algoritmoKnnPonderado(k)
        return (xPonderado, yPonderado, colormapPonderado)
    
    def obtenerGraficoKnnConK(self,k):
        self.algoritmo.algoritmoKnn(k)

    def obtenerGraficoPonderadoConK(self,k):
        return self.algoritmo.algoritmoKnnPonderado(k)

    def mostrarGraficoBarras(self):
        self.algoritmo.obtenerKOptimo()
        return self.algoritmo.graficarBarras()

    def mostrarGraficoBarrasPonderado(self):
        self.algoritmo.obtenerKOptimoKnnPonderado()
        return self.algoritmo.graficarBarrasKnnPonderado()
        
