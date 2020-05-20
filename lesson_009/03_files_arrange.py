# -*- coding: utf-8 -*-

import os
import time
import shutil

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
from pprint import pprint


class GrouperFiles:

    def __init__(self, source_directory, result_directory):
        self.source_directory = source_directory
        self.result_directory = result_directory
        self.files = {}

    def run(self):
        self.parsing_source_folder()
        self.copy_in_group()

    def parsing_source_folder(self):
        self.files = {}
        content_source_dir = os.walk(self.source_directory)
        for content_dir in content_source_dir:
            self._parsing_folder(content_dir)

    def _parsing_folder(self, content_dir):
        for file_name in content_dir[2]:
            full_path_to_file = os.path.join(content_dir[0], file_name)
            datetime_file = time.gmtime(os.path.getmtime(full_path_to_file))
            year_file = datetime_file.tm_year
            month_file = datetime_file.tm_mon
            if year_file in self.files:
                if month_file in self.files[year_file]:
                    self.files[year_file][month_file].append([content_dir[0], file_name])
                else:
                    self.files[year_file][month_file] = [[content_dir[0], file_name]]
            else:
                self.files[year_file] = {month_file: [[content_dir[0], file_name]]}

    def copy_in_group(self):
        for year, year_folder in self.files.items():
            for month, month_folder in year_folder.items():
                path_folder = os.path.join(self.result_directory, str(year), str(month))
                if not os.path.exists(path_folder):
                    os.makedirs(path_folder)
                for folder, file in month_folder:
                    path_file = os.path.join(folder, file)
                    shutil.copy2(path_file, path_folder)


source_folder = 'icons'
result_folder = 'icons_by_year'
grouper_icons = GrouperFiles(source_folder, result_folder)
grouper_icons.run()

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
