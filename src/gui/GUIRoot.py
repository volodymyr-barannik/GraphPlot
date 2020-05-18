from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QToolTip, QPushButton, QSpinBox, QSlider, QLineEdit, QLabel

from src.Constants import WINDOW_WIDTH, SCREEN_WIDTH, WINDOW_HEIGHT, SCREEN_HEIGHT, PLOTWINDOW_WIDTH, PLOTWINDOW_HEIGHT
from src.components.PlotWindow import windowPlot
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class UI_MainWindow(object):
    def initUI(self, MainWindow):
        self.q = MainWindow
        MainWindow.setGeometry(int(SCREEN_WIDTH / 2 - WINDOW_WIDTH / 2),
                               int(SCREEN_HEIGHT / 2 - WINDOW_HEIGHT / 2),
                               WINDOW_WIDTH, WINDOW_HEIGHT)
        MainWindow.setWindowTitle('Spiralus')
        MainWindow.setWindowIcon(QIcon('../../res/icon.png'))
        QToolTip.setFont(QFont('SansSerif', 8))

        # self.setToolTip('This is a <b>QWidget</b> widget')

        self.buttonQuit = QPushButton('Quit', MainWindow)
        self.buttonQuit.resize(self.buttonQuit.sizeHint())
        self.buttonQuit.setToolTip('Exit program with optional plot saving')
        self.buttonQuit.move(int(WINDOW_WIDTH / 2 - self.buttonQuit.width() / 2),
                             int(WINDOW_HEIGHT / 2 - self.buttonQuit.height() / 2))

        self.boxPlotArgA = QLineEdit(MainWindow)
        self.boxPlotArgA.setValidator(QDoubleValidator())
        self.boxPlotArgA.resize(self.boxPlotArgA.sizeHint())
        self.boxPlotArgA.move(int(1 * WINDOW_WIDTH / 4 - self.boxPlotArgA.width() / 2),
                              int(34.75 * WINDOW_HEIGHT / 38 - self.boxPlotArgA.height() / 2))

        self.labelPlotArgA = QLabel("a:", MainWindow)
        self.labelPlotArgA.resize(self.labelPlotArgA.sizeHint())
        self.labelPlotArgA.move(int(1 * WINDOW_WIDTH / 4 - 5*self.boxPlotArgA.width() / 8),
                              int(34.75 * WINDOW_HEIGHT / 38 - self.labelPlotArgA.height() / 2))

        self.boxPlotArgB = QLineEdit(MainWindow)
        self.boxPlotArgB.setValidator(QDoubleValidator())
        self.boxPlotArgB.resize(self.boxPlotArgB.sizeHint())
        self.boxPlotArgB.move(int(2 * WINDOW_WIDTH / 4 - self.boxPlotArgB.width() / 2),
                              int(34.75 * WINDOW_HEIGHT / 38 - self.boxPlotArgB.height() / 2))

        self.labelPlotArgB = QLabel("b:", MainWindow)
        self.labelPlotArgB.resize(self.labelPlotArgB.sizeHint())
        self.labelPlotArgB.move(int(2 * WINDOW_WIDTH / 4 - 5*self.boxPlotArgB.width() / 8),
                                int(34.75 * WINDOW_HEIGHT / 38 - self.labelPlotArgB.height() / 2))

        self.boxPlotArgPrecision = QLineEdit(MainWindow)
        self.boxPlotArgPrecision.setValidator(QDoubleValidator())
        self.boxPlotArgPrecision.resize(self.boxPlotArgPrecision.sizeHint())
        self.boxPlotArgPrecision.move(int(3 * WINDOW_WIDTH / 4 - self.boxPlotArgPrecision.width() / 2),
                              int(34.75 * WINDOW_HEIGHT / 38 - self.boxPlotArgPrecision.height() / 2))

        self.labelPlotArgPrecision = QLabel("precis:", MainWindow)
        self.labelPlotArgPrecision.resize(self.labelPlotArgPrecision.sizeHint())
        self.labelPlotArgPrecision.move(int(3 * WINDOW_WIDTH / 4 - 13*self.boxPlotArgPrecision.width()/16),
                                int(34.75 * WINDOW_HEIGHT / 38 - self.labelPlotArgPrecision.height() / 2))

        self.buttonPlot = QPushButton('Plot', MainWindow)
        self.buttonPlot.resize(self.buttonPlot.sizeHint().width()*4, self.buttonPlot.sizeHint().height())
        self.buttonPlot.setToolTip('Plots a graph if you enter all three parameters')
        self.buttonPlot.move(int(2 * WINDOW_WIDTH / 4 - self.buttonPlot.width() / 2),
                                        int(18.25 * WINDOW_HEIGHT / 19 - self.buttonPlot.height() / 2))

        self.windowPlotObject = windowPlot(parent=MainWindow)
        self.windowPlotObject.move(0, 0)
        self.windowPlotObject.resize(PLOTWINDOW_WIDTH, PLOTWINDOW_HEIGHT)

    def drawWindowPlot(self):
        del self.windowPlotObject
        self.windowPlotObject = windowPlot(parent=self.q)
        self.windowPlotObject.move(0, 0)
        self.windowPlotObject.resize(PLOTWINDOW_WIDTH, PLOTWINDOW_HEIGHT)