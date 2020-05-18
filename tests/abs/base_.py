from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, qApp
from qtpy import QtGui

from tests.abs.abstract_gui_builder import AbstractGUIBuilder


class BaseGUI(AbstractGUIBuilder):

    def __init__(self):
        super().__init__()

    def init_window(self):
        self.setGeometry(50, 50, 850, 650)
        self.setWindowTitle('Learn like me')
        self.setWindowIcon(QtGui.QIcon('../../../assets/favicon.png'))
        self.showMaximized()

    def init_menu(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&文件')
        exitAct = QAction(QIcon('../../assets/exit.png'), '&退出', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('退出')
        exitAct.triggered.connect(qApp.quit)
        fileMenu.addAction(exitAct)
        print('init_menu')

    def init_status_bar(self):
        print('init_status_bar')

    def init_central_area(self):
        print('init_central_area')
