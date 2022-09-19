from turtle import st
import matplotlib.pyplot as plt
import csv
import math
import operator

class Algoritmo:

    def __init__(self):
        self.x = []
        self.y = []
        self.clase = []
        self.contador=0
        self.colormap=[]
        self.k=0
        self.nuevoPunto=[]
        self.distanciasOrdenadas=[]
        self.vecino=[]

    #Lee el csv y guarda los datos en las listas x, y, clase
    def leerArchivo(self,nombreArchivo):
        with open(nombreArchivo, 'r') as file:
            plots = csv.reader(file, delimiter = ',')
            for row in plots:
                contador=contador+1
                if(contador!=1):
                    self.x.append(float(row[0]))
                    self.y.append(float(row[1]))
                    self.clase.append(float(row[2]))
    
    #Define el mapa de colores para el grafico, habria que hacerlo mas general porque ahora esta hecho para 3 clases
    def definirMapaDeColores(self):
        for color in self.clase:
            if(color==0):
                self.colormap.append('r')
            if(color==1):
                self.colormap.append('g')
            if(color==2):
                self.colormap.append('b')
    
    #Define el atributo K
    def setK(self,k):
        self.k=k

    #Define el punto que se va a analizar
    def definirNuevoPunto(self,xNuevo,yNuevo):
        self.nuevoPunto=[xNuevo,yNuevo]

    #Calcula la distancia del punto nuevo contra todos los puntos del dataset
    def calcularDistancia(self):
        distancia=[]
        for punto in range(600):
            distanciaPunto = math.sqrt((self.nuevoPunto[0]-self.x[punto])**2+(self.nuevoPunto[1]-self.y[punto])**2)
            distancia.append([distanciaPunto,self.x[punto],self.y[punto],self.clase[punto]])
        self.distanciasOrdenadas = sorted(distancia, key=lambda x:x[0])

    #Define de que clase es el nuevo punto ingresado
    def obtenerClaseNuevoPunto(self):
        vecinos={}
        for cantidadK in range(self.k):
            if(self.distanciasOrdenadas[cantidadK][3] in vecinos):
                vecinos[self.distanciasOrdenadas[cantidadK][3]]=vecinos[self.distanciasOrdenadas[cantidadK][3]]+1
            else:
                vecinos[self.distanciasOrdenadas[cantidadK][3]]=1
        self.vecino = sorted(vecinos.items(), key=operator.itemgetter(1))
        self.vecino.reverse()

    #Genera el grafico
    def graficarResultado(self):
        plt.scatter(self.x, self.y, c=self.colormap)
        colorNuevoPunto=''
        if(self.vecino[0][0]==0):
            colorNuevoPunto = 'red'
        if(self.vecino[0][0]==1):
            colorNuevoPunto = 'green'
        if(self.vecino[0][0]==2):
            colorNuevoPunto= 'blue'
        plt.scatter(self.nuevoPunto[0],self.nuevoPunto[1], color=colorNuevoPunto)
        plt.annotate("Nuevo Punto", (self.nuevoPunto[0],self.nuevoPunto[1]))
        plt.axvline(x=0, c="black")
        plt.axhline(y=0, c="black")
        plt.axis('equal')
        plt.show()