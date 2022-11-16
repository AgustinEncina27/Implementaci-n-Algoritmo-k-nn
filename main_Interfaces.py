import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from Ui_Interfaz_Principal import Ui_MainWindow
from Ui_Interfaz_k import Ui_Form2
from Ui_Interfaz_Grafica import Ui_Form3
from Ui_Interfaz_Grafica_K_optimo import Ui_Form4
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolBar
import matplotlib.pyplot as plt
from Controlador import Controlador
import ctypes


class MainWindow(QMainWindow):
    #Construtor de la clase MainWindow
    def __init__(self):
        super(MainWindow,self).__init__()
        view = Ui_MainWindow()
        view.setupUi(self)
        view.Analizar_Dataset.triggered.connect(self.cambiar_A_Interfaz_opcion)
    
    #Cambia a la interfaz donde buscas el Dataset
    def cambiar_A_Interfaz_opcion(self):
        interfaz_k=Interfaz_k()
        widget.addWidget(interfaz_k)
        widget.setCurrentWidget(interfaz_k)
        resolucion=ctypes.windll.user32
        resolucion_ancho=resolucion.GetSystemMetrics(0)
        resolucion_alto=resolucion.GetSystemMetrics(1)
        left=(resolucion_ancho/2)-(342/2)
        top=(resolucion_alto/2)-(172/2)
        widget.setFixedWidth(342)
        widget.setFixedHeight(172)
        widget.move(int(left),int(top)) 


#-------------------------------------------------------------------------
class Interfaz_k(QWidget):
    #Construtor de la clase Interfaz_k
    def __init__(self):
        super(Interfaz_k,self).__init__()
        self.view = Ui_Form2()
        self.fname=None
        self.view.setupUi(self)
        self.view.pushButton_5.clicked.connect(self.buscar_Dataset)
        self.view.pushButton_3.clicked.connect(self.cambiar_A_Interfaz_Principal)
        self.view.pushButton_4.clicked.connect(self.cambiar_A_Interfaz_opcion)

    #Busca archivos .csv
    def buscar_Dataset(self):
        self.fname=QFileDialog.getOpenFileName(self,'Open File','E:','Archivo CSV(*.csv)')
        self.view.lineEdit_4.setText(self.fname[0])

    #Cambia a la interfaz principal
    def cambiar_A_Interfaz_Principal(self):
        self.limpiarComponentes()
        widget.setCurrentWidget(principal)
        resolucion=ctypes.windll.user32
        resolucion_ancho=resolucion.GetSystemMetrics(0)
        resolucion_alto=resolucion.GetSystemMetrics(1)
        left=(resolucion_ancho/2)-(911/2)
        top=(resolucion_alto/2)-(531/2)
        widget.setFixedWidth(911)
        widget.setFixedHeight(531)
        widget.move(int(left),int(top))    

    #Cambia a la interfaz donde se representan los datos del dataset seleccionado
    def cambiar_A_Interfaz_opcion(self):
        if(not self.view.lineEdit_4.text()):
            QtWidgets.QMessageBox.critical(self, "error", "Ingrese todos los campos por favor")
        else:   
            control.obtenerDatos(self.fname[0])
            interfaz_grafica=Interfaz_Grafica()
            widget.addWidget(interfaz_grafica)
            self.limpiarComponentes()
            widget.setCurrentWidget(interfaz_grafica)
            resolucion=ctypes.windll.user32
            resolucion_ancho=resolucion.GetSystemMetrics(0)
            resolucion_alto=resolucion.GetSystemMetrics(1)
            left=(resolucion_ancho/2)-(1500/2)
            top=(resolucion_alto/2)-(620/2)
            widget.setFixedWidth(1500)
            widget.setFixedHeight(620)
            widget.move(int(left),int(top))    
    
    #Reinicia los componentes
    def limpiarComponentes(self):
        self.view.lineEdit_4.setText("")

