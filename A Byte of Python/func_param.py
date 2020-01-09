# Имя файла : func_param.py
from colorama import init, Back, Fore
init()
print(Back.GREEN)
print(Fore.BLACK)


def printMax(a, b):
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print(a,'равно', b)
    else:
        print(b,'максимально')

printMax(3,4)# прямая передача значений

x = 5
y = 7

printMax(x, y)# передача переменных в качестве аргументов


"""OUTPUT
$ py func_param.py


4 максимально
7 максимально
"""