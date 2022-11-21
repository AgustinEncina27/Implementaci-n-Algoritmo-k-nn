import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QTableWidget, QTableWidgetItem, QHeaderView
from Ui_Interfaz_Principal import Ui_MainWindow
from Ui_Interfaz_k import Ui_Form2
from Ui_Interfaz_Grafica import Ui_Form3
from Ui_Interfaz_Grafica_K_optimo import Ui_Form4
from Ui_Interfaz_Grafica_Tabla import Ui_Form5
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
        left=(resolucion_ancho/2)-(1033/2)
        top=(resolucion_alto/2)-(620/2)
        widget.setFixedWidth(1033)
        widget.setFixedHeight(620)
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
            left=(resolucion_ancho/2)-(1360/2)
            top=(resolucion_alto/2)-(550/2)
            widget.setFixedWidth(1360)
            widget.setFixedHeight(550)
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
        Interfaz_Grafica_K_Optim=Interfaz_Grafica_K_Optimo(self.pantalla_grafico+3)
        widget.addWidget(Interfaz_Grafica_K_Optim)
        self.pantalla_k=widget.indexOf(Interfaz_Grafica_K_Optim)
        Interfaz_Grafica_Tabl=Interfaz_Grafica_Tabla(self.pantalla_grafico+3)
        widget.addWidget(Interfaz_Grafica_Tabl)
        self.pantalla_k2=widget.indexOf(Interfaz_Grafica_Tabl)
        

        self.view.pushButton.clicked.connect(self.cambiarGrafico)
        self.view.pushButton_2.clicked.connect(self.cambiar_A_Interfaz_Principal)
        self.view.pushButton_3.clicked.connect(self.cambiar_A_Interfaz_Grafica_K_optimo)
        self.view.pushButton_4.clicked.connect(self.cambiar_A_Interfaz_Grafica_Tabla)
        
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
        textoKnn, textoKnnPonderado=control.obtenerAciertosYErroresKTexto(self.view.horizontalSlider.value())
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
        left=(resolucion_ancho/2)-(1033/2)
        top=(resolucion_alto/2)-(620/2)
        widget.setFixedWidth(1033)
        widget.setFixedHeight(620)
        widget.move(int(left),int(top))
    
    #Cambia a la interfaz donde se muestra un grafico evolutivo de los k
    def cambiar_A_Interfaz_Grafica_K_optimo(self):
        widget.setCurrentIndex(self.pantalla_k)
        resolucion=ctypes.windll.user32
        resolucion_ancho=resolucion.GetSystemMetrics(0)
        resolucion_alto=resolucion.GetSystemMetrics(1)
        left=(resolucion_ancho/2)-(1000/2)
        top=(resolucion_alto/2)-(560/2)
        widget.setFixedWidth(1000)
        widget.setFixedHeight(560)
        widget.move(int(left),int(top))
    
    def cambiar_A_Interfaz_Grafica_Tabla(self):
        widget.setCurrentIndex(self.pantalla_k2)
        resolucion=ctypes.windll.user32
        resolucion_ancho=resolucion.GetSystemMetrics(0)
        resolucion_alto=resolucion.GetSystemMetrics(1)
        left=(resolucion_ancho/2)-(1077/2)
        top=(resolucion_alto/2)-(570/2)
        widget.setFixedWidth(1077)
        widget.setFixedHeight(570)
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
        self.view.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">K óptimo sin ponderación="+a+"<br>K optimo entre 1-15="+b+"</span></p></body></html>"))

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
        self.view.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">K óptimo con ponderación="+a+"<br>K optimo entre 1-15="+b+"</span></p></body></html>"))
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
        left=(resolucion_ancho/2)-(1360/2)
        top=(resolucion_alto/2)-(550/2)
        widget.setFixedWidth(1360)
        widget.setFixedHeight(550)
        widget.move(int(left),int(top))
    
#------------------------------------------------------------------------- 

