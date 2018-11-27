# Задача 3 Запустить браузер
# немного про модули ----------> https://pythonworld.ru/moduli/modul-os.html
import os
import subprocess

# возвращает текущую директорию:
current_directory = os.getcwd()
print(current_directory)

# возвращает список файлов в текущей директории:
list_of_docs = []
list_of_docs = os.listdir()
print(list_of_docs)

# немного про модуль os.path ---------> https://pythonworld.ru/moduli/modul-os-path.html
# время последнего доступа к файлу, в секундах:
last_time_opened = os.path.getatime(current_directory)
print (last_time_opened)
# время последнего изменения файла, в секундах:
last_time_changed = os.path.getmtime(current_directory)
print (last_time_changed)


# 1-й вариант открытия:
# вариант открытия браухера через запуск его exe файла по указанному пути:
os.startfile(r'C:/Program Files/internet explorer/iexplore.exe')  # запуск Internet Explorer
os.startfile(r'C:/Users/a.pimenov/AppData/Local/Yandex/YandexBrowser/Application/browser.exe')  # Yandex


# Задача 2 запускать скрипт из любой точки

__file__ = 'Problem_1.py'
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path, 'директория скрипта')

goon = os.path.join(dir_path, 'Problem_1.py')
os.startfile(goon)

