# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())


class Magic:
    def __str__(self):
        return 'Щепоточка магии'

    def __add__(self, other):
        if isinstance(other, Magic):
            return FlyingKoala()
        elif isinstance(other, Water):
            return Beer()
        elif isinstance(other, Fire):
            return Dragon()
        elif isinstance(other, Soil):
            return Golem()
        elif isinstance(other, Dust):
            return StarDust()


class Water:
    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        if isinstance(other, Water):
            return Water()
        elif isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Soil):
            return Dirt()
        elif isinstance(other, Magic):
            return Beer()


class Air:
    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Air):
            return Air()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Soil):
            return Dust


class Fire:
    def __str__(self):
        return 'Огонь'

    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Soil):
            return Lava()
        elif isinstance(other, Fire):
            return Fire()
        elif isinstance(other, Magic):
            return Dragon()


class Soil:
    def __str__(self):
        return 'Земля'

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        elif isinstance(other, Soil):
            return Soil
        elif isinstance(other, Magic):
            return Golem()


class Storm:
    def __str__(self):
        return 'Шторм'

    def __add__(self, other):
        if isinstance(other, Storm):
            return Storm


class Steam:
    def __str__(self):
        return 'Пар'

    def __add__(self, other):
        if isinstance(other, Steam):
            return Steam()


class Dirt:
    def __str__(self):
        return 'Грязь'

    def __add__(self, other):
        if isinstance(other, Dirt):
            return Dirt()


class Lightning:
    def __str__(self):
        return 'Молния'

    def __add__(self, other):
        if isinstance(other, Lightning):
            return Lightning


class Dust:
    def __str__(self):
        return 'Пыль'

    def __add__(self, other):
        if isinstance(other, Dust):
            return Dust
        elif isinstance(other, Magic):
            return StarDust()


class Lava:
    def __str__(self):
        return 'Лава'

    def __add__(self, other):
        if isinstance(other, Lava):
            return Lava


class FlyingKoala:
    def __str__(self):
        return 'Летающая коала'


class Beer:
    def __str__(self):
        return 'Пивко'


class Dragon:
    def __str__(self):
        return 'Дракон'


class Golem:
    def __str__(self):
        return 'Голем'


class StarDust:
    def __str__(self):
        return 'Звездная пыль'


print(Water(), '+', Air(), '=', Water() + Air())
print(Fire(), '+', Air(), '=', Fire() + Air())
print(Fire(), '+', Magic(), '=', Fire() + Magic())
print(Magic(), '+', Water(), '=', Magic() + Water())
# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
