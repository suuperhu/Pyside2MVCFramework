# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
                            QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
                           QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(640, 480)
        # 设置Form的布局
        self.formLayout = QVBoxLayout(Form)
        self.formLayout.setObjectName(u"formLayout")

        # 创建一个frame1并设置布局
        self.frame1 = QFrame(Form)
        self.frame1.setObjectName(u"frame1")
        self.frame1.setStyleSheet(u"background-color: rgb(85, 255, 0);")
        self.frame1.setFrameShape(QFrame.StyledPanel)
        self.frame1.setFrameShadow(QFrame.Raised)
        self.frame1Layout = QHBoxLayout(self.frame1)
        self.frame1Layout.setObjectName(u"frame1Layout")

        # 向fram1的布局中添加控件
        self.pushButton = QPushButton(self.frame1)
        self.pushButton.setObjectName(u"pushButton")
        self.frame1Layout.addWidget(self.pushButton)
        self.pushButton_2 = QPushButton(self.frame1)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.frame1Layout.addWidget(self.pushButton_2)

        # 创建一个frame2
        self.frame2 = QFrame(Form)
        self.frame2.setObjectName(u"frame2")
        self.frame2.setStyleSheet(u"background-color: rgb(255, 170, 255);")
        self.frame2.setFrameShape(QFrame.StyledPanel)
        self.frame2.setFrameShadow(QFrame.Raised)

        # 将frame1和frame2添加到form布局中
        self.formLayout.addWidget(self.frame1)
        self.formLayout.addWidget(self.frame2)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"PushButton", None))
    # retranslateUi
