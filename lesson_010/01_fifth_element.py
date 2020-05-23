# -*- coding: utf-8 -*-

# Умножить константу BRUCE_WILLIS на пятый элемент строки, введенный пользователем

BRUCE_WILLIS = 42


def generate_multi_pass_number():
    input_data = input('Если хочешь что-нибудь сделать, сделай это сам: ')
    leeloo = int(input_data[4])
    result = BRUCE_WILLIS * leeloo
    print(f"- Leeloo Dallas! Multi-pass № {result}!")


try:
    generate_multi_pass_number()
except ValueError as ex:
    print('пятый элемеент не является числом! Ошибка:', ex)
except IndexError as ex:
    print('вы ввели меньше 5 символов! Ошибка:', ex)
except Exception as ex:
    print('Неизвестная ошибка:', ex)

# Ообернуть код и обработать исключительные ситуации для произвольных входных параметров
# - ValueError - невозможно преобразовать к числу
# - IndexError - выход за границы списка
# - остальные исключения
# для каждого типа исключений написать на консоль соотв. сообщение

