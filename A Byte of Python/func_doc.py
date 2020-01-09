# Имя файла : func_doc.py
from colorama import init, Back, Fore
init()
print(Back.GREEN)
print(Fore.BLACK)


def printMax(x, y):
    '''Выводит максимальное из двух чисел.
        Оба значения должны быть целыми числами.'''
    x = int(x)
    y = int(y)# конвертируем в целые, если возможно

    if x > y:
        print(x,'наибольшее')
    else:
        print(y,'наибольшее')

printMax(3, 5)
print(printMax.__doc__)


"""OUTPUT
$ py func_doc.py


5 наибольшее
Выводит максимальное из двух чисел.
        Оба значения должны быть целыми числами.
"""