# -*- coding: utf-8 -*-

import simple_draw as sd


# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 50
speed = 10

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()


def generate_snowflakes_data():
    x = sd.random_number(0, sd.resolution[0])
    y = sd.random_number(sd.resolution[1] - 50, sd.resolution[1] + 500)
    length = sd.random_number(10, 40)
    factor_a = sd.random_number(50, 70) / 100
    factor_b = sd.random_number(25, 45) / 100
    factor_c = sd.random_number(50, 70)
    return {'x': x,
            'y': y,
            'length': length,
            'factor_a': factor_a,
            'factor_b': factor_b,
            'factor_c': factor_c}


snowflakes = []
for _ in range(N):
    snowflakes.append(generate_snowflakes_data())

while True:
    for snowflake in snowflakes:
        point = sd.get_point(snowflake['x'], snowflake['y'])
        sd.snowflake(center=point,
                     length=snowflake['length'],
                     color=sd.background_color,
                     factor_a=snowflake['factor_a'],
                     factor_b=snowflake['factor_b'],
                     factor_c=snowflake['factor_c'])
        snowflake['y'] -= speed
        snowflake['x'] += sd.random_number(-2, 2)
        point = sd.get_point(snowflake['x'], snowflake['y'])
        sd.snowflake(center=point,
                     length=snowflake['length'],
                     factor_a=snowflake['factor_a'],
                     factor_b=snowflake['factor_b'],
                     factor_c=snowflake['factor_c'])
        if snowflake['y'] < 10:
            snowflake['y'] = sd.random_number(sd.resolution[1] - 50, sd.resolution[1] + 300)
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


