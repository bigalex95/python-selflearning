# Имя файла : mymodule.py
from colorama import init, Back, Fore
init()
print(Back.GREEN)
print(Fore.BLACK)


def sayhi():
    print('Привет! Это говорит мой модуль.')

__version__ = "0.1"


"""Output

"""