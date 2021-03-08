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
import os
import platform

if platform.system() == "Windows":
    BASE_PATH: str = "F:\\PycharmProject\\pythonProject\\PySide2MVCFramework"
    BASE_STYLE_FILE_PATH = os.path.join(BASE_PATH, "src\\core\\base.qss")
elif platform.system() == "Linux":
    BASE_PATH = ""
    BASE_STYLE_FILE_PATH = ""
else:
    BASE_PATH = ""
    BASE_STYLE_FILE_PATH = ""

if __name__ == '__main__':
    print("unit test from {filename}".format(filename=__file__))
    with open(BASE_STYLE_FILE_PATH) as fp:
        content = fp.read() + "哈哈哈"
        print(content)
