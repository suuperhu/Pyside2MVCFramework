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
from PySide2.QtWidgets import QLabel

from pyside2mvcframework.core.service import Service


class ButtonWindowService(Service):

    def showMsg(self, message: str):
        print(message)

    def changeName(self, label: QLabel, value: str):
        print("设置界面name")
        label.setText(value)
        label.repaint()

    def changeAge(self, label: QLabel, value: str):
        print("设置界面age")
        label.setText(value)
        label.repaint()


if __name__ == '__main__':
    print("unit test from {filename}".format(filename=__file__))
