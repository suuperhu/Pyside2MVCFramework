# -*- coding: utf-8 -*-
"""
# @SoftwareIDE          : PyCharm2020Pro
# @ProjectName          : PySide2MVCFramework
# @FileName             : view2.py
# @Author               : 胡守杰
# @Email                : 2839414139@qq.com
# @ZhFileDescription    :
# @EnFileDescription    :
"""
from PySide2.QtWidgets import QWidget, QVBoxLayout, QPushButton
from test_layout.untitled2 import Ui_Form
from test_layout.view import TestView


class Form2(Ui_Form, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

        frame2Layout = QVBoxLayout(self.frame2)
        frame2Layout.setObjectName("frame2Layout")
        window = TestView.createWindow(parent=self.frame2)
        # btn1 = QPushButton(self.frame2)
        # btn1.setObjectName("btn1")
        # btn2 = QPushButton(self.frame2)
        # btn2.setObjectName("btn2")
        # frame2Layout.addWidget(btn1)
        # frame2Layout.addWidget(btn2)
        frame2Layout.addWidget(window)


if __name__ == '__main__':
    print("unit test from {filename}".format(filename=__file__))
    import sys
    from PySide2.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = Form2(parent=None)
    window.show()
    sys.exit(app.exec_())
