# Написать программу, которая будет выводить топ 10 самых часто встречающихся в новостях слов
# длиннее 6 символов для каждого файла.
# В решении домашнего задания вам могут помочь: split(), sort или sorted.

# Написать программу, к. выводит 10 самых часто встречающихся в новостях слов длиннее 6 символов для каждого файла.

# Принцип работы программы:
# 1 - работа с json файлом
# 2 - работа с xml файлом
# 0 - выход из программы

# 1:
# Фунция Ф1: чтение .json файла, на входе файл, на выходе словарь
# Далее идет основная Ф2, которая проходит по глубинному ключу 'description' и формирует новый список
# Ф3: во входящем списке находит 10 самых часто встрчающихся слов длиннее 6 символов и выводит их на экран

# 2:
# Фунция Ф4: чтение .xml файла, на входе файл, на выходе словарь
# Далее идет основная Ф2, которая проходит по каждому ключу (в данном случае это id) и для каждого вызывает Ф3
# Ф3: проходит по спискам и в кажлом списке находит 10 самых часто встрчающихся слов длиннее 6 символов

# -------------------------------------------------------------------------------------------------------

# Подготовительный этап:
import json
from pprint import pprint


# Ф1. на вход .json файл на выход словарь:
def json_dic(file_name):
    with open(file_name + '.json', encoding='utf-8') as datafile:
        json_data = json.load(datafile)
    return json_data


# ф2. по ключу 'rss' вызвать содержание исходного словаря, далее:
# --> по ключу 'channel' содержание -->
# --> по ключу 'items' содержание это список
# цикл по всем элементам списка:
# каждый элемент списка это словарь в котором по ключу 'description' смотреть содержание
def digging_data(dictionary):
    # будущий список для Ф3:
    mass_data = []

    # цикл в том случае если не один, а несколько информационных каналов
    keys = dictionary.keys()
    for key in keys:
        # добираемся до сути:
        main_list = dictionary.setdefault(key).setdefault('channel').setdefault('items')
        # pprint(main_list)
        pprint(len(main_list))
        for i in range(len(main_list)):
            # a = main_list[i].setdefault('description')
            # pprint(main_list[i].setdefault('description'))
            # print(i)
            # print(len(a),'\n')
            mass_data.append(main_list[i].setdefault('description'))
    pprint(mass_data)
    # важно что это список списков:
    return mass_data


# ф3. Получен список, в котором каждый элемент это список символов:
# Запустить цикл по всем спискам списка и для каждого: если элемент списка меньше 6 символов, то удалить
# распечатать на экране
def topten_searcher(list):
    # формирование единого списка в котором бужем искать топ 10 наиболее чатсо встречаемых слов
    one_list = []

    # поиск по всем спискам:
    for i in range(len(list)):
        new_list = list[i].split(' ')
        for word in new_list:
            print(len(word))
            if len(word) >= 6:
                one_list.append(word)

    # отсортируем полученный список слов в алфавитном порядке:
    pprint(sorted(one_list))















# Тектсовый интерфейс управления всей программой:
print(
    "Управление:\n 0 - выход,\n 1 - запуск .json файла,\n 2 - запуск .xml файла\n")

while (True):
    print("\n  Введите команду")
    user_command = input()
    if user_command == '0':
        print("Работа программы завершена")
        break

    elif user_command == '1':
        print('Работаем с .json файлом')
        print("Введите название файла")
        file_name = input()

        print("Печать содержимого rss: ")
        topten_searcher(digging_data(json_dic(file_name)))

    elif user_command == '2':
        print('Работаем с .xml файлом')
        print('Работаем с .json файлом')
        print("Введите название файла")
        file_name = input()

        pprint(json_dic(file_name))
