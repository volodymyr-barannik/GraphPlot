from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QToolTip, QPushButton, QSpinBox

from src.Constants import WINDOW_WIDTH, SCREEN_WIDTH, WINDOW_HEIGHT, SCREEN_HEIGHT, PLOTWINDOW_WIDTH, PLOTWINDOW_HEIGHT
from src.components.PlotWindow import windowPlot


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

        self.boxPlotParameterA = QSpinBox(MainWindow)
        self.boxPlotParameterA.resize(self.boxPlotParameterA.sizeHint())
        self.boxPlotParameterA.setSingleStep(0.05)
        self.boxPlotParameterA.move(int(3 * WINDOW_WIDTH / 4 - self.boxPlotParameterA.width() / 2),
                                    int(3 * WINDOW_HEIGHT / 4 - self.boxPlotParameterA.height() / 2))

        self.windowPlotObject = windowPlot(parent=MainWindow)
        self.windowPlotObject.move(0, 0)
        self.windowPlotObject.resize(PLOTWINDOW_WIDTH, PLOTWINDOW_HEIGHT)

    def drawWindowPlot(self):
        del self.windowPlotObject
        self.windowPlotObject = windowPlot(parent=self.q)
        self.windowPlotObject.move(0, 0)
        self.windowPlotObject.resize(PLOTWINDOW_WIDTH, PLOTWINDOW_HEIGHT)