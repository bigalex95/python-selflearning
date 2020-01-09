# Имя файла : function1.py
from colorama import init, Back, Fore
init()
print(Back.GREEN)
print(Fore.BLACK)


def sayHello():
    print('Привет, Мир!')# блок, принадлежащий функции
# Конец функции

sayHello()# вызов функции
sayHello()# ещё один вызов функции


"""OUTPUT
$ py function1.py


Привет, Мир!
Привет, Мир!
"""