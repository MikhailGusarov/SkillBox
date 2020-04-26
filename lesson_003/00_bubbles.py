# -*- coding: utf-8 -*-

import simple_draw as sd


def draw_bubble(center, radius, step):
    """Function draw bubble - 3 circles with 1 center, different radius."""
    radius -= step
    for _ in range(3):
        radius += step
        sd.circle(center, radius)


sd.resolution = (1200, 600)

draw_bubble(sd.get_point(100, 100), 50, 5)

# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код

# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код

sd.pause()


