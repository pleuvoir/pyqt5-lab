#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64
import os
import sys

import qdarkstyle
import requests
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QHBoxLayout, QApplication, QWidget, QTextBrowser, QDesktopWidget

AK = 'X0xlt5vmch3wGvHUbYZF2aTo'
SK = 'pA9H7w2hl0F3sUGK9KC5LN9bdmdhzztQ'


def get_token(ak, sk):
    url = 'https://aip.baidubce.com/oauth/2.0/token'
    params = {
        'grant_type': 'client_credentials',
        'client_id': ak,
        'client_secret': sk,
    }
    r = requests.post(url, params=params)
    return r.json()['access_token']


TOKEN = get_token(AK, SK)


def ocr(img_bytes):
    url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic'
    params = {'access_token': TOKEN}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    img = base64.b64encode(img_bytes)
    data = {'image': img}
    r = requests.post(url, data=data, params=params, headers=headers)
    words_result = r.json()['words_result']
    return '\n\n'.join([item['words'] for item in words_result])


class MainWidget(QWidget):

    def __init__(self):
        super(MainWidget, self).__init__()

        self.browser = QTextBrowser(self)
        self.browser.setPlaceholderText('请拖拽图片到此区域，可重复拖拽')

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.browser)

        self.setLayout(self.h_layout)

        self.resize(800, 600)
        self.setAcceptDrops(True)
        self.center()

    def dragEnterEvent(self, e):
        m = e.mimeData()
        if m.hasUrls():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        m = e.mimeData()
        if m.hasUrls():
            local_img_path = m.urls()[0].toLocalFile()
            with open(file=local_img_path, mode='rb') as img:
                img_bytes = img.read()
                self.browser.clear()
                self.browser.setText(ocr(img_bytes))

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    current_dir = os.path.dirname(__file__)
    icon_path = os.path.join(current_dir, '../../assets/favicon.png')

    app.setWindowIcon(QIcon(icon_path))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    main_widget = MainWidget()
    main_widget.show()
    sys.exit(app.exec_())
