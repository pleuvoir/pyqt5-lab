#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from PyQt5.QtWidgets import QHBoxLayout, QApplication, QWidget, QLabel, QTextEdit, QPushButton, QMessageBox, \
    QTextBrowser


class Demo(QWidget):

    def __init__(self):
        super().__init__()
        self.edit = QTextEdit(self)
        self.edit.setPlaceholderText('请输入文字')
        self.edit.textChanged.connect(lambda: self.sync_slot(self.edit.toPlainText()))

        self.browser = QTextBrowser(self)

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.edit)
        self.h_layout.addWidget(self.browser)

        self.setLayout(self.h_layout)

    def sync_slot(self, text: str):
        self.browser.setText(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
