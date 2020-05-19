import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.axes_grid1 import Divider, Size
from mpl_toolkits.axes_grid1.mpl_axes import Axes
import PyQt5
from src.Constants import PLOT_PRECISION, PLOT_SCALING_LIMITS_FACTOR, INITIAL_XY_LIMITS, PLOT_SCALING_LIMITS_UNIT_FACTOR
from decimal import *


class windowPlot(FigureCanvas):
    def __init__(self, parent=None):
        self.fig = Figure(figsize=(10, 10))
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        # Moving the origin (0,0) to the center of the screen
        self.ax = self.fig.add_subplot("111")
        self.ax.spines['top'].set_color('none')
        self.ax.spines['bottom'].set_position('zero')
        self.ax.spines['left'].set_position('zero')
        self.ax.spines['right'].set_color('none')

        # Setting up boundaries
        xy_lim = INITIAL_XY_LIMITS
        self.ax.set_xlim([-xy_lim, xy_lim])
        self.ax.set_ylim([-xy_lim, xy_lim])

        self.ax.set_title('ЛОГАРИФМІЧНА СПІРАЛЬ')
        self.fig.tight_layout()

    def plot_spiral(self, a=1, b=0.1, precision=PLOT_PRECISION):
        # Setting up polar coordinates needed for further calculations
        theta = np.arange(0, 4 * np.pi, precision)
        r = a * np.e ** (b * theta)

        # and converting them into cartesian coordinates
        x = r * (np.cos(theta))
        y = r * (np.sin(theta))

        print(max(x, key=abs))
        # Calculating spiral graph boundaries
        if max(x, key=abs) >= 1:
            xy_lim = max(x, key=abs) * PLOT_SCALING_LIMITS_FACTOR + 1
        elif 0 < max(x, key=abs) < 1:
            xy_lim = max(x, key=abs) * PLOT_SCALING_LIMITS_FACTOR * PLOT_SCALING_LIMITS_UNIT_FACTOR
        elif max(x, key=abs) == 0:
            xy_lim = 2
        elif 0 > max(x, key=abs) > -1:
            xy_lim = -max(x, key=abs) * PLOT_SCALING_LIMITS_FACTOR * PLOT_SCALING_LIMITS_UNIT_FACTOR
        else:
            xy_lim = -max(x, key=abs) * PLOT_SCALING_LIMITS_FACTOR + 1

        # Setting up spiral graph boundaries
        self.ax.set_xbound([-xy_lim, xy_lim])
        self.ax.set_ybound([-xy_lim, xy_lim])

        # Plotting spiral graph
        self.ax.plot(x, y, color='b', label="Логарифмічна спіраль")
        self.ax.legend()

        # self.draw()
