# -*- coding: utf-8 -*-
"""
# @SoftwareIDE          : PyCharm2020Pro
# @ProjectName          : PySide2MVCFramework
# @FileName             : service.py
# @Author               : 胡守杰
# @Email                : 2839414139@qq.com
# @ZhFileDescription    :
# @EnFileDescription    :
"""

from pyside2mvcframework.core.service import Service
from example.first_example.window.inputWindow.controller import InputController


class MainWindowService(Service):
    def showInputWindow(self):
        window = InputController().createWindow(parent=None)
        window.show()


if __name__ == '__main__':
    print("unit test from {filename}".format(filename=__file__))
