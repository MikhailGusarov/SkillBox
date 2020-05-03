# -*- coding: utf-8 -*-

import simple_draw as sd
from .building_parts import draw_wall, draw_window, draw_roof


def simple_house(point_start, point_end_wall, roof_pitch=45):
    draw_wall(width_brick=50, height_brick=25, point_start_wall=point_start, point_end_wall=point_end_wall)

    start_roof = sd.get_point(point_start.x-10, point_end_wall.y)
    length_roof = point_end_wall.x - point_start.x + 20
    draw_roof(start_point=start_roof, length_grounds=length_roof, angle=roof_pitch)

    length_window = (((point_end_wall.x - point_start.x) + (point_end_wall.y - point_start.y)) / 2) * 0.4
    window_x = point_start.x + (point_end_wall.x - point_start.x) / 2 - length_window / 2
    window_y = point_start.y + (point_end_wall.y - point_start.y) / 2 - length_window / 2
    start_window = sd.get_point(window_x, window_y)
    draw_window(start_point=start_window, length=length_window)
