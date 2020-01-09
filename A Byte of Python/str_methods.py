# Имя файла : str_methods.py
from colorama import init, Back, Fore
init()
print(Back.GREEN)
print(Fore.BLACK)


name = 'Swaroop'# Это объект строки

if name.startswith("Swa"):
    print('Да, строка начинается на "Swa"')

if "a" in name:
    print('Да, она содержит строку "a"')

if name.find("war") != -1:
    print('Да, она содержит строку "war"')

delimiter = "_*_"
mylist=['Бразилия', 'Россия', 'Индия', 'Китай']
print(delimiter.join(mylist))


"""Output
$ py str_methods.py


Да, строка начинается на "Swa"
Да, она содержит строку"a"
Да, она содержит строку"war"
Бразилия_*_Россия_*_Индия_*_Китай
"""