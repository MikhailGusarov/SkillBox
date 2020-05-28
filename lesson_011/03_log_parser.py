# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234
from collections import defaultdict


def log_parse(log_file):
    res = defaultdict(lambda: 0)
    with open(log_file, encoding='utf8') as file:
        for line in file:
            if line.endswith('NOK\n'):
                datetime = line[1:20]
                res[datetime] += 1
    for min, count in res.items():
        yield min, count


log_file = 'events.txt'
grouped_events = log_parse(log_file)
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')


