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
        print(self.mainWindow.gui.boxPlotArgB.text())

        argAtext = self.mainWindow.gui.boxPlotArgA.text().replace(",", ".")
        argA = float(argAtext) if argAtext else 0

        argBtext = self.mainWindow.gui.boxPlotArgB.text().replace(",", ".")
        argB = float(argBtext) if argBtext else 0

        argPrecisiontext = self.mainWindow.gui.boxPlotArgPrecision.text().replace(",", ".")
        argPrecision = float(argPrecisiontext) if argPrecisiontext else 0

        self.mainWindow.gui.windowPlotObject.plotSpiral(a=argA, b=argB, precision = argPrecision)
        #self.mainWindow.gui.windowPlotObject.draw()
        self.mainWindow.gui.windowPlotObject.show()
