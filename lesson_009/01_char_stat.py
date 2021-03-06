# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

import zipfile
from pprint import pprint
from os.path import join, normpath, dirname


class StaticChars:
    file_name = None

    def __init__(self, path):
        self.file_path = normpath(path)
        self.stat = {}
        self.stat_for_print = []
        self.all_count_char = 0

    def unzip(self, file_zip_path):
        file_zip = zipfile.ZipFile(file_zip_path)
        for filename in file_zip.namelist():
            file_zip.extract(filename)
            self.file_path = filename

    def collect(self):
        if self.file_path.endswith('.zip'):
            self.unzip(self.file_path)
        with open(self.file_path, encoding='cp1251') as file:
            for line in file:
                self._collect_in_line(line)

    def _collect_in_line(self, line):
        for ch in line:
            if ch.isalpha():
                if ch in self.stat:
                    self.stat[ch] += 1
                else:
                    self.stat[ch] = 1

    def prepare(self):
        self.stat_for_print = []
        self.all_count_char = 0
        for ch, count in self.stat.items():
            self._prepare_append(ch, count)
            self.all_count_char += count

    def _prepare_append(self, ch, count):
        self.stat_for_print.append([count, ch])

    def print_stat(self):
        print('+---------+----------+')
        print('|  буква  | частота  |')
        print('+---------+----------+')
        self._print_stat_body()
        print('+---------+----------+')
        print(f'|  итого  |{self.all_count_char:^10}|')
        print('+---------+----------+')

    def _print_stat_body(self):
        for count, ch in self.stat_for_print:
            print(f'|{ch:^9}|{count:^10}|')

    def sort_stat(self):
        self.stat_for_print.sort(reverse=True)

    def run_and_print(self):
        self.collect()
        self.prepare()
        self.sort_stat()
        self.print_stat()


class StaticCharReverse(StaticChars):
    def sort_stat(self):
        self.stat_for_print.sort()


class StaticCharAlphabetReverse(StaticCharReverse):
    def _prepare_append(self, ch, count):
        self.stat_for_print.append([ch, count])

    def _print_stat_body(self):
        for ch, count in self.stat_for_print:
            print(f'|{ch:^9}|{count:^10}|')


class StaticCharAlphabet(StaticCharAlphabetReverse):
    def sort_stat(self):
        self.stat_for_print.sort(reverse=True)

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828


file_zip_path = join('python_snippets', 'voyna-i-mir.txt.zip')
stat = StaticCharAlphabet(file_zip_path)
stat.run_and_print()
