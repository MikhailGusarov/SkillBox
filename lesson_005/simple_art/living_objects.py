# -*- coding: utf-8 -*-

import simple_draw as sd


def draw_cat_face(x, y, size=50, color=sd.COLOR_YELLOW):
    point = sd.get_point(x, y)
    sd.circle(center_position=point, radius=size, color=color)
    sd.line(sd.get_point(x-0.8*size, y+0.6*size), sd.get_point(x-0.4*size, y+1.4*size))
    sd.line(sd.get_point(x - 0.4*size, y + 1.4*size), sd.get_point(x, y + size))
    sd.line(sd.get_point(x+0.1*size, y+size), sd.get_point(x+0.5*size, y+1.4*size))
    sd.line(sd.get_point(x+0.5*size, y+1.4*size), sd.get_point(x+0.8*size, y+0.6*size))
    sd.ellipse(sd.get_point(x-0.6*size, y-0.6*size), sd.get_point(x+0.6*size, y), width=1)
    sd.rectangle(sd.get_point(x-0.6*size, y-0.3*size),
                 sd.get_point(x+0.6*size, y+0.3*size),
                 width=0,
                 color=sd.background_color)
    sd.line(sd.get_point(x, y), sd.get_point(x, y-0.2*size))
    sd.circle(sd.get_point(x-0.3*size, y+0.3*size), radius=int(0.14*size))
    sd.circle(sd.get_point(x + 0.3*size, y + 0.3*size), radius=int(0.14*size))
    sd.line(sd.get_point(x-0.16*size, y+0.3*size), sd.get_point(x+0.16*size, y+0.3*size))
    sd.line(sd.get_point(x-0.44*size, y+0.3*size), sd.get_point(x-0.8*size, y+0.6*size))
    sd.line(sd.get_point(x+0.44*size, y+0.3*size), sd.get_point(x+0.8*size, y+0.6*size))


def draw_cow(start_point, length, width):
    right_top = sd.get_point(start_point.x + width, start_point.y + length)
    sd.rectangle(left_bottom=start_point, right_top=right_top, color=sd.COLOR_WHITE)

    # рисуем пятно
    center = sd.get_point(start_point.x + width / 2, start_point.y + length * 0.6)
    sd.circle(center_position=center, radius=int(0.4 * length), color=sd.COLOR_DARK_ORANGE, width=0)

    left_bottom = sd.get_point(start_point.x + 0.3 * width, start_point.y + 0.55 * length)
    right_top = sd.get_point(start_point.x + 0.8 * width, start_point.y + length)
    sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=sd.COLOR_DARK_ORANGE)

    center = sd.get_point(start_point.x + 0.6 * width, start_point.y + 0.6 * length)
    sd.circle(center_position=center, radius=int(0.4 * length), color=sd.COLOR_DARK_ORANGE, width=0)

    left_bottom = sd.get_point(start_point.x + 0.5 * width, start_point.y + 0.2 * length)
    right_top = sd.get_point(start_point.x + 0.6 * width, start_point.y + length)
    sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=sd.COLOR_DARK_ORANGE)

    # рисуем копыта
    left_bottom = sd.get_point(start_point.x, start_point.y - 0.5 * length)
    right_top = sd.get_point(start_point.x + 0.05 * width, start_point.y)
    sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=sd.COLOR_WHITE)

    left_bottom = sd.get_point(start_point.x, start_point.y - 0.5 * length)
    right_top = sd.get_point(start_point.x + 0.05 * width, start_point.y - 0.35 * length)
    sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=sd.COLOR_DARK_ORANGE)

    left_bottom = sd.get_point(start_point.x + 0.95 * width, start_point.y - 0.5 * length)
    right_top = sd.get_point(start_point.x + width, start_point.y)
    sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=sd.COLOR_WHITE)
    left_bottom = sd.get_point(start_point.x + 0.95 * width, start_point.y - 0.5 * length)
    right_top = sd.get_point(start_point.x + width, start_point.y - 0.35 * length)
    sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=sd.COLOR_DARK_ORANGE)

    # рисуем голову
    left_bottom = sd.get_point(start_point.x + 0.925 * width, start_point.y + 0.1 * length)
    right_top = sd.get_point(start_point.x + 1.325 * width, start_point.y + 1.1 * length)
    sd.ellipse(left_bottom, right_top, color=sd.COLOR_WHITE)

    left_bottom = sd.get_point(start_point.x + 0.95 * width, start_point.y + 0.05 * length)
    right_top = sd.get_point(start_point.x + 1.35 * width, start_point.y + 0.55 * length)
    sd.ellipse(left_bottom, right_top, color=sd.COLOR_DARK_ORANGE)

    sd.circle(sd.get_point(start_point.x + 1.25 * width, start_point.y + 0.25 * length),
              radius=int(0.05 * length), color=sd.COLOR_BLACK, width=0)
    sd.circle(sd.get_point(start_point.x + 1.05 * width, start_point.y + 0.25 * length),
              radius=int(0.05 * length), color=sd.COLOR_BLACK, width=0)

    #  рисуем глаза
    sd.circle(sd.get_point(start_point.x + 1.225 * width, start_point.y + 0.75 * length),
              radius=int(0.05 * length), color=sd.COLOR_BLACK, width=0)
    sd.circle(sd.get_point(start_point.x + 1.075 * width, start_point.y + 0.75 * length),
              radius=int(0.05 * length), color=sd.COLOR_BLACK, width=0)
    # рисуем рога
    sd.line(sd.get_point(start_point.x + 1.075 * width, start_point.y + 1.05 * length),
            sd.get_point(start_point.x + 1.025 * width, start_point.y + 1.20 * length),
            color=sd.COLOR_DARK_ORANGE, width=int(0.05 * length))
    sd.line(sd.get_point(start_point.x + 1.175 * width, start_point.y + 1.05 * length),
            sd.get_point(start_point.x + 1.225 * width, start_point.y + 1.2 * length),
            color=sd.COLOR_DARK_ORANGE, width=int(0.05 * length))

    # рисуем уши
    points = [sd.get_point(start_point.x + 0.925 * width, start_point.y + 1.05 * length),
              sd.get_point(start_point.x + 1.025 * width, start_point.y + 1.05 * length),
              sd.get_point(start_point.x + 0.975 * width, start_point.y + 0.9 * length)]
    sd.polygon(points, sd.COLOR_DARK_ORANGE, 0)

    points = [sd.get_point(start_point.x + 1.225 * width, start_point.y + 1.05 * length),
              sd.get_point(start_point.x + 1.325 * width, start_point.y + 1.05 * length),
              sd.get_point(start_point.x + 1.275 * width, start_point.y + 0.9 * length)]
    sd.polygon(points, sd.COLOR_DARK_ORANGE, 0)

    # рисуем хвост
    sd.line(sd.get_point(start_point.x, start_point.y + length),
            sd.get_point(start_point.x - 0.075 * width,
                         start_point.y + 0.2 * length), color=sd.COLOR_WHITE, width=int(0.08 * length))
