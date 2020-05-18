#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from PyQt5.QtWidgets import QHBoxLayout, QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QFormLayout


class Demo(QWidget):

    def __init__(self):
        super().__init__()

        self.user_label = QLabel('username_copy', self)

        self.f_layout = QFormLayout()
        self.f_layout.addRow(self.user_label, QLineEdit(self))
        self.f_layout.addRow('username', QLineEdit(self))
        self.f_layout.addRow('password', QLineEdit(self))

        self.v = QVBoxLayout()
        self.v.addLayout(self.f_layout)  # 注意这里是 addLayout 不是 addWidget

        self.setLayout(self.v)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
