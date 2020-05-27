#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
使用面向对象的方式
"""

import os
import sys

from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMenu
from PyQt5.QtGui import QPixmap, QCursor

current_dir = os.path.dirname(__file__)
icon_path = os.path.join(current_dir, '../assets/favicon.png')


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口的位置和大小
        self.setGeometry(300, 300, 300, 220)
        # 设置窗口的标题
        self.setWindowTitle('我是标题')
        self.setWindowIcon(QIcon(icon_path))

        btn = QPushButton(self)

        btn.move(20, 20)

        pixmap = QIcon(icon_path)
        btn.setIcon(pixmap)
        btn.setIconSize(QtCore.QSize(48, 48))

        btn.setStyleSheet("""
                  border: 0px;
                  background: gray;
              """)

        # 往按钮上增加菜单
        # menu = QMenu()
        # menu.addAction('This is Action 1', lambda: print(1))
        # menu.addAction('This is Action 2', lambda: print(2))
        # btn.setMenu(menu)

        # 显示窗口
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(icon_path))  # MAC 下 程序图标是显示在程序坞中的， 切记
    example = Example()
    sys.exit(app.exec_())
