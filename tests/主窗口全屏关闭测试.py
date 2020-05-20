import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

      #  QApplication.setQuitOnLastWindowClosed(True)  # 最后一个窗口点击关闭后不退出程序
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')
        self.show()

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        print(event)

        self.hide()
        event.ignore()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
