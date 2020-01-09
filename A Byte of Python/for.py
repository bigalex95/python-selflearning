# Имя файла : for.py
from colorama import init, Back, Fore
init()
print(Back.GREEN)
print(Fore.BLACK)


for i in range(1, 5):
    print(i)
else:
    print('Цикл for закончен')

# get element every 2 step
for i in range(1, 10, 2):
    print(i)
else:
    print('Цикл for закончен')


"""OUTPUT
$ py for.py


1
2
3
4
Цикл for закончен
1
3
5
7
9
Цикл for закончен
"""