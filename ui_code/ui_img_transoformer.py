# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'img_transoformeroCZqPP.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QCursor,
                           QFont,)
from PySide6.QtWidgets import (QGridLayout, QPushButton,
                               QSizePolicy, QSpacerItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 500)
        font = QFont()
        font.setPointSize(23)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"#MainWindow{background-color:rgb(102, 124, 137)}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(500, 500))
        font1 = QFont()
        font1.setPointSize(23)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.centralwidget.setFont(font1)
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_2.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.scaleButton = QPushButton(self.centralwidget)
        self.scaleButton.setObjectName(u"scaleButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scaleButton.sizePolicy().hasHeightForWidth())
        self.scaleButton.setSizePolicy(sizePolicy1)
        self.scaleButton.setFont(font1)
        self.scaleButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.scaleButton, 1, 1, 1, 1)

        self.dupButton = QPushButton(self.centralwidget)
        self.dupButton.setObjectName(u"dupButton")
        sizePolicy1.setHeightForWidth(self.dupButton.sizePolicy().hasHeightForWidth())
        self.dupButton.setSizePolicy(sizePolicy1)
        self.dupButton.setFont(font1)
        self.dupButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.dupButton, 1, 3, 1, 1)

        self.sizeButton = QPushButton(self.centralwidget)
        self.sizeButton.setObjectName(u"sizeButton")
        sizePolicy1.setHeightForWidth(self.sizeButton.sizePolicy().hasHeightForWidth())
        self.sizeButton.setSizePolicy(sizePolicy1)
        self.sizeButton.setFont(font1)
        self.sizeButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.sizeButton, 0, 3, 1, 1)

        self.renameButton = QPushButton(self.centralwidget)
        self.renameButton.setObjectName(u"renameButton")
        sizePolicy1.setHeightForWidth(self.renameButton.sizePolicy().hasHeightForWidth())
        self.renameButton.setSizePolicy(sizePolicy1)
        self.renameButton.setFont(font1)
        self.renameButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.renameButton, 0, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u56fe\u5f62\u6279\u91cf\u5904\u7406\u5de5\u5177", None))
        self.scaleButton.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u7f29\u653e", None))
        self.dupButton.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u53bb\u91cd", None))
        self.sizeButton.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u8d28\u91cf\u8c03\u6574", None))
        self.renameButton.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u91cd\u547d\u540d", None))
    # retranslateUi

