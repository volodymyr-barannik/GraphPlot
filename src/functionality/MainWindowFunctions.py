from PyQt5.QtCore import QCoreApplication, QFileInfo, QPoint, QTimer
from PyQt5.QtWidgets import QFileDialog, QToolTip

from src.Constants import STATUSBAR_TEXT_COLOR, STATUSBAR_BACKGROUND_COLOR, STATUSBAR_ERROR_TEXT_COLOR, \
    STATUSBAR_MESSAGE_TIME, PLOT_WINDOW_BACKGROUND_COLOR


class mainWindowFunctions(object):
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow


    def quit(self):
        QCoreApplication.quit()


    def plot_spiral(self):
        arg_a_text = self.mainWindow.gui.lineA.text().replace(",", ".")
        if arg_a_text:
            if arg_a_text=="-":
                self.show_tooltip_message("Введіть, будь ласка, число", self.mainWindow.gui.lineA)
                self.show_statusbar_message("Помилка вводу", STATUSBAR_ERROR_TEXT_COLOR)
                return
            else:
                arg_a = float(arg_a_text)
        else:
            self.show_tooltip_message("Поле \"а\" не може бути пустим", self.mainWindow.gui.lineA)
            self.show_statusbar_message("Помилка вводу", STATUSBAR_ERROR_TEXT_COLOR)
            return

        if arg_a > 100000000:
            self.show_tooltip_message("Значення \"a\" занадто велике", self.mainWindow.gui.lineA)
            self.show_statusbar_message("Помилка вводу", STATUSBAR_ERROR_TEXT_COLOR)
            return

        arg_b_text = self.mainWindow.gui.lineB.text().replace(",", ".")
        if arg_b_text:
            if arg_b_text == "-":
                self.show_tooltip_message("Введіть, будь ласка, число", self.mainWindow.gui.lineB)
                self.show_statusbar_message("Помилка вводу", STATUSBAR_ERROR_TEXT_COLOR)
                return
            else:
                arg_b = float(arg_b_text)
        else:
            self.show_tooltip_message("Поле \"b\" не може бути пустим", self.mainWindow.gui.lineB)
            self.show_statusbar_message("Помилка вводу", STATUSBAR_ERROR_TEXT_COLOR)
            return

        if arg_b > 55:
            self.show_tooltip_message("Значення \"b\" занадто велике", self.mainWindow.gui.lineB)
            self.show_statusbar_message("Помилка вводу", STATUSBAR_ERROR_TEXT_COLOR)
            return

        arg_range = self.decode_range()

        if arg_range[0] > arg_range[1]:
            message = "Проміжок проінтерпретовано як: "
            actual_input = self.mainWindow.gui.lineRange.text()
            left_parentheses = '[' if arg_range[3] == True else '('
            right_parentheses = ']' if arg_range[2] == True else ')'
            actual_input = actual_input.replace(" ", "")
            actual_input = actual_input[1:-1].split(';')
            message = message + left_parentheses + actual_input[1] + "; " + actual_input[0] + right_parentheses
            self.show_statusbar_message(message)

            # Swap
            arg_range[0], arg_range[1], arg_range[2], arg_range[3] = arg_range[1], arg_range[0], arg_range[3], arg_range[2]

        if arg_range[0] < 0  or arg_range[1] > 4*3.14159265359:
            self.show_tooltip_message("Проміжок має бути підмножиною [0; 4pi]",
                                      self.mainWindow.gui.lineRange)
            self.show_statusbar_message("Помилка вводу", STATUSBAR_ERROR_TEXT_COLOR)
            return

        arg_step_text = self.mainWindow.gui.lineStep.text().replace(",", ".")
        if arg_step_text:
            arg_step = float(arg_step_text)
        else:
            self.show_tooltip_message("Поле \"Δφ\" не може бути пустим", self.mainWindow.gui.lineStep)
            self.show_statusbar_message("Помилка вводу", STATUSBAR_ERROR_TEXT_COLOR)
            return

        if arg_step <= 0:
            self.show_tooltip_message("Поле \"Δφ\" має бути додатним", self.mainWindow.gui.lineStep)
            self.show_statusbar_message("Помилка вводу", STATUSBAR_ERROR_TEXT_COLOR)
            return

        self.mainWindow.gui.windowPlotObject.plot_spiral(a=arg_a, b=arg_b,
                                                         range = arg_range, step=arg_step)
        self.mainWindow.gui.windowPlotObject.draw()
        self.show_statusbar_message("Графік побудовано")


    def save_file(self):
        file_choices = "PNG *.png"

        path, ext = QFileDialog.getSaveFileName(self.mainWindow, 'Save file', '', file_choices)
        if not QFileInfo(path).completeSuffix() == "":
            if not path[-4:] == file_choices[-4:]:
                path += file_choices[-4:]

        if path:
            self.mainWindow.gui.windowPlotObject.fig.savefig(path, dpi=1000, facecolor=PLOT_WINDOW_BACKGROUND_COLOR,
                                                             edgecolor=PLOT_WINDOW_BACKGROUND_COLOR,
                                                             orientation='portrait', papertype=None, format=None,
                                                             transparent=False, bbox_inches='tight', pad_inches=0.2,
                                                             metadata=None, figsize = (10, 10))


    def show_tooltip_message(self, message, gui_object, text_color = STATUSBAR_TEXT_COLOR,
                               background_color = STATUSBAR_BACKGROUND_COLOR):
        actual_tooltip = gui_object.toolTip()
        QToolTip.showText(gui_object.mapToGlobal(QPoint(20, -30)), message)
        gui_object.setToolTip(actual_tooltip)

    def null_statusbar_message(self):
        self.mainWindow.gui.statusBar.showMessage("")

    def show_statusbar_message(self, message, text_color = STATUSBAR_TEXT_COLOR,
                               background_color = STATUSBAR_BACKGROUND_COLOR):
        self.mainWindow.gui.statusBar.setStyleSheet("QStatusBar {{ background-color: {background_color};"
                                                    "color: {text_color}; }}"
                                                    .format(background_color = background_color,
                                                            text_color = text_color))
        self.mainWindow.gui.statusBar.showMessage(message)

        self.timer = QTimer()
        self.timer.timeout.connect(self.null_statusbar_message)
        self.timer.start(1000*STATUSBAR_MESSAGE_TIME)


    def decode_range(self):
        range_str = self.mainWindow.gui.lineRange.text()

        is_left_bound_included = True if range_str[0] == "[" else False
        is_right_bound_included = True if range_str[-1] == "]" else False

        range_str = range_str.replace(" ", "")
        range_str = range_str.replace(",", ".")
        range_str = range_str[1:-1]
        range_str = range_str.split(";")

        interval = []
        for i in range(len(range_str)):
            if "p" in range_str[i]:
                if "i" in range_str[i]:
                    range_str[i] = range_str[i].replace("i", "")
                range_str[i] = range_str[i].replace("p", "*3.14159265359")
                range_str[i] = range_str[i].split("*")
                interval.append(float(range_str[i][0]) * float(range_str[i][1]))
            else:
                interval.append(float(range_str[i]))

        interval.append(is_left_bound_included)
        interval.append(is_right_bound_included)

        return interval
