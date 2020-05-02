# -*- coding: utf-8 -*-

import simple_draw as sd


def rainbow(center_point, radius, width):
    """Draw rainbow"""
    if radius < width:
        print('Укажите радиус больше', width)
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
    step = - width
    for color in rainbow_colors:
        step += width
        sd.circle(center_position=center_point, radius=int(radius + step), color=color, width=width)
    left_bottom = sd.get_point(x=center_point.x - radius - step, y=center_point.y - radius - step)
    right_top = sd.get_point(x=center_point.x + radius + step + 1, y=center_point.y)
    sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=sd.background_color)


sd.pause()
