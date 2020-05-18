#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import QApplication
import src.components.MainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainWindowObject = src.components.MainWindow.mainWindow()
    mainWindowObject.show()

    sys.exit(app.exec_())
