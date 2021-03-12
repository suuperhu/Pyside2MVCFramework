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
import os
from pyside2mvcframework.core.view import View
from conf.global_settings import BASE_PATH


class InputWindowView(View):
    uiFilePath = os.path.join(BASE_PATH, "src\\window\\inputWindow\\inputWindow.ui")


if __name__ == '__main__':
    print("unit test from {filename}".format(filename=__file__))
    import sys
    from PySide2.QtWidgets import QApplication

    app = QApplication(sys.argv)
    view = InputWindowView().birth()
    view.show()
    sys.exit(app.exec_())
