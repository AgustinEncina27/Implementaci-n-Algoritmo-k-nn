from turtle import st
import matplotlib.pyplot as plt
import csv
import math
import operator
import numpy

class KOptimo:

    def __init__(self):
        self.x = []
        self.y = []
        self.clase = []
        self.contador=0
        self.minimo=0
        self.actual=0
        self.minimoAnterior=0
        self.dato=0

    #carga la matriz con las distancias
    def leerArchivo(self,nombreArchivo):
        with open(nombreArchivo, 'r') as file:
            plots = csv.reader(file, delimiter = ',')
            for row in plots:
                self.contador=self.contador+1
                if(self.contador!=1):
                    self.x.append(float(row[0]))
                    self.y.append(float(row[1]))
                    self.clase.append(float(row[2]))
            matrizDistancia =  [ [ None for y in range( self.contador-1) ] for x in range( self.contador-1) ]   
            for fila in range(self.contador-1):       
                for columna in range(fila,self.contador-1):
                    if(fila==columna):
                        matrizDistancia[fila][columna]=0
                    else:
                        matrizDistancia[fila][columna]=math.sqrt(((self.x[fila]-self.x[columna])**2+(self.y[fila]-self.y[columna])**2))
                        matrizDistancia[columna][fila]=matrizDistancia[fila][columna]
            print(matrizDistancia)
            #carga la matriz ordenada para  calcular los k
            matrizK= [ [ None for y in range( self.contador-1) ] for x in range( self.contador-1) ]
            for columna in range(self.contador-1):     
                for fila in range(self.contador-1):
                    self.minimo=0
                    for cantidad in range(self.contador-1):
                        self.actual=matrizDistancia[columna][cantidad]
                        if(self.minimo==0):
                            self.minimo= self.actual
                        if(self.actual!=0): 
                            if(self.actual<=self.minimo and self.actual>self.minimoAnterior):
                                print("hola")
                                print(columna)
                                print(fila)
                                print(self.minimo)
                                print(self.actual)
                                self.minimo=self.actual
                                self.dato=cantidad
                                print(self.dato)
                    self.minimoAnterior=self.minimo
                    self.minimo=0
                    matrizK[fila][columna]=self.dato
                self.minimoAnterior=0
                self.minimo=0
            print(matrizK)



    
    