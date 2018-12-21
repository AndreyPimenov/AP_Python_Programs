
# Необходимо реализовать менеджер контекста, печатающего на экран:
# 1. Время запуска в менеджере контекста
# 2. Время окончания работы кода
# 3. Сколько было потрачено времени на выполнение кода
# Придумать и написать программу, использующую менеджер контекста из 1-го задания
# -------------------------------------------------------------------------------
# Как я вижу решение:
# 1. открываем файл
# 2. запускаем функцию
# 3. закрываем файл



import time
import textwrap

start = time.monotonic()
print ('the time is: ', time.time())

class ContextManager:
    """
    Самодельный менеджер контекста для запуска разных функций работы с файлом
    """

    # obj = self.__enter__

    def __init__(self, obj, timer_time):
        self.obj = obj           # запускает объект
        self.timer = timer_time  # инициализирует временную метку

    def __enter__(self):
        return self.obj          # привязка к активному объекту with-блока






def triadfunction():
    """
    # Дан список, состоящий из n элементов:
    # 1. разбить исходный на триады (группа трех соседних элементов)
    # если элементы не вошли в триаду, то убрать их из рассмотрения.
    # 2. Вычислить сумму каждой триады
    # 3. Вывести на экран триады, в порядке возрастания их суммы
    # 4. Записать результаты в файл
    # 5. Особенность файла в том, что в его названии указана дата
    """

    # введем список
    from random import randrange
    print("Введите кол-во элементов в списке")
    n = int(input())
    list_random = [randrange(0, 1 * n) for i in range(n)]
    print("Исходный список:" + '\n', str(list_random) + '\n')

    # Формируем список, который можно разбить на триады:
    if n % 3 == 2:
        list_random = list_random[:-2]
    elif n % 3 == 1:
        list_random = list_random[:-1]
    print("Cписок, который можно разбить на триады:" + '\n', str(list_random) + '\n')

    # Задание 1 и 2. Формируем через два списка.
    triada = []  # сюда будем сохранять значения текущей триады
    list_triad = []  # это список списков, где каждый элемент это триада
    list_sum = []  # это список сумм
    i, j, k = 0, 0, 0

    for i in range(len(list_random)):
        if j < 3:
            triada.append(list_random[i])
            j += 1
        if j == 3:
            print(triada, sum(triada))
            list_triad.append(triada)
            list_sum.append(sum(triada))
            k += 1
            triada = []
            j = 0

    # задание 3.
    print(sorted(list_triad))
    return (list_triad)

# получаем значение, которое хотим записать в файл:
triad_list = triadfunction()


# Вариант работы работы без контекст менеджера
# дописываем в файл:
f = open('LogFile.txt', 'a') # тут дописываем информацию в файл
try:
    f.write(str(triad_list) + '\n')

except IOError:
    print("An IOError has occured")

except IndexError:
    print("got Index error")

finally:
    print ('триады сформированы, отсортированы и записаны')

# В работе над проектом очень помогла эта ссылка:
# https://www.internet-technologies.ru/articles/modul-time-taymery-vremeni.html

# get_clock_info()

print ('the time is: ', time.time())
end = time.monotonic()

print ('start : {:>9.2f}'.format(start))
print ('end   : {:>9.2f}'.format(end))
print ('span  : {:>9.2f}'.format(end - start))
