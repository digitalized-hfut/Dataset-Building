#!/usr/bin/python
#-*- coding: UTF-8 -*-

import os

name_path = 'C:\Coding\Faster_RCNN(Project_1)\Dataset\Img5' 
xml_path = 'C:\Coding\Faster_RCNN(Project_1)\Annotation\Img5'
list_name = []
list_rename = []

class read_name_of_file:
    def __init__(self, path, list):
        self.path = path
        self.list = list

    def reading(self):
        for name in os.listdir(self.path):
            content = os.path.splitext(name)[0]
            self.list.append(content)

class rename_file:
    i = 0;
    def __init__(self, counter, list_1, list1_path, list_2, list2_path):
        self.counter = counter
        self.list_1 = list_1
        self.list1_path = list1_path
        self.list_2 = list_2
        self.list2_path = list2_path

    def renaming(self):
        while rename_file.i < self.counter:
            if self.list_2[rename_file.i] != self.list_1[rename_file.i]:
                os.rename(self.list2_path + '\\' + self.list_2[rename_file.i] + '.xml', self.list2_path + '\\' + self.list_1[rename_file.i] + '.xml')
            rename_file.i += 1

def main():
    Read = read_name_of_file(name_path, list_name)
    Read.reading()

    Read_1 = read_name_of_file(xml_path, list_rename)
    Read_1.reading()

    if len(list_name) != len(list_rename):
        print('!ERROR!')
    else:
        counts = len(list_name)
        working = rename_file(counts, list_name, name_path, list_rename, xml_path)
        working.renaming()
        print('\n%d images were Finished, My Lord.'%counts)

if __name__ == '__main__':
    main()
    