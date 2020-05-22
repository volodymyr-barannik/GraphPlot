#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys

from PyQt5 import QtWidgets
import PyQt5
import os
import sys

from PyQt5.QtWidgets import QApplication

import src.components.MainWindow


if __name__ == '__main__':
    # for Windows
    pyqt = os.path.dirname(PyQt5.__file__)
    QtWidgets.QApplication.addLibraryPath(os.path.join(pyqt, "Qt", "plugins"))

    app = QApplication(sys.argv)

    mainWindowObject = src.components.MainWindow.mainWindow()
    mainWindowObject.show()

    sys.exit(app.exec_())
