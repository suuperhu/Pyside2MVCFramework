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
from src.core.view import View
from src.core.settings import BASE_PATH


class ButtonWindowView(View):
    uiFilePath = os.path.join(BASE_PATH, "src\\window\\buttonWindow\\dButtonWindow.ui")


if __name__ == '__main__':
    print("unit test from {filename}".format(filename=__file__))
    from PySide2.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    view = ButtonWindowView().birth()
    print(type(view))
    view.show()
    sys.exit(app.exec_())
