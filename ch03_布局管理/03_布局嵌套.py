#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from PyQt5.QtWidgets import QHBoxLayout, QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout


class Demo(QWidget):

    def __init__(self):
        super().__init__()
        self.user_label = QLabel('username:', self)
        self.user_line = QLineEdit(self)

        self.pwd_label = QLabel('password:', self)
        self.pwd_line = QLineEdit(self)

        self.h1 = QHBoxLayout()  # 水平布局
        self.h1.addWidget(self.user_label)
        self.h1.addWidget(self.user_line)

        self.h2 = QHBoxLayout()  # 水平布局
        self.h2.addWidget(self.pwd_label)
        self.h2.addWidget(self.pwd_line)

        self.v = QVBoxLayout()
        self.v.addLayout(self.h1)  # 注意这里是 addLayout 不是 addWidget
        self.v.addLayout(self.h2)

        self.setLayout(self.v)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
