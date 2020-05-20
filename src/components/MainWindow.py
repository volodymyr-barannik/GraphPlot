from PyQt5.QtWidgets import QMainWindow

from src.functionality.MainWindowFunctions import mainWindowFunctions
from src.gui.GUIMainWindow import UI_MainWindow


class mainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.gui = UI_MainWindow()
        self.gui.init_ui(self)
        self.main_window_functions = mainWindowFunctions(self)

        # gui bindings
        self.gui.buttonQuit.clicked.connect(self.main_window_functions.quit)
        self.gui.buttonPlot.clicked.connect(self.main_window_functions.plot_spiral)
        self.gui.buttonSave.clicked.connect(self.main_window_functions.file_save)