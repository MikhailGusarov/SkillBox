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

ENLIGHTENMENT_CARMA_LEVEL = 777


class IamGodError(BaseException):
    pass


class DrunkError(BaseException):
    pass


class CarCrashError(BaseException):
    pass


class GluttonyError(BaseException):
    pass


class DepressionError(BaseException):
    pass


class SuicideError(BaseException):
    pass


def one_day():
    errors = [IamGodError('Я - Бог'), DrunkError('Напился'), CarCrashError('Разбился на машине'),
              GluttonyError('Объелся'), DepressionError('Умер от депрессии'), SuicideError('Самоубийство')]

    rand_error = randint(0, 12)

    if rand_error >= len(errors):
        return randint(1, 7)
    else:
        raise errors[rand_error]


karma = 0

while ENLIGHTENMENT_CARMA_LEVEL > karma:
    try:
        karma += one_day()
    except IamGodError as exc:
        print(exc)
    except DrunkError as exc:
        print(exc)
    except CarCrashError as exc:
        print(exc)
    except GluttonyError as exc:
        print(exc)
    except DepressionError as exc:
        print(exc)
    except SuicideError as exc:
        print(exc)
    else:
        print('Текущее значение кармы:', karma)


