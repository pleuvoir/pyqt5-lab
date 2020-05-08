#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication)

"""
这种应该不常用
"""


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        hbox = QHBoxLayout()  # 将两个按钮添加到一个横着的布局中去
        hbox.addStretch(1)  # 弹性布局？我觉得这个就是为了把它左边填充下，把按钮挤到右边去
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()  # 垂直布局
        vbox.addStretch(1)
        vbox.addLayout(hbox)  # 将刚才的水平布局加进来

        self.setLayout(hbox)  # 最关键的一步

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
