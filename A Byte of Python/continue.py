# Имя файла : continue.py
from colorama import init, Back, Fore
init()
print(Back.GREEN)
print(Fore.BLACK)


while True:
    s = input('Введите что-нибудь :')
    if s == 'выход':
        break
    elif len(s) < 3:
        print('Слишком мало')
        continue
    print('Введённая строка достаточной длины')
    # Разные другие действия здесь...
print('Завершение')


"""OUTPUT
$ py continue.py


Введите что-нибудь :a
Слишком мало
Введите что-нибудь :ab
Слишком мало
Введите что-нибудь :abc
Введённая строка достаточной длины
Введите что-нибудь :выход
Завершение
"""