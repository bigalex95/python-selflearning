# Имя файла : template.py
from colorama import init, Back, Fore
init()
print(Back.GREEN)
print(Fore.BLACK)


# 'ab' - сокращение от 'a'ddress'b'ook

ab = {
    'Swaroop':'swaroop@swaroopch.com',
    'Larry':'larry@wall.org',
    'Matsumoto':'matz@ruby-lang.org',
    'Spammer':'spammer@hotmail.com',
}

print("Адрес Swaroop'а:", ab['Swaroop'])

# Удаление пары ключ-значение
del ab['Spammer']

print('\nВ адресной книге {0} контактов\n'.format(len(ab)))

for name, address in ab.items():
    print('Контакт {0} с адресом {1}'.format(name, address))

# Добавление пары ключ-значение
ab['Guido'] = "guido@python.org"

if "Guido" in ab:
    print("\nАдрес Guido:", ab['Guido'])


"""Output
$ py using_dict.py


Адрес Swaroop'а: swaroop@swaroopch.com

В адресной книге 3 контактов

Контакт Swaroop с адресом swaroop@swaroopch.com
Контакт Larry с адресом larry@wall.org
Контакт Matsumoto с адресом matz@ruby-lang.org

Адрес Guido: guido@python.org
"""