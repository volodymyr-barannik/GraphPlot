from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout
from matplotlib.backends.backend_template import FigureCanvas

from src.functionality.MainWindowFunctions import mainWindowFunctions
from src.gui.GUIRoot import UI_MainWindow
from src.functionality import MainWindowFunctions
import src.components.PlotWindow
import numpy as np
import matplotlib.pyplot as plt
from src.components.PlotWindow import windowPlot


class mainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.gui = UI_MainWindow()
        self.gui.initUI(self)
        self.root_functions = mainWindowFunctions(self)

        # bindings
        self.gui.buttonQuit.clicked.connect(self.root_functions.quit)
        # self.gui.boxWindowPlotParameterA.editingFinished.connect(self.gui.drawWindowPlot(a=self.gui.boxWindowPlotParameterA.value(),
        # b=0.01, parent=self))
        self.gui.boxPlotParameterA.valueChanged.connect(self.root_functions.drawWindowPlot)
