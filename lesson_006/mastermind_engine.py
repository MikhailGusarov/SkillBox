from random import randint

SECRET_NUMBER = ''
_count_steps = 0


def make_number():
    global SECRET_NUMBER,  _count_steps
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
    else:
        print('Данные введены некорректно')


def get_count_steps():
    return _count_steps


def check_input(user_number):
    # TODO написать функцию проверки
    return True
