import os
from PySide6.QtWidgets import QFileDialog, QStyleFactory
from logic_code.utils import load_style
from logic_code.utils import message, error
from ui_code.ui_img_rename_thwb import Ui_ThwbWindow
from ui_code.ui_img_rename_tjwb import Ui_TjwbWindow
from ui_code.ui_img_rename_gs import Ui_GsWindow


class ThwbWindow(Ui_ThwbWindow):  # 替换文本
    def __init__(self):
        super(ThwbWindow, self).__init__()
        self.RenameWindow = None
        self.oldstr = ''
        self.newstr = ''
        self.example = None
        self.list = None
        self.dir = None
        self.setupUi(self)
        self.styleSheet
        # load_style("qss/py_dracula_light.qss", self)
        self.pbn_openfd.clicked.connect(self.open)
        self.btn_rename.clicked.connect(self.rename)
        self.comboBox.activated.connect(self.chmode)
        self.lineEdit.textChanged.connect(self.old)
        self.lineEdit_2.textChanged.connect(self.new)

    def show_name(self, old=str, new=str, example=str):
        show_nam = example
        if len(old) == 0:
            return show_nam
        show_nam = show_nam.replace(old, new)
        return show_nam

    def open(self):
        self.dir = QFileDialog.getExistingDirectory(None, "选择文件夹路径", os.getcwd())
        if len(self.dir) > 0:
            self.list = os.listdir(self.dir)
            if len(self.list) <= 0:
                error(content="文件夹为空，请重新选择文件夹")
                self.open()
            else:
                self.example = self.list[0]
                self.label_4.setText(self.example)

    def chmode(self):
        current = self.comboBox.currentText()
        if current == "添加文本":
            self.RenameWindow = TjwbWindow()
            self.RenameWindow.show()
            self.close()
        elif current == "格式":
            self.RenameWindow = GsWindow()
            self.RenameWindow.show()
            self.close()

    def old(self):
        self.oldstr = self.lineEdit.text()
        if self.example.find(self.oldstr) != -1:
            self.label_4.setText(self.show_name(self.oldstr, self.newstr, self.example))

    def new(self):
        self.newstr = self.lineEdit_2.text()
        if self.example.find(self.oldstr) != -1:
            self.label_4.setText(self.show_name(self.oldstr, self.newstr, self.example))

    def rename(self):
        if len(self.oldstr) != 0:
            for old_name in self.list:
                old_path = os.path.join(self.dir, old_name)
                new_name = old_name.replace(self.oldstr, self.newstr)
                new_path = os.path.join(self.dir, new_name)
                os.rename(old_path, new_path)
            message("重命名成功")
            ThwbWindow.close(self)


class TjwbWindow(Ui_TjwbWindow):  # 添加文本
    def __init__(self):
        super(TjwbWindow, self).__init__()
        self.RenameWindow = None
        self.example = None
        self.dir = None
        self.list = None
        self.addstr = ''
        self.setupUi(self)
        # load_style("qss/py_dracula_dark.qss", self)
        self.pbn_openfd.clicked.connect(self.open)
        self.btn_rename.clicked.connect(self.rename)
        self.comboBox.activated.connect(self.chmode)
        self.lineEdit.textChanged.connect(self.strchg)

    def show_name(self, addstr, example=str):
        if self.comboBox_2.currentText() == "名称之前":
            return addstr + example
        else:
            name, imgtype = os.path.splitext(example)
            return name + addstr + imgtype

    def strchg(self):
        self.addstr = self.lineEdit.text()
        self.label_4.setText(self.show_name(self.addstr, self.example))

    def open(self):
        self.dir = QFileDialog.getExistingDirectory(None, "选择文件夹路径", os.getcwd())
        if len(self.dir) > 0:
            self.list = os.listdir(self.dir)
            if len(self.list) <= 0:
                error(content="文件夹为空，请重新选择文件夹")
                self.open()
            else:
                self.example = self.list[0]
                self.label_4.setText(self.example)

    def chmode(self):
        current = self.comboBox.currentText()
        if current == "替换文本":
            self.RenameWindow = ThwbWindow()
            self.RenameWindow.show()
            self.close()
        elif current == "格式":
            self.RenameWindow = GsWindow()
            self.RenameWindow.show()
            self.close()

    def rename(self):
        if len(self.addstr) != 0:
            for old_name in self.list:
                old_path = os.path.join(self.dir, old_name)
                if self.comboBox_2.currentText() == "名称之前":
                    new_name = self.addstr + old_name
                else:
                    name, tp = os.path.splitext(old_name)
                    new_name = name + self.addstr + tp
                new_path = os.path.join(self.dir, new_name)
                os.rename(old_path, new_path)
            message("重命名成功")
            TjwbWindow.close(self)


