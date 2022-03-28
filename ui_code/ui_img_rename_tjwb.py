from PySide6.QtCore import QCoreApplication,QMetaObject, QRect

from PySide6.QtWidgets import QComboBox, QLabel, QLineEdit, QMainWindow, QPushButton, QSizePolicy, QWidget

class Ui_TjwbWindow(QMainWindow):
    def setupUi(self, TjwbWindow):
        if not TjwbWindow.objectName():
            TjwbWindow.setObjectName(u"TjwbWindow")
        TjwbWindow.resize(550, 87)
        self.centralwidget = QWidget(TjwbWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(16, 16, 106, 32))
        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(429, 16, 106, 32))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(130, 20, 291, 21))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(61, 59, 231, 16))
        self.btn_rename = QPushButton(self.centralwidget)
        self.btn_rename.setObjectName(u"btn_rename")
        self.btn_rename.setGeometry(QRect(458, 50, 70, 32))
        self.pbn_openfd = QPushButton(self.centralwidget)
        self.pbn_openfd.setObjectName(u"pbn_openfd")
        self.pbn_openfd.setGeometry(QRect(340, 50, 97, 32))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(24, 59, 40, 16))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        TjwbWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(TjwbWindow)

        QMetaObject.connectSlotsByName(TjwbWindow)
    # setupUi

    def retranslateUi(self, TjwbWindow):
        TjwbWindow.setWindowTitle(QCoreApplication.translate("TjwbWindow", u"\u6279\u91cf\u56fe\u50cf\u91cd\u547d\u540d", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("TjwbWindow", u"\u6dfb\u52a0\u6587\u672c", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("TjwbWindow", u"\u66ff\u6362\u6587\u672c", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("TjwbWindow", u"\u683c\u5f0f", None))

        self.comboBox_2.setItemText(0, QCoreApplication.translate("TjwbWindow", u"\u540d\u79f0\u4e4b\u524d", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("TjwbWindow", u"\u540d\u79f0\u4e4b\u540e", None))

        self.lineEdit.setText("")
        self.label_4.setText("")
        self.btn_rename.setText(QCoreApplication.translate("TjwbWindow", u"\u91cd\u547d\u540d", None))
        self.pbn_openfd.setText(QCoreApplication.translate("TjwbWindow", u"\u9009\u62e9\u6587\u4ef6\u5939", None))
        self.label_3.setText(QCoreApplication.translate("TjwbWindow", u"\u793a\u4f8b\uff1a", None))
    # retranslateUi

