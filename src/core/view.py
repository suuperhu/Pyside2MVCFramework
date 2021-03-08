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
from src.core.exceptions import UiFileNullError
from src.core.utils import OpenQFile
from src.core.settings import BASE_STYLE_FILE_PATH


class View(object):
    uiFilePath: str = None
    styleFilePath: str = BASE_STYLE_FILE_PATH

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.load()
        self.setupStyleSheet()

    def load(self):
        if self.uiFilePath == None:
            raise UiFileNullError("uiFilePath 不能为 Null")
        with OpenQFile(self.uiFilePath) as fp:
            self.ui = QUiLoader().load(fp)

    def setupStyleSheet(self):
        """
        初始化界面样式
        Initialize interface style
        :return: None
        """
        # with open(BASE_STYLE_FILE_PATH, encoding="utf-8") as fp:
        #     baseStyleSheet = fp.read()
        # if self.styleFilePath == BASE_STYLE_FILE_PATH:
        #     self.ui.setStyleSheet(baseStyleSheet)
        #     print(baseStyleSheet)
        # else:
        #     with open(self.styleFilePath, encoding="utf-8") as fp:
        #         styleSheet = fp.read()
        #         styleSheet = baseStyleSheet + styleSheet
        #         self.ui.setStyleSheet(styleSheet)
        #         print(styleSheet)
        pass

    def birth(self) -> Union[QMainWindow, QWidget, QDialog]:
        return self.ui


if __name__ == '__main__':
    print("unit test from {filename}".format(filename=__file__))
