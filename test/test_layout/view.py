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
from PySide2.QtWidgets import QApplication, QWidget

from test_layout.untitled import Ui_Form


class TestView(Ui_Form, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

    @staticmethod
    def createWindow(parent=None):
        window = TestView(parent=parent)
        return window


if __name__ == '__main__':
    print("unit test from {filename}".format(filename=__file__))
    import sys

    app = QApplication(sys.argv)
    window = TestView(parent=None)
    window.show()
    sys.exit(app.exec_())
