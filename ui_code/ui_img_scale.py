# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'img_scaleAuvYzj.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication,
    QMetaObject,QRect,)

from PySide6.QtWidgets import (QComboBox, QLabel, QMainWindow,
    QProgressBar, QPushButton, QRadioButton,
    QSpinBox, QWidget)

class Ui_ScaleWindow(QMainWindow):
    def setupUi(self, ScaleWindow):
        if not ScaleWindow.objectName():
            ScaleWindow.setObjectName(u"ScaleWindow")
        ScaleWindow.resize(588, 110)
        self.centralwidget = QWidget(ScaleWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(480, 74, 81, 32))
        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(90, 15, 99, 20))
        self.radioButton.setChecked(True)
        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(144, 15, 99, 20))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(287, 50, 111, 16))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(223, 50, 58, 16))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(287, 80, 111, 16))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(222, 80, 58, 16))
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(24, 17, 58, 16))
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(360, 13, 201, 23))
        self.progressBar.setValue(0)
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(211, 10, 121, 32))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(24, 50, 58, 16))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(24, 80, 58, 16))
        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(81, 47, 51, 22))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(99999)
        self.spinBox.setValue(256)
        self.spinBox_2 = QSpinBox(self.centralwidget)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setGeometry(QRect(81, 77, 51, 22))
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(99999)
        self.spinBox_2.setValue(256)
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(24, 64, 131, 16))
        self.spinBox_3 = QSpinBox(self.centralwidget)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setGeometry(QRect(154, 61, 51, 22))
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setMaximum(1000)
        self.spinBox_3.setValue(50)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(480, 43, 81, 32))
        ScaleWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ScaleWindow)

        QMetaObject.connectSlotsByName(ScaleWindow)
    # setupUi

    def retranslateUi(self, ScaleWindow):
        ScaleWindow.setWindowTitle(QCoreApplication.translate("ScaleWindow", u"MainWindow", None))
        self.pushButton_2.setText(QCoreApplication.translate("ScaleWindow", u"\u5f00\u59cb\u8f6c\u6362", None))
        self.radioButton.setText(QCoreApplication.translate("ScaleWindow", u"\u6587\u4ef6", None))
        self.radioButton_2.setText(QCoreApplication.translate("ScaleWindow", u"\u6587\u4ef6\u5939", None))
        self.label_7.setText("")
        self.label_5.setText(QCoreApplication.translate("ScaleWindow", u"\u539f\u59cb\u5927\u5c0f\uff1a", None))
        self.label_8.setText("")
        self.label_6.setText(QCoreApplication.translate("ScaleWindow", u"\u76ee\u6807\u5927\u5c0f\uff1a", None))
        self.label_9.setText(QCoreApplication.translate("ScaleWindow", u"\u60a8\u5c06\u7f29\u653e\uff1a", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("ScaleWindow", u"\u6307\u5b9a\u5bbd\u9ad8\u7f29\u653e", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("ScaleWindow", u"\u6309\u6bd4\u4f8b\u7f29\u653e", None))

        self.label_3.setText(QCoreApplication.translate("ScaleWindow", u"\u76ee\u6807\u5bbd\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("ScaleWindow", u"\u76ee\u6807\u9ad8\uff1a", None))
        self.label_10.setText(QCoreApplication.translate("ScaleWindow", u"\u7f29\u653e\u4e3a\u539f\u56fe\u7684\u767e\u5206\u4e4b\uff1a", None))
        self.pushButton.setText(QCoreApplication.translate("ScaleWindow", u"\u9009\u62e9\u6587\u4ef6", None))
    # retranslateUi

