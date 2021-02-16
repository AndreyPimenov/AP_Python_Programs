# Problem 1 Summ of three numbers----------------------
# Эта программа считывает три числа и выводит их сумму:
a = int(input())
b = int(input())
c = int(input())

print(a + b + c)


# Problem 2 Area of the square angle triangle----------
# Числа b и h можно считывать так:
b = int(input())
h = int(input())
# Выводите результат через print()
S = 1/2 * b * h
print(S)

# Problem 3 Apples --------------------------------------
# Число n можно считать так:
n = int(input())
k = int(input())

# Выводите результат через print()
print(k // n)
print (k % n)

# Пример на деление, вычисление частного и остатка:
#print(63 / 5)
#print(63 // 5)
#print(63 % 5)

#------------------ Problem 4 ----------------------------
n = int(input())
# (n % 1440) - кол-во минут в последних сутках
print ((n % 1440) // 60)
print ((n % 1440) % 60)

# ---------------- Problem 5 -----------------------------
s = input()
print('Hello, ' + s + '!')

# ---------------- Problem 6 -----------------------------
n = int(input())
print ('The next number for the number ' + str(n) + ' is ' + str(n+1) )
print ('The previous number for the number ' + str(n) + ' is ' + str(n-1))

# ---------------- Problem 7 -----------------------------
n1, n2, n3 = int(input()), int(input()), int(input())
print ((n1//2 + n2//2 + n3//2) + (n1%2 + n2%2 + n3%2))

# ---------------- Problem 8 -----------------------------
a, b, l, N = int(input()), int(input()), int(input()), int(input())
print (2*l + (2*N-2)*(b + a) + a )


