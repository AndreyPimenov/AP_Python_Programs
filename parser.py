# лекторий:
# 1) о том как прописать путь к папке или файлу с помощью Python
# https://pythonturbo.ru/kak-propisat-na-python-put-k-fajlu-v-windows-mac-i-linux/?ysclid=lpaw08o4ei358216493
# 2) о том как в имя фала добавить переменную:

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from pathlib import Path

data_folder = Path("C:/Users/andrey.pimenov/Desktop/Exp/1")
# {1, 2, 3} - для тестирования
# 4 5 6 - the relevant for Zirconium,
# 7 - additional for Titanium

file = "0000"
string = "SN-2023-11-22-13-27-36-00000" + file + ".csv"
file_to_open = data_folder / string
#f = open(file_to_open)
#print(f.read())

x_list = []
y_list = []

def parser_func():
    with open(file_to_open, 'r') as f:
        for i in range(9): # тут пропускаем мета-данные
            f.readline()
        for i in range(2048): # тут цикл считывания всех строк
            line = f.readline()
            for j in range (len(line)):
                if line[j] == ',':
                    boarder = j
            # тут разделение на x и y:
            x = float(line[0:boarder])
            y = float(line[(boarder+1):])
            x_list.append(x)
            y_list.append(y)
    #print(x_list, y_list, len(x_list), len(y_list))

parser_func()
print(x_list)
print(y_list)
