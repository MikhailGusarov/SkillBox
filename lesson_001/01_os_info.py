# -*- coding: utf-8 -*-

# Нужно собрать информацию об операционной системе и версиии пайтона

# TODO запустить этот скрипт и закомитить результат его работы (файл os_info.txt)

import sys
import platform

info = 'OS info is \n{}\n\nPython version is {} {}'.format(
    platform.uname(), sys.version, platform.architecture())
print(info)

with open('os_info.txt', 'w') as ff:
    ff.write(info)
