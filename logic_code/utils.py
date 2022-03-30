import os
import tempfile
import shutil
import cv2
import numpy as np
from PySide6.QtWidgets import QMessageBox
suffix = (
    '.jpg',
    'jpeg',
    '.png',
    '.PNG',
    '.JPG',
    '.JPEG',
    '.webp',
    ',WEBP',
    '.tif',
    '.bmp',
    '.tiff',
)

def file_move(file_list, dir, save_folder_name):
    save_dir = os.path.join(dir, save_folder_name)
    i = 0
    while os.path.exists(save_dir):
        i += 1
        save_dir = os.path.join(dir, save_folder_name + '_' + str(i))
    os.mkdir(save_dir)
    for name in file_list:
        old_path = os.path.join(dir, name)
        new_path = os.path.join(save_dir, name)
        shutil.move(old_path, new_path)
    return save_dir


def error(content="操作错误"):
    QMessageBox.critical(None, "错误", content)


def message(content="操作成功"):
    QMessageBox.information(None, "提示", content)


def load_style(file, widget):
    """
    加载样式
    :param file: 加载的qss样式文件
    :param widget: qss样式显示的控件
    :return:
    """
    # 读取样式文件内容
    with open(file, 'r', encoding='UTF-8') as f:
        style_sheet = f.read()
        widget.setStyleSheet(style_sheet)


def get_file_size(file):
    return str(os.path.getsize(file) / (1024 * 1024))[0:5] + ' mb'


def get_tmp_name(file):
    tmp_dir = tempfile.gettempdir()
    return os.path.join(tmp_dir, 'tmp' + os.path.splitext(file)[1])


def imread(src, mode):
    if cv2.imdecode(np.fromfile(src, dtype=np.uint8), mode) is None:
        print(f'file is None {src}')
    return cv2.imdecode(np.fromfile(src, dtype=np.uint8), mode)


def get_files_list(dir):
    temp = os.listdir(dir)
    temp = [os.path.join(dir, file_name) for file_name in temp if file_name[0] != '.']

    return [os.path.basename(file) for file in temp if os.path.isfile(file)]


def get_images_list(dir):
    temp = os.listdir(dir)
    for file in temp:
        if not file.endswith(suffix):
            temp.remove(file)
    return temp
