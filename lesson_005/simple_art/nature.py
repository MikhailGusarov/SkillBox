# -*- coding: utf-8 -*-

import simple_draw as sd


def draw_rainbow(center_point, radius, width):
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
    if length < 10:
        vector_color = sd.COLOR_GREEN
    else:
        vector_color = (255, 255, 0)
    vector_0.draw(color=vector_color)
    next_point = vector_0.end_point
    delta_angle = 30 + sd.random_number(0, 40) / 100
    delta_length = .75 + sd.random_number(-10, 10) / 100
    draw_branches(start_point=next_point, angle=angle + delta_angle, length=length * delta_length)
    delta_angle = 30 + sd.random_number(0, 40) / 100
    delta_length = .75 + sd.random_number(-10, 10) / 100
    draw_branches(start_point=next_point, angle=angle - delta_angle, length=length * delta_length)


def generate_snowflakes_data(x_start=0, x_end=sd.resolution[0],
                             y_start=sd.resolution[1] - 50, y_end=sd.resolution[1] + 500):
    """Generate random data for snowflake. x_start and x_end diapason asix x"""
    x = sd.random_number(x_start, x_end)
    y = sd.random_number(y_start, y_end)
    length = sd.random_number(10, 40)
    factor_a = sd.random_number(50, 70) / 100
    factor_b = sd.random_number(25, 45) / 100
    factor_c = sd.random_number(50, 70)
    return {'x': x,
            'y': y,
            'length': length,
            'factor_a': factor_a,
            'factor_b': factor_b,
            'factor_c': factor_c}


def draw_snowflake(x, y, length, color=sd.COLOR_WHITE, factor_a=0.6, factor_b=0.35, factor_c=60):
    """"""
    point = sd.get_point(x, y)
    sd.snowflake(center=point,
                 length=length,
                 color=color,
                 factor_a=factor_a,
                 factor_b=factor_b,
                 factor_c=factor_c)


sd.pause()
