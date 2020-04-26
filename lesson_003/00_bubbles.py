# -*- coding: utf-8 -*-

import simple_draw as sd


def draw_bubble(center, radius, step, color):
    """Function draw bubble - 3 circles with 1 center, different radius."""
    radius -= step
    for _ in range(3):
        radius += step
        sd.circle(center, radius, color)


sd.resolution = (1200, 600)

for _ in range(300):
    x = sd.random_number(-100, 1300)
    y = sd.random_number(-100, 700)
    radius = sd.random_number(10, 50)
    step = sd.random_number(3, 15)
    color = sd.random_color()
    draw_bubble(sd.get_point(x, y), radius, step, color)

sd.pause()


