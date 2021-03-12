# -*- coding: utf-8 -*-
"""
# @SoftwareIDE          : PyCharm2020Pro
# @ProjectName          : PySide2MVCFramework
# @FileName             : settings.py
# @Author               : 胡守杰
# @Email                : 2839414139@qq.com
# @ZhFileDescription    : PySide2MVCFramework设置模块
# @EnFileDescription    : PySide2MVCFramework Setting Module
"""
from pathlib import Path
import platform
import os

BASE_DIR = Path(__file__).resolve().parent.parent

if platform.system() == "Windows":
    GLOBAL_QSS_PATH = os.path.join(BASE_DIR, "conf\global.qss")
else:
    GLOBAL_QSS_PATH = os.path.join(BASE_DIR, "conf/global.qss")

if __name__ == '__main__':
    print("unit test from {filename}".format(filename=__file__))
    print(BASE_DIR)
    print(GLOBAL_QSS_PATH)
    with open(GLOBAL_QSS_PATH, encoding="utf-8") as fp:
        globalStyleSheet = fp.read()
    print(globalStyleSheet)
