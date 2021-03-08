# -*- coding: utf-8 -*-
"""
# @SoftwareIDE          : PyCharm2020Pro
# @ProjectName          : PySide2MVCFramework
# @FileName             : test_metaclass.py
# @Author               : 胡守杰
# @Email                : 2839414139@qq.com
# @ZhFileDescription    :
# @EnFileDescription    :
"""
from PySide2.QtCore import QObject, Signal
from typing import Any
from threading import Lock


class Data(object):
    def __init__(self, data: Any = None):
        self.data = data


class ModelMetaclass(type):
    def __new__(mcls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(mcls, name, bases, attrs)
        signals_attrs = dict()
        for k, v in attrs.items():
            if isinstance(v, Data):
                signals_attrs[k + "Changed"] = Signal()
        signals = type("signals", (QObject,), signals_attrs)()
        attrs["signals"] = signals
        return type.__new__(mcls, name, bases, attrs)


class Model(object, metaclass=ModelMetaclass):
    lock = Lock()

    def __new__(cls, *args, **kwargs):
        if hasattr(cls, "_instance"):
            return cls._instance
        with cls.lock:
            cls._instance = super().__new__(cls)
            return cls._instance

    def __setattr__(self, key, value):
        if hasattr(self.__class__, key):
            data_instance = getattr(self.__class__, key)
            data_instance.data = value
            signals = getattr(self.__class__, "signals")
            signal = getattr(signals, key + "Changed")
            signal.emit()
        else:
            raise Exception("{} has not {}".format(self.__class__.__name__, key))


if __name__ == '__main__':
    print("unit test from {filename}".format(filename=__file__))


    class User(Model):
        id = Data(123)
        name = Data("hushoujie")
        email = Data("xxx@qq.com")


    u = User()


    def do():
        print(u.id.data)


    u.signals.idChanged.connect(lambda: do())
    u.id = 11111
