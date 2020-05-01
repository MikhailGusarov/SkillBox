# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

# TODO здесь ваш код


from district.central_street.house1 import room1 as cs_house1_room1
from district.central_street.house1 import room2 as cs_house1_room2
from district.central_street.house2 import room1 as cs_house2_room1
from district.central_street.house2 import room2 as cs_house2_room2
from district.soviet_street.house1 import room1 as ss_house1_room1
from district.soviet_street.house1 import room2 as ss_house1_room2
from district.soviet_street.house2 import room1 as ss_house2_room1
from district.soviet_street.house2 import room2 as ss_house2_room2

folks = []

folks += (cs_house1_room1.folks)
folks += (cs_house2_room1.folks)
folks += (cs_house1_room2.folks)
folks += (cs_house2_room2.folks)
folks += (ss_house1_room1.folks)
folks += (ss_house2_room1.folks)
folks += (ss_house1_room2.folks)
folks += (ss_house2_room2.folks)
print('На районе живут', ', '.join(folks))


