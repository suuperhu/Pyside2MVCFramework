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
from example.first_example.window.inputWindow.view import InputWindowView
from example.first_example.window.inputWindow.service import InputService
from example.first_example.model import UserModel


class InputController(Controller):

    def __init__(self):
        self.model = UserModel()
        self.view = InputWindowView().birth()
        self.service = InputService()
        self.setupController()

    def setupViewToModel(self):
        print("设置按钮窗口的vtm")
        print("model id:{}".format(self.model))
        self.view.okBtn.clicked.connect(lambda: self.service.setNameAndAge(self.view, self.model))


if __name__ == '__main__':
    print("unit test from {filename}".format(filename=__file__))
    import sys
    from PySide2.QtWidgets import QApplication

    app = QApplication(sys.argv)
    controller = InputController()
    window = controller.createWindow(parent=None)
    window.show()
    sys.exit(app.exec_())
