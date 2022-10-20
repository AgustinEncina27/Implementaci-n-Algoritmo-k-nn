from traceback import print_tb
from turtle import st
import matplotlib.pyplot as plt
import csv
import math
import operator
import numpy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class Algoritmo:

    def __init__(self):
        self.x = []
        self.y = []
        self.clase = []
        self.contador=0
        self.colormap=[]
        self.k=0
        self.matrizDistancia=[]
        self.clasesCalculadas=[]
        self.listaK=[]
        self.listaKPonderado=[]
        self.grafico=None
        self.cantClases=[]

    def limpiarDatos(self):
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
        self.clasesCalculadas=[]
    
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
        for a in range(self.contador-1):
            self.listaK.append(0)
        for a in range(self.contador-1):
            vecinos={}
            self.cantClases.append(vecinos)
        bandera=False
        for i in range(1,self.contador-1):
            self.k=i
            for fila in range(self.contador-1):
                resultadoClase = self.obtenerClaseNuevoPunto(fila)
                if(len(resultadoClase)>1):
                    if(resultadoClase[0][1]==resultadoClase[1][1]):
                        bandera=False
                    else:
                        bandera=True
                else:
                    bandera=True
                if(resultadoClase[0][0]==self.clase[fila] and bandera):
                    self.listaK[i-1] = self.listaK[i-1] + 1
                bandera=False
            #print(i)
        #print(self.listaK)
        max_value = max(self.listaK)
        print('Maximum value:', max_value, "At index:", self.listaK.index(max_value)+1)
        return self.listaK.index(max_value)+1

    def obtenerKOptimoKnnPonderado(self):
        for a in range(self.contador-1):
            self.listaKPonderado.append(0)
        self.cantClases.clear()
        for a in range(self.contador-1):
            vecinos={}
            self.cantClases.append(vecinos)
        bandera=False
        for i in range(1,self.contador-1):
            self.k=i
            for fila in range(self.contador-1):
                resultadoClase = self.obtenerClaseNuevoPuntoPonderado(fila)
                if(len(resultadoClase)>1):
                    if(resultadoClase[0][1]==resultadoClase[1][1]):
                        bandera=False
                    else:
                        bandera=True
                else:
                    bandera=True
                if(resultadoClase[0][0]==self.clase[fila] and bandera):
                    self.listaKPonderado[i-1] = self.listaKPonderado[i-1] + 1
                bandera=False
            #print(i)
        #print(self.listaKPonderado)
        max_value = max(self.listaKPonderado)
        print('Maximum value:', max_value, "At index:", self.listaKPonderado.index(max_value)+1)
        return self.listaKPonderado.index(max_value)+1

    
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
        self.colormap.clear()
        contador=0
        for color in self.clase:
            if(color==0):
                if(self.clasesCalculadas[contador]==0):
                    self.colormap.append('r')
                else:
                    self.colormap.append('lightcoral')
            if(color==1):
                if(self.clasesCalculadas[contador]==1):
                    self.colormap.append('g')
                else:
                    self.colormap.append('lightgreen')
            if(color==2):
                if(self.clasesCalculadas[contador]==2):
                    self.colormap.append('b')
                else:
                    self.colormap.append('cyan')
            contador+=1
        #print(self.colormap)

    #Define el atributo K
    def setK(self,k):
        self.k=k

    #Define de que clase es el nuevo punto ingresado
    def obtenerClaseNuevoPunto(self,fila):
        auxiliar=self.matrizDistancia[fila][self.k][3]
        auxiliarClases=self.cantClases[fila]
        if(auxiliar in auxiliarClases):
            auxiliarClases[auxiliar]+=1
        else:
            auxiliarClases[auxiliar]=1
        vecinoOrdenado = sorted(auxiliarClases.items(), key=operator.itemgetter(1),reverse=True)
        return vecinoOrdenado

    def obtenerClaseNuevoPuntoPonderado(self,fila):
        auxiliar=self.matrizDistancia[fila][self.k][3]
        auxiliarClases=self.cantClases[fila]
        if(auxiliar in auxiliarClases):
            auxiliarClases[auxiliar]+=(1/((self.matrizDistancia[fila][self.k][0])**2))
        else:
            auxiliarClases[auxiliar]=(1/((self.matrizDistancia[fila][self.k][0])**2))
        vecinoOrdenadoPonderado = sorted(auxiliarClases.items(), key=operator.itemgetter(1),reverse=True)
        return vecinoOrdenadoPonderado

    def obtenerNuevaClaseKnn(self,fila):
        vecinos={}
        for cantidadK in range(self.k):
            auxiliar=self.matrizDistancia[fila][cantidadK+1][3]
            if(auxiliar in vecinos):
                vecinos[auxiliar]+=1
            else:
                vecinos[auxiliar]=1
        vecinoOrdenado = sorted(vecinos.items(), key=operator.itemgetter(1),reverse=True)
        return vecinoOrdenado

    def obtenerNuevaClaseKnnPonderado(self,fila):
        vecinos={}
        for cantidadK in range(self.k):
            auxiliar=self.matrizDistancia[fila][cantidadK+1][3]
            if(auxiliar in vecinos):
                vecinos[auxiliar]+=(1/((self.matrizDistancia[fila][cantidadK+1][0])**2))
            else:
                vecinos[auxiliar]=(1/((self.matrizDistancia[fila][cantidadK+1][0])**2))
        vecinoOrdenadoPonderado = sorted(vecinos.items(), key=operator.itemgetter(1),reverse=True)
        return vecinoOrdenadoPonderado

    #Genera el grafico
    def graficarResultado(self):
        return (self.x,self.y,self.colormap)
    
    def algoritmoKnn(self,k):
        self.setK(k)
        bandera=False
        for a in range(600):
            resultadoClase = self.obtenerNuevaClaseKnn(a)
            if(len(resultadoClase)>1):
                if(resultadoClase[0][1]==resultadoClase[1][1]):
                    bandera=False
                else:
                    bandera=True
            else:
                bandera=True
            if(bandera):
                self.clasesCalculadas.append(self.obtenerNuevaClaseKnn(a)[0][0])
            else:
                self.clasesCalculadas.append(-1)
            bandera=False
        self.definirMapaDeColores()
        return (self.x,self.y,self.colormap)

    def algoritmoKnnPonderado(self,k):
        self.setK(k)
        self.clasesCalculadas.clear()
        for a in range (600):
            self.clasesCalculadas.append(self.obtenerNuevaClaseKnnPonderado(a)[0][0])
        self.definirMapaDeColores()
        return (self.x,self.y,self.colormap)

    def limpiarVariables(self):
        self.colormap.clear()
        self.k=0
        self.clasesCalculadas.clear()

    def graficarBarras(self):
        listaAciertos=[]
        listaDeKs=[]
        colores=[]
        for a in range(15):
            listaAciertos.append(self.listaK[a])
            listaDeKs.append(a+1)
            colores.append('red')
        if(self.listaK.index(max(self.listaK))>14):
            listaAciertos.append(max(self.listaK))
            listaDeKs.append(self.listaK.index(max(self.listaK))+1)
            colores.append('red')
        return (listaAciertos,listaDeKs,colores)

    def graficarBarrasKnnPonderado(self):
        listaAciertos=[]
        listaDeKs=[]
        colores=[]
        for a in range(15):
            listaAciertos.append(self.listaKPonderado[a])
            listaDeKs.append(a+1)
            colores.append('red')
        if(self.listaKPonderado.index(max(self.listaKPonderado))>14):
            listaAciertos.append(max(self.listaKPonderado))
            listaDeKs.append(self.listaKPonderado.index(max(self.listaKPonderado))+1)
            colores.append('red')
        return (listaAciertos,listaDeKs,colores)