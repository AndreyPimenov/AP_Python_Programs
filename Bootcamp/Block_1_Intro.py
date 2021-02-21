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

# Решение 1: Подход через внутренний цикл, но в этом случае весь список проходится кртано больше 1-го раза:
for i in range(0, len(numb_list)):
    for j in range (0, numb_list.count(0)):
        numb_list.append(0)
        numb_list.remove(0)
    print(numb_list[i], end = ' ')
    

# Решение 2: Использование basis - возвращающей к тому же месту списка, с которого начали смотреть последовательность нулей:
numb_list = [int(x) for x in input().split()]

for i in range(0, len(numb_list)):
    if numb_list[i] == 0:
        numb_list.append(0)
        if numb_list[i+1] != 0:
            numb_list[i] = numb_list[i+1]
            numb_list.pop(i+1)
        else: # in case the sequence of zeros:
            basis = i
            while (numb_list[i] == 0) and (len(numb_list) - basis > 1):
                numb_list.pop(i)
                numb_list.append(0)
                basis = basis + 1
            
    print(numb_list[i], end = ' ')
    
    
    numb_list = [int(x) for x in input().split()]
count = 0
n = len(numb_list)
k = numb_list.count(0)

print (n, k)

for i in range(0, n):
    if numb_list[i] == 0:
        count = count + 1 
        numb_list.append(0)
        if numb_list[i+1] != 0:
            numb_list[i] = numb_list[i+1]
            numb_list.pop(i+1)
        else: # in case the sequence of zeros:
            basis = i
            while (numb_list[i] == 0) and ((count + basis) < k):
                numb_list.pop(i)
                numb_list.append(0)
                basis = basis + 1
            
    print(numb_list[i], end = ' ')
#print (numb_list)

n = len(numb_list)
k = numb_list.count(0)
count = 0

print (n, k)

for i in range(0, n):
    if numb_list[i] == 0:
        count = count + 1 
        numb_list.append(0)
        if numb_list[i+1] != 0:
            numb_list[i] = numb_list[i+1]
            numb_list.pop(i+1)
        else: # in case the sequence of zeros:
            basis = i
            while (numb_list[i] == 0) and ((count + basis) < k):
                numb_list.pop(i)
                #numb_list.append(0)
                basis = basis + 1
            
    print(numb_list[i], end = ' ')
print (numb_list)

    
