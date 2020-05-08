#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtCore import QCoreApplication, pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton("Button 1", self)
        btn1.move(30, 50)

        btn2 = QPushButton("Button 2", self)
        btn2.move(150, 50)

      #  self.statusBar().showMessage('Ready 1')
        self.statusBar()
        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()


    def buttonClicked(self):
        print('buttonClicked..')
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')  # 不起作用我也不知道为啥


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
