# -*- coding: utf-8 -*-

import simple_draw as sd

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения
sd.resolution = (1200, 900)


def draw_branches(start_point, angle, length):
    if length < 5:
        return
    vector_0 = sd.get_vector(start_point=start_point, angle=angle, length=length)
    vector_0.draw()
    next_point = vector_0.end_point
    delta_angle = 30 + sd.random_number(0, 40) / 100
    delta_length = .75 + sd.random_number(-10, 10) / 100
    draw_branches(start_point=next_point, angle=angle + delta_angle, length=length * delta_length)
    delta_angle = 30 + sd.random_number(0, 40) / 100
    delta_length = .75 + sd.random_number(-10, 10) / 100
    draw_branches(start_point=next_point, angle=angle - delta_angle, length=length * delta_length)


point = sd.get_point(600, 0)
draw_branches(start_point=point, angle=90, length=200)

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()


