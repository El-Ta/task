print("Зад1. Определить простое ли число.")
x = int(input("Введите целое число:"))
i = 2
bool =  True
if x == 1:
    bool = True
else:
    while i != x:
        if x % i == 0:
            print("Число x =", x, "не является простым")
            bool = False
            break
        i = i+1
if bool:
    print("Число x =", x, "- простое число")

print("Зад2. Найти число Фибоначчи.")
n = int(input("Введите порядковый номер числа Фибоначчи:"))
a = 1
b = 1
if n == 1 or n == 2:
    Fib = a
else:
    for i in range(3, n+1):
        Fib = a+b
        a = b
        b = Fib
print("Число Фибоначчи под номером", n, "равно", Fib)

print("Зад3. Вывести n строк с повтрением ААА m раз.")
n = int(input("Введите количество строк:"))
m = int(input("Введите количество троек ААА в строке:"))
for i in range(n):
    for j in range(m):
        if i%2 == 0:
            print("AAABBB", end='')
        else:
            print("BBBAAA", end='')
    print(" ")