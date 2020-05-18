#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from PyQt5.QtWidgets import QHBoxLayout, QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QGridLayout, QPushButton


class Demo(QWidget):

    def __init__(self):
        super().__init__()

        self.grid_layout = QGridLayout()

        self.user_label = QLabel('username:', self)
        self.user_line = QLineEdit(self)

        self.pwd_label = QLabel('password:', self)
        self.pwd_line = QLineEdit(self)

        self.q_login_btn = QPushButton('Login in', self)
        self.q_sign_btn = QPushButton('Sign in', self)

        self.grid_layout.addWidget(self.user_label, 0, 0)
        self.grid_layout.addWidget(self.user_line, 0, 1)
        self.grid_layout.addWidget(self.pwd_label, 1, 0)
        self.grid_layout.addWidget(self.pwd_line, 1, 1)
        self.grid_layout.addWidget(self.q_login_btn, 2, 0)
        self.grid_layout.addWidget(self.q_sign_btn, 2, 1)

        self.setLayout(self.grid_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
