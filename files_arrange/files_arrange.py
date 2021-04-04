# -*- coding: utf-8 -*-
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

import os, time, shutil
import zipfile


class FilesArrange:
    def __init__(self, zip_name, file_icon_arrange):
        self.name_zip = zip_name
        self.file_icon_arrange = file_icon_arrange

    def extract_zip(self):
        f = zipfile.ZipFile(self.name_zip, 'r')
        for file in f.infolist():
            d = file.date_time
            gettime = "%s/%s/%s %s:%s" % (d[0], d[1], d[2], d[3], d[4])
            f.extract(file)
            filep = os.path.join(file.filename)
            timearry = time.mktime(time.strptime(gettime, '%Y/%m/%d %H:%M'))
            os.utime(filep, (timearry, timearry))

    def read_file(self, file_name):
        files_icons = os.listdir(file_name)
        for file_icon in files_icons:
            path_icons_files = os.path.join(file_name, file_icon)
            icons = os.listdir(path_icons_files)
            for icon in icons:
                path_icon = os.path.join(path_icons_files, icon)
                icon_creation_dateos = time.ctime(os.path.getmtime(path_icon)).split()
                year = icon_creation_dateos[-1]
                month = icon_creation_dateos[1]
                self.check_path(year, month)
                self.icons_arrange(path_icon, year, month)

    def check_path(self, year, month):
        if os.path.exists(self.file_icon_arrange) == False:
            os.mkdir(self.file_icon_arrange)

        arrange_path_year = os.path.join(self.file_icon_arrange, year)
        if os.path.exists(arrange_path_year) == False:
            os.mkdir(arrange_path_year)

        arrange_path_month = os.path.join(arrange_path_year, month)
        if os.path.exists(arrange_path_month) == False:
            os.mkdir(arrange_path_month)

    def icons_arrange(self, path_icon, year, month):
        path_to_save = os.path.join(self.file_icon_arrange, year, month)
        shutil.move(path_icon, path_to_save)


arrange = FilesArrange('icons.zip', 'icons_arrange')
arrange.extract_zip()
arrange.read_file('icons')

# os.mkdir() - создаст папку
# os.path.exists() - проверка есть ли папка
