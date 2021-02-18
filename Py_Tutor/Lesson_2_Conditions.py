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
 
# NB Операторы сравнения в Питоне можно объединять в цепочки 
# (в отличии от большинства других языков программирования, где для этого нужно использовать логические связки), например, a == b == c или 1 <= x <= 10
   


