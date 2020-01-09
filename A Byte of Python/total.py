# Имя файла : total.py
from colorama import init, Back, Fore
init()
print(Back.GREEN)
print(Fore.BLACK)


def total(initial = 5, *numbers, **keywords):
    count = initial
    for number in numbers:
        count += number
    for key in keywords:
        count += keywords[key]
    return count

print(total(10,1,2,3, vegetables=50, fruits=100))


"""OUTPUT
$ py total.py


166
"""