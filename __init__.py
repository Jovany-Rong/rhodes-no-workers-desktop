#!/usr/local/bin python
# -*- coding: utf-8 -*-

import sys
import ctypes
import os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from app import MainWindow


#app start
if __name__ == '__main__':
    try:
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("RhodesNoWorkers")
    except:
        pass

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("src/favicon.png"))

    #splash = splashScreen.splashScreen()
    #splash.effect()

    app.processEvents()

    mainWin = MainWindow()
    mainWin.showMaximized()

    #splash.finish(mainWin)

    sys.exit(app.exec_())