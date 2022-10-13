from leer_archivo import Algoritmo

algoritmo=Algoritmo()
algoritmo.leerArchivo("dataset/dataset1.csv")
algoritmo.calcularMatrizDistancias()
#algoritmo.obtenerKOptimo()
algoritmo.algoritmoKnn(33)
#algoritmo.algoritmoKnnPonderado("dataset/dataset1.csv",10,10,5)