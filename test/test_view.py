# -*- coding: utf-8 -*-
"""
# @SoftwareIDE          : PyCharm2020Pro
# @ProjectName          : PySide2MVCFramework
# @FileName             : test_view.py
# @Author               : 胡守杰
# @Email                : 2839414139@qq.com
# @ZhFileDescription    :
# @EnFileDescription    :
"""
from pyside2mvcframework.core.view import View
from conf.global_settings import BASE_DIR
import os


class TestView(View):
    uiFilePath = os.path.join(BASE_DIR.parent, "test\\test_view.ui")
    styleFilePath = os.path.join(BASE_DIR.parent, "test\\test_view.qss")


if __name__ == '__main__':
    print("unit test from {filename}".format(filename=__file__))
    import sys
    from PySide2.QtWidgets import QApplication

    app = QApplication(sys.argv)
    view = TestView().birth()
    view.show()
    sys.exit(app.exec_())
