#!/usr/local/bin python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import QSize, QUrl
from PyQt5.QtWidgets import QMainWindow, QToolBar, QAction, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView

import os

class MainWindow(QMainWindow):
    homePath = os.path.abspath('page/index.html').replace("\\", '/')
    homeUrl = 'file:///%s' % homePath
    honorUrl = 'https://rhodesworkers.ltd/honor/'
    storyUrl = 'https://rhodesworkers.ltd/story'
    button_style = '''
QPushButton{border:2px solid #F3F3F5;
        border-radius:7px;
        color:black;
        background:darkGrey;}
        QPushButton:hover{color:white;
                    border:2px solid #F3F3F5;
                    border-radius:7px;
                    background:darkGray;}
}
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 设置窗口标题
        self.setWindowTitle('Rhodes no Workers Desktop')
        # 设置窗口图标
        self.setWindowIcon(QIcon('src/favicon.png'))

        # 设置浏览器
        self.browser = QWebEngineView()

        # 添加导航栏
        navigation_bar = QToolBar('Navigation')
        # 设定图标的大小
        navigation_bar.setIconSize(QSize(20, 20))
        self.addToolBar(navigation_bar)

        # 添加前进、后退、停止加载和刷新的按钮
        back_button = QAction(QIcon('src/back.png'), 'Back', self)
        next_button = QAction(QIcon('src/forward.png'), 'Forward', self)
        stop_button = QAction(QIcon('src/stop.png'), 'Stop', self)
        reload_button = QAction(QIcon('src/reload.png'), 'Reload', self)

        home_button = QPushButton('  HomePage  ', self)
        honor_button = QPushButton('  ArkHonor  ', self)
        honor_button.setStyleSheet("QPushButton{background: lightpink;}")
        story_button = QPushButton('  ArkStory  ', self)
        story_button.setStyleSheet("QPushButton{background: lightblue;}")

        back_button.triggered.connect(self.browser.back)
        next_button.triggered.connect(self.browser.forward)
        stop_button.triggered.connect(self.browser.stop)
        reload_button.triggered.connect(self.browser.reload)

        home_button.clicked.connect(self.homeClick)
        honor_button.clicked.connect(self.honorClick)
        story_button.clicked.connect(self.storyClick)

        # 将按钮添加到导航栏上
        navigation_bar.addAction(back_button)
        navigation_bar.addAction(next_button)
        navigation_bar.addAction(stop_button)
        navigation_bar.addAction(reload_button)

        navigation_bar.addSeparator()

        navigation_bar.addWidget(home_button)
        navigation_bar.addWidget(honor_button)
        navigation_bar.addWidget(story_button)

        # 指定打开界面的 URL
        self.browser.setUrl(QUrl(self.homeUrl))
         # 添加浏览器到窗口中
        self.setCentralWidget(self.browser)
        self.setStyleSheet(self.button_style)

    def homeClick(self):
        self.browser.setUrl(QUrl(self.homeUrl))

    def honorClick(self):
        self.browser.setUrl(QUrl(self.honorUrl))

    def storyClick(self):
        self.browser.setUrl(QUrl(self.storyUrl))