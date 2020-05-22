from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QAction

from src.functionality.MainWindowFunctions import mainWindowFunctions
from src.gui.GUIMainWindow import UI_MainWindow


class mainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.gui = UI_MainWindow()
        self.gui.init_ui(self)
        self.main_window_functions = mainWindowFunctions(self)

        self.first_run = True

        if self.first_run:
            self.main_window_functions.show_statusbar_message(
                "Ця програма будує графік логарифмічної спіралі: r = a*e^(b*phi).", time=15)
            self.first_run = False

        # gui bindings
        self.gui.buttonQuit.clicked.connect(self.main_window_functions.quit)
        self.gui.buttonPlot.clicked.connect(self.main_window_functions.plot_spiral)
        self.gui.buttonSave.clicked.connect(self.main_window_functions.save_file)

        #shortcuts
        self.gui.shortcutSave.activated.connect(self.main_window_functions.save_file)

        # Menu actions
        self.gridAction = QAction('&Сітка', self)
        self.gridAction.setShortcut('Ctrl+G')
        self.gridAction.triggered.connect(self.main_window_functions.grid_toggle)
        self.gui.viewMenu.addAction(self.gridAction)

        self.dotsAction = QAction('&Показувати виколоті та зафарбовані точки', self)
        self.dotsAction.setShortcut('Ctrl+D')
        self.dotsAction.triggered.connect(self.main_window_functions.dots_toggle)
        self.gui.viewMenu.addAction(self.dotsAction)

        self.forceLastPoint = QAction('&Завжди будувати останню точку проміжка', self)
        self.forceLastPoint.setShortcut('Ctrl+F')
        self.forceLastPoint.triggered.connect(self.main_window_functions.force_last_point_toggle)
        self.gui.viewMenu.addAction(self.forceLastPoint)