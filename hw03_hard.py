import re
import testfunc


# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


class Fraction:
    def __init__(self, n, x, y):
        if not n:
            self.err = False
            if n is str:
                self.x, self.y = self.str2fraction(n)
            if y == 0:
                self.err = True
                raise FractionError("Fraction can't have y==0")
            self.x, self.y = x + n * y, y
            i = gcd(self.x, self.y)
            self.x = self.x // i
            self.y = self.y // i
        else:
            self.err = True

    def __add__(self, other):
        if self.err or other.err: raise FractionError("Один из операндов ошибочный")
        if other is Fraction:
            x = self.x * other.y + self.y * other.x
            y = self.y * other.y
        else:
            try:
                x = int(other) * self.y + self.x
                y = self.y
            except TypeError as err:
                raise FractionError(err)
        return Fraction(0, x, y)


def str2fraction(self, str):


class FractionError(Exception):
    pass

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"



# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

f1 = Fraction()

print("-" * 8, " Задание 1 ", "-" * 8)

testfunc.test("Проверка str2fraction", f1.str2fraction("3 2/5"), (17, 5))
testfunc.test("Проверка str2fraction", f1.str2fraction("2/5"), (2, 5))
testfunc.test("Проверка str2fraction", f1.str2fraction("3"), (3, 1))