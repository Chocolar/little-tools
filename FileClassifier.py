# -*- coding: utf-8 -*-

'''
通过文件后缀进行文件整理分类
'''

import os
import shutil


class Tidy():

    def __init__(self, path):
        self.suffix_d = {
            '图片': ['.jpg', '.png', '.gif', '.bmp', '.jpeg','.raw','.tif','.ico'],
            '文档': ['.pdf', '.doc', '.json', '.mobi','.txt','.docx','.md'],
            '压缩包': ['.7z', '.rar', '.zip','.gz','.tar','.z'],
            '安装包': ['.exe', '.EXE', '.msi'],
            '文献': ['.caj'],
            '表格':['.xlsx','.xls','.csv','.'],
            '视频':['.avi','.mp4','.rmvb','.mkv','.mpg','.webm','.mov','.fiv','.m4v','.fiv'],
            '音频':['.wmv','.mp3','.mid','.wav','.ogg','.amr','.m4a','.flac'],
        }
        self.path = os.path.normpath(path)

    def create_dir(self):
        '''从字典创建对应目录'''
        for i in self.suffix_d.keys():
            try:
                os.makedirs(self.path + '/' + i)
            except FileExistsError:
                pass

    def get_keys(self, value):
        '''从字典获取文件后缀对应的目录名'''
        for k, v in self.suffix_d.items():
            if value in v:
                return k

    def move(self):
        '''移动文件到对应目录'''
        for f in os.listdir(self.path):
            try:
                suffix = os.path.splitext(f)[1]
                dir_name = self.get_keys(suffix)
                if dir_name:
                    try:
                        shutil.move(self.path+'/'+f, self.path+'/'+dir_name)
                    except Exception as e:
                        print(e)
            except PermissionError:
                print('目标文件访问出错')

    def remove_dir(self):
        '''删除空目录'''
        for i in self.suffix_d.keys():
            try:
                os.rmdir(self.path + '/' + i)
            except OSError:
                pass

    def start(self):
        print('开始整理...')
        self.create_dir()
        self.move()
        self.remove_dir()
        print('完成')


if __name__ == "__main__":
    tidy = Tidy(input())
    tidy.start()