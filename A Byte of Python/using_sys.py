# Имя файла : using_sys.py
from colorama import init, Back, Fore
init()
print(Back.GREEN)
print(Fore.BLACK)


import sys

print('Аргументы командной строки:')
for i in sys.argv:
    print(i)

print('\n\nПеременная PYTHONPATH содержит', sys.path,'\n')


"""OUTPUT
$ py using_sys.py


Аргументы командной строки:
using_sys.py


Переменная PYTHONPATH содержит ['C:\\Users\\Asaloy\\Desktop\\git\\python-selflearning\\A Byte of Python', 'C:\\Users\\Asaloy\\AppData\\Local\\Programs\\Python\\Python38\\python38.zip', 'C:\\Users\\Asaloy\\AppData\\Local\\Programs\\Python\\Python38\\DLLs', 'C:\\Users\\Asaloy\\AppData\\Local\\Programs\\Python\\Python38\\lib', 'C:\\Users\\Asaloy\\AppData\\Local\\Programs\\Python\\Python38', 'C:\\Users\\Asaloy\\AppData\\Roaming\\Python\\Python38\\site-packages', 'C:\\Users\\Asaloy\\AppData\\Local\\Programs\\Python\\Python38\\lib\\site-packages'] 
"""