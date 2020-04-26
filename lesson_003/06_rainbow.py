# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# point_1, point_2 = [50, 50], [350, 450]
# width = 4
# step = 5
# for color in rainbow_colors:
#     sd.lines([sd.get_point(point_1[0], point_1[1]), sd.get_point(point_2[0], point_2[1])], color, width)
#     point_1[0] += step
#     point_2[0] += step


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
point = sd.get_point(sd.resolution[0]/2, -200)
step = 50 - 15
for color in rainbow_colors:
    step += 15
    sd.circle(point, int(sd.resolution[0]/2 + step), color, 15)

sd.pause()
