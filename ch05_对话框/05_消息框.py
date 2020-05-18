#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QVBoxLayout


class Demo(QWidget):

    def __init__(self):
        super().__init__()
        self.msg_btn = QPushButton('消息', self)
        self.ask_btn = QPushButton('提问', self)
        self.cn_btn = QPushButton('中文消息框展示', self)

        self.msg_btn.clicked.connect(lambda: self.btn_slot(self.msg_btn))
        self.ask_btn.clicked.connect(lambda: self.btn_slot(self.ask_btn))
        self.cn_btn.clicked.connect(lambda: self.btn_slot(self.cn_btn))

        self.h_layout = QVBoxLayout()
        self.h_layout.addWidget(self.msg_btn)
        self.h_layout.addWidget(self.ask_btn)
        self.h_layout.addWidget(self.cn_btn)

        self.setLayout(self.h_layout)

        self.resize(1200, 850)

    def btn_slot(self, btn: QPushButton):
        if btn == self.ask_btn:
            print('ask_btn')
            ret = QMessageBox.question(self, 'Question', 'Dou you want save id ?',
                                       QMessageBox.Yes | QMessageBox.No)
            if ret == QMessageBox.Yes:
                print('saved')
                self.close()
            else:
                print('no close')

        elif btn == self.msg_btn:
            print('msg_btn')
            ret = QMessageBox.information(self, 'information', 'hello world',
                                          QMessageBox.Ok)
            if ret == QMessageBox.Ok:
                print('ok')
        else:
            print('cn_btn')
            cn_box = QMessageBox()
            cn_box.setWindowTitle('中文对话框')
            cn_box.setText('你看到我了')
            # cn_box.setIcon(QMessageBox.NoIcon)
            cn_box.setIcon(QMessageBox.Question)
            cn_box.addButton('确定', QMessageBox.YesRole)  # RET 0
            cn_box.addButton('不', QMessageBox.NoRole)  # RET 1  这个是按照增加的顺序来的，我不知道能不能修改返回值
            ret = cn_box.exec_()

            # 我们可以根据按钮的文本来判断他按了什么
            print(ret, cn_box.clickedButton().text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
