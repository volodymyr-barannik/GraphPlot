from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QFileDialog


class mainWindowFunctions(object):
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow


    def quit(self):
        print("END")
        QCoreApplication.quit()


    def plot_spiral(self):
        arg_a_text = self.mainWindow.gui.lineA.text().replace(",", ".")
        arg_a = float(arg_a_text) if arg_a_text else 0

        arg_b_text = self.mainWindow.gui.lineB.text().replace(",", ".")
        arg_b = float(arg_b_text) if arg_b_text else 0

        arg_precision_text = self.mainWindow.gui.lineStep.text().replace(",", ".")
        arg_precision = float(arg_precision_text) if arg_precision_text else 0

        self.mainWindow.gui.windowPlotObject.plot_spiral(a=arg_a, b=arg_b, precision=arg_precision)
        self.mainWindow.gui.windowPlotObject.draw()


    def file_save(self):
        file_choices = "PNG *.png"

        path, ext = QFileDialog.getSaveFileName(self.mainWindow, 'Save file', '', file_choices)
        if not path[-4:] == file_choices[-4:]:
            path += file_choices[-4:]

        if path:
            self.mainWindow.gui.windowPlotObject.fig.savefig(path, dpi=None, facecolor='w', edgecolor='b',
                                                             orientation='portrait', papertype=None, format=None,
                                                             transparent=False, bbox_inches=None, pad_inches=0.1,
                                                             metadata=None)
