# Имя файла : func_global.py
from colorama import init, Back, Fore
init()
print(Back.GREEN)
print(Fore.BLACK)


x = 50

def func():
    global x

    print('x равно', x)
    x = 2
    print('Заменяем глобальное значение x на', x)

func()
print('Значение x составляет', x)


"""OUTPUT
$ py func_global.py


x равно 50
Заменяем глобальное значение x на 2
Значение x составляет 2
"""