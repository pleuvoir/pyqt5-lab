import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QApplication, QLabel, QWidget


"""
划过超链接会触发下面的事件
"""

class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label2 = QLabel(self)
        label4 = QLabel(self)

        label2.setText("<a href='#'>欢迎使用Python  GUI程序</a>")

        # 如果设为True，用浏览器打开网页，如果设为False，调用槽函数
        label4.setOpenExternalLinks(True)

        label4.setText("<a href='https://item.jd.com/12417265.html'>感谢关注《Python从菜鸟到高手》</a>")

        label4.setAlignment(Qt.AlignRight)

        label4.setToolTip('这是一个超级链接')

        vbox = QVBoxLayout()

        vbox.addWidget(label2)
        vbox.addWidget(label4)

        label2.linkHovered.connect(self.linkHovered)

        label4.linkActivated.connect(self.linkClicked)

        self.setLayout(vbox)
        self.setWindowTitle('QLabel控件演示')

    def linkHovered(self):
        print('当鼠标滑过label2标签时，触发事件')

    def linkClicked(self):
        print('当鼠标单击label4标签时，触发事件')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLabelDemo()
    main.show()
    sys.exit(app.exec_())
