# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'img_dupmqXyZG.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication,
                            QMetaObject, QRect, Qt)
from PySide6.QtWidgets import (QLabel, QMainWindow, QProgressBar,
                               QPushButton, QSlider, QWidget)


class Ui_DupWindow(QMainWindow):
    def setupUi(self, DupWindow):
        if not DupWindow.objectName():
            DupWindow.setObjectName(u"DupWindow")
        DupWindow.resize(352, 103)
        self.centralwidget = QWidget(DupWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(102, 18, 160, 25))
        self.horizontalSlider.setValue(50)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 58, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(281, 20, 58, 16))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(23, 55, 81, 32))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setGeometry(QRect(267, 55, 71, 32))
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(125, 59, 118, 23))
        self.progressBar.setValue(0)
        DupWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(DupWindow)
        self.horizontalSlider.valueChanged.connect(self.label_2.setNum)

        QMetaObject.connectSlotsByName(DupWindow)

    # setupUi

    def retranslateUi(self, DupWindow):
        DupWindow.setWindowTitle(QCoreApplication.translate("DupWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("DupWindow", u"\u53bb\u91cd\u529b\u5ea6\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("DupWindow", u"50", None))
        self.pushButton.setText(QCoreApplication.translate("DupWindow", u"\u9009\u62e9\u6587\u4ef6\u5939", None))
        self.pushButton_2.setText(QCoreApplication.translate("DupWindow", u"\u5f00\u59cb\u53bb\u91cd", None))
    # retranslateUi
