# -*- coding: utf-8 -*-

import simple_draw as sd


def draw_brick(start_point, width, height, color):
    point_1 = start_point
    point_2 = sd.get_point(start_point.x + width, start_point.y + height)
    sd.rectangle(point_1, point_2, color, 1)


def draw_wall(width_brick, height_brick, point_start_wall, point_end_wall):
    color = sd.COLOR_ORANGE
    sd.rectangle(left_bottom=point_start_wall, right_top=point_end_wall, color=color, width=1)
    count = 0
    for y in range(point_start_wall.y, point_end_wall.y, height_brick):
        if count % 2:
            point_start_x = point_start_wall.x
        else:
            point_start_x = point_start_wall.x + int(width_brick / 2)
        for x in range(point_start_x, point_end_wall.x, width_brick):
            if x + width_brick > point_end_wall.x:
                width_brick_final = point_end_wall.x - x
            else:
                width_brick_final = width_brick

            start_point_brick = sd.get_point(x=x, y=y)
            get_brick(start_point=start_point_brick, width=width_brick_final, height=height_brick, color=color)
        count += 1

