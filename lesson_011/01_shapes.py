# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):
    def draw_equilateral_figure(point, angle, length):
        new_point = point
        for step_angle in range(angle, angle + int((360 - 360 / n)) + 1, int(360 / n)):
            vector = sd.get_vector(start_point=new_point, angle=step_angle, length=length)
            vector.draw(width=3)
            new_point = vector.end_point
    return draw_equilateral_figure


draw_triangle = get_polygon(n=5)
draw_triangle(point=sd.get_point(200, 200), angle=13, length=100)


sd.pause()
