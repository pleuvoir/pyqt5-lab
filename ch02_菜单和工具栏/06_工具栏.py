import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon


"""
可以点右键 隐藏或者显示工具栏
"""

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        #exitAct = QAction('点我退出', self)

        # 用图片替换文字
        exitAct1 = QAction(QIcon('assets/favicon.png'), '点我退出', self)
        exitAct1.setShortcut('Ctrl+Q')
        exitAct1.triggered.connect(qApp.quit)

        exitAct2 = QAction('点我退出2', self)
        exitAct2.setShortcut('Ctrl+Q')
        exitAct2.triggered.connect(qApp.quit)

        self.toolbar = self.addToolBar('Exit Group')  #增加工具栏
        self.toolbar.addAction(exitAct1)
        self.toolbar.addAction(exitAct2)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Toolbar')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())