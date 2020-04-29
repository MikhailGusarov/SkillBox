# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg


def draw_equilateral_figure(start_point, angle, length, count_angles, color=sd.COLOR_YELLOW):
    """Draw triangle.
    Start_point is start position for draw (down left angle)
    angle is tilt angle base regarding axis x
    length is length one side"""
    new_point = start_point
    for step_angle in range(angle, angle + int((360 - 360 / count_angles)) + 1, int(360 / count_angles)):
        vector = sd.get_vector(start_point=new_point, angle=step_angle, length=length)
        vector.draw(width=3, color=color)
        new_point = vector.end_point


def draw_triangle(start_point, angle, length, color=sd.COLOR_YELLOW):
    """Draw triangle.
    Start_point is start position for draw (down left angle)
    angle is tilt angle base regarding axis x
    length is length one side"""
    draw_equilateral_figure(start_point=start_point, angle=angle, length=length, count_angles=3, color=color)


def draw_square(start_point, angle, length, color=sd.COLOR_YELLOW):
    """Draw square.
    Start_point is start position for draw (down left angle)
    angle is tilt angle base regarding axis x
    length is length one side"""
    draw_equilateral_figure(start_point=start_point, angle=angle, length=length, count_angles=4, color=color)


def draw_pentagon(start_point, angle, length, color=sd.COLOR_YELLOW):
    """Draw triangle.
    Start_point is start position for draw (down left angle)
    angle is tilt angle base regarding axis x
    length is length one side"""
    draw_equilateral_figure(start_point=start_point, angle=angle, length=length, count_angles=5, color=color)


def draw_hexagon(start_point, angle, length, color=sd.COLOR_YELLOW):
    """Draw triangle.
    Start_point is start position for draw (down left angle)
    angle is tilt angle base regarding axis x
    length is length one side"""
    draw_equilateral_figure(start_point=start_point, angle=angle, length=length, count_angles=6, color=color)


figures_list = ['треугольник', 'квадрат', 'пятиугольник', 'шестиугольник']

print("Возможные фигуры: ")
for num, figure in enumerate(figures_list):
    print(num, ':', figure)

while True:
    user_answer = int(input('Введите номер фигууры > '))
    if 0 <= user_answer <= len(figures_list) - 1:
        break
    print('Вы ввели некорректный номер фигуры')

point = sd.get_point(300, 300)
if user_answer == 0:
    draw_triangle(start_point=point, angle=10, length=100)
elif user_answer == 1:
    draw_square(start_point=point, angle=20, length=100)
elif user_answer == 2:
    draw_pentagon(start_point=point, angle=0, length=100)
else:
    draw_hexagon(start_point=point, angle=0, length=100)

sd.pause()