#-------------------------------------------------------------------------     
class Interfaz_Grafica(QWidget):
    #Construtor de la clase Interfaz_Grafica
    def __init__(self):
        super(Interfaz_Grafica,self).__init__()
        self.view = Ui_Form3()
        self.view.setupUi(self)
        self.size=self.view.horizontalSlider.value()
        self.contador=0
        control.inicilizarGraficoBarras()
        pantallaActual=widget.currentWidget()
        self.pantalla_grafico=widget.indexOf(pantallaActual)
        Interfaz_Grafica_K_Optim=Interfaz_Grafica_K_Optimo(self.pantalla_grafico+2)
        widget.addWidget(Interfaz_Grafica_K_Optim)
        self.pantalla_k=widget.indexOf(Interfaz_Grafica_K_Optim)
        

        self.view.pushButton.clicked.connect(self.cambiarGrafico)
        self.view.pushButton_2.clicked.connect(self.cambiar_A_Interfaz_Principal)
        self.view.pushButton_3.clicked.connect(self.cambiar_A_Interfaz_Grafica_K_optimo)
        
        self.view.mostrarK.setText(str(self.view.horizontalSlider.value()))
        self.view.horizontalSlider.valueChanged.connect(self.cambiarValor)

        
        self.grafica1=Canvas_grafica()
        self.grafica2=Canvas_grafica()
        self.cambiarGrafico()
        self.navigrafica1=NavigationToolBar(self.grafica1,self)
        self.navigrafica2=NavigationToolBar(self.grafica2,self)


        self.view.grafica1.addWidget(self.grafica1)
        self.view.grafica2.addWidget(self.grafica2)
        self.view.grafica1.addWidget(self.navigrafica1)
        self.view.grafica2.addWidget(self.navigrafica2)
    
    #Establece los parametros de los gráficos así se grafica en la interfaz
    def cambiarGrafico(self):
        self.grafica1.ax.clear()
        x, y, colormap, listaLeyendas = control.mostrarResultadoAlgoritmo(self.size)
        textoKnn, textoKnnPonderado=control.obtenerAciertosYErroresK(self.view.horizontalSlider.value())
        self.grafica1.ax.scatter(x, y, c=colormap, s=7)
        self.grafica1.ax.axvline(x=0, c="black")
        self.grafica1.ax.axhline(y=0, c="black")
        self.grafica1.ax.set_xlabel('Eje X')
        self.grafica1.ax.set_ylabel('Eje Y')
        self.grafica1.ax.legend(handles=listaLeyendas, fontsize='x-small', loc=2)
        self.grafica1.ax.axis('equal')
        self.grafica1.draw()
        self.view.plainTextEdit.setPlainText(textoKnn)
        control.algoritmo.limpiarVariables()

        self.grafica2.ax.clear()
        xPonderado, yPonderado, colormapPonderado, listaLeyendasPonderado = control.mostrarResultadoAlgoritmoPonderado(self.size)
        self.grafica2.ax.scatter(xPonderado, yPonderado, c=colormapPonderado, s=7)
        self.grafica2.ax.axvline(x=0, c="black")
        self.grafica2.ax.axhline(y=0, c="black")
        self.grafica2.ax.set_xlabel('Eje X')
        self.grafica2.ax.set_ylabel('Eje Y')
        self.grafica2.ax.legend(handles=listaLeyendasPonderado, fontsize='x-small', loc=2)
        self.grafica2.ax.axis('equal')
        self.grafica2.draw()
        self.view.plainTextEdit_2.setPlainText(textoKnnPonderado)
        control.algoritmo.limpiarVariables()
        if(self.contador!=0):
            QtWidgets.QMessageBox.information(self, "Atención", "Se han actualizado los gráficos")  
        if(self.contador==0):
            self.contador=1
         
    #Cambia el valor del label que muestra el K con respecto al slide
    def cambiarValor(self):
        self.size=self.view.horizontalSlider.value()
        self.view.mostrarK.setText(str(self.size))

    #Cambia a la interfaz principal
    def cambiar_A_Interfaz_Principal(self):
        pantalla1=widget.widget(self.pantalla_grafico)
        pantalla2=widget.widget(self.pantalla_k)
        widget.removeWidget(pantalla1)
        widget.removeWidget(pantalla2)
        widget.setCurrentWidget(principal)
        resolucion=ctypes.windll.user32
        resolucion_ancho=resolucion.GetSystemMetrics(0)
        resolucion_alto=resolucion.GetSystemMetrics(1)
        left=(resolucion_ancho/2)-(911/2)
        top=(resolucion_alto/2)-(531/2)
        widget.setFixedWidth(911)
        widget.setFixedHeight(531)
        widget.move(int(left),int(top))
    
    #Cambia a la interfaz donde se muestra un grafico evolutivo de los k
    def cambiar_A_Interfaz_Grafica_K_optimo(self):
        widget.setCurrentIndex(self.pantalla_k)
        resolucion=ctypes.windll.user32
        resolucion_ancho=resolucion.GetSystemMetrics(0)
        resolucion_alto=resolucion.GetSystemMetrics(1)
        left=(resolucion_ancho/2)-(1500/2)
        top=(resolucion_alto/2)-(620/2)
        widget.setFixedWidth(1500)
        widget.setFixedHeight(620)
        widget.move(int(left),int(top))

#------------------------------------------------------------------------- 

