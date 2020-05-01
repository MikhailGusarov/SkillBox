# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

from district.central_street.house1 import room1 as cs_house1_room1
from district.central_street.house1 import room2 as cs_house1_room2
from district.central_street.house2 import room1 as cs_house2_room1
from district.central_street.house2 import room2 as cs_house2_room2
from district.soviet_street.house1 import room1 as ss_house1_room1
from district.soviet_street.house1 import room2 as ss_house1_room2
from district.soviet_street.house2 import room1 as ss_house2_room1
from district.soviet_street.house2 import room2 as ss_house2_room2


room_1 = []

room_1 += (cs_house1_room1.folks)
room_1 += (cs_house2_room1.folks)
room_1 += (ss_house1_room1.folks)
room_1 += (ss_house2_room1.folks)

print('В комнате room_1 живут:', ', '.join(room_1))

room_2 = []
room_2 += (cs_house1_room2.folks)
room_2 += (cs_house2_room2.folks)
room_2 += (ss_house1_room2.folks)
room_2 += (ss_house2_room2.folks)

print('В комнате room_2 живут:', ', '.join(room_2))
