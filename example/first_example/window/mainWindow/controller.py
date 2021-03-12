# -*- coding: utf-8 -*-
"""
# @SoftwareIDE          : PyCharm2020Pro
# @ProjectName          : PySide2MVCFramework
# @FileName             : controller.py
# @Author               : 胡守杰
# @Email                : 2839414139@qq.com
# @ZhFileDescription    :
# @EnFileDescription    :
"""

from pyside2mvcframework.core.controller import Controller
from example.first_example.window.mainWindow.view import MainWindowView
from example.first_example.window.mainWindow import MainWindowService
from example.first_example.window.buttonWindow.controller import ButtonWindowController


class MainWindowController(Controller):
    def __init__(self):
        self.view = MainWindowView().birth()
        self.service = MainWindowService()
        self.setupController()

    def setupBlank(self):
        self.window1 = ButtonWindowController().createWindow(parent=self.view.central)
        self.view.btnBlankLayout.addWidget(self.window1)
        self.window2 = ButtonWindowController().createWindow(parent=self.view.central)
        self.view.adBlankLayout.addWidget(self.window2)

    def setupSolts(self):
        self.view.open.triggered.connect(lambda: self.service.showInputWindow())


if __name__ == '__main__':
    print("unit test from {filename}".format(filename=__file__))
    from PySide2.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    window = MainWindowController().createWindow(parent=None)
    window.show()
    sys.exit(app.exec_())
