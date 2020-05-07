
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        exitAct = QAction(QIcon('favicon.png'), '&退出', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('退出啊')
        exitAct.triggered.connect(qApp.quit)

        self.statusBar() #当移动到 退出按钮上会出现这个bar 退出啊

        menubar = self.menuBar()
        menubar.setStatusTip("选中菜单栏进行操作")

        fileMenu = menubar.addMenu('&文件')
        fileMenu.addAction(exitAct)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Simple menu')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())