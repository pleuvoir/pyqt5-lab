#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from PyQt5.QtWidgets import QVBoxLayout, QApplication, QWidget, QLabel, QTextEdit, QPushButton, QMessageBox, \
    QTextBrowser


class Demo(QWidget):

    def __init__(self):
        super().__init__()
        self.user_label = QLabel('username', self)
        self.text_edit = QTextEdit(self)
        self.text_edit.setPlainText('你好啊，我是原始的文本')
        self.text_edit.setPlaceholderText('请输入文字')
        self.text_edit.textChanged.connect(lambda: print('text changed.'))
        self.text_edit.setReadOnly(False)  # 设置为True后就和 QTextBrowser 一样了，只让看

        self.save_btn = QPushButton('保存', self)
        self.save_btn.clicked.connect(lambda: self.save_slot(self.save_btn))
        self.clear_btn = QPushButton('清空', self)
        self.clear_btn.clicked.connect(lambda: self.save_slot(self.clear_btn))

        self.h_layout = QVBoxLayout()
        self.h_layout.addWidget(self.user_label)
        self.h_layout.addWidget(self.text_edit)
        self.h_layout.addWidget(self.save_btn)
        self.h_layout.addWidget(self.clear_btn)

        self.setLayout(self.h_layout)

    def save_slot(self, btn: QPushButton):

        if btn == self.save_btn:
            with open('text_edit.txt', mode='a', encoding='utf-8') as f:
                print(self.text_edit.toPlainText(), end='\n', file=f)
            QMessageBox.information(self, 'information', '保存成功！', QMessageBox.Ok)
        else:
            self.text_edit.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
