# Имя файла : func_default.py
from colorama import init, Back, Fore
init()
print(Back.GREEN)
print(Fore.BLACK)


def func(a, b = 5, c = 10):
    print('a равно', a,', b равно', b,', а c равно', c)

func(3, 7)
func(25, c = 24)
func(c = 50, a = 100)


"""OUTPUT
$ py func_key.py


a равно 3 , b равно 7 , а c равно 10
a равно 25 , b равно 5 , а c равно 24
a равно 100 , b равно 5 , а c равно 50
"""