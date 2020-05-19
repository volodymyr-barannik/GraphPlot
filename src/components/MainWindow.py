from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout
from matplotlib.backends.backend_template import FigureCanvas

from src.functionality.MainWindowFunctions import mainWindowFunctions
from src.gui.GUIMainWindow import UI_MainWindow
from src.functionality import MainWindowFunctions
import src.components.PlotWindow
import numpy as np
import matplotlib.pyplot as plt
from src.components.PlotWindow import windowPlot


class mainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.gui = UI_MainWindow()
        self.gui.init_ui(self)
        self.main_window_functions = mainWindowFunctions(self)

        # gui bindings
        self.gui.buttonQuit.clicked.connect(self.main_window_functions.quit)
        self.gui.buttonPlot.clicked.connect(self.main_window_functions.plot_spiral)
