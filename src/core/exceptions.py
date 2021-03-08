# -*- coding: utf-8 -*-
"""
# @SoftwareIDE          : PyCharm2020Pro
# @ProjectName          : PySide2MVCFramework
# @FileName             : exceptions.py
# @Author               : 胡守杰
# @Email                : 2839414139@qq.com
# @ZhFileDescription    : PySide2MVCFramework 核心异常模块
# @EnFileDescription    : PySide2MVCFramework core exception module
"""


class PySide2MVCException(Exception):
    """
    PySide2MVC 异常基类
    PySide2MVC exception base class
    """
    pass


class UiFileNullError(PySide2MVCException):
    """
    uiFile路径为None时异常
    """
    pass


class OpenQFileError(PySide2MVCException):
    """
    打开
    """
    pass


class ServiceOrViewOrModelNullError(PySide2MVCException):
    pass


if __name__ == '__main__':
    print("unit test from {filename}".format(filename=__file__))
