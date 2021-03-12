# -*- coding: utf-8 -*-
"""
# @SoftwareIDE          : PyCharm2020Pro
# @ProjectName          : PySide2MVCFramework
# @FileName             : test_model_signal.py
# @Author               : 胡守杰
# @Email                : 2839414139@qq.com
# @ZhFileDescription    :
# @EnFileDescription    :
"""

from pyside2mvcframework.core.model import Model, Data


class User(Model):
    name = Data("hushoujie")
    age = Data(24)


if __name__ == '__main__':
    print("unit test from {filename}".format(filename=__file__))
    test_list = list()

    user = User()


    def add_name():
        test_list.append(user.name.data)


    def add_age():
        test_list.append(user.age.data)


    user.signals.nameChanged.connect(add_name)
    user.signals.ageChanged.connect(lambda: add_age())

    user.name = "hujie"
    user.age = 20

    assert test_list[0] == "hujie"
    assert test_list[1] == 20
