# Задача 1

# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции

# Алгоритм работы:
# 1. Формирование изначального списка на основе всех .sql файлов в директории
# 2. Функция проверки наличия введенной строки в файле
# 3. Цикл перебора файлов в зависимости от того сколько их осталось и нажимали ли

# шаг 1:
import os
import glob


# шаг 2:
# Функция принимает строку введеную пользователем и имя файла в котором нужно произвести поиск
# Построчно ищет в файле и возвращает: True -  если в файле было совпадение, False - если совпадения не было
def match_searcher(input_str, sql_file):
    coinsidence = False
    with open(sql_file) as f:
        for line in f:
            #print(line)
            if input_str in line:
                coinsidence = True
                break
            else:
                coinsidence = False
    return (coinsidence)


# шаг 3:
# Функция которая получает список файлов и строку для поиска для каждого файла запускает фунцию поиска
# возвращает новый список и кол-во элементов в нем
def list_former(input_str, path_list):
    new_list = []
    for i in range(len(path_list)):
        if (match_searcher(input_str, path_list[i])) != False:
            new_list.append(path_list[i])
    return new_list

# шаг 1:
# Получение изначального списка:
migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)

files = glob.glob(os.path.join(migrations, "*.sql"))
path_list = []
for file in files:
    print(file)
    path_list.append(file)
print(path_list)
print(len(path_list), ' .sql фалов в папке изначально')

# Отработка кода:
# print('введите строку:')
# a = input()
# print(a)
#
# b = match_searcher(a, 'Migrations\\000_1-28_Create_user_grant_rights_A400M.sql')
# print(b)
#
# c = list_former(a, path_list)
# print(c)
# print(len(list_former(a, path_list)), 'столько файлов осталось')

# Интерфейсная часть програамы:
print('В поисковике файлов доступен выход при нажатии клавиши: "q" - quit' )

while (1):
    print(' \n введите строку:')
    input_str = input()
    if input_str != 'q':
        print(list_former(input_str, path_list))
        print(len(list_former(input_str, path_list)), 'столько файлов осталось')
        path_list = list_former(input_str, path_list)
    else:
        break
