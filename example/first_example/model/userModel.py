# -*- coding: utf-8 -*-
"""
# @SoftwareIDE          : PyCharm2020Pro
# @ProjectName          : PySide2MVCFramework
# @FileName             : userModel.py
# @Author               : 胡守杰
# @Email                : 2839414139@qq.com
# @ZhFileDescription    :
# @EnFileDescription    :
"""
from PySide2.QtCore import Signal, QObject
from src.core.model import Model


class UserModel(Model):
    name = None
    age = None

    nameChanged: QObject = Signal()
    ageChanged: QObject = Signal()

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def setName(self, value):
        print("设置name, 发送信号")
        self.name = value
        self.nameChanged.emit()

    def setAge(self, value):
        print("设置age, 发送信号")
        self.age = value
        self.ageChanged.emit()


if __name__ == '__main__':
    print("unit test from {filename}".format(filename=__file__))


    def showName(name):
        print(name)


    def showAge(age):
        print(age)


    model = UserModel()
    model.ageChanged.connect(lambda: showName(model.name))
    model.ageChanged.connect(lambda: showAge(model.age))
    model.setName("hushoujie")
    model.setAge("24")
