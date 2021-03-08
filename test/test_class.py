# -*- coding: utf-8 -*-
"""
# @SoftwareIDE          : PyCharm2020Pro
# @ProjectName          : PySide2MVCFramework
# @FileName             : test_class.py
# @Author               : 胡守杰
# @Email                : 2839414139@qq.com
# @ZhFileDescription    :
# @EnFileDescription    :
"""


class A(object):
    a = 1
    b = 2
    c = 3


if __name__ == '__main__':
    print("unit test from {filename}".format(filename=__file__))
    a = A()
    print(a.a)