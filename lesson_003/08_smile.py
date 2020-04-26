# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.


def draw_smile(x, y, color=sd.COLOR_YELLOW):
    """Draw smile in point (x,y)"""
    point = sd.get_point(x, y)
    sd.circle(point, color=color)
    sd.line(sd.get_point(x-40, y+30), sd.get_point(x-20, y+70))
    sd.line(sd.get_point(x - 20, y + 70), sd.get_point(x, y + 50))
    sd.line(sd.get_point(x+5, y+50), sd.get_point(x+25, y+70))
    sd.line(sd.get_point(x+25, y+70), sd.get_point(x+40, y+30))
    sd.ellipse(sd.get_point(x-30, y-30), sd.get_point(x+30, y), width=1)
    sd.rectangle(sd.get_point(x - 30, y - 15), sd.get_point(x + 30, y+15), width=0, color=sd.background_color)
    sd.line(sd.get_point(x, y), sd.get_point(x, y - 10))
    sd.circle(sd.get_point(x-15, y+15), radius=7)
    sd.circle(sd.get_point(x + 15, y + 15), radius=7)
    sd.line(sd.get_point(x - 8, y + 15), sd.get_point(x + 8, y + 15))
    sd.line(sd.get_point(x - 22, y + 15), sd.get_point(x - 40, y + 30))
    sd.line(sd.get_point(x + 22, y + 15), sd.get_point(x+40, y+30))


for _ in range(100):
    draw_smile(sd.random_number(0, sd.resolution[0]), sd.random_number(0, sd.resolution[1]))
sd.pause()
