# import os
#
# print('Process (%s) start...' % os.getpid())
# # Only works on Unix/Linux/Mac:
# pid = os.fork()  # 返回两次，在两个不同的进程中（第一次返回主进程pid，第二次返回0，即子进程）
# print(pid)
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

# from multiprocessing import Process  # Process类代表一个进程对象
# import os
#
#
# # 子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))
#
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))  # 示例化了一个进程对象p
#     print('Child process will start.')
#     p.start()
#     p.join()  # 主进程等待子进程结束才运行下一行代码，用来保证进程同步
#     print('Child process end.')


# def long_time_task(src, num):
#     src.append(num)
#
#
# if __name__ == '__main__':
#     print(Pool())
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)
#     src = Manager().dict()
#     tmp = [7, 2, 4, 8, 1, 8, 3, 4]
#     for i in range(4):
#         tepp = tmp[i * 2: i * 2 + 2]
#         p.apply_async(long_time_task, args=(src, tepp,))
#     print('Waiting for all subprocesses done...')
#     p.close()  # 用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
#     p.join()  # 没有join，则主进程直接执行任务结束！对Pool对象调用join()方法会等待所有子进程执行完毕
#     print('All subprocesses done.')
#     print(src)

# from logic_code.utils import list_split
# img_name_list = [
#     'one',
#     'two',
#     'three',
#     'four',
#     'five'
# ]
#
#
# temp = list_split(img_name_list, 2)
# print(len(temp))


# import os, cv2
# import numpy as np
# import random
# import time
# import multiprocessing
# from multiprocessing import Pool, Manager
# from logic_code.utils import message, error, file_move, imread, get_images_list, list_split, mul_get_hash
#
#
#
#
# def hamming_dst(self, arr1, arr2):
#     # print(np.logical_xor(arr1, arr2).sum())
#     return np.logical_xor(arr1, arr2).sum()
#
#
# def pHash(img_path):  # 感知哈希值，精确度高，速度较差
#     # img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
#     img = imread(img_path, cv2.IMREAD_UNCHANGED)
#     # print(img.dtype)
#     img = cv2.resize(img, (32, 32), interpolation=cv2.INTER_CUBIC)
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     img = img.astype(np.float32)
#     img = cv2.dct(img)
#     vis1 = img[0:8, 0:8]
#     avg = np.sum(vis1) / 64.
#     vis1[vis1 < avg] = 0
#     vis1[vis1 > avg] = 1
#     return vis1
#
#
# def mul_get_hash(img_name_list_split, folder_path, pHash, hash_dict):
#     print('enter new Process')
#     for i, img in enumerate(img_name_list_split):
#         i += 1
#         img_path = os.path.join(folder_path, img)
#         try:
#             hash = pHash(img_path)
#         except Exception as ex:
#             print(f'图像：{img}求哈希失败')
#             print(ex)
#             continue
#         hash_dict[img] = hash
#
# def get_hash_dict_mul(folder_path):
#     print(multiprocessing.get_start_method())
#     img_name_list = get_images_list(folder_path)
#     x = 4
#     img_name_list = list_split(img_name_list, 4)
#     p = multiprocessing.Pool(4)  # 创建了4个进程的进程池
#     hash_dict = multiprocessing.Manager().dict()  # 创建进程共享字典
#     for i_process, img_name_list_split in enumerate(img_name_list):  # 把一个list切成四份分给四个进程处理
#         p.apply_async(mul_get_hash, args=(img_name_list_split, folder_path, pHash, hash_dict))
#     p.close()  # 用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
#     p.join()  # 没有join，则主进程直接执行任务结束！对Pool对象调用join()方法会等待所有子进程执行完毕
#     print(len(hash_dict))
#     return hash_dict
#
# if __name__ == '__main__':
#     folder_path = '/Users/ls/code/images的副本'
#     get_hash_dict_mul(folder_path)


