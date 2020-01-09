# Имя файла : while.py
from colorama import init, Back, Fore
init()
print(Back.GREEN)
print(Fore.BLACK)


number = 23
running = True

while running:
    guess = int(input('Введите целое число :'))

    if guess == number:
        print('Поздравляю, вы угадали.')
        running=False# это останавливает цикл while
    elif guess < number:
        print('Нет, загаданное число немного больше этого')
    else:
        print('Нет, загаданное число немного меньше этого.')
else:
    print('Цикл while закончен.')
    # Здесь можете выполнить всё что вам ещё нужно

print('Завершение.')


"""OUTPUT
$ py while.py


Введите целое число :15
Нет, загаданное число немного больше этого
Введите целое число :39
Нет, загаданное число немного меньше этого.
Введите целое число :23
Поздравляю, вы угадали.
Цикл while закончен.
Завершение.
"""