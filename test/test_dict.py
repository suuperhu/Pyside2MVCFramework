# -*- coding: utf-8 -*-
"""
# @SoftwareIDE          : PyCharm2020Pro
# @ProjectName          : PySide2MVCFramework
# @FileName             : test_dict.py
# @Author               : 胡守杰
# @Email                : 2839414139@qq.com
# @ZhFileDescription    :
# @EnFileDescription    :
"""
import inspect

from PySide2.QtCore import QObject, Signal, QMetaObject


class PySide2MVCFrameworkSignal(QObject):
    def __init__(self):
        super().__init__()


class Model(QObject):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._hasInit = False
            return cls._instance
        cls._hasInit = True
        return cls._instance

    def __init__(self, *args, **kwargs):
        if not self._hasInit:
            super().__init__(*args, **kwargs)
            modelClass = self.__class__
            modelClassProperties = [p for p in modelClass.__dict__.keys() if
                                    not inspect.isbuiltin(getattr(modelClass, p))]
            modelClassProperties.remove("__module__")
            modelClassProperties.remove("__doc__")
            modelClassProperties.remove("_instance")
            modelClassProperties.remove("_hasInit")
            modelClassProperties.remove("staticMetaObject")
            print(modelClassProperties)
            print(self.__class__.__dict__)
            for name in modelClassProperties:
                signalName = name + "Changed"
                PySide2MVCFrameworkSignal.__setattr__(signalName, Signal())
                modelClass.__setattr__("signal", PySide2MVCFrameworkSignal())

            print(self.__class__.__dict__)


class UserModel(Model):
    username = None
    userage = None


class MsgModel(Model):
    size = 10
    height = 2.3


if __name__ == '__main__':
    print("unit test from {filename}".format(filename=__file__))
    model = UserModel()
    model2 = MsgModel()
