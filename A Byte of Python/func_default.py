# Имя файла : func_default.py
from colorama import init, Back, Fore
init()
print(Back.GREEN)
print(Fore.BLACK)


def say(message, times = 1):
    print(message * times)

say('Привет')
say('Мир',5)


"""OUTPUT
$ py func_default.py


Привет
МирМирМирМирМир
"""