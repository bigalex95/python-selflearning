# Имя файла : func_param.py
from colorama import init, Back, Fore
init()
print(Back.GREEN)
print(Fore.BLACK)


x = 50

def func(x):
    print('x равен', x)
    x = 2
    print('Замена локального x на', x)

func(x)
print('x по прежнему', x)


"""OUTPUT
$ py func_local.py


x равен 50
Замена локального x на 2
x по прежнему 50
"""