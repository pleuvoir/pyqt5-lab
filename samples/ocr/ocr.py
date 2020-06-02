#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
import base64

import requests

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
    return '\n'.join([item['words'] for item in words_result])


class Button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setAcceptDrops(True)

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
                print(ocr(img_bytes))


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        button = Button("", self)
        button.resize(200, 200)
        button.move(0, 0)

        self.label = QLabel(self)
        self.label.move(150, 150)

        self.setWindowTitle('Simple drag & drop')
        self.setGeometry(300, 300, 300, 300)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()
