import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QScrollArea, QScrollBar, \
    QHBoxLayout, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.label = QLabel(self)                              # 1
        self.label.setPixmap(QPixmap('../assets/exit.png'))
        self.label.setScaledContents(True) #设置自适应变大

        self.scroll_area = QScrollArea(self)                   # 2
        self.scroll_area.setWidget(self.label)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff) #关闭横向

        self.bigger_btn = QPushButton('Zoom in', self)         # 4
        self.smaller_btn = QPushButton('Zoom out', self)

        self.bigger_btn.clicked.connect(self.bigger_func)      # 5

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.bigger_btn)
        self.h_layout.addWidget(self.smaller_btn)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.scroll_area)
        self.v_layout.addLayout(self.h_layout) #把按钮放在最下面

        self.setLayout(self.v_layout)

    def bigger_func(self):
        self.label.resize(self.label.width()*1.2, self.label.height()*1.2)

    def smaller_func(self):
        self.label.resize(self.label.width() * 0.8, self.label.height() * 0.8)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())