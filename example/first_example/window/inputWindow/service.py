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


class InputService(Service):
    def setNameAndAge(self, view, model):
        print("点击了确认按钮")
        name = view.nameData.text()
        age = view.ageData.text()
        print("开始设置userModel")
        print("usermodel id:{}".format(id(model)))
        model.setName(name)
        model.setAge(age)
        print("设置usermodel完毕")


if __name__ == '__main__':
    print("unit test from {filename}".format(filename=__file__))
