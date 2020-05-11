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
        self.y -= 15

    def draw(self, color=sd.COLOR_WHITE):
        """ нарисовать снежинку"""
        sd.snowflake(center=sd.get_point(self.x, self.y),
                     length=self.length,
                     color=color,
                     factor_a=self.factor_a,
                     factor_b=self.factor_b,
                     factor_c=self.factor_c)

    def can_fall(self):
        """ снежинка может падать ниже?"""
        return self.y > 0


flake = Snowflake()

while True:
    flake.clear_previous_picture()
    flake.move()
    flake.draw()
    if not flake.can_fall():
        break
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

sd.pause()
