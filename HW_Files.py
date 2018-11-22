#2.1 Открытие и чтение файла, запись в файл
# Необходимо написать программу для кулинарной книги
# Список рецептов должен храниться в следующем формате:
# Название блюда
# Кол-во ингридлиентов в блюде
# Навзание ингридиента | Кол-во | Единица измерения

# В одном файле может быть произвольное кол-во блюд
# читать список рецептов из этого файла
# разбивать логику на функции и не использовать глобальных переменных 

#Задача 1 Должен получиться следующий словарь:
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
# Замечу, что требуемый формат файла это словарь, состоящий из списков блюд, причем каждое блюдо это словарь с ключами: название, кол-во, ед. измр-ия 

# задача 1:
# создать словарь
# открыть файл 
# # считывать по строчке
# # теперь нужно правильно наполнить словарь

# Функция формирования словаря кулинарной книги из файла:
def Create_Dict():
  CookBook_dict = {}
  with open ('CookBook.txt') as f:
    for line in f:
      dish = line
      if dish == '\n':
        #print ('закончилось')
        dish = f.readline()
      ingridients_number = int(f.readline().strip())
      #print('кол-во:',ingridients_number)
      dish_list = [] #пустой список для будущих блюд
      for i in range(ingridients_number):
        ingr = f.readline().strip().split(' | ')
        #print (ingr)
        #наполнение словаря ингридиента:
        ingridient_dict = {'ingridient_name': ingr[0], 'quantity': ingr[1], 'measure': ingr[2]}
        #print (ingridient_dict)
        #наполнение списка блюда:
        dish_list.append(ingridient_dict)
        #dishes = '{}\n'.format(dish_list)
        #наполение по новому ключу расширяет словарь
        CookBook_dict[dish.strip()] = dish_list
      #print(dish_list)
  #print(CookBook_dict)
  #форматирование вывода:
  for key, value in CookBook_dict.items():
    print(key,': \n', value, '\n')


# Функция добавления нового блюда в файл:
# ввести информацию о блюде, кол-ве ингридиентов, самих ингридиентах 
# все ли верно?
# # записать в кулинарную книгу? Y / N
# # записать

def add_new_dish():
  # сбор информации:
  print ('введите название нового блюда')
  new_dish_name = input()
  print ('кол-во ингридиентов')
  # создание списка в котором будут хран-ся словари ингириентов блюда:
  new_dish_list =[] 
  try:
    ingrs_num = int(input())
  except ValueError:
    print ('got Value error' + 'Вы ввели не число') 
  
  #построчная интерпретация ингридиентов нового блюда:
  try:
    print ('укажите одной строкой через пробел:')
    for i in range(ingrs_num):
      print(i+1, '-й ингридиент, его кол-во, и измеряемая величина:') 
      ingr = list(input().split(' '))
      ingridient_dict = {'ingridient_name': ingr[0], 'quantity': ingr[1], 'measure': ingr[2]}
      #print(ingridient_dict)
      new_dish_list.append(ingridient_dict)
  except IndexError:
    print ('got IndexError')
  except ValueError:
    print ('got Value error')
  except TypeError:
    print ('got TypeError')
  
  finally:
    print('записать рецепт в файл? - Y/N')
    if input() == 'Y':
      print ('Да')
      # тут дозаписываем в уже существующий текстовый файл:
      f = open('test_write.txt', 'a')
      try:
        f.write(new_dish_name + '\n') #запишем название блюда
        f.write(str(ingrs_num)+ '\n') #запишем кол-во ингридиентов в блюде
        for i in range(ingrs_num):
          ex = str(new_dish_list[i].get(0)) # +, ' | ', + new_dish_list[i].get(1) + , ' | ', + new_dish_list[i].get(2))
          #string = str(dish_list[i])
          #f.write(string)
          print(new_dish_list[i])
      except IOError:
        print("An IOError has occurred!")
      except IndexError:
        print("got Index Error")
      finally:
        f.write()
    else:
      print ('Не стали перезаписывать файл')
print('Рецепт записан')





#Задача2
#Нужно написать функцию, которая на вход принимает список блюд из cook_book и количество персон для кого мы будем готовить
'''
def get_shop_list_by_dishes(dishes, person_count):
  shop_list = {}
  for dish in dishes:
    for ingridient in cook_book[dish]:
      new_shop_list_item = dict(ingridient)

      new_shop_list_item['quantity'] *= person_count
      if new_shop_list_item['ingridient_name'] not in shop_list:
        shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
      else:
        shop_list[new_shop_list_item['ingridient_name']]['quantity'] +=
          new_shop_list_item['quantity']
  return shop_list

def print_shop_list(shop_list):
  for shop_list_item in shop_list.values():
    print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], 
                            shop_list_item['measure']))

def create_shop_list():
  person_count = int(input('Введите количество человек: '))
  dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
    .lower().split(', ')
  shop_list = get_shop_list_by_dishes(dishes, person_count)
  print_shop_list(shop_list)

create_shop_list()

'''

# Основная работа:
print ('В программе кулинарная книга вы можете выбрать любое из следующих доступных действий:\n nd - (new dish), добавить новое блюдо, \n bv - (book view), посмотреть рецепты из книги, \n fr - (find receipt) поиск интересующего вас рецепта и его распечатка. \n wd - (welcome dinner) - список покупок для формирования стола и угощения людей \n q - (quit)кроме того вы можете завершить работу программы:  \n Приятной работы')
# тут я все-таки использую глобальную переменную user_command
while(1):
  print('\n введите команду:')
  user_command = input()
  if  user_command == 'q': 
    break;
    print ("Работа программы завершена")
  elif user_command == 'nd':
    add_new_dish()
  elif user_command == 'bv':
    Create_Dict()
  elif user_command == 'fr':
    pass
  elif user_command == 'wd':
    pass

#Create_Dict()
#add_new_dish()
