# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.
from random import randint
import os.path

ENLIGHTENMENT_CARMA_LEVEL = 777


class IamGodError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class SuicideError(Exception):
    pass


def one_day():
    errors = [IamGodError('Я - Бог'), DrunkError('Напился'), CarCrashError('Разбился на машине'),
              GluttonyError('Объелся'), DepressionError('Депрессия'), SuicideError('Самоубийство')]

    rand_error = randint(0, 12)

    if rand_error >= len(errors):
        return randint(1, 7)
    else:
        raise errors[rand_error]


def add_in_error_log(day_error, exception):
    log_file = 'error.log'
    if not os.path.exists(log_file):
        with open(log_file, encoding='utf8', mode='w') as file:
            file.write('day #{}: {}: {}'.format(day_error, exception.__class__.__name__, exception))
    else:
        with open(log_file, encoding='utf8', mode='a') as file:
            file.write('day #{}: {}: {}\n'.format(day_error, exception.__class__.__name__, exception))


karma = 0
day = 0
while ENLIGHTENMENT_CARMA_LEVEL > karma:
    day += 1
    try:
        karma += one_day()
    except IamGodError as exc:
        add_in_error_log(day, exc)
    except DrunkError as exc:
        add_in_error_log(day, exc)
    except CarCrashError as exc:
        add_in_error_log(day, exc)
    except GluttonyError as exc:
        add_in_error_log(day, exc)
    except DepressionError as exc:
        add_in_error_log(day, exc)
    except SuicideError as exc:
        add_in_error_log(day, exc)



