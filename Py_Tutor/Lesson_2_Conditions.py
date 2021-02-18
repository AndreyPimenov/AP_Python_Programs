#0.1  finding module
x = int(input())
if x > 0:
    print(x)
else:
    print(-x)

#0.2 detecting point placement on which quater of the decard system this point is located
x = int(input())
y = int(input())
if x > 0:
    if y > 0:               # x > 0, y > 0
        print("Первая четверть")
    else:                   # x > 0, y < 0
        print("Четвертая четверть")
else:
    if y > 0:               # x < 0, y > 0
        print("Вторая четверть")
    else:                   # x < 0, y < 0
        print("Третья четверть")
        
# или так:
x = int(input())
y = int(input())
if x > 0 and y > 0:
    print("Первая четверть")
elif x > 0 and y < 0:
    print("Четвертая четверть")
elif y > 0:
    print("Вторая четверть")
else:
    print("Третья четверть")       
 
 
# NB Операторы сравнения в Питоне можно объединять в цепочки 
# (в отличии от большинства других языков программирования, где для этого нужно использовать логические связки), например, a == b == c или 1 <= x <= 10
   
#0.3 
a = int(input())
b = int(input())
if a % 10 == 0 or b % 10 == 0: # проверка заканчиваются ли числа на ноль
    print('YES')
else:
    print('NO')
if a > 0 and not (b < 0): # проверка что а больше 0, а число b меньше нуля
     print('YES')
else:
    print('NO')
n % 2 == 0 and m % 2 == 0 # проверка что числа четные
     print('YES')
else:
    print('NO')
    
#1
a = int(input())
b = int(input())

if a < b:
    print (a)
else:
    print (b)
    
# 2
# В математике функция sign(x) (знак числа) определена так:
# sign(x) = 1, если x > 0,
# sign(x) = -1, если x < 0,
# sign(x) = 0, если x = 0.
# Для данного числа x выведите значение sign(x). Эту задачу желательно решить с использованием каскадных инструкций if... elif... else.
a = int(input())
if a < 0:
    print (-1)
elif a == 0:
    print (0)
else:
    print (1)
    
    
# 3
# Заданы две клетки шахматной доски. Если они покрашены в один цвет, то выведите слово YES, а если в разные цвета — то NO. 
# Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки.
a = int(input()) # column of the 1st cell 
b = int(input()) # row of the 1st cell 
c = int(input()) # column of the 2nd cell 
d = int(input()) # row of the 2nd cell 

if (a + b) % 2 == 0  and (c + d) % 2 == 0 or (a + b) % 2 == 1  and (c + d) % 2 == 1:
    print ("YES")
else:
    print ('NO')

# интересное решение:
if (x1 + y1 + x2 + y2) % 2 == 0:
    print('YES')
else:
    print('NO')

# 4 Дано натуральное число. Требуется определить, является ли год с данным номером високосным. Если год является високосным, то выведите YES, иначе выведите NO. 
# Напомним, что в соответствии с григорианским календарем, год является високосным, если его номер кратен 4, но не кратен 100, а также если он кратен 400.

a = int(input())
if a % 4 != 0:
    print ("NO")
elif a % 100 == 0 and a % 400 !=0 : 
    print ("NO")
else:
    print ("YES")
    
# интересное решение:
year = int(input())
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print('YES')
else:
    print('NO')

# 5 
a = int(input())
b = int(input())
c = int(input())
if (a < b) and (a < c):
    print (a)
elif (b < c):
    print (b)
else:
    print (c)

# интересное решение:
if b >= a <= c:
    print(a)
elif a >= b <= c:
    print(b)
else:
    print(c)




