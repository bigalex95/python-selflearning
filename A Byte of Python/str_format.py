# Имя файла : str_format.py
from colorama import init, Back, Fore
init()
print(Back.GREEN)
print(Fore.BLACK)


age = 26
name = "Swaroop"

print("Age of {0} -- {1} years old".format(name,age))
print("Why {0} like Python".format(name))
#получить такой же результат, как и ранее
print('Возраст {} -- {} лет.'.format(name, age))
print('Почему {} забавляется с этим Python?'.format(name))

# десятичное число (.) с точностью в 3 знака для плавающих:
print('{0:.3}'.format(1/3))

# заполнить подчёркиваниями (_) с центровкой текста (^) по ширине  11:
print('{0:_^11}'.format('hello'))

# по ключевым словам:
print('{name} написал {book}'.format(name='Swaroop', book='A Byte of Python'))


"""OUTPUT
$ py str_format.py


Age of Swaroop -- 26 years old
Why Swaroop like Python
Возраст Swaroop -- 26 лет.
Почему Swaroop забавляется с этим Python?
0.333
___hello___
Swaroop написал A Byte of Python
"""