# лекторий:
# 1) о том как прописать путь к папке или файлу с помощью Python
# https://pythonturbo.ru/kak-propisat-na-python-put-k-fajlu-v-windows-mac-i-linux/?ysclid=lpaw08o4ei358216493
# 2) о том как в имя фала добавить переменную:

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pathlib import Path

data_folder = Path("/home/andrey/Desktop/Exp/Exp/5 - workone/")  #("C:/Users/andrey.pimenov/Desktop/Exp/1")
# {1, 2, 3} - для тестирования
# 4 5 6 - the relevant for Zirconium,
# 7 - additional for Titanium

x_list = [str()] * 2048
y_list = [str()] * 2048
data_t = [str()] * 2048

def parser_func(file_to_open):
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
            x_list[i] = x
            y_list[i] = y
            #x_list.append(x)
            #y_list.append(y)

def save_data_func(both_list_flag): # if 0 = init, if 1 = add

    with open(file_to_save, 'r+') as f:
        if both_list_flag == 0:
            for i in range(len(x_list)):
                x = x_list[i]
                f.write(str(x))
                f.write('\n')

        elif both_list_flag == 1:
            for i in range(len(y_list)):
                y = y_list[i]
                line = f.readline()

                output = line.replace('\n', (" " + str(y) + '\n'))
                # print(output)

                data_t[i] = output
                print(data_t[i])
                data_t.append(output)

    with open(file_to_save, 'r+') as f:
        for i in range(len(x_list)):
            f.write(data_t[i])



# Шаг 1 - выбераем файл:
file = 1 # 1 - 332
string = "Exp_5_" + str(file) + ".csv"
file_to_open = data_folder / string
file_to_save = data_folder / "biuld.txt"

for file in range(332):
    string = "Exp_5_" + str(file) + ".csv"
    file_to_open = data_folder / string
    file_to_save = data_folder / "biuld.txt"

    if file == 1:
        parser_func(file_to_open)
        save_data_func(0)
        print ("Сделал X")
        save_data_func(1)
        print ("Cделал Y")
    elif (file > 1):
        print (file_to_open)
        parser_func(file_to_open)
        save_data_func(1)
