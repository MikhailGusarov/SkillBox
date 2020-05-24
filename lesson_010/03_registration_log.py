# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError +
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.
import os.path


class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


def add_in_log(log_file_path, line):
    if not os.path.exists(log_file_path):
        with open(log_file_path, encoding='utf8', mode='w') as log_file:
            log_file.write(line)
    else:
        with open(log_file_path, encoding='utf8', mode='a') as log_file:
            log_file.write(line)


file_reg = 'registrations.txt'
file_reg_good = 'registrations_good.log'
file_reg_bad = 'registrations_bad.log'

with open(file_reg, encoding='utf8') as file:
    for number_line, line in enumerate(file):
        try:
            name, email, age = str(line[:-1]).split(' ')
            if not name.isalpha():
                raise NotNameError('Имя содержит не только буквы')
            if '@' not in email:
                raise NotEmailError('e-mail не содержит "@"')
            if '.' not in email:
                raise NotEmailError('e-mail не ссодержит "."')
            add_in_log(log_file_path=file_reg_good, line=line)

        except ValueError as exc:
            exc_line = 'Line {}: "{}". Ошибка: не присутствуют все 3 поля. Trace: {} {} \n'.format(
                number_line + 1, line[:-1], type(exc), exc)
            add_in_log(log_file_path=file_reg_bad, line=exc_line)
        except (NotNameError, NotEmailError) as exc:
            exc_line = 'Line {}: "{}". Ошибка: {} {} \n'.format(
                number_line + 1, line[:-1], type(exc), exc)
            add_in_log(log_file_path=file_reg_bad, line=exc_line)