class GsWindow(Ui_GsWindow):  # 格式
    def __init__(self):
        super(GsWindow, self).__init__()
        self.num_flies = 0
        self.RenameWindow = None
        self.dir = None
        self.list = None
        self.example = None
        self.setupUi(self)
        # load_style("qss/py_dracula_da.qss", self)
        self.bgnum = 0
        self.pbn_openfd.clicked.connect(self.open)
        self.btn_rename.clicked.connect(self.rename)
        self.comboBox.activated.connect(self.chmode)
        self.lineEdit.textChanged.connect(self.show_name)
        self.spinBox.textChanged.connect(self.show_name)
        self.comboBox_3.currentTextChanged.connect(self.show_name)
        self.comboBox_2.currentTextChanged.connect(self.show_name)

    def show_name(self):
        # if len(self.lineEdit.text()) > 0 or len(self.lineEdit_2.text()) > 0:
        self.bgnum = self.spinBox.text()
        imgtype = os.path.splitext(self.example)[1]
        if self.comboBox_3.currentText() == "名称之后":
            if self.comboBox_2.currentText() == "名称和索引":
                self.label_4.setText(self.lineEdit.text() + str(self.bgnum) + imgtype)
            else:
                num = self.bgnum.zfill(len(str(self.num_flies)))
                self.label_4.setText(self.lineEdit.text() + num + imgtype)
        else:
            if self.comboBox_2.currentText() == "名称和索引":
                self.label_4.setText(str(self.bgnum) + self.lineEdit.text() + imgtype)
            else:
                num = self.bgnum.zfill(len(str(self.num_flies)))
                self.label_4.setText(num + self.lineEdit.text() + imgtype)

    def chmode(self):
        current = self.comboBox.currentText()
        if current == "添加文本":
            self.RenameWindow = TjwbWindow()
            self.RenameWindow.show()
            self.close()
        elif current == "替换文本":
            self.RenameWindow = ThwbWindow()
            self.RenameWindow.show()
            self.close()
        else:
            print("吃饱撑的")

    def open(self):
        self.dir = QFileDialog.getExistingDirectory(None, "选择文件夹路径", os.getcwd())
        if len(self.dir) > 0:
            self.list = os.listdir(self.dir)
            if len(self.list) <= 0:
                error(content="文件夹为空，请重新选择文件夹")
                self.open()
            else:
                self.example = self.list[0]
                self.num_flies = len(self.list)
                self.show_name()

    def rename(self):
        if len(self.lineEdit.text()) > 0 or len(self.spinBox.text()) > 0:
            self.bgnum = self.spinBox.value()
            for num, old_name in enumerate(self.list):
                imgtype = os.path.splitext(old_name)[1]
                old_path = os.path.join(self.dir, old_name)
                if self.comboBox_3.currentText() == "名称之后":
                    if self.comboBox_2.currentText() == "名称和索引":
                        new_name = self.lineEdit.text() + str(num + self.bgnum) + imgtype
                        new_path = os.path.join(self.dir, new_name)
                        os.rename(old_path, new_path)
                    else:
                        _num = num + self.bgnum
                        _num = str(str(_num).zfill(len(str(self.num_flies))))
                        new_name = str(self.lineEdit.text()) + _num + imgtype
                        new_path = os.path.join(self.dir, new_name)
                        os.rename(old_path, new_path)
                else:
                    if self.comboBox_2.currentText() == "名称和索引":
                        new_name = str(num + self.bgnum) + str(self.lineEdit.text()) + imgtype
                        new_path = os.path.join(self.dir, new_name)
                        os.rename(old_path, new_path)
                    else:
                        _num = num + self.bgnum
                        _num = str(str(_num).zfill(len(str(self.num_flies))))
                        new_name = _num + self.lineEdit.text() + imgtype
                        new_path = os.path.join(self.dir, new_name)
                        os.rename(old_path, new_path)
            message("重命名成功")
            GsWindow.close(self)
        else:
            error("请先输入自定名称或开始数字")
