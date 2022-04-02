from PySide6.QtWidgets import QFileDialog, QMainWindow, QApplication
from logic_code.utils import message, error, file_move, imread, get_images_list, list_split, mul_get_hash, yes_or_not
from ui_code.ui_img_dup import Ui_DupWindow
import multiprocessing
import cv2
import numpy as np
import os


class DupWindow(Ui_DupWindow, QMainWindow):  # 替换文本
    def __init__(self):
        super(DupWindow, self).__init__()
        self.list = None
        self.dir = None
        self.num_process = multiprocessing.cpu_count()
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
        if yes_or_not(f"原文件数：{len(self.list)}  重复文件数：{len(self.failed_name_list)}\n 是否将重复文件移动到新文件夹\n(可选否然后重新调整去重力度)"):
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
        pct = int(64 * pct / 100)
        hash_dict = self.get_hash_dict_mul(path)
        true_dict = {}
        for i, (name, hash) in enumerate(hash_dict.items()):
            i += 1
            flag = 1
            QApplication.processEvents()
            self.progressBar.setValue(len(hash_dict) + i)
            if len(true_dict) == 0:
                true_dict[name] = hash
                # print(f'列表初始化')
            else:
                for name_i, hash_i in true_dict.items():
                    dst = self.hamming_dst(hash_i, hash)
                    if dst < pct:
                        # print(f'{name}和{name_i}较为相似，汉明距离为{dst}，阈值为{pct}, 图片{name}被丢弃')
                        flag = 0
                        self.failed_name_list.append(name)
                        break
                    # else:
                    #     print(f'{name}和{name_i}不相似，汉明距离为{dst}，阈值为{pct}接着往下比较')
                if flag:
                    true_dict[name] = hash
                    # print(f'{name}与不重复列表中所有图像不相似，被添加入不重复列表中')

    def get_hash_dict_mul(self, folder_path):
        print(multiprocessing.get_start_method())
        img_name_list = get_images_list(folder_path)
        self.progressBar.setMaximum(2 * len(img_name_list))
        img_name_list_gener = list_split(img_name_list, self.num_process)
        p = multiprocessing.Pool(self.num_process)  # 创建了4个进程的进程池
        hash_dict = multiprocessing.Manager().dict()  # 创建进程共享字典
        progress = multiprocessing.Manager().Value('int64', 0)
        progress_bar = self.progressBar
        for i_process, img_name_list_split in enumerate(img_name_list_gener):  # 把一个list切成四份分给四个进程处理
            p.apply_async(mul_get_hash, args=(img_name_list_split, folder_path, pHash, hash_dict, progress))
        while True:
            self.progressBar.setValue(progress.get())
            QApplication.processEvents()
            if progress.get() > len(img_name_list) * 0.8:
                break
        p.close()  # 用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
        p.join()  # 没有join，则主进程直接执行任务结束！对Pool对象调用join()方法会等待所有子进程执行完毕
        return hash_dict

    def hamming_dst(self, arr1, arr2):
        # print(np.logical_xor(arr1, arr2).sum())
        return np.logical_xor(arr1, arr2).sum()


def pHash(img_path):  # 感知哈希值，精确度高，速度较差
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


def mul_get_hash(img_name_list_split, folder_path, pHash, hash_dict, progress):
        print('enter new Process')
        for i, img in enumerate(img_name_list_split):
            progress.set(progress.get() + 1)
            img_path = os.path.join(folder_path, img)
            try:
                hash = pHash(img_path)
            except Exception as ex:
                print(f'图像：{img}求哈希失败')
                print(ex)
                continue
            hash_dict[img] = hash

