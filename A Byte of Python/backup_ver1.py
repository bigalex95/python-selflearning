# Имя файла : backup_ver1.py
from colorama import init, Back, Fore
init()
print(Back.GREEN)
print(Fore.BLACK)


import os
import time

# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = ['"C:\\Users\Asaloy\Desktop\git\python-selflearning\A Byte of Python"']
# Заметьте, что для имён, содержащих пробелы, необходимо использовать
# двойные кавычки внутри строки.

# 2. Резервные копии должны храниться в основном каталоге резерва.
targit_dir = 'E:\\Backup'# Подставьте тот путь, который вы будете использовать.

# 3. Файлы помещаются в zip-архив.
# 4. Именем для zip-архива служит текущая дата и время.
target = targit_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

# 5. Используем команду "zip" для помещения файлов в zip-архив
zip_command="zip -qr {0} {1}".format(target,' '.join(source))

# Запускаем создание резервной копии
if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')


"""Output
$ py backup_ver1.py


Резервная копия успешно создана в E:\Backup\20200109204104.zip
"""