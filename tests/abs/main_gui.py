import sys

from PyQt5.QtWidgets import QApplication

from tests.abs.base_ import BaseGUI

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = BaseGUI()  # 一定要用变量接收，否则不会出现窗口，坑啊
    sys.exit(app.exec_())
    