import collections
import threading

from PyQt5.QtCore import QCoreApplication, QFileInfo, QPoint
from PyQt5.QtWidgets import QFileDialog, QToolTip

from src.Constants import STATUSBAR_TEXT_COLOR, STATUSBAR_BACKGROUND_COLOR, STATUSBAR_ERROR_TEXT_COLOR, \
    STATUSBAR_MESSAGE_TIME, PLOT_WINDOW_BACKGROUND_COLOR


class mainWindowFunctions(object):
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow
        self.message_queue = []
        self.timer_queue = collections.deque()

    def quit(self):
        # Cancel all timers and quit
        for timer in self.timer_queue:
            timer.cancel()
        QCoreApplication.quit()

    def plot_spiral(self):
        arg_a_text = self.mainWindow.gui.lineA.text().replace(",", ".")
        if arg_a_text:
            if arg_a_text == "-":
                self.show_tooltip_message("Введіть, будь ласка, число", self.mainWindow.gui.lineA)
                self.show_statusbar_message("Помилка вводу.", STATUSBAR_ERROR_TEXT_COLOR)
                return
            else:
                arg_a = float(arg_a_text)
        else:
            self.show_tooltip_message("Поле \"а\" не може бути пустим", self.mainWindow.gui.lineA)
            self.show_statusbar_message("Помилка вводу.", STATUSBAR_ERROR_TEXT_COLOR)
            return

        if arg_a > 100000000:
            self.show_tooltip_message("Значення \"a\" занадто велике", self.mainWindow.gui.lineA)
            self.show_statusbar_message("Помилка вводу.", STATUSBAR_ERROR_TEXT_COLOR)
            return

        arg_b_text = self.mainWindow.gui.lineB.text().replace(",", ".")
        if arg_b_text:
            if arg_b_text == "-":
                self.show_tooltip_message("Введіть, будь ласка, число", self.mainWindow.gui.lineB)
                self.show_statusbar_message("Помилка вводу.", STATUSBAR_ERROR_TEXT_COLOR)
                return
            else:
                arg_b = float(arg_b_text)
        else:
            self.show_tooltip_message("Поле \"b\" не може бути пустим", self.mainWindow.gui.lineB)
            self.show_statusbar_message("Помилка вводу.", STATUSBAR_ERROR_TEXT_COLOR)
            return

        if arg_b > 55:
            self.show_tooltip_message("Значення \"b\" занадто велике", self.mainWindow.gui.lineB)
            self.show_statusbar_message("Помилка вводу.", STATUSBAR_ERROR_TEXT_COLOR)
            return

        try:
            arg_range = self.decode_range()
        except:
            self.show_tooltip_message("Проміжок задано лише частково. Завершіть введення.",
                                       self.mainWindow.gui.lineRange)
            self.show_statusbar_message("Помилка вводу.", STATUSBAR_ERROR_TEXT_COLOR)
            return

        if not self.mainWindow.gui.range_regexp.exactMatch(self.mainWindow.gui.lineRange.text()):
            self.show_tooltip_message("Проміжок задано лише частково. Завершіть введення.",
                                      self.mainWindow.gui.lineRange)
            self.show_statusbar_message("Помилка вводу.", STATUSBAR_ERROR_TEXT_COLOR)
            return

        if arg_range[0] > arg_range[1]:
            message = "Проміжок проінтерпретовано як: "
            actual_input = self.mainWindow.gui.lineRange.text()
            left_parentheses = '[' if arg_range[3] == True else '('
            right_parentheses = ']' if arg_range[2] == True else ')'
            actual_input = actual_input.replace(" ", "")
            actual_input = actual_input[1:-1].split(';')
            message = message + left_parentheses + actual_input[1] + "; " + actual_input[0] + right_parentheses + '.'
            self.show_statusbar_message(message)

            # Swap
            arg_range[0], arg_range[1], arg_range[2], arg_range[3] = arg_range[1], arg_range[0], arg_range[3], \
                                                                     arg_range[2]

        if arg_range[0] < 0 or arg_range[1] > 4 * 3.14159265359:
            self.show_tooltip_message("Проміжок має бути підмножиною [0; 4pi]",
                                      self.mainWindow.gui.lineRange)
            self.show_statusbar_message("Помилка вводу.", STATUSBAR_ERROR_TEXT_COLOR)
            return

        if arg_range[0] == arg_range[1] and (bool(arg_range[2]) ^ bool(arg_range[3])):
            self.show_tooltip_message("Проміжок не може включати та виключати одну й ту ж точку",
                                      self.mainWindow.gui.lineRange)
            self.show_statusbar_message("Помилка вводу.", STATUSBAR_ERROR_TEXT_COLOR)
            return

        if arg_range[0] == arg_range[1] and (arg_range[2] is False and arg_range[3] is False):
            self.show_tooltip_message("Проміжок не може бути порожньою множиною",
                                      self.mainWindow.gui.lineRange)
            self.show_statusbar_message("Помилка вводу.", STATUSBAR_ERROR_TEXT_COLOR)
            return

        arg_step_text = self.mainWindow.gui.lineStep.text().replace(",", ".")
        if arg_step_text:
            arg_step = float(arg_step_text)
        else:
            self.show_tooltip_message("Поле \"Δφ\" не може бути пустим", self.mainWindow.gui.lineStep)
            self.show_statusbar_message("Помилка вводу.", STATUSBAR_ERROR_TEXT_COLOR)
            return

        if arg_step <= 0:
            self.show_tooltip_message("Поле \"Δφ\" має бути додатним", self.mainWindow.gui.lineStep)
            self.show_statusbar_message("Помилка вводу.", STATUSBAR_ERROR_TEXT_COLOR)
            return

        self.mainWindow.gui.windowPlotObject.plot_spiral(a=arg_a, b=arg_b,
                                                         range=arg_range, step=arg_step)
        self.mainWindow.gui.windowPlotObject.draw()
        self.show_statusbar_message("Графік побудовано.")

    def grid_toggle(self):
        self.mainWindow.gui.windowPlotObject.show_grid(toggle=True)

    def dots_toggle(self):
        self.mainWindow.gui.windowPlotObject.show_dots(toggle=True)

    def force_last_point_toggle(self):
        self.mainWindow.gui.windowPlotObject.force_last_point(toggle=True)

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
                                                             metadata=None, figsize=(10, 10))

    def show_tooltip_message(self, message, gui_object, text_color=STATUSBAR_TEXT_COLOR,
                             background_color=STATUSBAR_BACKGROUND_COLOR):
        actual_tooltip = gui_object.toolTip()
        QToolTip.showText(gui_object.mapToGlobal(QPoint(20, -35)), message)
        gui_object.setToolTip(actual_tooltip)

    def pop_statusbar_message(self):
        # Restore default message color
        if len(self.message_queue) >= 2:
            self.mainWindow.gui.statusBar.setStyleSheet(self.mainWindow.gui.statusBar.styleSheet().
                                                        replace(self.message_queue[-1][2], STATUSBAR_TEXT_COLOR))

        # Find the oldest call with minimum time and pop it
        if self.message_queue:
            min_time = min(list(x[0] for x in self.message_queue))
            for i in range(len(self.message_queue)):
                if self.message_queue[i][0] == min_time:
                    self.message_queue.pop(i)
                    break

        # Show current messages (update status bar)
        msg = " ".join(x[1] for x in self.message_queue)
        self.mainWindow.gui.statusBar.showMessage(msg)
        self.timer_queue.pop()

    def show_statusbar_message(self, message, text_color=STATUSBAR_TEXT_COLOR,
                               background_color=STATUSBAR_BACKGROUND_COLOR,
                               time=STATUSBAR_MESSAGE_TIME):

        self.mainWindow.gui.statusBar.setStyleSheet("QStatusBar {{ background-color: {background_color};"
                                                    "color: {text_color}; }}"
                                                    .format(background_color=background_color,
                                                            text_color=text_color))
        # Create call-tuple and append it to the queue
        self.message_queue.append((time, message, text_color))
        # Show current messages (update status bar)
        self.mainWindow.gui.statusBar.showMessage(" ".join(x[1] for x in self.message_queue))
        # Start the timer
        timer = threading.Timer(time, self.pop_statusbar_message)
        self.timer_queue.append(timer)
        self.timer_queue[-1].start()

    def decode_range(self):
        # Read input
        range_str = self.mainWindow.gui.lineRange.text()

        is_left_bound_included = True if range_str[0] == "[" else False
        is_right_bound_included = True if range_str[-1] == "]" else False

        # Prepare for parsing
        range_str = range_str.replace(" ", "")
        range_str = range_str.replace(",", ".")
        range_str = range_str[1:-1]
        range_str = range_str.split(";")

        # Replace every pi for 3,1459.. and calculate multiplication
        # Put result into interval variable (left bound at 0, right one at 1)
        interval = []
        for i in range(len(range_str)):
            if "p" in range_str[i]:
                if "i" in range_str[i]:
                    range_str[i] = range_str[i].replace("i", "")
                range_str[i] = range_str[i].replace("p", "*3.14159265359")
                range_str[i] = range_str[i].split("*")
                interval.append(float(range_str[i][0]) * float(range_str[i][1]))

            # Replace every pi for 3,1459.. and calculate multiplication
            # Put result into interval variable (left bound at 0, right one at 1)
            else:
                try:
                    interval.append(float(range_str[i]))
                except Exception as e:
                    raise Exception

        interval.append(is_left_bound_included)
        interval.append(is_right_bound_included)

        return interval
