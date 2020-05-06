# -*- coding: utf-8 -*-

from random import randint
from termcolor import cprint

SECRET_NUMBER = ''
_count_steps = 0


def make_number():
    """Сгенерировать число и обнулить результат"""
    global SECRET_NUMBER, _count_steps
    SECRET_NUMBER = ''
    _count_steps = 0
    while len(SECRET_NUMBER) < 4:
        if len(SECRET_NUMBER) == 0:
            SECRET_NUMBER = str(randint(1, 9))
        else:
            random_numeral = str(randint(0, 9))
            if random_numeral not in SECRET_NUMBER:
                SECRET_NUMBER += random_numeral


def check_number(user_number):
    """проверка числа на соответсвие SECRET_NUMBER"""
    if check_input(user_number):
        bulls_and_cows = {'bulls': 0, 'cows': 0}
        global _count_steps
        _count_steps += 1
        for i, symbol in enumerate(user_number):
            if symbol == SECRET_NUMBER[i]:
                bulls_and_cows['bulls'] += 1
            elif symbol in SECRET_NUMBER:
                bulls_and_cows['cows'] += 1
        return bulls_and_cows


def get_count_steps():
    """Функция возвращает кол-во шагов"""
    return _count_steps


def check_input(user_number):
    """Проверка ввода пчисла пользователя"""
    if len(user_number) != 4:
        cprint('Число должно быть четырехзначным!', color='red')
        return False
    if user_number.isdigit() is False:
        cprint('Вы должны ввести число!', color='red')
        return False
    if user_number[0] == '0':
        cprint('Первая цифра не должна быть равна 0', color='red')
        return False
    for i, symbol in enumerate(user_number):
        if i+1 == len(user_number):
            continue
        if symbol in user_number[i+1:]:
            cprint('Нельзя вводить одинаковые значения', color='red')
            return False
    return True
