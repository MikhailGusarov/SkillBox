# -*- coding: utf-8 -*-

import simple_draw as sd

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:
    def __init__(self, x=sd.randint(0, sd.resolution[0]), y=sd.resolution[1],
                 length=100, factor_a=0.6, factor_b=0.35, factor_c=60):
        self.x = x
        self.y = y
        self.length = length
        self.factor_a = factor_a
        self.factor_b = factor_b
        self.factor_c = factor_c

    def clear_previous_picture(self):
        """ Очистить предыдущее значение снежинки с экрана"""
        self.draw(color=sd.background_color)

    def move(self):
        """ сдивинуть снежинку"""
        self.y -= 10

    def draw(self, color=sd.COLOR_WHITE):
        """ нарисовать снежинку"""
        sd.snowflake(center=sd.get_point(self.x, self.y),
                     length=self.length,
                     color=color,
                     factor_a=self.factor_a,
                     factor_b=self.factor_b,
                     factor_c=self.factor_c)

    def can_fall(self):
        """ снежинка может падать ниже? """
        return self.y > 0

    def __del__(self):
        self.clear_previous_picture()


# flake = Snowflake()

# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break


def get_flakes(count_snowflakes, y1=0, y2=sd.resolution[1]):
    """ Генератор снеджинок, где count_snowflakes = кол-во снежинок"""
    snowflakes = []
    for _ in range(count_snowflakes):
        x = sd.random_number(0, sd.resolution[0])
        y = sd.random_number(y1, y2)
        length = sd.random_number(10, 40)
        factor_a = sd.random_number(50, 70) / 100
        factor_b = sd.random_number(25, 45) / 100
        factor_c = sd.random_number(50, 70)
        snowflake = Snowflake(x=x, y=y, length=length, factor_a=factor_a, factor_b=factor_b, factor_c=factor_c)
        snowflakes.append(snowflake)
    return snowflakes


flakes = get_flakes(count_snowflakes=30)  # создать список снежинок
while True:
    flakes_on_del = []
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
        if not flake.can_fall():
            flakes_on_del.append(flake)
    if flakes_on_del:
        flakes += get_flakes(count_snowflakes=len(flakes_on_del), y1=sd.resolution[1])  # добавить еще сверху
    for flake in flakes_on_del:
        flakes.remove(flake)
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
