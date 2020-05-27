#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QMainWindow, QApplication

"""
pip3 install PyQtWebEngine
"""


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('加载外部网页的例子')
        self.setGeometry(5, 30, 1355, 730)
        self.browser = QWebEngineView()
        # 加载外部的web界面
        self.browser.load(QUrl('https://github.com/pleuvoir'))
        self.setCentralWidget(self.browser)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exit(app.exec_())
