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
    
    def mostrarResultadoAlgoritmo(self,k):
        x, y, colormap, listaLeyendas = self.algoritmo.algoritmoKnn(k)
        return (x,y,colormap,listaLeyendas)
    
    def mostrarResultadoAlgoritmoPonderado(self,k):
        xPonderado, yPonderado, colormapPonderado, listaLeyendasPonderado = self.algoritmo.algoritmoKnnPonderado(k)
        return (xPonderado, yPonderado, colormapPonderado, listaLeyendasPonderado)
    
    def obtenerGraficoKnnConK(self,k):
        self.algoritmo.algoritmoKnn(k)

    def obtenerGraficoPonderadoConK(self,k):
        return self.algoritmo.algoritmoKnnPonderado(k)

    def inicilizarGraficoBarras(self):
        self.algoritmo.obtenerKOptimo()
        self.algoritmo.obtenerKOptimoKnnPonderado()

    def mostrarGraficoBarras(self):
        return self.algoritmo.graficarBarras()

    def mostrarGraficoBarrasPonderado(self):
        return self.algoritmo.graficarBarrasKnnPonderado()
        
