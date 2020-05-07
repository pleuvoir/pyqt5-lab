
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.statusBar()
        menubar = self.menuBar()
        menubar.setStatusTip("选中菜单栏进行操作")
        fileMenu = menubar.addMenu('&文件')
        importMenu = menubar.addMenu('&导入')

        exitAct = QAction(QIcon('favicon.png'), '&退出', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('退出啊')
        exitAct.triggered.connect(qApp.quit)
        fileMenu.addAction(exitAct)
        exitAct2 = QAction(QIcon('favicon.png'), '&退出2', self)
        fileMenu.addAction(exitAct2)

        importAct1 = QAction(QIcon('favicon.png'), '&导入1', self)
        importAct2 = QAction(QIcon('favicon.png'), '&导入2', self)
        importMenu.addAction(importAct1)
        importMenu.addAction(importAct2)



        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Simple menu')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())