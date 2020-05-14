from abc import ABCMeta, abstractmethod

from PyQt5.QtWidgets import QMainWindow
from qtpy import QtGui


class AbstractGUIBuilder(metaclass=ABCMeta):

    def __init__(self):
        super().__init__()
        self.q_main = QMainWindow()

    def build(self):
        self.init_window()
        self.init_menu()
        self.init_status_bar()
        self.init_central_area()

        self.q_main.show() # 不能这样会一闪而过 可能需要继承的形式

    def init_window(self):
        # 1. 设置窗口
        self.q_main.setGeometry(50, 50, 850, 650)
        self.q_main.setWindowTitle('Learn like me')
        self.q_main.setWindowIcon(QtGui.QIcon('../../assets/1.gif'))
     #   self.q_main.showMaximized()

    @abstractmethod
    def init_menu(self):
        pass

    @abstractmethod
    def init_status_bar(self):
        pass

    @abstractmethod
    def init_central_area(self):
        pass
