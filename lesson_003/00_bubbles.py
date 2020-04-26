# -*- coding: utf-8 -*-

import simple_draw as sd


def draw_bubble(center, radius, step):
    """Function draw bubble - 3 circles with 1 center, different radius."""
    radius -= step
    for _ in range(3):
        radius += step
        sd.circle(center, radius)


sd.resolution = (1200, 600)

# Нарисовать три ряда по 10 пузырьков
for x in range(100, 1001, 100):
    for y in range(200, 401, 100):
        draw_bubble(sd.get_point(x, y), 50, 5)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код

sd.pause()


