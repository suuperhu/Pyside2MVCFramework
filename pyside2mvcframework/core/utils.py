# -*- coding: utf-8 -*-
"""
# @SoftwareIDE          : PyCharm2020Pro
# @ProjectName          : PySide2MVCFramework
# @FileName             : utils.py
# @Author               : 胡守杰
# @Email                : 2839414139@qq.com
# @ZhFileDescription    : PySide2MVCFramework的工具模块
# @EnFileDescription    :Tool module of PySide2MVCFramework
"""

from PySide2.QtCore import QFile

from pyside2mvcframework.core.exceptions import OpenQFileError


class OpenQFile(object):
    def __init__(self, filename: str):
        self.filename = filename

    def __enter__(self):
        self.fp = QFile(self.filename)
        self.fp.open(QFile.ReadOnly)
        return self.fp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            raise OpenQFileError(exc_val)
        self.fp.close()
        return True


if __name__ == '__main__':
    print("unit test from {filename}".format(filename=__file__))
