from qtpy import QtWidgets, QtGui, QtCore


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        # 1. set up gui windows
        self.setGeometry(50, 50, 850, 650)
        self.setWindowTitle('Learn like me')
        self.setWindowIcon(QtGui.QIcon("source/gui/image/star.png"))
        self.init_menu()
        self.init_status_bar()
        self.init_central_area()

    def init_menu(self):
        """
        初始化菜单
        """
        menubar = self.menuBar()

        # 文件
        sysMenu = menubar.addMenu('File')

        sysMenu.addSeparator()  # 分隔符

        # 退出
        sysMenu.addSeparator()
        sys_exitAction = QtWidgets.QAction('Exit', self)
        sys_exitAction.setShortcut('Ctrl+Q')
        sys_exitAction.setStatusTip('Exit GUI')
        sys_exitAction.triggered.connect(self.close)
        sysMenu.addAction(sys_exitAction)

    def init_status_bar(self):
        pass

    def init_central_area(self):
        """
        初始化中心区域的视图，这里使用堆叠窗口来实现
        """

        self.central_widget = QtWidgets.QStackedWidget()

        # 最左侧的目录窗口
        catalog_widget = QtWidgets.QWidget()
        catalog_widget.setWindowTitle('catalog_widget')
        hbox1 = QtWidgets.QHBoxLayout()  # 水平布局

        second_catalog_widget = QtWidgets.QWidget()
        second_catalog_widget.setWindowTitle('second_catalog_widget')
        btn = QtWidgets.QPushButton('我是一个按钮', second_catalog_widget)
        btn.setToolTip('这是<b>QPushButton</b> widget')

        splitter1 = QtWidgets.QSplitter()
        splitter1.addWidget(catalog_widget)
        splitter1.addWidget(second_catalog_widget)
        splitter1.setSizes([500, 500])

        hbox1.addWidget(splitter1)


        self.central_widget.addWidget(catalog_widget)
        self.central_widget.setCurrentIndex(0)
        self.setCentralWidget(self.central_widget)
