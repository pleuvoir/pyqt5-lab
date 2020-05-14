import sys

from PyQt5 import QtWidgets

from tests.abs.base_ import BaseGUI

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    BaseGUI().build()
    sys.exit(app.exec_())
