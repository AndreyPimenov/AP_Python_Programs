# 2.1 Открытие и чтение файла, запись в файл
# Необходимо написать программу для кулинарной книги
# Список рецептов должен храниться в следующем формате:
# Название блюда
# Кол-во ингридлиентов в блюде
# Навзание ингридиента | Кол-во | Единица измерения

# В одном файле может быть произвольное кол-во блюд
# читать список рецептов из этого файла
# разбивать логику на функции и не использовать глобальных переменных

# Задача 1 Должен получиться следующий словарь:
'''
cook_book = {
  'Омлет': [
    {'ingridient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingridient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingridient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingridient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingridient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingridient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingridient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingridient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingridient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'},
    {'ingridient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }
'''


# Замечу, что требуемый формат файла это словарь, значениями котрого явля-ся списки ингридиентов, а ключами названия блюд. Причем каждый ингридиент это словарь с ключами: название, кол-во, ед. измр-ия и соответвующими значениями.

# задача 1: Формирования словаря, решается одной функцией
# создать словарь
# открыть файл
# # считывать по строчке
# # теперь нужно правильно наполнить словарь

# Функция формирования словаря кулинарной книги из файла:
def create_dict():
    CookBook_dict = {}
    with open('CookBook.txt') as f:
        for line in f:
            dish = line
            if dish == '\n':
                # print ('закончилось')
                dish = f.readline()
            ingridients_number = int(f.readline().strip())
            # print('кол-во:',ingridients_number)
            dish_list = []  # пустой список для будущих блюд
            for i in range(ingridients_number):
                ingr = f.readline().strip().split(' | ')
                # print (ingr)
                # наполнение словаря ингридиента:
                ingridient_dict = {'ingridient_name': ingr[0], 'quantity': ingr[1], 'measure': ingr[2]}
                # print (ingridient_dict)
                # наполнение списка блюда:
                dish_list.append(ingridient_dict)
                # dishes = '{}\n'.format(dish_list)
                # наполение по новому ключу расширяет словарь
                CookBook_dict[dish.strip()] = dish_list
            # print(dish_list)
    # print(CookBook_dict)
    return CookBook_dict


# Доп функция форматирование вывода:
def dictionary_output(Dictionary):
    for key, value in Dictionary.items():  # CookBook_dict.items():
        print(key, ': \n', value, '\n')


# Решил написать функцию по добавлению в файл новых блюд, с предварительной проверкой записи.
# ввести информацию о блюде, кол-ве ингридиентов, самих ингридиентах
# все ли верно?
# # записать в кулинарную книгу? Y / N
# # записать в файл: Cook_Book.txt

# Функция добавления нового блюда в файл:
def add_dish():
    # сбор информации:
    print('введите название нового блюда')
    new_dish_name = input()

    # создание списка в котором будут хран-ся словари ингириентов блюда:
    new_dish_list = []

    print('кол-во ингридиентов')
    try:
        ingrs_num = int(input())
    except ValueError:
        print('got Value error' + 'Вы ввели не число')

        # построчная интерпретация ингридиентов нового блюда:
    try:
        print('укажите одной строкой через запятую:')
        for i in range(ingrs_num):
            print(i + 1, '-й ингридиент, его кол-во, и измеряемая величина:')
            ingr = list(input().split(','))
            ingridient_dict = {'ingridient_name': ingr[0], 'quantity': ingr[1], 'measure': ingr[2]}
            new_dish_list.append(
                ingridient_dict)  # NB далее обращаясь к элементам этого списка, мы работаем со словарем (каждый элемент списка - словарь)
    except IndexError:
        print('got IndexError')
    except ValueError:
        print('got Value error')
    except TypeError:
        print('got TypeError')
    finally:
        print('записать рецепт в файл? - Y/N')
        if input() == 'Y':
            print('Да')
            # тут дозаписываем в уже существующий текстовый файл:
            f = open('CookBook.txt', 'a')
            try:
                f.write('\n' + new_dish_name + '\n')  # запишем название блюда
                f.write(str(ingrs_num) + '\n')  # запишем кол-во ингридиентов в блюде
                for i in range(ingrs_num):
                    f.write(new_dish_list[i].get('ingridient_name') + ' | ' + new_dish_list[i].get('quantity') + ' | ' +
                            new_dish_list[i].get('measure') + '\n')

            except IOError:
                print("An IOError has occurred!")
            except IndexError:
                print("got Index Error")
            finally:
                # f.write('\n') #добавить отступ строки после нового блюда
                print('Новый рецепт записан')
        else:
            print('Не стали перезаписывать файл')


# Задача2
# Нужно написать функцию, которая на вход принимает список блюд из cook_book и количество персон для кого мы будем готовить
'''
На выходе:
{
  'Картофель': {'measure': 'кг', 'quantity': 2},
  'Молоко': {'measure': 'мл', 'quantity': 200},
  'Помидор': {'measure': 'шт', 'quantity': 8},
  'Сыр гауда': {'measure': 'г', 'quantity': 200},
  'Яйцо': {'measure': 'шт', 'quantity': 4},
  'Чеснок': {'measure': 'зубч', 'quantity': 6}
}
'''


# указать персон, выбрать блюда
# # построчный поиск в словаре
# формироавние списка покупок для ужина

def welcome_dinner(Dictionary):
    print('На скольких человек будет ужин: ')
    persons = int(input())
    print('Укажите черз запятую названия блюд, которые планируете включить в ужин (в расчете на 1 человека):')
    dinner_dishes = list(input().split(', ' or ' '))

    # формирование словаря:
    shop_dict = {}  

    # наполнение словарей значениями в зависимости от кол-ва персон на ужине
    for i in range(len(dinner_dishes)):
        for key in Dictionary.keys():
            if dinner_dishes[i] == key:
                dish_receipt = Dictionary.get(key)
                for j in range(len(dish_receipt)):
                    dish_receipt[j]['quantity'] = int(dish_receipt[j]['quantity']) * persons
                    if dish_receipt[j]['ingridient_name'] not in shop_dict:
                        shop_dict[dish_receipt[j]['ingridient_name']] = dish_receipt[j]
                    else:
                        shop_dict[dish_receipt[j]['ingridient_name']]['quantity'] += dish_receipt[j]['quantity']

    # распечатка
    return shop_dict


# Интерфейсная часть программы:
print(
    'В программе кулинарная книга вы можете выбрать любое из следующих доступных действий:\n nd - (new dish), добавить новое блюдо, \n bv - (book view), посмотреть рецепты из книги, \n wd - (welcome dinner) - список покупок для формирования стола и угощения людей \n q - (quit) кроме того вы можете завершить работу программы:  \n Приятного аппетита =)')
# тут я все-таки использую глобальную переменную user_command
while (true):
    print('\n введите команду:')
    User_command = input()
    if User_command == 'q':
        break
        print("Работа программы завершена")
    elif User_command == 'nd':
        add_dish()
    elif User_command == 'bv':
        dictionary_output(create_dict())
    elif User_command == 'wd':
        dictionary_output(welcome_dinner(create_dict()))
