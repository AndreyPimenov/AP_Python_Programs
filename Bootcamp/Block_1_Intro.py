# Дан список целых чисел. Требуется “сжать” его, переместив все ненулевые элементы в левую часть списка, не меняя их порядок, а все нули - в правую часть. 
# Порядок ненулевых элементов изменять нельзя, дополнительный список использовать нельзя, задачу нужно выполнить за один проход по списку. Распечатайте полученный список.
# Пример входных данных: 
4 0 5 0 3 0 0 5 
# Пример результата: 
4 5 3 5 0 0 0 0

# -------------------------------------------

# тестовые выборки:
# 4 0 5 0 3 0 0 5
# 0 1 0 0 2 0 0 0 3 0
# 0 1 0 0 2 0 0 0 3 0 0 0 0 4 0
# 0 1 0 0 2 0 0 0 3 0 0 0 0 4 0 0 0 0 0 5 0
# 0 1 0 0 2 0 0 0 3 0 0 0 0 4 0 0 0 0 0 5 0 0 0 0 0 0 6 0

numb_list = [int(x) for x in input().split()]
n = len(numb_list) 
k = numb_list.count(0)

for i in range(0, n):
    if ((numb_list[i] == 0) and (k != 0)):
        while ((numb_list[i] == 0) and (k != 0)) : 
            numb_list.pop(i)
            numb_list.append(0)
            k = k - 1
                
    print(numb_list[i], end = ' ')
    
#---------------------------------------

# Напишите программу, которая запрашивает у пользователя количество строк для введенного стихотворения. 
# Дальше дает пользователю возможность пользователю ввести нужное число строк.
# Затем нужно вывести количество строк, гласных и согласных в стихотворении и в каждой строке.
# Для упрощения давайте вводить стихотворение только маленькими русскими буквами. 

# гласные: а, о, у, э, ы, я, е, ю, и 
# тестовая выборка:
#белеет парус одинокой
#в тумане моря голубом
#что ищет он в стране далекой
#что кинул он в краю родном
#играют волны ветер свищет
#и мачта гнется и скрыпит
#увы он счастия не ищет
#и не от счастия бежит
#под ним струя светлей лазури
#над ним луч солнца золотой
#а он мятежный просит бури
#как будто в бурях есть покой

print ("Сколько будет строк в стихотворении?")
n = int (input())

# гласные: а, о, у, э, ы, я, е, ю, и 
a_volwes, b_spaces, c_consonants = 0, 0, 0

#def simbol_counter():
s=str(input())
for i in range (0, len(s)):
    if (s[i]=='а' or s[i]=='о' or s[i]=='у' or s[i]=='э' or s[i]=='ы' or s[i]=='я' or s[i]=='е' or s[i]=='ю' or s[i]=='и'):
        a_volwes += 1 
    
    elif s[i] == ' ':
        b_spaces += 1 
    #c_consonats = len(s) - a_volwes - b_spaces
    
    #return  a_volwes, b_spaces, c_consonats   


#for i in range (0, n): # цикл по строкам:
#a_volwes, b_spaces, c_consonants += simbol_counter()
print ("Гласных:", a_volwes)
print ("Согласных:", len(s) - a_volwes - b_spaces)


