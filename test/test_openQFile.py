# -*- coding: utf-8 -*-
"""
# @SoftwareIDE          : PyCharm2020Pro
# @ProjectName          : PySide2MVCFramework
# @FileName             : test_openQFile.py
# @Author               : 胡守杰
# @Email                : 2839414139@qq.com
# @ZhFileDescription    :
# @EnFileDescription    :
"""
from pyside2mvcframework.core.utils import OpenQFile

if __name__ == '__main__':
    print("unit test from {filename}".format(filename=__file__))
    with OpenQFile("测试.txt") as fp:
        content = fp.readAll().data().decode()
    assert content == "测试"