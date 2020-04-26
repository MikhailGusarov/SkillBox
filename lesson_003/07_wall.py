# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
color = sd.COLOR_ORANGE
width = 100
height = 50
count = 0
for y in range(0, sd.resolution[1] + 1, height):
    count += 1
    for x in range(0 - int(width / 2 * (count % 2)), sd.resolution[0] + 1, width):
        point_1 = sd.get_point(x, y)
        point_2 = sd.get_point(x + width, y + height)
        sd.rectangle(point_1, point_2, color,  1)

sd.pause()
