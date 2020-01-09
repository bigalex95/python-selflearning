# Имя файла : mymodule_demo.py
from colorama import init, Back, Fore
init()
print(Back.GREEN)
print(Fore.BLACK)


import mymodule

mymodule.sayhi()
print('Версия', mymodule.__version__)


"""Output
$ py mymodule_demo.py




Привет! Это говорит мой модуль.
Версия 0.1
"""