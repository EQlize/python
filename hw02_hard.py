# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y

import re

def ex2(equation, x):
    pattern="[0-9]+\.?[0-9]*"
    numbers = re.findall(pattern,equation)
    if len(numbers) == 2:
        k=float(numbers[0])
        b=float(numbers[1])
        res = k*x+b
        return res


# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
date = '01.11.1985'

# Примеры некорректных дат
date = '01.22.1001'
date = '1.12.1001'
date = '-2.10.3001'

def check_date(textdate):
    try:
        numbers = textdate.split(".")
        # print(numbers)
        if len(numbers) != 3: return False
        if (len(numbers[0]) != 2) or (len(numbers[1]) != 2) or (len(numbers[2]) != 4): return False
        date = int(numbers[0])
        month = int(numbers[1])
        year = int(numbers[2])
        if 0<year<10000:
            if 0<month<13:
                if 0<date<31: return True
                if (date == 31) and (month in (1,3,5,7,8,10,12)): return True
        return False
    except:
        return False
		
# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3

def babylon_tower(n):
    def walk(our_room,room, floor,room_on_floor):
        room_on_floor += 1
        new_room = room+ room_on_floor**2
        if new_room>=our_room:
            room_in_block = our_room-room
            return (floor+(room_in_block-1)//room_on_floor+1,(room_in_block-1)%room_on_floor+1)
        else:
            floor += room_on_floor
            return walk(our_room,new_room, floor,room_on_floor)
    if n == 1:
        return (1,1)
    if 1<n<=2000000:
        return walk(n, 1, 1, 1)
    else:
        return "Неверный порядковый номер"



# testing

def test(text,got, expected):
    prefix = "OK" if got == expected else "X"
    print("{0} - Тест: {1} | Получено: {2} | Ожидалось: {3}".format(prefix, text, repr(got), repr(expected)))


print("Задание 1: вычисление y")
test("1", ex2("343",2),None)
test("2", ex2('y = -12x + 11111140.2121',2.5),11111170.2121)
test("3", ex2("y=3x+5.1",4),17.1)

print("\nЗадание 2: проверка даты")
tests=(("31.12.0002",True),
       ("29.02.0900",True),
       ("01.11.1985",True),
       ('01.22.1001',False),
       ('1.12.1001',False),
       ('-2.10.3001',False))
for text,expected in tests:
    test(text,check_date(text),expected)

print("\nЗадание 3: Перевернутая башня")
test("14",babylon_tower(14),(6,3))
test("15",babylon_tower(15),(7,1))
test("25",babylon_tower(25),(9,3))
test(" 9",babylon_tower(9),(5,1))
test(" 2",babylon_tower(2),(2,1))
test(" 3",babylon_tower(3),(2,2))
test(" 1",babylon_tower(1),(1,1))
test(" 0",babylon_tower(0),"Неверный порядковый номер")
test("1999999",babylon_tower(1999999),(1,1))