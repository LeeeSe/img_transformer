import os
import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QStyleFactory
from ui_code.ui_img_transoformer import Ui_MainWindow  # 引入主UI
from logic_code.img_rename import ThwbWindow  # 引入替换文本UI
from logic_code.img_quality import QtWindow
from logic_code.img_dup import DupWindow
from logic_code.img_scale import ScaleWindow


class MainWindow(QMainWindow, Ui_MainWindow):  # 主窗口
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ScaleWindow = None
        self.DupWindow = None
        self.QualityWindow = None
        self.RenameWindow = None
        self.setupUi(self)
        if 'macOS' in QStyleFactory.keys():
            QApplication.setStyle(QStyleFactory.create('macos'))
        else:
            QApplication.setStyle(QStyleFactory.create('Fusion'))
        self.renameButton.clicked.connect(self.rename)
        self.sizeButton.clicked.connect(self.quality)
        self.dupButton.clicked.connect(self.dup)
        self.scaleButton.clicked.connect(self.scale)

    def rename(self):
        self.RenameWindow = ThwbWindow()
        self.RenameWindow.show()

    def quality(self):
        self.QualityWindow = QtWindow()
        self.QualityWindow.show()

    def dup(self):
        self.DupWindow = DupWindow()
        self.DupWindow.show()

    def scale(self):
        self.ScaleWindow = ScaleWindow()
        self.ScaleWindow.show()


app = QApplication([])
app.setWindowIcon(QIcon(os.path.join(os.getcwd(), 'images/icon.png')))
MainWindow = MainWindow()
MainWindow.show()
sys.exit(app.exec())
