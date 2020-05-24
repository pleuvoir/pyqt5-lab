import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication, QWidget, QPushButton, QDialog, QVBoxLayout, \
    QLabel, QLineEdit
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.dialog = Dialog()
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')

        btn = QPushButton('点我弹框', self)
        btn.clicked.connect(lambda: self.showDialog())

        self.show()

    def showDialog(self):
        print('showDialog')
        self.dialog.show()
        self.dialog.exec()


class Dialog(QDialog):
    """
    对话框类
    """

    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)

        # 设置对话框的标题及大小
        self.setWindowTitle('对话框')
        self.resize(810, 474)

        layout = QVBoxLayout()

        layout.addWidget(QLabel('名称',self))
        layout.addWidget(QLineEdit(self))

        self.setLayout(layout)

        # 设置窗口为模态，用户只有关闭弹窗后，才能关闭主界面
        self.setWindowModality(Qt.ApplicationModal)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
