# -*- coding: utf-8 -*-
"""
# @SoftwareIDE          : PyCharm2020Pro
# @ProjectName          : PySide2MVCFramework
# @FileName             : test_conf.py
# @Author               : 胡守杰
# @Email                : 2839414139@qq.com
# @ZhFileDescription    :
# @EnFileDescription    :
"""
from pyside2mvcframework.conf.global_settings import GLOBAL_QSS_PATH

if __name__ == '__main__':
    print("unit test from {filename}".format(filename=__file__))

    with open(GLOBAL_QSS_PATH, encoding="utf-8") as fp:
        content = " ".join(fp.read().split())
    test_str = """/* Pyside2MVCFramework global qss*/ * { font: normal bold 16px "微软雅黑"; margin: 5px; border: 1px dashed black; padding: 0px; spacing: 0px; text-align: center center; border-radius: 3px 5px; }"""
    assert content == test_str
