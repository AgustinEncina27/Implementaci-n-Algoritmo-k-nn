import pandas as pd
import numpy as np
import operator

# loading data file into the program. give the location of your csv file
dataset = pd.read_csv("E:/input/iris.csv")
print(dataset.head()) # prints first five tuples of your data.

# making function for calculating euclidean distance
def E_Distance(x1, x2, length):
    distance = 0
    for x in range(length):
        distance += np.square(x1[x] - x2[x])
    return np.sqrt(distance)

# making function for defining K-NN model

def knn(trainingSet, testInstance, k):
    distances = {}
    length = testInstance.shape[1]
    for x in range(len(trainingSet)):
        dist = E_Distance(testInstance, trainingSet.iloc[x], length)
        distances[x] = dist[0]
    sortdist = sorted(distances.items(), key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(sortdist[x][0])
    Count = {}  # to get most frequent class of rows
    for x in range(len(neighbors)):
        response = trainingSet.iloc[neighbors[x]][-1]
        if response in Count:
            Count[response] += 1
        else:
            Count[response] = 1
    sortcount = sorted(Count.items(), key=operator.itemgetter(1), reverse=True)
    return (sortcount[0][0], neighbors)

# making test data set
testSet = [[6.8, 3.4, 4.8, 2.4]]
test = pd.DataFrame(testSet)

# assigning different values to k
k = 1
k1 = 3
k2 = 11

# supplying test data to the model
result, neigh = knn(dataset, test, k)
result1, neigh1 = knn(dataset, test, k1)
result2, neigh2 = knn(dataset, test, k2)

# printing output prediction

print(result)
print(neigh)
print(result1)
print(neigh1)
print(result2)
print(neigh2)