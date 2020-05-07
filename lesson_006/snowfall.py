import simple_draw as sd

_snowflakes = []


def create_snowflakes(count_snowflakes):
    """ Генератор снеджинок, где count_snowflakes = кол-во снежинок"""
    global _snowflakes
    for _ in range(count_snowflakes):
        x = sd.random_number(0, sd.resolution[0])
        y = sd.random_number(0, sd.resolution[1])
        length = sd.random_number(10, 40)
        factor_a = sd.random_number(50, 70) / 100
        factor_b = sd.random_number(25, 45) / 100
        factor_c = sd.random_number(50, 70)
        snowflake = {'x': x,
                     'y': y,
                     'length': length,
                     'factor_a': factor_a,
                     'factor_b': factor_b,
                     'factor_c': factor_c}
        _snowflakes.append(snowflake)


def draw_snowflakes(color=sd.COLOR_WHITE):
    """Нарисовать снежинки цветом color """
    global _snowflakes
    for snowflake in _snowflakes:
        sd.snowflake(center=sd.get_point(snowflake['x'], snowflake['y']),
                     length=snowflake['length'],
                     color=color,
                     factor_a=snowflake['factor_a'],
                     factor_b=snowflake['factor_b'],
                     factor_c=snowflake['factor_c'])


def move_down():
    """Сдвинуть снежинки на 5 пикселей вниз"""
    global _snowflakes
    for snowflake in _snowflakes:
        snowflake['y'] -= 5


def get_reached_bottom():
    """Вернуть снежинки, которые упали за пределы экрана"""
    global _snowflakes
    reached_bottom_snowflake = []
    for snowflake in _snowflakes:
        if snowflake['y'] <= 0:
            reached_bottom_snowflake.append(snowflake)
    return reached_bottom_snowflake


def delete_snowflakes(snowflakes_for_del):
    """Удалить снежинки, которые есть в списке snowflakes_for_del из списка снежинок"""
    global _snowflakes
    for snowflake_for_del in snowflakes_for_del:
        if snowflake_for_del in _snowflakes:
            sd.snowflake(center=sd.get_point(snowflake_for_del['x'], snowflake_for_del['y']),
                         length=snowflake_for_del['length'],
                         color=sd.background_color,
                         factor_a=snowflake_for_del['factor_a'],
                         factor_b=snowflake_for_del['factor_b'],
                         factor_c=snowflake_for_del['factor_c'])
            _snowflakes.remove(snowflake_for_del)
