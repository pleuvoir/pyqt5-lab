#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        grid.setSpacing(10)

        x = 0
        y = 0

        self.text = "x: {0},  y: {1}".format(x, y)

        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)  # 还可以设置位置
        self.setWindowOpacity(0.8)  # 设置窗体透明

        self.setMouseTracking(True)  # 开启鼠标轨迹跟踪

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Event object')
        self.showMaximized()
        self.show()

    # 鼠标移动事件
    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()

        text = "x: {0},  y: {1}".format(x, y)
        self.label.setText(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
