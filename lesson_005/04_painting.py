# -*- coding: utf-8 -*-
import simple_draw as sd
from simple_art import houses, living_objects, nature

sd.resolution = (1300, 900)

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги +
#  - стены +
#  - дерева +
#  - смайлика +
#  - снежинок +
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.
nature.draw_rainbow(center_point=sd.get_point(1200, 400), radius=500, width=15)
nature.draw_landscape(height=100)
start_house = sd.get_point(500, 100)
point_end_wall = sd.get_point(800, 400)
houses.simple_house(point_start=start_house, point_end_wall=point_end_wall)
nature.draw_tree(start_point=sd.get_point(1000, 50), angle=90, length=100)
nature.draw_tree(start_point=sd.get_point(1100, 60), angle=90, length=30)
sun_center = sd.get_point(150, 750)
nature.draw_sun(center_point=sun_center, radius=80, length_sunbeam=70)
living_objects.draw_cat_face(x=650, y=220, size=30)

for _ in range(300):
    data_snowflake = nature.generate_snowflakes_data(x_start=30, x_end=200, y_start=20, y_end=100)
    nature.draw_snowflake(**data_snowflake)

living_objects.draw_cow(start_point=sd.get_point(300, 100), length=100, width=200)

sd.pause()

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик. +
#  - слева от дома - сугроб (предположим что это ранняя весна) +
#  - справа от дома - дерево (можно несколько) +
#  - справа в небе - радуга, слева - солнце (весна же!) +
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

# TODO здесь ваш код

# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.
