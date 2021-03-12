# -*- coding: utf-8 -*-
"""
# @SoftwareIDE          : PyCharm2020Pro
# @ProjectName          : PySide2MVCFramework
# @FileName             : controller.py
# @Author               : 胡守杰
# @Email                : 2839414139@qq.com
# @ZhFileDescription    : PySide2MVCFramework controller 层
# @EnFileDescription    : PySide2MVCFramework controller layer
"""
from typing import Union
from PySide2.QtWidgets import QDialog, QWidget, QMainWindow


class Controller(object):
    view = None
    service = None

    def __init__(self):
        self.setupController()

    def setupController(self):
        """
        初始化view层界面
        Initialize the view layer interface
        :return: None
        """
        self.setupBlank()
        self.setupSolts()
        self.setupViewToModel()
        self.setupModelToView()

    def setupBlank(self):
        """
        初始化view层空白区域
        Initialize the blank area of the view layer
        :return: None
        """
        pass

    def setupViewToModel(self):
        """
        将view层数据保存到model层
        Save the view layer data to the model layer
        :return: None
        """
        pass

    def setupModelToView(self):
        """
        将model层数据显示到view层
        Display the model layer data to the view layer
        :return: None
        """
        pass

    def setupSolts(self):
        """
        绑定当前界面的原生信号槽函数
        Bind the native signal slot function of the current interface
        :return: None
        """
        pass

    def createWindow(self, parent=None) -> Union[QDialog, QWidget, QMainWindow]:
        """
        返回一个完全初始化的界面(包括ui,美化,动作等)
        Return to a fully initialized interface (including ui, beautification, actions, etc.)
        :param parent: QWidget
        :return: Union[QDialog, QWidget, QMainWindow]
        """
        if self.view:
            self.view.setParent(parent)
            return self.view
        raise Exception("view属性不能为空")


if __name__ == '__main__':
    print("unit test from {filename}".format(filename=__file__))
