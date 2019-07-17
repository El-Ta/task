import random
print("Зад1. Вывести максимальную цифру числа.")
a = random.randint(11, 10000)
print("a=", a)
max = 0
b=0
while a > 0:
    b = a%10
    a=a//10
    if b > max:
        max = b
print(max)
print("Зад2. Поменять значения переменных местами.")
a = int(input("Введите с:"))
b = int(input("Введите d:"))
a, b=b, a
print("После перестановки: c =", a, "d =", b)
print("Зад3. Решить квадратное уравнение.")
import math
print("Имеем уравнение вида ax^2 + bx + c = 0")
a = int(input("Введите коэффициент a:"))
b = int(input("Введите коэффициент b:"))
c = int(input("Введите коэффициент c:"))
D = b*b-4*a*c
if D < 0:
    print("Решений нет")
else:
    x = (-b + math.sqrt(D))/(2*a)
    y = (-b - math.sqrt(D))/(2*a)
    print("Корни уравнения: x =", x, ", y =", y)