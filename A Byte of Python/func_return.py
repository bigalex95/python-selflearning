# Имя файла : func_return.py
from colorama import init, Back, Fore
init()
print(Back.GREEN)
print(Fore.BLACK)


def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'Числа равны.'
    else:
        return y
    
print(maximum(2, 3))


"""OUTPUT
$ py func_return.py


3
"""