class Interfaz_Grafica_Tabla(QWidget):
    #Construtor de la clase Interfaz_Grafica_K_Optimo
    def __init__(self,pantallaAnterior):
        super(Interfaz_Grafica_Tabla,self).__init__()
        self.view = Ui_Form5()
        self.view.setupUi(self)
        self.view.pushButton.clicked.connect(self.cambiar_A_Interfaz_Grafica)
        self.pantallaAnterior=pantallaAnterior
        listaKTabla, listaAciertosXClaseTabla, listaKPonderadoTabla, listaAciertosXClasesPonderadoTabla, kOptimoGlobal, kOptimoGlobalPonderado, kOptimoRango, kOptimoPonderadoRango = control.obtenerAciertosYErroresTabla()
        
        if(kOptimoGlobal==kOptimoRango):
            kOptimoGlobal=-1
        if(kOptimoGlobalPonderado==kOptimoPonderadoRango):
            kOptimoGlobalPonderado=-1

        if(listaAciertosXClaseTabla[0][4]!=0 and listaAciertosXClaseTabla[0][4]!=0):
            self.view.tableWidget.setRowCount(12)
        else:
            self.view.tableWidget.setRowCount(8)
            
        if(len(listaKTabla)>15):
            self.view.tableWidget.setColumnCount(17)
        else:
            self.view.tableWidget.setColumnCount(16)
    
        self.view.tableWidget.setItem(0,0, QTableWidgetItem("Clase 0"))
        self.view.tableWidget.setItem(1,0, QTableWidgetItem("K"))
        self.view.tableWidget.setItem(2,0, QTableWidgetItem("Aciertos"))
        self.view.tableWidget.setItem(3,0, QTableWidgetItem("Errores"))
        for a in listaKTabla:
            if(a>15):
                self.view.tableWidget.setItem(1,16, QTableWidgetItem(f"{a}"))
            else:
                self.view.tableWidget.setItem(1,a, QTableWidgetItem(f"{a}"))
        contadorColumna=1
        for b in listaAciertosXClaseTabla:
            self.view.tableWidget.setItem(2,contadorColumna, QTableWidgetItem(f"{b[0]}"))
            self.view.tableWidget.setItem(3,contadorColumna, QTableWidgetItem(f"{b[1]}"))
            contadorColumna+=1
        self.view.tableWidget.setItem(4,0, QTableWidgetItem("Clase 1"))
        self.view.tableWidget.setItem(5,0, QTableWidgetItem("K"))
        self.view.tableWidget.setItem(6,0, QTableWidgetItem("Aciertos"))
        self.view.tableWidget.setItem(7,0, QTableWidgetItem("Errores"))
        for a in listaKTabla:
            if(a>15):
                self.view.tableWidget.setItem(5,16, QTableWidgetItem(f"{a}"))
            else:
                self.view.tableWidget.setItem(5,a, QTableWidgetItem(f"{a}"))
        contadorColumna=1
        for b in listaAciertosXClaseTabla:
            self.view.tableWidget.setItem(6,contadorColumna, QTableWidgetItem(f"{b[2]}"))
            self.view.tableWidget.setItem(7,contadorColumna, QTableWidgetItem(f"{b[3]}"))
            contadorColumna+=1
        self.view.tableWidget.item(1, kOptimoRango).setBackground(QColor(108,187,60))
        self.view.tableWidget.item(2, kOptimoRango).setBackground(QColor(108,187,60))
        self.view.tableWidget.item(3, kOptimoRango).setBackground(QColor(108,187,60))
        self.view.tableWidget.item(5, kOptimoRango).setBackground(QColor(108,187,60))
        self.view.tableWidget.item(6, kOptimoRango).setBackground(QColor(108,187,60))
        self.view.tableWidget.item(7, kOptimoRango).setBackground(QColor(108,187,60))

        if(listaAciertosXClaseTabla[0][4]!=0 and listaAciertosXClaseTabla[0][4]!=0):
            self.view.tableWidget.setItem(8,0, QTableWidgetItem("Clase 2"))
            self.view.tableWidget.setItem(9,0, QTableWidgetItem("K"))
            self.view.tableWidget.setItem(10,0, QTableWidgetItem("Aciertos"))
            self.view.tableWidget.setItem(11,0, QTableWidgetItem("Errores"))
            for a in listaKTabla:
                if(a>15):
                    self.view.tableWidget.setItem(9,16, QTableWidgetItem(f"{a}"))
                else:
                    self.view.tableWidget.setItem(9,a, QTableWidgetItem(f"{a}"))
            contadorColumna=1
            for b in listaAciertosXClaseTabla:
                self.view.tableWidget.setItem(10,contadorColumna, QTableWidgetItem(f"{b[4]}"))
                self.view.tableWidget.setItem(11,contadorColumna, QTableWidgetItem(f"{b[5]}"))
                contadorColumna+=1
            self.view.tableWidget.item(9, kOptimoRango).setBackground(QColor(108,187,60))
            self.view.tableWidget.item(10, kOptimoRango).setBackground(QColor(108,187,60))
            self.view.tableWidget.item(11, kOptimoRango).setBackground(QColor(108,187,60))
        if(kOptimoGlobal!=-1):
            self.view.tableWidget.item(1, 16).setBackground(QColor(255,181,82))
            self.view.tableWidget.item(2, 16).setBackground(QColor(255,181,82))
            self.view.tableWidget.item(3, 16).setBackground(QColor(255,181,82))
            self.view.tableWidget.item(5, 16).setBackground(QColor(255,181,82))
            self.view.tableWidget.item(6, 16).setBackground(QColor(255,181,82))
            self.view.tableWidget.item(7, 16).setBackground(QColor(255,181,82))
            self.view.tableWidget.item(9, 16).setBackground(QColor(255,181,82))
            self.view.tableWidget.item(10, 16).setBackground(QColor(255,181,82))
            self.view.tableWidget.item(11, 16).setBackground(QColor(255,181,82))

        
        self.view.tableWidget.verticalHeader().setVisible(False)
        self.view.tableWidget.horizontalHeader().setVisible(False)

        #-----------------------------------------------------------------------------------------------------

        #Contar filas
        if(listaAciertosXClasesPonderadoTabla[0][4]!=0 and listaAciertosXClasesPonderadoTabla[0][4]!=0):
            self.view.tableWidget_2.setRowCount(12)
        else:
            self.view.tableWidget_2.setRowCount(8)
        
        #Contar columnas
        if(len(listaKPonderadoTabla)>15):
            self.view.tableWidget_2.setColumnCount(17)
        else:
            self.view.tableWidget_2.setColumnCount(16)

        self.view.tableWidget_2.setItem(0,0, QTableWidgetItem("Clase 0"))
        self.view.tableWidget_2.setItem(1,0, QTableWidgetItem("K"))
        self.view.tableWidget_2.setItem(2,0, QTableWidgetItem("Aciertos"))
        self.view.tableWidget_2.setItem(3,0, QTableWidgetItem("Errores"))
        for a in listaKPonderadoTabla:
            if(a>15):
                self.view.tableWidget_2.setItem(1,16, QTableWidgetItem(f"{a}"))
            else:
                self.view.tableWidget_2.setItem(1,a, QTableWidgetItem(f"{a}"))
        contadorColumna=1
        for b in listaAciertosXClasesPonderadoTabla:
            self.view.tableWidget_2.setItem(2,contadorColumna, QTableWidgetItem(f"{b[0]}"))
            self.view.tableWidget_2.setItem(3,contadorColumna, QTableWidgetItem(f"{b[1]}"))
            contadorColumna+=1
        self.view.tableWidget_2.setItem(4,0, QTableWidgetItem("Clase 1"))
        self.view.tableWidget_2.setItem(5,0, QTableWidgetItem("K"))
        self.view.tableWidget_2.setItem(6,0, QTableWidgetItem("Aciertos"))
        self.view.tableWidget_2.setItem(7,0, QTableWidgetItem("Errores"))

        for a in listaKPonderadoTabla:
            if(a>15):
                self.view.tableWidget_2.setItem(5,16, QTableWidgetItem(f"{a}"))
            else:
                self.view.tableWidget_2.setItem(5,a, QTableWidgetItem(f"{a}"))
        contadorColumna=1
        for b in listaAciertosXClasesPonderadoTabla:
            self.view.tableWidget_2.setItem(6,contadorColumna, QTableWidgetItem(f"{b[2]}"))
            self.view.tableWidget_2.setItem(7,contadorColumna, QTableWidgetItem(f"{b[3]}"))
            contadorColumna+=1
        self.view.tableWidget_2.item(1, kOptimoPonderadoRango).setBackground(QColor(108,187,60))
        self.view.tableWidget_2.item(2, kOptimoPonderadoRango).setBackground(QColor(108,187,60))
        self.view.tableWidget_2.item(3, kOptimoPonderadoRango).setBackground(QColor(108,187,60))
        self.view.tableWidget_2.item(5, kOptimoPonderadoRango).setBackground(QColor(108,187,60))
        self.view.tableWidget_2.item(6, kOptimoPonderadoRango).setBackground(QColor(108,187,60))
        self.view.tableWidget_2.item(7, kOptimoPonderadoRango).setBackground(QColor(108,187,60))

        if(listaAciertosXClasesPonderadoTabla[0][4]!=0 and listaAciertosXClasesPonderadoTabla[0][4]!=0):
            self.view.tableWidget_2.setItem(8,0, QTableWidgetItem("Clase 2"))
            self.view.tableWidget_2.setItem(9,0, QTableWidgetItem("K"))
            self.view.tableWidget_2.setItem(10,0, QTableWidgetItem("Aciertos"))
            self.view.tableWidget_2.setItem(11,0, QTableWidgetItem("Errores"))
            for a in listaKPonderadoTabla:
                if(a>15):
                    self.view.tableWidget_2.setItem(9,16, QTableWidgetItem(f"{a}"))
                else:
                    self.view.tableWidget_2.setItem(9,a, QTableWidgetItem(f"{a}"))
            contadorColumna=1
            for b in listaAciertosXClasesPonderadoTabla:
                self.view.tableWidget_2.setItem(10,contadorColumna, QTableWidgetItem(f"{b[4]}"))
                self.view.tableWidget_2.setItem(11,contadorColumna, QTableWidgetItem(f"{b[5]}"))
                contadorColumna+=1
            self.view.tableWidget_2.item(9, kOptimoPonderadoRango).setBackground(QColor(108,187,60))
            self.view.tableWidget_2.item(10, kOptimoPonderadoRango).setBackground(QColor(108,187,60))
            self.view.tableWidget_2.item(11, kOptimoPonderadoRango).setBackground(QColor(108,187,60))
        if(kOptimoGlobalPonderado!=-1):
            self.view.tableWidget_2.item(1, 16).setBackground(QColor(255,181,82))
            self.view.tableWidget_2.item(2, 16).setBackground(QColor(255,181,82))
            self.view.tableWidget_2.item(3, 16).setBackground(QColor(255,181,82))
            self.view.tableWidget_2.item(5, 16).setBackground(QColor(255,181,82))
            self.view.tableWidget_2.item(6, 16).setBackground(QColor(255,181,82))
            self.view.tableWidget_2.item(7, 16).setBackground(QColor(255,181,82))
            self.view.tableWidget_2.item(9, 16).setBackground(QColor(255,181,82))
            self.view.tableWidget_2.item(10, 16).setBackground(QColor(255,181,82))
            self.view.tableWidget_2.item(11, 16).setBackground(QColor(255,181,82))
        
        self.view.tableWidget_2.verticalHeader().setVisible(False)
        self.view.tableWidget_2.horizontalHeader().setVisible(False)
   
        #Table will fit the screen horizontally
        self.view.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.view.tableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)
        self.view.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.view.tableWidget_2.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)        
             
    
    #Vuelve a la interfaz donde se encuentra representado los datos del Dataset
    def cambiar_A_Interfaz_Grafica(self):
        widget.setCurrentIndex(self.pantallaAnterior)
        resolucion=ctypes.windll.user32
        resolucion_ancho=resolucion.GetSystemMetrics(0)
        resolucion_alto=resolucion.GetSystemMetrics(1)
        left=(resolucion_ancho/2)-(1360/2)
        top=(resolucion_alto/2)-(550/2)
        widget.setFixedWidth(1360)
        widget.setFixedHeight(550)
        widget.move(int(left),int(top))
    
#------------------------------------------------------------------------- 

class Canvas_grafica(FigureCanvas):
    #Construtor de la clase Canvas_grafica.Creacion del grafico
    def __init__(self):
        self.fig , self.ax = plt.subplots(1, dpi=100, figsize=(3.8, 3.8), 
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
    left=(resolucion_ancho/2)-(1033/2)
    top=(resolucion_alto/2)-(620/2)
    widget.setFixedWidth(1033)
    widget.setFixedHeight(620)
    widget.move(int(left),int(top))
    widget.show()

    try:
        sys.exit(app.exec_())
    except:
        print("Ya existe")