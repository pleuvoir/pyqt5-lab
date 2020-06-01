#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import time

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class CrawlWindow(QWidget):
    def __init__(self):
        super(CrawlWindow, self).__init__()
        self.resize(800, 600)
        self.setWindowTitle('猫眼Top100电影爬取软件')

        self.start_btn = QPushButton('go', self)
        self.start_btn.move(*(0,0))
        self.over_btn = QPushButton('over', self)
        self.over_btn.move(*(72,0))
        self.start_btn.clicked.connect(lambda: self.crawl_thread_start())
        self.over_btn.clicked.connect(lambda: self.crawl_thread_stop())

        self.crawl_thread = CrawlThread()  # 1
        self.crawl_thread_start()

    def crawl_thread_start(self):
        self.crawl_thread.start()

    def crawl_thread_stop(self):
        self.crawl_thread.terminate()


class CrawlThread(QThread):
    result_signal = pyqtSignal(str)

    def __init__(self):
        super(CrawlThread, self).__init__()
        self.result_signal.connect(self.set_table_slot)

    def set_table_slot(self, message):
        print(f'自定义信号{message}')

    def run(self):
        print('开始爬取！')
        time.sleep(5)
        print('全部爬取完毕！')

        self.result_signal.emit('呵呵')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CrawlWindow()
    window.show()
    sys.exit(app.exec_())
