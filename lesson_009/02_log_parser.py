# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
from pprint import pprint


class LogParser:
    answer_event = 'NOK'

    def __init__(self, log_file, result_file):
        self.log_file = log_file
        self.result_file = result_file
        self.res_parse = {}

    def run(self):
        self.parse()
        self.write_result()

    def parse(self):
        self.res_parse = {}
        with open(self.log_file, encoding='utf8') as file:
            for line in file:
                self._parse_line(line)

    def _parse_line(self, line):
        if line.endswith(self.answer_event + '\n'):
            datetime = line[1:20]
            if datetime in self.res_parse:
                self.res_parse[datetime] += 1
            else:
                self.res_parse[datetime] = 1

    def write_result(self):
        with open(self.result_file, encoding='utf8', mode='w') as file:
            for datetime, count in self.res_parse.items():
                file.write('[{}] {}\n'.format(datetime, count))


log_file = 'events.txt'
result_file = 'res.txt'
parse = LogParser(log_file=log_file, result_file=result_file)
parse.run()
# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
