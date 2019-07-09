Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import re

def make_dir (name):
    try:
        os.makedirs(name)
    except FileExistsError:
        print('{} - уже существует'.format(name))
		
def remove_dir (name):
    try:
        os.removedirs(name)
    except FileNotFoundError:
        print('{} - папки не существует'.format(name))

		
def start ():
    answer =''
    quantity_dirs = range(1, 10)

    while answer != '3':

        answer = input('Выберите пункт меню:\n'
                       '1. Создать папки dir_1 - dir_9\n'
                       '2. Удалить папки dir_1 - dir_9\n'
                       '3. Выход\n')
        if answer =='3':
            break
        if answer == '1':
            for i in quantity_dirs:
                i = str(i)
                make_dir('dir_' + i)
        elif answer == '2':
            for i in quantity_dirs:
                i = str(i)
                remove_dir('dir_' + i)

start()
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def list_dir ():
    buffer = os.listdir()
    print('****************************************')
    print('Список файлов:')
    for index, element in enumerate(buffer, start=1):
        if os.path.isdir(element):
            print('{}. {}'.format(index, element))

list_dir()
	
# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import sys

 
destdir = os.path.abspath('destdir')
if not os.path.exists(destdir):
    os.makedirs(destdir)
 
# с использованием системного shell'а  
os.system('copy %s %s' % (__file__,destdir))
# другой вариант - с получением полного имени скрипта через sys.argv[0]
os.system('copy %s %s' % (sys.argv[0],destdir))
 
# без shell'а
dirname,filename = os.path.split(__file__)
content = open(__file__).read()
open(os.path.join(destdir,filename),'w').write(content)