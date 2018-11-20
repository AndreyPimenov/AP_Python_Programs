# нужно реализовать Польскую нотацию двух положительных чисел. 
# Реализовать нужно будет следующие операции: сложение, вычитание, умножение, деление

#С помощью метода assert проверять что числа положительные
#C помощью метода try/exception ловить ошибки и выводить предупреждения
print ( "Добро пожаловать в программу: калькулятор простых операций, записанных в Польской нотации над двумя положительными числами" )
print ('Можно работать: ')

equation = input().split(' ')

print ('знак =  ', equation[0])
print ('знак =  ', equation[1])
print ('знак =  ', equation[2])



try:
    a = float(equation[1]) 
    b = float(equation[2])

    assert a > 0, 'первое число не положительное' 
    assert b > 0, 'второе число не положительное'
    
    if equation[0] == '+':
        print (a + b)
    elif equation[0] == '-':
        print (a - b)
    elif equation[0] == '/':
        print (a / b) 
    elif equation[0] == '*':
        print (a * b)
    else:
        print ('Неправильно ввели операнд')
   
except IndexError:
    print ('got IndexError')
except TypeError:
    print ('got TypeError')
except ValueError:
    print ('got Value error')
finally:
    print('Готово')

    
#Задание 3 по ссылке: https://repl.it/@Numenorec/Homework4     
