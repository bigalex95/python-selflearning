# Имя файла : keyword_only.py
from colorama import init, Back, Fore
init()
print(Back.GREEN)
print(Fore.BLACK)


def total(initial = 5, *numbers, extra_number):
    count = initial
    for number in numbers:
        count += number
    count += extra_number
    print(count)

total(10, 1, 2, 3, extra_number = 50)
total(10, 1, 2, 3)
# Вызовет ошибку, поскольку мы не указали значение
# аргумента по умолчанию для 'extra_number'.


"""OUTPUT
$ py keyword_only.py


66
Traceback (most recent call last):
  File "keyword_only.py", line 16, in <module>
    total(10, 1, 2, 3)
TypeError: total() missing 1 required keyword-only argument: 'extra_number'
"""