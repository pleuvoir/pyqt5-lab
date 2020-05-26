#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
使用面向对象的方式
"""

import os
import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QDesktopWidget

current_dir = os.path.dirname(__file__)
icon_path = os.path.join(current_dir, '../assets/favicon.png')


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置窗口的位置和大小
        self.setGeometry(300, 300, 300, 220)
        # 设置窗口的标题
        self.setWindowTitle('我是标题')

        self.center() #居中
        # 设置icon，我感觉这个设置只有在window下有小
        self.setWindowIcon(QIcon(icon_path))
        # 这种静态的方法设置一个用于显示工具提示的字体。我们使用10px滑体字体。
        #  QToolTip.setFont(QFont('SansSerif', 10))
        # 创建一个PushButton并为他设置一个tooltip，移动上去有提示
        btn = QPushButton('我是一个按钮', self)
        btn.setToolTip('这是<b>QPushButton</b> widget')
        # btn.sizeHint()显示默认尺寸
        btn.resize(btn.sizeHint())

        # 关闭按钮
        qbtn = QPushButton('关闭', self)
        print('默认尺寸，',qbtn.sizeHint())
        qbtn.clicked.connect(QCoreApplication.instance().quit) #绑定事件
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)
        # 显示窗口
        self.show()

    def center(self):
        qr = self.frameGeometry() #获得主窗口所在的框架 并做一个虚拟的和目前一样的窗体
        print('qr1',qr)
        cp = QDesktopWidget().availableGeometry().center() #获取显示器的分辨率，然后得到屏幕中间点的位置
        print('cp',cp)
        qr.moveCenter(cp)   # 将虚拟的移动过去
        print('qr2',qr)
        print('topLeft',qr.topLeft())
        self.move(qr.topLeft()) #然后通过move函数把主窗口的左上角移动到虚拟框架的左上角，这样就把窗口居中了
        print('self',self.frameGeometry())

    def closeEvent(self, event):
        print('closeEvent trigger..')
        """
        重写关闭事件，点击X时回调此方法
        """
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(icon_path))  # MAC 下 程序图标是显示在程序坞中的， 切记
    example = Example()
    sys.exit(app.exec_())
