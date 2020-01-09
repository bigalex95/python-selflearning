# Имя файла : expression.py
from colorama import init, Back, Fore
init()
print(Back.GREEN)
print(Fore.BLACK)


length = 5
breadth = 2

area = length * breadth
print('Площадь равна =', area)
print('Периметр равен =',2*(length+breadth))


"""OUTPUT
$ py expression.py


Площадь равна = 10
Периметр равен = 14
"""