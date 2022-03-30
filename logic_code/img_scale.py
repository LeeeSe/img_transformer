import os
from PySide6.QtWidgets import QFileDialog, QMainWindow, QApplication
from logic_code.utils import message, error, imread, get_images_list
from ui_code.ui_img_scale import Ui_ScaleWindow
import cv2


class ScaleWindow(Ui_ScaleWindow, QMainWindow):  # 替换文本
    def __init__(self):
        super(ScaleWindow, self).__init__()
        self.tmp = None
        self.example = None
        self.example_size = None
        self.failed_list = []
        self.setupUi(self)
        self.dst_size = [self.spinBox.value(), self.spinBox_2.value()]
        self.label_8.setText(str(self.dst_size))
        self.pushButton_2.hide()
        self.label_10.hide()
        self.spinBox_3.hide()
        self.comboBox.currentTextChanged.connect(self.change_mode)
        self.pushButton.clicked.connect(self.open)
        self.spinBox.valueChanged.connect(self.refresh)
        self.spinBox_2.valueChanged.connect(self.refresh)
        self.spinBox_3.valueChanged.connect(self.refresh)
        self.pushButton_2.clicked.connect(self.transfm)

    def change_mode(self):
        if self.comboBox.currentText() == "指定长宽缩放":
            self.label_3.show()
            self.label_4.show()
            self.spinBox.show()
            self.spinBox_2.show()
            self.label_10.hide()
            self.spinBox_3.hide()
            self.refresh()
        else:  # 按比例缩放
            self.label_3.hide()
            self.label_4.hide()
            self.spinBox.hide()
            self.spinBox_2.hide()
            self.label_10.show()
            self.spinBox_3.show()
            self.refresh()

    def transfm(self):
        self.pushButton_2.setEnabled(False)
        if self.radioButton.isChecked():
            self.img_sf(self.example, self.example)
            self.progressBar.setValue(100)
            message(f"转换成功")
            self.close()
        else:
            path_list = [os.path.join(self.dir, name) for name in self.list]
            self.progressBar.setMaximum(len(self.list))
            for i, path in enumerate(path_list):
                QApplication.processEvents()
                try:
                    self.img_sf(path, path)
                    self.progressBar.setValue(i)
                except:
                    self.failed_list.append(path)
                    continue
            num_success = len(self.list) - len(self.failed_list)
            num_failed = len(self.failed_list)
            message(f"成功{num_success}张\n失败{num_failed}张\n{self.failed_list}")
            self.close()

    def refresh(self):
        if self.comboBox.currentText() == "指定长宽缩放":
            if self.example is not None:
                self.label_7.setText(str(self.example_size))
            self.dst_size = [self.spinBox_2.value(), self.spinBox.value()]
            self.label_8.setText(str(self.dst_size))
        else:
            if self.example is not None:
                self.label_7.setText(str(self.example_size))
                self.dst_size = [self.example_size[0] * self.spinBox_3.value() // 100,
                                 self.example_size[1] * self.spinBox_3.value() // 100]
                self.label_8.setText(str(self.dst_size))
            else:
                self.label_7.clear()
                self.label_8.clear()

    def img_sf(self, src, dst):
        img = imread(src, cv2.IMREAD_UNCHANGED)
        if self.comboBox.currentText() == "指定长宽缩放":
            img = cv2.resize(img, (self.dst_size[0], self.dst_size[1]))
        else:
            img = cv2.resize(img, (img.shape[1] * self.spinBox_3.value() // 100, img.shape[0] * self.spinBox_3.value() // 100))
        cv2.imwrite(dst, img)

    def open(self):
        if self.radioButton.isChecked():
            self.example = QFileDialog.getOpenFileName(None, "选择单个图片文件", os.getcwd())[0]
            if len(self.example) > 0:
                self.example_size = imread(self.example, cv2.IMREAD_UNCHANGED).shape[0:2]
        else:
            self.dir = QFileDialog.getExistingDirectory(None, "选择文件夹路径", os.getcwd())
            if len(self.dir) > 0:
                self.list = get_images_list(self.dir)
                if len(self.list) <= 0:
                    error(content="文件夹为空，请重新选择文件夹")
                    self.open()
                else:
                    self.example = os.path.join(self.dir, self.list[0])
                    self.example_size = imread(self.example, cv2.IMREAD_UNCHANGED).shape[0:2]
        self.example_size = [self.example_size[1], self.example_size[0]]
        self.refresh()
        self.pushButton_2.show()
