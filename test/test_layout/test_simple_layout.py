# -*- coding: utf-8 -*-
"""
# @SoftwareIDE          : PyCharm2020Pro
# @ProjectName          : PySide2MVCFramework
# @FileName             : test_simple_layout.py
# @Author               : 胡守杰
# @Email                : 2839414139@qq.com
# @ZhFileDescription    :
# @EnFileDescription    :
"""

from PySide2.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLayoutItem, QFrame
from PySide2.QtCore import Qt


class TestLayoutWidget(QWidget):
    def __init__(self, parant=None):
        super().__init__(parent=parant)
        self.setupUI()

    def setupUI(self):
        btn1 = QPushButton(parent=self)
        btn1.setObjectName("btn1")
        btn1.setText("btn1")
        btn1.move(0, 0)
        btn2 = QPushButton(parent=self)
        btn2.setObjectName("btn2")
        btn2.setText("btn2")
        btn2.move(30, 30)
        btnsLayout = QHBoxLayout(self)
        btnsLayout.addWidget(btn2)
        btnsLayout.addWidget(btn1)

        frameWidget = QFrame(parent=self)
        frameWidget.setObjectName("frameWidget")
        frameLayout = QHBoxLayout(parent=self)
        frameLayout.addWidget(frameWidget)
        frameLayout.addLayout(btnsLayout)

        # QLayoutItem()
        # btnsLayout.addItem(btn1)
        # btnsLayout.addItem(btn2)

        self.setObjectName("mywidget")
        self.setWindowTitle("test simple layout")
        widgetLayout = QVBoxLayout(self)
        widgetLayout.addLayout(btnsLayout)


if __name__ == '__main__':
    print("unit test from {filename}".format(filename=__file__))
    import sys

    app = QApplication(sys.argv)
    window = TestLayoutWidget(parant=None)
    window.show()
    sys.exit(app.exec_())
