# -*- coding: utf-8 -*-
"""
# @SoftwareIDE          : PyCharm2020Pro
# @ProjectName          : PySide2MVCFramework
# @FileName             : view.py
# @Author               : 胡守杰
# @Email                : 2839414139@qq.com
# @ZhFileDescription    :
# @EnFileDescription    :
"""

from src.core.view import View


class MainWindowView(View):
    uiFilePath = "F:\PycharmProject\pythonProject\PySide2MVCFramework\src\window\mainWindow\dMainWindow.ui"


if __name__ == '__main__':
    print("unit test from {filename}".format(filename=__file__))
    from PySide2.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    view = MainWindowView().birth()
    view.show()
    sys.exit(app.exec_())
