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
from src.core.controller import Controller
from example.first_example.window.buttonWindow.service import ButtonWindowService
from example.first_example.window.buttonWindow.view import ButtonWindowView
from example.first_example.model import UserModel


class ButtonWindowController(Controller):
    def __init__(self):
        self.model = UserModel()
        self.view = ButtonWindowView().birth()
        self.service = ButtonWindowService()
        self.setupController()

    def setupSolts(self):
        self.view.btn1.clicked.connect(lambda: self.service.showMsg("btn1"))
        self.view.btn2.clicked.connect(lambda: self.service.showMsg("btn2"))
        self.view.btn3.clicked.connect(lambda: self.service.showMsg("btn3"))
        self.view.btn4.clicked.connect(lambda: self.service.showMsg("btn4"))

    def setupModelToView(self):
        print("设置btnwindow的mtv")
        self.model.nameChanged.connect(lambda: self.service.changeName(self.view.nameLabel, self.model.name))
        self.model.ageChanged.connect(lambda: self.service.changeAge(self.view.ageLabel, self.model.age))


if __name__ == '__main__':
    print("unit test from {filename}".format(filename=__file__))
    import sys
    from PySide2.QtWidgets import QApplication

    app = QApplication(sys.argv)
    controller = ButtonWindowController()
    window = controller.createWindow(parent=None)
    window.show()
    model = UserModel()
    model.setName("hushoujie")
    model.setAge("24")
    sys.exit(app.exec_())
