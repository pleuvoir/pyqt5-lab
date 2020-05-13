#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, qApp, QAction, QDesktopWidget


class Example(QMainWindow):  # 继承主窗口

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        menubar = self.menuBar()  # 菜单栏
        about_menu = menubar.addMenu('&关于')

        # 退出
        exitAct = QAction(QIcon('../assets/exit.png'), '  &退出 Ctrl+Q', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)
        about_menu.addAction(exitAct)

        self.setWindowTitle('你又来学习了')
        self.resize(1200, 650)
        self.center()  # 居中

    def center(self):
        qr = self.frameGeometry()  # 获得主窗口所在的框架
        cp = QDesktopWidget().availableGeometry().center()  # 获取显示器的分辨率，然后得到屏幕中间点的位置
        qr.moveCenter(cp)  # 获取显示器的分辨率，然后得到屏幕中间点的位置
        self.move(qr.topLeft())  # 然后通过move函数把主窗口的左上角移动到其框架的左上角，这样就把窗口居中了


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('../assets/favicon.png'))
    example = Example()
    example.show()
    sys.exit(app.exec_())
