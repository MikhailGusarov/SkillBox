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


def draw_tree(start_point, angle, length):
    """Draw tree with angle axic x = angle"""
    if length < 5:
        return
    vector_0 = sd.get_vector(start_point=start_point, angle=angle, length=length)
    vector_0.draw()
    next_point = vector_0.end_point
    delta_angle = 30 + sd.random_number(0, 40) / 100
    delta_length = .75 + sd.random_number(-10, 10) / 100
    draw_branches(start_point=next_point, angle=angle + delta_angle, length=length * delta_length)
    delta_angle = 30 + sd.random_number(0, 40) / 100
    delta_length = .75 + sd.random_number(-10, 10) / 100
    draw_branches(start_point=next_point, angle=angle - delta_angle, length=length * delta_length)


sd.pause()
