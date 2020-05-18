#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from PyQt5.QtWidgets import QHBoxLayout, QApplication, QWidget, QLabel, QLineEdit


class Demo(QWidget):

    def __init__(self):
        super().__init__()
        self.user_label = QLabel('username', self)
        self.user_line = QLineEdit(self)

        self.h_layout = QHBoxLayout()  # 水平布局
        # self.h_layout.addStretch(1)  # 最左边增加，布局会靠右
        self.h_layout.addWidget(self.user_label)
        self.h_layout.addWidget(self.user_line)

        self.setLayout(self.h_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
