#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import (QWidget, QGridLayout,
                             QApplication, QDesktopWidget, QPushButton)


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def center(self):
        qr = self.frameGeometry()  # 获得主窗口所在的框架
        cp = QDesktopWidget().availableGeometry().center()  # 获取显示器的分辨率，然后得到屏幕中间点的位置
        qr.moveCenter(cp)  # 获取显示器的分辨率，然后得到屏幕中间点的位置
        self.move(qr.topLeft())  # 然后通过move函数把主窗口的左上角移动到其框架的左上角，这样就把窗口居中了

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        # 构造一个三行
        btn = QPushButton("(0,0)")
        grid.addWidget(btn, *(0, 0))
        grid.addWidget(QPushButton("(0,1)"), *(0, 1))
        grid.addWidget(QPushButton("(1,0)"), *(1, 0))
        grid.addWidget(QPushButton("(1,1)"), *(1, 1))
        grid.addWidget(QPushButton("(1,2)"), *(1, 2))

        self.setWindowTitle('珊栏布局')
        self.resize(450, 150)
        self.center()
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
