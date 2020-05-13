import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from tests.like_me_learn.ui_main_window import MainWindow


def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.showMaximized()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
