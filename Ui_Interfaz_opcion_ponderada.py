from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_Form1(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(350, 130)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(350, 130)
        Form.setMaximumSize(350, 130)
        Form.setMouseTracking(False)
        Form.setTabletTracking(False)
        Form.setAcceptDrops(True)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(270, 100, 75, 23))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 100, 81, 21))
        self.radioButton = QRadioButton(Form)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(40, 40, 111, 16))
        self.radioButton_2 = QRadioButton(Form)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(40, 70, 111, 16))

        self.RadioGroup = QButtonGroup()
        self.RadioGroup.addButton(self.radioButton)
        self.RadioGroup.addButton(self.radioButton_2)  

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 331, 20))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Siguiente", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Volver al inicio", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"Ponderado", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"No ponderado", None))
        self.label.setText(QCoreApplication.translate("Form", u"Indique que tipo de Algoritmo k-nn desea implementar.", None))
    # retranslateUi

