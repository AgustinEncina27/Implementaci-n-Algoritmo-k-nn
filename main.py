import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from Ui_Interfaz_Principal import Ui_MainWindow
from Ui_Interfaz_opcion_ponderada import Ui_Form1
from Ui_Interfaz_k import Ui_Form2
from Controlador import Controlador


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        view = Ui_MainWindow()
        view.setupUi(self)
        view.Analizar_Dataset.triggered.connect(self.cambiar_A_Interfaz_opcion)
    
    def cambiar_A_Interfaz_opcion(self):
        widget.setCurrentWidget(interfaz_opcion)
        widget.setFixedWidth(350)
        widget.setFixedHeight(130)

#-------------------------------------------------------------------------
class Interfaz_opcion(QWidget):
    def __init__(self):
        super(Interfaz_opcion,self).__init__()
        self.view = Ui_Form1()
        self.view.setupUi(self)
        self.view.pushButton_2.clicked.connect(self.cambiar_A_Interfaz_Principal)
        self.view.pushButton.clicked.connect(self.cambiar_A_Interfaz_k)

    def cambiar_A_Interfaz_Principal(self):
        self.limpiarRadioButton()
        widget.setCurrentWidget(principal)
        widget.setFixedWidth(600)
        widget.setFixedHeight(320)
    
    def cambiar_A_Interfaz_k(self):
        if(not self.view.radioButton.isChecked() and not self.view.radioButton_2.isChecked()):
            
            QtWidgets.QMessageBox.critical(self, "error", "Ingrese como quiere implementar el Algoritmo k-nn")
        else:
            self.limpiarRadioButton()
            widget.setCurrentWidget(interfaz_k)
            widget.setFixedWidth(660)
            widget.setFixedHeight(300)

    def limpiarRadioButton(self):
        self.view.RadioGroup.setExclusive(False)
        self.view.radioButton.setChecked(False)
        self.view.radioButton_2.setChecked(False)
        self.view.RadioGroup.setExclusive(True)


#-------------------------------------------------------------------------
class Interfaz_k(QWidget):
    def __init__(self):
        super(Interfaz_k,self).__init__()
        self.view = Ui_Form2()
        self.view.setupUi(self)
        self.view.pushButton_5.clicked.connect(self.buscar_Dataset)
        self.view.pushButton_3.clicked.connect(self.cambiar_A_Interfaz_Principal)
        self.view.pushButton_4.clicked.connect(self.cambiar_A_Interfaz_opcion)

    def buscar_Dataset(self):
        fname=QFileDialog.getOpenFileName(self,'Open File','E:','Archivo CSV(*.csv)')
        self.view.lineEdit_4.setText(fname[0])

    def cambiar_A_Interfaz_Principal(self):
        self.limpiarComponentes()
        widget.setCurrentWidget(principal)
        widget.setFixedWidth(600)
        widget.setFixedHeight(320)

    def cambiar_A_Interfaz_opcion(self):
        a=self.view.lineEdit.text()
        if((not self.view.lineEdit_4.text())or(not self.view.lineEdit_2.text())or(not self.view.lineEdit_3.text())or(not a)):
            QtWidgets.QMessageBox.critical(self, "error", "Ingrese todos los campos por favor")
        else:
            
            if '.' in a:
                QtWidgets.QMessageBox.critical(self, "error", "Ingrese un K entero")   
            else:
                if ',' in a:
                    QtWidgets.QMessageBox.critical(self, "error", "Ingrese un K entero")   
                else:
                    if(int(a)<1):
                        QtWidgets.QMessageBox.critical(self, "error", "Ingrese un K mayor a 0")
                    else:
                        self.limpiarComponentes()
                        widget.setCurrentWidget(interfaz_opcion)
                        widget.setFixedWidth(350)
                        widget.setFixedHeight(130)
    
    def limpiarComponentes(self):
        self.view.lineEdit.setText("")
        self.view.lineEdit_2.setText("")
        self.view.lineEdit_3.setText("")
        self.view.lineEdit_4.setText("")

#-------------------------------------------------------------------------      
app= QApplication(sys.argv)
widget=QtWidgets.QStackedWidget()
control=Controlador()
principal = MainWindow()
interfaz_opcion=Interfaz_opcion()
interfaz_k=Interfaz_k()
widget.addWidget(interfaz_opcion)
widget.addWidget(principal)
widget.addWidget(interfaz_k)
widget.setCurrentWidget(principal)
widget.setFixedWidth(600)
widget.setFixedHeight(320)
widget.show()


try:
    sys.exit(app.exec_())
except:
    print("Ya existe")