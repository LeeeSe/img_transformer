from PySide6.QtWidgets import QFileDialog, QMainWindow, QApplication
from logic_code.utils import message, error, file_move, imread, get_images_list
from ui_code.ui_img_dup import Ui_DupWindow
import cv2
import numpy as np
import os


class DupWindow(Ui_DupWindow, QMainWindow):  # 替换文本
    def __init__(self):
        super(DupWindow, self).__init__()
        self.list = None
        self.dir = None
        self.failed_name_list = []
        self.setupUi(self)
        self.pct = self.horizontalSlider.value()
        self.pushButton.clicked.connect(self.open)
        self.pushButton_2.clicked.connect(self.dup_start)
        self.horizontalSlider.valueChanged.connect(self.adjust_pct)

    def open(self):
        self.dir = QFileDialog.getExistingDirectory(None, "选择文件夹路径", os.getcwd())
        if len(self.dir) > 0:
            self.list = get_images_list(self.dir)
            if len(self.list) <= 0:
                error(content="文件夹为空，请重新选择文件夹")
                self.open()
            else:
                self.pushButton_2.setEnabled(True)

    def dup_start(self):
        self.get_qc_dict(self.dir, self.pct)
        save_dir = file_move(self.failed_name_list, self.dir, '重复文件')
        if len(self.failed_name_list) > 0:
            message(f"原文件数：{len(self.list)}  重复文件数：{len(self.failed_name_list)}\n重复文件被移动在：\n{save_dir}")
        else:
            message(f"原文件数：{len(self.list)}  重复文件数：{len(self.failed_name_list)}\n请调整去重力度")
        self.failed_name_list.clear()
        return True

    def adjust_pct(self):
        self.pct = self.horizontalSlider.value()

    def get_qc_dict(self, path, pct):
        pct = int(64 * pct/100)
        hash_dict = self.get_hash_list(path)
        true_dict = {}
        for i, (name, hash) in enumerate(hash_dict.items()):
            i += 1
            flag = 1
            QApplication.processEvents()
            self.progressBar.setValue(len(hash_dict) + i)
            if len(true_dict) == 0:
                true_dict[name] = hash
                print(f'列表初始化')
            else:
                for name_i, hash_i in true_dict.items():
                    dst = self.hamming_dst(hash_i, hash)
                    if dst < pct:
                        print(f'{name}和{name_i}较为相似，汉明距离为{dst}，阈值为{pct}, 图片{name}被丢弃')
                        flag = 0
                        self.failed_name_list.append(name)
                        break
                    # else:
                    #     print(f'{name}和{name_i}不相似，汉明距离为{dst}，阈值为{pct}接着往下比较')
                if flag:
                    true_dict[name] = hash
                    # print(f'{name}与不重复列表中所有图像不相似，被添加入不重复列表中')

    def pHash(self, img_path):  # 感知哈希值，精确度高，速度较差
        # img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
        img = imread(img_path, cv2.IMREAD_UNCHANGED)
        # print(img.dtype)
        img = cv2.resize(img, (32, 32), interpolation=cv2.INTER_CUBIC)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = img.astype(np.float32)
        img = cv2.dct(img)
        vis1 = img[0:8, 0:8]
        avg = np.sum(vis1) / 64.
        vis1[vis1 < avg] = 0
        vis1[vis1 > avg] = 1
        return vis1

    def get_hash_list(self, folder_path):
        hash_dict = {}
        img_name_list = get_images_list(folder_path)
        self.progressBar.setMaximum(2 * len(img_name_list))
        for i, img in enumerate(img_name_list):
            i += 1
            img_path = os.path.join(folder_path, img)
            QApplication.processEvents()
            self.progressBar.setValue(i)
            try:
                hash = self.pHash(img_path)
            except Exception as ex:
                print(f'图像：{img}求哈希失败')
                print(ex)
                continue
            hash_dict[img] = hash
        return hash_dict

    def hamming_dst(self, arr1, arr2):
        # print(np.logical_xor(arr1, arr2).sum())
        return np.logical_xor(arr1, arr2).sum()

