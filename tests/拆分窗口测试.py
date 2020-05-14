import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QSplitter, QListView, QTreeView, QTableView, QDirModel, QLabel
from qtpy import QtWidgets


class Demo(QSplitter):  # 1
    def __init__(self):
        super(Demo, self).__init__()

        self.setGeometry(300, 300, 1000, 1000)

        self.title = QLabel('Title')

        self.catalog_widget = QtWidgets.QWidget()
        self.catalog_widget.setWindowTitle('catalog_widget')
        self.btn = QtWidgets.QPushButton('我是一个按钮', self.catalog_widget)
        self.btn.setToolTip('这是<b>QPushButton</b> widget')

        self.catalog_widget2 = QtWidgets.QWidget()
        self.catalog_widget2.setWindowTitle('catalog_widget2')
        self.btn2 = QtWidgets.QPushButton('我是一个按钮2', self.catalog_widget2)
        self.btn2.setToolTip('这是<b>QPushButton2</b> widget')

        # self.setOrientation(Qt.Vertical)                      # 5 设置拆分方向，设置此属性则为上下几行的效果，默认是从左往右
        self.addWidget(self.catalog_widget)
        self.addWidget(self.catalog_widget2)
        self.addWidget(self.title)
        # self.insertWidget(0, self.table_view)
        self.setSizes([1000, 2000])

    def initUI(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
