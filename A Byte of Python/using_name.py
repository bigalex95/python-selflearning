# Имя файла : using_name.py
from colorama import init, Back, Fore
init()
print(Back.GREEN)
print(Fore.BLACK)


if __name__ == "__main__":
    print('Эта программа запущена сама по себе.')
else:
    print('Меня импортировали в другой модуль.')


"""Output
$ py using_name.py


Эта программа запущена сама по себе.

$ py
Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import using_name


Меня импортировали в другой модуль.
>>> 
"""