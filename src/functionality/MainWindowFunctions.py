from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QMainWindow
from src.components.PlotWindow import windowPlot
import src.Run


class mainWindowFunctions(object):
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow

    def quit(self):
        print("END")
        QCoreApplication.quit()

    def drawWindowPlot(self):
        print("inside MainWindowFunctions.drawWindowPlot()")
        self.mainWindow.gui.drawWindowPlot()
        print(self.mainWindow.gui.boxPlotParameterA.value())
        self.mainWindow.gui.windowPlotObject.plot(a=1, b=self.mainWindow.gui.boxPlotParameterA.value())
        self.mainWindow.gui.windowPlotObject.show()
