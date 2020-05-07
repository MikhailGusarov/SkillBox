# -*- coding: utf-8 -*-

import simple_draw as sd
from snowfall import create_snowflakes, draw_snowflakes, delete_snowflakes, move_down, get_reached_bottom

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall
N = 50

create_snowflakes(N)
while True:
    draw_snowflakes(color=sd.background_color)
    move_down()
    draw_snowflakes()
    reached_bottom = get_reached_bottom()
    if reached_bottom:
        count_reached_bottom = len(reached_bottom)
        delete_snowflakes(reached_bottom)
        create_snowflakes(count_reached_bottom)
    sd.sleep(0.3)
    if sd.user_want_exit():
        break

sd.pause()
