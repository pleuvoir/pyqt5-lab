#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import sys

import qdarkstyle
from PyQt5 import QtCore
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

current_dir = os.path.dirname(__file__)
icon_path = os.path.join(current_dir, '../assets/favicon.png')

"""
所以采用自定义信号的方式来实现
"""


class CloseAppSignal(QObject):
    signal_ins = pyqtSignal()


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('我是标题')
        qbtn = QPushButton('关闭', self)
    #    qbtn.clicked.connect(self.close)  # 绑定事件
        qbtn.clicked.connect(self.closeFunc)  # 绑定事件

        # 将这个信号绑定到关闭事件上
        self.cs = CloseAppSignal()
        self.cs.signal_ins.connect(self.close)

        qbtn.move(50, 50)
        self.showFullScreen()
        self.show()

    def closeFunc(self):
        print('closeFunc')

        # QCoreApplication.instance().quit 这个不行
        # qApp.quit()   #这个可以关闭，但是不会触发closeEvent事件

        self.cs.signal_ins.emit()

    def closeEvent(self, event):
        print('closeEvent trigger..event=QCloseEvent', event)
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(icon_path))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    example = Example()
    sys.exit(app.exec_())
