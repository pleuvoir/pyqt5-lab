#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication)

"""
可参考 QT的相关介绍 https://blog.csdn.net/liang19890820/article/details/51537246
"""


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        hbox = QHBoxLayout()  # 将两个按钮添加到一个横着的布局中去 横着的
        hbox.addStretch(1)  # 最左边增加，布局会靠最右
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
      #  hbox.addStretch(1)  # 如果这里也增加的话，布局会居中

        vbox = QVBoxLayout()  # 垂直布局 竖着的
        vbox.addStretch(1)
        vbox.addLayout(hbox)  # 将刚才的水平布局加进来
        vbox.addStretch(1)

        self.setLayout(vbox)  # 最关键的一步

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
