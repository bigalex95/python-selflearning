# Имя файла : break.py
from colorama import init, Back, Fore
init()
print(Back.GREEN)
print(Fore.BLACK)


while True:
    s = input('Введите что-нибудь :')
    if s == 'выход':
        break
    print('Длина строки:',len(s))
print('Завершение')


"""OUTPUT
$ py break.py


Введите что-нибудь :25
Длина строки: 2
Введите что-нибудь :123456
Длина строки: 6
Введите что-нибудь :выход
Завершение
"""