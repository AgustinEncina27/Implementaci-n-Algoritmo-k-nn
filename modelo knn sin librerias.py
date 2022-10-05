import pandas as pd
import numpy as np
import operator
import matplotlib as plt


# cargamos el DataSet
dataframe = pd.read_csv(r"dataset3.csv", sep=',')

# Calculamos la distancia Euclidiana
def Distancia_Euclidiana(x1, x2, length):
    distancia = 0
    for x in range(length):
        distancia += np.square(x1[x] - x2[x])
    return np.sqrt(distancia)

# Algoritmo KN-N
def knn(trainingSet, testInstance, k):
    distancias = {}
    length = testInstance.shape[1]
    for x in range(len(trainingSet)):
        dist = Distancia_Euclidiana(testInstance, trainingSet.iloc[x], length)
        distancias[x] = dist[0]
    sortdist = sorted(distancias.items(), key=operator.itemgetter(1))
    vecinos = []
    for x in range(k):
        vecinos.append(sortdist[x][0])
    Count = {}  # aquie obtenemos la clase de fila mas frecuente
    for x in range(len(vecinos)):
        response = trainingSet.iloc[vecinos[x]][-1]
        if response in Count:
            Count[response] += 1
        else:
            Count[response] = 1
    sortcount = sorted(Count.items(), key=operator.itemgetter(1), reverse=True)
    return (sortcount[0][0], vecinos)

# testamos un conjunto de datos
testSet = [[12.83113937, 13.06713831]]
test = pd.DataFrame(testSet)

# asiganmos distintintos valores de K
k = 3

# Le mostramos al KKN algunos conjuntos de datos probaddos
result, neigh = knn(dataframe, test, k)

# mostramos la sallida
print(result)
print(neigh)
