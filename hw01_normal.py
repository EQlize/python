__author__ = 'Анненсков Андрей Игоревич'

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

num = 58375
num_str = str(num)
num_max = int(num_str[0])
for i in range(len(num_str) - 1):
    num_tmp = int(num_str[i + 1])
    if num_tmp > num_max:
        num_max = num_tmp
print(num_max)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

print('Введите число a:')
a = input()
print('Введите число b:')
b = input()
a, b = b, a
print(a)
print(b)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

import math

print("Школа и дискриминанты")
a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))
if a == 0:
    if b == 0:
        print("Нули в a и b, Вы серьезно, Перестукин?.")
    else:
        x = -c / b;
        print("x = ", x)
else:
    d = pow(b, 2) - 4 * a * c
    if d == 0:
        x = -b / (2 * a)
        print("x = ", x)
    elif d > 0:
        d = math.sqrt(d)
        x1 = (-b - d) / (2 * a)
        x2 = (-b + d) / (2 * a)
        print("x1 = ", x1, ", x2 = ", x2)
    else:
        print("Корней на множестве действительных чисел нет.")