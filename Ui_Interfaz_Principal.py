# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Cosas de guardar\Uni\Año 5\Segundo cuatrimestre\Inteligencia artificial 2\TP Integrador\Codigo\Codigo Fuente\Interfaz_Principal.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(911, 531)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("PMingLiU-ExtB")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 9)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 911, 21))
        self.menubar.setObjectName("menubar")
        self.menuAlgoritmo_K_nn = QtWidgets.QMenu(self.menubar)
        self.menuAlgoritmo_K_nn.setObjectName("menuAlgoritmo_K_nn")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Analizar_Dataset = QtWidgets.QAction(MainWindow)
        self.Analizar_Dataset.setObjectName("Analizar_Dataset")
        self.menuAlgoritmo_K_nn.addAction(self.Analizar_Dataset)
        self.menubar.addAction(self.menuAlgoritmo_K_nn.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "BIENVENIDO"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>GUÍA DEL USUARIO</p><p>En la esquina superior izquierda se encuentra el menú con las distintas funcionalidades que posee esta aplicación.</p><p>1-Interfaz &quot;Principal&quot;</p><p>1.1-Pestaña de &quot;Algoritmo k-nn&quot;:</p><p>1.1.1-Pestaña &quot;Analizar Dataset&quot;:Al presionar esta pestaña se trasladará a la interfaz &quot;Buscar Dataset&quot;.<br/></p><p>2-Interfaz &quot;Buscar DataSet&quot;:</p><p>2.1-El botón &quot;Volver al inicio&quot; regresa a la Interfaz Principal.</p><p>2.2-El botón &quot;Buscar DataSet&quot; le abrirá un buscador en donde tendrá que buscar y seleccionar un DataSet que deseé analizar.</p><p>2.2.1-Luego de seleccionar el DataSet oprimir el botón &quot;Siguiente&quot; para pasar a la Interfaz &quot;Análisis de K-nn&quot; en donde se analizará el DataSet seleccionado.<br/></p><p>3-Interfaz &quot;Análisis de K-nn&quot;:</p><p>3.1-Se encuentra un slide y un botón llamado &quot;Aplicar k&quot; para seleccionar el K entre 1 al 15 y mostrar un gráfico donde se visualiza la selección de clases de cada dato del DataSet elegido.</p><p>3.2-El botón &quot;Mostrar K óptimo&quot; permite trasladarse a la Interfaz &quot;Mostrar K óptimo&quot; en donde se mostrar los aciertos de los k entre 1 al 15 y el óptimo.</p><p>3.3-El botón &quot;Volver al inicio&quot; regresa a la Interfaz Principal.<br/></p><p>4-Interfaz &quot;Mostrar K óptimo&quot;</p><p>4.1-El botón &quot;Volver&quot; regresa a la Interfaz &quot;Análisis de K-nn&quot;.</p></body></html>"))
        self.menuAlgoritmo_K_nn.setTitle(_translate("MainWindow", "Algoritmo K-nn"))
        self.Analizar_Dataset.setText(_translate("MainWindow", "Analizar Dataset"))
