# Имя файла : mymodule_demo2.py
from colorama import init, Back, Fore
init()
print(Back.GREEN)
print(Fore.BLACK)


from mymodule import sayhi, __version__

sayhi()
print('Версия', __version__)


"""Output
$ py mymodule_demo2.py




Привет! Это говорит мой модуль.
Версия 0.1
"""