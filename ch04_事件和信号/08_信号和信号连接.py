#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from PyQt5.QtWidgets import QVBoxLayout, QApplication, QWidget, QLabel, QLineEdit, QPushButton


class Demo(QWidget):

    def __init__(self):
        super().__init__()
        self.user_label = QLabel('原始名称', self)
        self.btn = QPushButton('点击改变名称', self)

        self.btn.pressed.connect(self.btn.released)  # 类似于 当触发了 pressed 就是触发了 released
        self.btn.released.connect(lambda: self.text_change_slot('released'))

        self.h_layout = QVBoxLayout()
        self.h_layout.addWidget(self.user_label)
        self.h_layout.addWidget(self.btn)

        self.setLayout(self.h_layout)

    def text_change_slot(self, text: str):
        sender = self.sender()
        print(sender, text) # sender.text()  可以取到按钮的名称
        self.user_label.setText(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
