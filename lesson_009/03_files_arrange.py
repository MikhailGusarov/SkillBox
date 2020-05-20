# -*- coding: utf-8 -*-

import os
import time
import shutil
import zipfile
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
        self.parsing_source()
        self.copy_in_group()

    def parsing_source(self):
        self.files = {}
        content_source_dir = os.walk(self.source_directory)
        for content_dir in content_source_dir:
            files = content_dir[2]
            parent_dir = content_dir[0]
            for file_name in files:
                full_path_to_file = os.path.join(parent_dir, file_name)
                datetime_file = time.gmtime(os.path.getmtime(full_path_to_file))
                year_file = datetime_file.tm_year
                month_file = datetime_file.tm_mon
                self._group_file(full_path_to_file, month_file, year_file)

    def _group_file(self, path, month_file, year_file):
        if year_file in self.files:
            if month_file in self.files[year_file]:
                self.files[year_file][month_file].append(path)
            else:
                self.files[year_file][month_file] = [path]
        else:
            self.files[year_file] = {month_file: [path]}

    def copy_in_group(self):
        for year, year_folder in self.files.items():
            for month, month_folder in year_folder.items():
                path_folder = os.path.join(self.result_directory, str(year), str(month))
                if not os.path.exists(path_folder):
                    os.makedirs(path_folder)
                for path_file in month_folder:
                    self._copy_file(path_file, path_folder)

    @staticmethod
    def _copy_file(path_file, path_folder):
        shutil.copy2(path_file, path_folder)


class GrouperFilesOfZip(GrouperFiles):

    def __init__(self, source_zip_file, result_directory):
        self.source_zip_file = source_zip_file
        self.result_directory = result_directory
        self.files = {}
        self.zip_file = None

    def parsing_source(self):
        self.zip_file = zipfile.ZipFile(self.source_zip_file)
        for name in self.zip_file.infolist():
            year = name.date_time[0]
            month = name.date_time[1]
            path = name.filename
            print(self.zip_file.open(path))
            if str(path).endswith('/'):
                continue
            self._group_file(path, month, year)

    def copy_in_group(self):
        super().copy_in_group()
        self.zip_file.close()

    def _copy_file(self, path_file, path_folder):
        path_file = self.zip_file.getinfo(path_file)
        path_file.filename = os.path.basename(path_file.filename)
        self.zip_file.extract(path_file, path_folder)


# source_folder = 'icons'
# result_folder = 'icons_by_year'
# grouper_icons = GrouperFiles(source_folder, result_folder)
# grouper_icons.run()

result_folder = 'icons_by_year'
source_file = 'icons.zip'
grouper = GrouperFilesOfZip(source_file, result_folder)
grouper.run()


# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
