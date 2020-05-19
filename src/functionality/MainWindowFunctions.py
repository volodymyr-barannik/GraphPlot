from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QMainWindow
from src.components.PlotWindow import windowPlot
import src.Run
from decimal import *

class mainWindowFunctions(object):
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow

    def quit(self):
        print("END")
        QCoreApplication.quit()

    def plot_spiral(self):
        print("inside MainWindowFunctions.drawWindowPlot()")
        self.mainWindow.gui.update_plot_window()
        print(self.mainWindow.gui.boxPlotArgB.text())

        arg_a_text = self.mainWindow.gui.boxPlotArgA.text().replace(",", ".")
        arg_a = float(arg_a_text) if arg_a_text else 0

        arg_b_text = self.mainWindow.gui.boxPlotArgB.text().replace(",", ".")
        arg_b = float(arg_b_text) if arg_b_text else 0

        arg_precision_text = self.mainWindow.gui.boxPlotArgPrecision.text().replace(",", ".")
        arg_precision = float(arg_precision_text) if arg_precision_text else 0

        self.mainWindow.gui.windowPlotObject.plot_spiral(a=arg_a, b=arg_b, precision = arg_precision)
        #self.mainWindow.gui.windowPlotObject.draw()
        self.mainWindow.gui.windowPlotObject.show()
