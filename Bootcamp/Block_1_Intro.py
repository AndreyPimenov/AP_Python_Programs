# Дан список целых чисел. Требуется “сжать” его, переместив все ненулевые элементы в левую часть списка, не меняя их порядок, а все нули - в правую часть. 
# Порядок ненулевых элементов изменять нельзя, дополнительный список использовать нельзя, задачу нужно выполнить за один проход по списку. Распечатайте полученный список.
# Пример входных данных: 
4 0 5 0 3 0 0 5 
# Пример результата: 
4 5 3 5 0 0 0 0

numb_list = [int(x) for x in input().split()]
print(numb_list)

for i in range(0, len(numb_list)):
    if numb_list[i] == 0:
        numb_list.append(0)
        if numb_list[i+1] != 0:
            numb_list[i] = numb_list[i+1]
            numb_list.pop(i+1)
        else:
            numb_list.pop(i)
            numb_list.pop(i)
            numb_list.append(0)
            
print(str(numb_list))


