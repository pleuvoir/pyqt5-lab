#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from PyQt5.QtWidgets import QVBoxLayout, QApplication, QWidget, QLabel, QLineEdit


class Demo(QWidget):

    def __init__(self):
        super().__init__()
        self.user_label = QLabel('username', self)
        self.pwd_label = QLabel('password', self)

        self.h_layout = QVBoxLayout()
        self.h_layout.addWidget(self.user_label)
        self.h_layout.addWidget(self.pwd_label)

        self.setLayout(self.h_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
