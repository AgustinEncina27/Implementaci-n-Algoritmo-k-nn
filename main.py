from leer_archivo import Algoritmo

algoritmo=Algoritmo()
algoritmo.leerArchivo("dataset/datasetprueba.csv")
algoritmo.calcularMatrizDistancias()
algoritmo.obtenerKOptimo()
#algoritmo.algoritmoKnnPonderado("dataset/dataset1.csv",10,10,5)
