import os
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QFileDialog, QMainWindow, QApplication
from logic_code.utils import get_file_size, get_tmp_name, message, error, imread, get_images_list
from ui_code.ui_img_quality import Ui_QtWindow
import cv2


class QtWindow(Ui_QtWindow, QMainWindow):  # 替换文本
    def __init__(self):
        super(QtWindow, self).__init__()
        self.tmp = None
        self.failed_list = []
        self.setupUi(self)
        self.pushButton_2.hide()
        self.radio = self.dial.value()
        self.pushButton.clicked.connect(self.open)
        self.dial.valueChanged.connect(self.refresh)
        self.pushButton_2.clicked.connect(self.transfm)

    def transfm(self):
        self.pushButton_2.setEnabled(False)
        if self.radioButton.isChecked():
            self.img_ys(self.example, self.example)
            self.progressBar.setValue(100)
            message(f"转换成功")
            self.close()
        else:
            path_list = [os.path.join(self.dir, name) for name in self.list]
            self.progressBar.setMaximum(len(self.list))
            for i, path in enumerate(path_list):
                i += 1
                QApplication.processEvents()
                try:
                    self.img_ys(path, path)
                    self.progressBar.setValue(i)
                except:
                    self.failed_list.append(path)
                    continue
            num_success = len(self.list) - len(self.failed_list)
            num_failed = len(self.failed_list)
            message(f"成功{num_success}张\n失败{num_failed}张\n{self.failed_list}")
            self.close()

    def refresh(self):
        org_size = get_file_size(self.example)
        dst_size = get_file_size(self.tmp)
        self.label_7.setText(org_size)
        self.label_8.setText(dst_size)
        self.show_img()

    def img_ys(self, src, dst):
        radio = self.dial.value()
        img = imread(src, cv2.IMREAD_UNCHANGED)
        if os.path.splitext(src)[1] in ['.png', '.PNG']:
            cv2.imwrite(dst, img, [cv2.IMWRITE_PNG_COMPRESSION, radio // 10])
        elif os.path.splitext(src)[1] in ['.webp', '.WEBP']:
            cv2.imwrite(dst, img, [cv2.IMWRITE_WEBP_QUALITY, radio])
        else:
            cv2.imwrite(dst, img, [cv2.IMWRITE_JPEG_QUALITY, radio])

    def label_show(self, label, img):
        Qimg = QPixmap(img)
        self.radio = self.dial.value()
        l_h, l_w = label.height(), label.width()
        i_h, i_w = Qimg.height(), Qimg.width()
        if i_w > i_h:
            radio = i_w / l_w
        else:
            radio = i_h / l_h
        new_i_h, new_i_w = (i_h // radio), (i_w // radio)
        label.setPixmap(Qimg.scaled(new_i_w, new_i_h))

    def show_img(self):
        if len(self.example) > 0:
            self.img_ys(self.example, self.tmp)
            self.label_show(self.label, self.example)
            self.label_show(self.label_2, self.tmp)

    def open(self):
        if self.radioButton.isChecked():
            self.example = QFileDialog.getOpenFileName(None, "选择单个图片文件", os.getcwd())[0]
            self.tmp = get_tmp_name(self.example)
            print(self.tmp)
            if len(self.example) > 0:
                self.pushButton.close()
                self.show_img()
                self.refresh()
                self.pushButton_2.show()
        else:
            self.dir = QFileDialog.getExistingDirectory(None, "选择文件夹路径", os.getcwd())
            if len(self.dir) > 0:
                self.list = get_images_list(self.dir)
                if len(self.list) <= 0:
                    error(content="文件夹为空，请重新选择文件夹")
                    self.open()
                else:
                    self.example = os.path.join(self.dir, self.list[0])
                    self.tmp = get_tmp_name(self.example)
                    self.pushButton.close()
                    self.show_img()
                    self.refresh()
                    self.pushButton_2.show()
