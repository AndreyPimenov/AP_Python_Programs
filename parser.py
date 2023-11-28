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

# Перестроить логику работы программы:
# 1 - Берем один файл и записываем X
# 2 - Потом в потоке берем в цикле каждый файл
# 3 -
# Парсим каждый фвйл и сохраняем X и Y для 1-го графика, а потом от каждого файла берем Y

# Шаг 1 - выбераем файл:
file = "0000"
string = "SN-2023-11-22-13-27-36-00000" + file + ".csv"
file_to_open = data_folder / string
file_to_save = data_folder / "biuld.txt"

# Шаг 2 - парсим файл file = "0000":
#parser_func(file_to_open)

# Шаг 3 - сохраняем этот файл с X и с Y:
#save_data_func(0)
#print ("Сделал X")

#save_data_func(1)
#print ("Cделал Y")

#Прогоняем по всем файлам из папки:
for i in range (40):

    if i <= 9:
        file = "000" + str(i)
        string = "SN-2023-11-22-13-27-36-00000" + file + ".csv"
        file_to_open = data_folder / string
        file_to_save = data_folder / "biuld.txt"
        if i == 0:
            parser_func(file_to_open)
            save_data_func(0)
            print ("Сделал X")
            save_data_func(1)
            print ("Cделал Y")
        else: # 1 - 9:
            file = "000" + str(i)
            string = "SN-2023-11-22-13-27-36-00000" + file + ".csv"
            file_to_open = data_folder / string

            print (file_to_open)
            parser_func(file_to_open)
            #save_data_func(0)
            #print(y_list)
            save_data_func(1)

    elif (i > 9) and (i < 40):
        print("hi")

#    elif: ((i > 0) && (i < 9)):

 #   file = str()

# поработай через np
