#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
使用面向对象的方式
"""

import os
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget

current_dir = os.path.dirname(__file__)
icon_path = os.path.join(current_dir, '../assets/favicon.png')


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口的位置和大小
        # setGeometry()有两个作用：把窗口放到屏幕上并且设置窗口大小。参数分别代表屏幕坐标的x、y和窗口大小的宽、高。也就是说这个方法是resize()和move()的合体。
        self.setGeometry(300, 300, 300, 220)
        # 设置窗口的标题
        self.setWindowTitle('Icon')
        # 设置icon，我感觉这个设置只有在window下有效
        self.setWindowIcon(QIcon(icon_path))
        # 显示窗口
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(icon_path))  # MAC 下 程序图标是显示在程序坞中的， 切记
    example = Example()
    sys.exit(app.exec_())
