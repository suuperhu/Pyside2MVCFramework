# -*- coding: utf-8 -*-
"""
# @SoftwareIDE          : PyCharm2020Pro
# @ProjectName          : PySide2MVCFramework
# @FileName             : view.py
# @Author               : 胡守杰
# @Email                : 2839414139@qq.com
# @ZhFileDescription    : view层工厂函数模式基类
# @EnFileDescription    : View layer factory function pattern base class
"""
from typing import Union

from PySide2.QtWidgets import QMainWindow, QWidget, QDialog
from PySide2.QtUiTools import QUiLoader
from pyside2mvcframework.core.exceptions import UiFileNullError
from pyside2mvcframework.core.utils import OpenQFile
from conf.global_settings import GLOBAL_QSS_PATH


class View(object):
    uiFilePath: str = None
    styleFilePath: str = GLOBAL_QSS_PATH

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.load()
        self.setupStyleSheet()

    def load(self):
        if self.uiFilePath == None:
            raise UiFileNullError("uiFilePath类属性不能为Null")
        with OpenQFile(self.uiFilePath) as fp:
            self.ui = QUiLoader().load(fp)

    def setupStyleSheet(self):
        """
        初始化界面样式
        Initialize interface style
        :return: None
        """
        with open(GLOBAL_QSS_PATH, encoding="utf-8") as fp:
            globalStyleSheet = fp.read()
        if self.styleFilePath == GLOBAL_QSS_PATH:
            self.ui.setStyleSheet(globalStyleSheet)
        else:
            with open(self.styleFilePath, encoding="utf-8") as fp:
                styleSheet = fp.read()
                styleSheet = globalStyleSheet + styleSheet
                self.ui.setStyleSheet(styleSheet)

    def birth(self) -> Union[QMainWindow, QWidget, QDialog]:
        return self.ui


if __name__ == '__main__':
    print("unit test from {filename}".format(filename=__file__))
