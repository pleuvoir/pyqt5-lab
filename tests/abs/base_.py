from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QAction, qApp
from qtpy import QtGui

from tests.abs.abstract_gui_builder import AbstractGUIBuilder


class BaseGUI(AbstractGUIBuilder):

    def __init__(self):
        super().__init__()

    def init_menu(self):
        menubar = self.q_main.menuBar()

        fileMenu = menubar.addMenu('&文件')

        exitAct = QAction(QIcon('favicon.png'), '&退出', self.q_main)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('退出')
        exitAct.triggered.connect(qApp.quit)

        fileMenu.addAction(exitAct)

    def init_status_bar(self):
        pass

    def init_central_area(self):
        pass