class Interfaz_Grafica_K_Optimo(QWidget):
    #Construtor de la clase Interfaz_Grafica_K_Optimo
    def __init__(self,pantallaAnterior):
        super(Interfaz_Grafica_K_Optimo,self).__init__()
        self.view = Ui_Form4()
        self.view.setupUi(self)
        self.view.pushButton_2.clicked.connect(self.cambiar_A_Interfaz_Grafica)
        self.pantallaAnterior=pantallaAnterior
        listaAciertos, listaDeKs, colores = control.mostrarGraficoBarras()
        mayor=0
        indice=0
        mayorEnRango=0
        indiceEnRango=0
        for n in listaAciertos:
            if(n>=mayor):
                mayor=n
                indice=listaAciertos.index(n)
            if(indice<15):
                mayorEnRango=mayor
                indiceEnRango=listaAciertos.index(mayorEnRango)
        a=str(listaDeKs[indice])
        b=str(listaDeKs[indiceEnRango])
        _translate = QtCore.QCoreApplication.translate
        self.view.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:22pt; font-weight:600;\">K óptimo sin ponderación="+a+"<br>K optimo entre 1-15="+b+"</span></p></body></html>"))

        self.grafica1=Canvas_grafica_Barras(listaAciertos, listaDeKs, colores)
        listaAciertosPonderado, listaDeKsPonderado, coloresPonderado= control.mostrarGraficoBarrasPonderado()
        mayor=0
        indice=0
        for n in listaAciertosPonderado:
            if(n>=mayor):
                mayor=n
                indice=listaAciertosPonderado.index(n)
            if(indice<15):
                mayorEnRango=mayor
                indiceEnRango=listaAciertosPonderado.index(mayorEnRango)
        a=str(listaDeKsPonderado[indice])
        b=str(listaDeKsPonderado[indiceEnRango])
        self.view.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:22pt; font-weight:600;\">K óptimo con ponderación="+a+"<br>K optimo entre 1-15="+b+"</span></p></body></html>"))
        self.grafica2=Canvas_grafica_Barras(listaAciertosPonderado, listaDeKsPonderado, coloresPonderado)
        self.navigrafica1=NavigationToolBar(self.grafica1,self)
        self.navigrafica2=NavigationToolBar(self.grafica2,self)

        self.view.grafica1.addWidget(self.grafica1)
        self.view.grafica2.addWidget(self.grafica2)
        self.view.grafica1.addWidget(self.navigrafica1)
        self.view.grafica2.addWidget(self.navigrafica2)
    
    #Vuelve a la interfaz donde se encuentra representado los datos del Dataset
    def cambiar_A_Interfaz_Grafica(self):
        widget.setCurrentIndex(self.pantallaAnterior)
        resolucion=ctypes.windll.user32
        resolucion_ancho=resolucion.GetSystemMetrics(0)
        resolucion_alto=resolucion.GetSystemMetrics(1)
        left=(resolucion_ancho/2)-(1500/2)
        top=(resolucion_alto/2)-(620/2)
        widget.setFixedWidth(1500)
        widget.setFixedHeight(620)
        widget.move(int(left),int(top))
    
#------------------------------------------------------------------------- 

class Canvas_grafica(FigureCanvas):
    #Construtor de la clase Canvas_grafica.Creacion del grafico
    def __init__(self):
        self.fig , self.ax = plt.subplots(1, dpi=100, figsize=(4.5, 4.5), 
            sharey=True, facecolor='white')
        super().__init__(self.fig)

class Canvas_grafica_Barras(FigureCanvas):
    #Construtor de la clase Canvas_grafica_Barras.Creacion del grafico de barras
    def __init__(self, listaAciertos, listaDeKs, colores, parent=None):
        self.fig , self.ax = plt.subplots(1, dpi=100, figsize=(5, 5), 
            sharey=True, facecolor='white')
        super().__init__(self.fig)
        self.ax.plot(listaDeKs, listaAciertos, marker='o', markersize=6)
        for a in range(len(listaDeKs)):
            self.ax.text(listaDeKs[a],listaAciertos[a],listaAciertos[a],size=6)
        self.ax.set_xticks(listaDeKs)
        self.ax.set_xlabel('Valor de K')
        self.ax.set_ylabel('Cantidad de aciertos')


#Inicializa la APP
if __name__ == '__main__':
    app= QApplication(sys.argv)
    widget=QtWidgets.QStackedWidget()
    widget.setWindowTitle("Algoritmo K-nn")
    control=Controlador()
    principal = MainWindow()
    widget.addWidget(principal)
    widget.setCurrentWidget(principal)
    resolucion=ctypes.windll.user32
    resolucion_ancho=resolucion.GetSystemMetrics(0)
    resolucion_alto=resolucion.GetSystemMetrics(1)
    left=(resolucion_ancho/2)-(911/2)
    top=(resolucion_alto/2)-(531/2)
    widget.setFixedWidth(911)
    widget.setFixedHeight(531)
    widget.move(int(left),int(top))
    widget.show()


    try:
        sys.exit(app.exec_())
    except:
        print("Ya existe")