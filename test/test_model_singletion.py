# -*- coding: utf-8 -*-
"""
# @SoftwareIDE          : PyCharm2020Pro
# @ProjectName          : PySide2MVCFramework
# @FileName             : test_model_singletion.py
# @Author               : 胡守杰
# @Email                : 2839414139@qq.com
# @ZhFileDescription    :
# @EnFileDescription    :
"""

from src.core.model import Model, Data


class User(Model):
    name = Data("hushoujie")
    age = Data("23")


if __name__ == '__main__':
    print("unit test from {filename}".format(filename=__file__))
    from threading import Thread

    id_list = list()


    def create():
        user = User()
        id_list.append(id(user))


    for _ in range(100):
        t = Thread(target=create)
        t.start()

    assert len(id_list) == 100
    for index in range(99):
        assert id_list[index] == id_list[index + 1]
