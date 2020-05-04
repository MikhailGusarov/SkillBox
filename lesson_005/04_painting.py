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



# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик. +
#  - слева от дома - сугроб (предположим что это ранняя весна) +
#  - справа от дома - дерево (можно несколько) +
#  - справа в небе - радуга, слева - солнце (весна же!) +
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

snowflakes = []
for _ in range(20):
    snowflakes.append(nature.generate_snowflakes_data(x_end=200, y_start=200, y_end=600))
count = 0
while True:
    count += 1
    for snowflake in snowflakes:
        point = sd.get_point(snowflake['x'], snowflake['y'])
        sd.snowflake(center=point,
                     length=snowflake['length'],
                     color=sd.background_color,
                     factor_a=snowflake['factor_a'],
                     factor_b=snowflake['factor_b'],
                     factor_c=snowflake['factor_c'])
        snowflake['y'] -= 10
        snowflake['x'] += sd.random_number(-2, 2)
        point = sd.get_point(snowflake['x'], snowflake['y'])
        sd.snowflake(center=point,
                     length=snowflake['length'],
                     factor_a=snowflake['factor_a'],
                     factor_b=snowflake['factor_b'],
                     factor_c=snowflake['factor_c'])
        if snowflake['y'] < 130:
            snowflake['y'] = sd.random_number(sd.resolution[1] - 50, sd.resolution[1] + 300)
    nature.draw_sun(center_point=sun_center, radius=80, length_sunbeam=70)
    if count % 20 == 0:
        sd.circle(sd.get_point(545, 175), radius=5, width=0, color=sd.COLOR_WHITE)
        sd.line(sd.get_point(540, 175), sd.get_point(550, 175), color=sd.COLOR_BLACK)
    sd.finish_drawing()
    sd.sleep(0.1)
    if count % 22 == 0:
        sd.circle(sd.get_point(545, 175), radius=5, width=0, color=sd.COLOR_BLACK)
    if sd.user_want_exit():
        break

sd.pause()
# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.
