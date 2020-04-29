# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg


def draw_equilateral_figure(start_point, angle, length, count_angles):
    """Draw triangle.
    Start_point is start position for draw (down left angle)
    angle is tilt angle base regarding axis x
    length is length one side"""
    new_point = start_point
    for step_angle in range(angle, angle + int((360 - 360 / count_angles)) + 1, int(360 / count_angles)):
        vector = sd.get_vector(start_point=new_point, angle=step_angle, length=length)
        vector.draw(width=3)
        new_point = vector.end_point


def draw_triangle(start_point, angle, length):
    """Draw triangle.
    Start_point is start position for draw (down left angle)
    angle is tilt angle base regarding axis x
    length is length one side"""
    draw_equilateral_figure(start_point=start_point, angle=angle, length=length, count_angles=3)


def draw_square(start_point, angle, length):
    """Draw square.
    Start_point is start position for draw (down left angle)
    angle is tilt angle base regarding axis x
    length is length one side"""
    draw_equilateral_figure(start_point=start_point, angle=angle, length=length, count_angles=4)


def draw_pentagon(start_point, angle, length):
    """Draw triangle.
    Start_point is start position for draw (down left angle)
    angle is tilt angle base regarding axis x
    length is length one side"""
    draw_equilateral_figure(start_point=start_point, angle=angle, length=length, count_angles=5)


def draw_hexagon(start_point, angle, length):
    """Draw triangle.
    Start_point is start position for draw (down left angle)
    angle is tilt angle base regarding axis x
    length is length one side"""
    draw_equilateral_figure(start_point=start_point, angle=angle, length=length, count_angles=6)


point = sd.get_point(100, 100)
draw_triangle(start_point=point, angle=10, length=100)

point = sd.get_point(300, 100)
draw_square(start_point=point, angle=20, length=100)

point = sd.get_point(100, 300)
draw_pentagon(start_point=point, angle=0, length=100)

point = sd.get_point(300, 300)
draw_hexagon(start_point=point, angle=0, length=100)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?
# Прикинул,  многовато выходит. Но вроде можно

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
