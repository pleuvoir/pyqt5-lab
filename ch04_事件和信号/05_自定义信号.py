#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox


class CloseAppSignal(QObject):
    signal_ins = pyqtSignal()


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.cs = CloseAppSignal()
        self.cs.signal_ins.connect(super().close)  # 将这个信息绑定到关闭事件上
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit signal')
        self.show()

    # 当点击鼠标时
    def mousePressEvent(self, event):
        print('mousePressEvent ..')
        # QMessageBox.about(self,'鼠标','你点鼠标了吧！')

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()  # 这一步其实没用还是写上，保证鼠标点击事件的传递连续性
            self.cs.signal_ins.emit()  # 提交这个信号，找到上面connect的 close 事件上，结果就是关闭了
        else:
            event.ignore()

    # 上面的close事件又会触发这里的事件，为了演示效果再次confirm下
    def closeEvent(self, event):
        print('closeEvent trigger..')
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
