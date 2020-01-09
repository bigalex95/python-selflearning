# Имя файла : func_nonlocal.py
from colorama import init, Back, Fore
init()
print(Back.GREEN)
print(Fore.BLACK)


def func_outer():
    x = 2
    print('x равно', x)

    def func_inner():
        nonlocal x
        x = 5

    func_inner()
    print('Локальное x сменилось на', x)

func_outer()


"""OUTPUT
$ py func_nonlocal.py


x равно 2
Локальное x сменилось на 5
"""