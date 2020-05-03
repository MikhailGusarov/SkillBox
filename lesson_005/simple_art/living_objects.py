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
