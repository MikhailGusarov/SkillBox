# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg


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


colors_list = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'purple']
colors = {'red': sd.COLOR_RED,
          'orange': sd.COLOR_ORANGE,
          'yellow': sd.COLOR_YELLOW,
          'green': sd.COLOR_GREEN,
          'cyan': sd.COLOR_CYAN,
          'blue': sd.COLOR_BLUE,
          'purple': sd.COLOR_PURPLE}

print("Возможные цвета: ")
for num, color in enumerate(colors_list):
    print(num, ':', color)

while True:
    user_answer = int(input('Введите номер цвета > '))
    if 0 <= user_answer <= len(colors) - 1:
        break
    print('Вы ввели некорректный номер цвета')

color = colors[colors_list[user_answer]]
point = sd.get_point(100, 100)
draw_triangle(start_point=point, angle=10, length=100, color=color)

point = sd.get_point(300, 100)
draw_square(start_point=point, angle=20, length=100, color=color)

point = sd.get_point(100, 300)
draw_pentagon(start_point=point, angle=0, length=100, color=color)

point = sd.get_point(300, 300)
draw_hexagon(start_point=point, angle=0, length=100, color=color)

sd.pause()
