from PySide6.QtCore import QCoreApplication,QMetaObject, QRect

from PySide6.QtWidgets import QComboBox, QLabel, QLineEdit, QMainWindow, QPushButton, QSizePolicy, QWidget

class Ui_ThwbWindow(QMainWindow):
    def setupUi(self, ThwbWindow):
        if not ThwbWindow.objectName():
            ThwbWindow.setObjectName(u"ThwbWindow")
        ThwbWindow.resize(550, 109)
        self.centralwidget = QWidget(ThwbWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(398, 44, 132, 21))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(23, 48, 40, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(339, 46, 53, 16))
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(14, 12, 106, 32))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(23, 79, 40, 16))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.btn_rename = QPushButton(self.centralwidget)
        self.btn_rename.setObjectName(u"btn_rename")
        self.btn_rename.setGeometry(QRect(463, 73, 70, 32))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(61, 46, 125, 21))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(63, 78, 241, 16))
        self.pbn_openfd = QPushButton(self.centralwidget)
        self.pbn_openfd.setObjectName(u"pbn_openfd")
        self.pbn_openfd.setGeometry(QRect(339, 73, 97, 32))
        ThwbWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ThwbWindow)

        QMetaObject.connectSlotsByName(ThwbWindow)
    # setupUi

    def retranslateUi(self, ThwbWindow):
        ThwbWindow.setWindowTitle(QCoreApplication.translate("ThwbWindow", u"MainWindow", None))
        self.lineEdit_2.setText("")
        self.label.setText(QCoreApplication.translate("ThwbWindow", u"\u67e5\u627e\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("ThwbWindow", u"\u66ff\u6362\u6210\uff1a", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("ThwbWindow", u"\u66ff\u6362\u6587\u672c", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("ThwbWindow", u"\u6dfb\u52a0\u6587\u672c", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("ThwbWindow", u"\u683c\u5f0f", None))

        self.label_3.setText(QCoreApplication.translate("ThwbWindow", u"\u793a\u4f8b\uff1a", None))
        self.btn_rename.setText(QCoreApplication.translate("ThwbWindow", u"\u91cd\u547d\u540d", None))
        self.lineEdit.setText("")
        self.label_4.setText("")
        self.pbn_openfd.setText(QCoreApplication.translate("ThwbWindow", u"\u9009\u62e9\u6587\u4ef6\u5939", None))
    # retranslateUi

