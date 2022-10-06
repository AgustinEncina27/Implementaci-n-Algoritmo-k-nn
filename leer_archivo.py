from turtle import st
import matplotlib.pyplot as plt
import csv
import math
import operator
import numpy

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
        self.vecinoPonderado=[]
        self.matrizDistancia=[]

    #Lee el csv y guarda los datos en las listas x, y, clase
    def leerArchivo(self,nombreArchivo):
        with open(nombreArchivo, 'r') as file:
            plots = csv.reader(file, delimiter = ',')
            for row in plots:
                self.contador=self.contador+1
                if(self.contador!=1):
                    self.x.append(float(row[0]))
                    self.y.append(float(row[1]))
                    self.clase.append(float(row[2]))
        
    def obtenerKOptimo(self):
        listaK=[]
        for a in range(600):
            listaK.append(0)
        bandera=False
        cantidadClases=[0.0,1.0,2.0]
        for i in range(1,600):
            self.k=i
            for fila in range(599):
                resultadoClase = self.obtenerClaseNuevoPunto(fila)
                if(len(resultadoClase)>1):
                    if(resultadoClase[0][1]==resultadoClase[1][1]):
                        bandera=False
                    else:
                        bandera=True
                else:
                    bandera=True
                if(resultadoClase[0][0]==self.clase[fila] and bandera):
                    listaK[i-1] = listaK[i-1] + 1
                bandera=False
            print("Contando")
            print(i)
        print(listaK)
        max_value = max(listaK)
        print('Maximum value:', max_value, "At index:", listaK.index(max_value))

    
    def calcularMatrizDistancias(self):
        self.matrizDistancia =  [ [ None for y in range(self.contador-1) ] for x in range( self.contador-1) ]   
        for fila in range(self.contador-1):       
            for columna in range(fila,self.contador-1):
                if(fila==columna):
                    self.matrizDistancia[fila][columna]=[0]
                else:
                    self.matrizDistancia[fila][columna]=[math.sqrt(((self.x[fila]-self.x[columna])**2+(self.y[fila]-self.y[columna])**2)),self.x[columna],self.y[columna],self.clase[columna]]
                    self.matrizDistancia[columna][fila]=[self.matrizDistancia[fila][columna][0],self.x[fila],self.y[fila],self.clase[fila]]
                    #self.matrizDistancia[fila][columna]
        #for fila in self.matrizDistancia:
        #    for valor in fila:
        #        print("\t", valor, end=" ")
        #print()
        print("------------------------------------------------")
        contadorAuxiliar=1
        filaAOrdenar=[]
        for fila in range(self.contador-1):
            for aux in range(self.contador-1):
                filaAOrdenar.append(self.matrizDistancia[fila][aux])
            filaOrdenada = sorted(filaAOrdenar, key=lambda x:x[0])
            for auxiliarOrdenar in range(len(filaOrdenada)):
                self.matrizDistancia[fila] = filaOrdenada
                #self.matrizDistancia[auxiliarOrdenar+contadorAuxiliar][columna]= -1
                #self.matrizDistancia[columna][auxiliarOrdenar+contadorAuxiliar]
            filaAOrdenar=[]
            contadorAuxiliar=contadorAuxiliar+1
        #for fila in self.matrizDistancia:
        #    for valor in fila:
        #        print("\t", valor, end=" ")
        #    print()
        print("++++++++++++++++++++++++++++++++++++++++++++")

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
        print(self.distanciasOrdenadas)

    #Define de que clase es el nuevo punto ingresado
    def obtenerClaseNuevoPunto(self,fila):
        vecinos={}
        #for a in cantidadClases:
            #vecinos[a]=0
        for cantidadK in range(self.k):
            auxiliar=self.matrizDistancia[fila][cantidadK+1][3]
            #for clave in vecinos.keys():
                #if(self.matrizDistancia[fila][cantidadK+1][3]==clave):
                    #vecinos[self.matrizDistancia[fila][cantidadK+1][3]]=vecinos[self.matrizDistancia[fila][cantidadK+1][3]]+1
            if(auxiliar in vecinos):
                vecinos[auxiliar]=vecinos[auxiliar]+1
            else:
                vecinos[auxiliar]=1
        vecinoOrdenado = sorted(vecinos.items(), key=operator.itemgetter(1),reverse=True)
        return vecinoOrdenado

    def obtenerClaseNuevoPuntoPonderado(self,fila):
        vecinos={}
        #for a in cantidadClases:
            #vecinos[a]=0
        for cantidadK in range(self.k):
            #for clave in vecinos.keys():
                #if(self.matrizDistancia[fila][cantidadK+1][3]==clave):
                    #vecinos[self.matrizDistancia[fila][cantidadK+1][3]]=vecinos[self.matrizDistancia[fila][cantidadK+1][3]]+(1/((self.matrizDistancia[fila][cantidadK+1][0])**2))
            auxiliar=self.matrizDistancia[fila][cantidadK+1][3]
            if(auxiliar in vecinos):
                vecinos[auxiliar]=vecinos[auxiliar]+(1/((self.matrizDistancia[fila][cantidadK+1][0])**2))
            else:
                vecinos[auxiliar]=(1/((self.matrizDistancia[fila][cantidadK+1][0])**2))
        vecinoOrdenadoPonderado = sorted(vecinos.items(), key=operator.itemgetter(1),reverse=True)
        return vecinoOrdenadoPonderado

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

    def graficarResultadoPonderado(self):
        plt.scatter(self.x, self.y, c=self.colormap)
        colorNuevoPunto=''
        if(self.vecinoPonderado[0][0]==0):
            colorNuevoPunto = 'red'
        if(self.vecinoPonderado[0][0]==1):
            colorNuevoPunto = 'green'
        if(self.vecinoPonderado[0][0]==2):
            colorNuevoPunto= 'blue'
        plt.scatter(self.nuevoPunto[0],self.nuevoPunto[1], color=colorNuevoPunto)
        plt.annotate("Nuevo Punto", (self.nuevoPunto[0],self.nuevoPunto[1]))
        plt.axvline(x=0, c="black")
        plt.axhline(y=0, c="black")
        plt.axis('equal')
        plt.show()
    
    def algoritmoKnn(self,nombreDelArchivo,NuevoX,NuevoY,k):
        self.leerArchivo(nombreDelArchivo)
        self.definirMapaDeColores()
        self.setK(k)
        self.definirNuevoPunto(NuevoX,NuevoY)
        self.calcularDistancia()
        self.obtenerClaseNuevoPunto()
        self.graficarResultado()

    def algoritmoKnnPonderado(self,nombreDelArchivo,NuevoX,NuevoY,k):
        self.leerArchivo(nombreDelArchivo)
        self.definirMapaDeColores()
        self.setK(k)
        self.definirNuevoPunto(NuevoX,NuevoY)
        self.calcularDistancia()
        self.obtenerClaseNuevoPuntoPonderado()
        self.graficarResultadoPonderado()
    
    def algoritmoKnnKoptimo(self,nombreDelArchivo):
        self.leerArchivo(nombreDelArchivo)
        self.definirMapaDeColores()
        self.obtenerKOptimo()
        self.graficarResultado()


    

