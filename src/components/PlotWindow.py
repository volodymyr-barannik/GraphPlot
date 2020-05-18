import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.axes_grid1 import Divider, Size
from mpl_toolkits.axes_grid1.mpl_axes import Axes
import PyQt5
from src.Constants import PLOT_PRECISION, PLOT_SCALING_LIMITS_FACTOR


class windowPlot(FigureCanvas):
    def __init__(self, parent = None):

        self.fig = Figure(figsize=(10,10))#plt.figure(figsize=(8, 8))
        #self.fig.tight_layout()
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def plot(self, a=1, b=0.1):
        print("inside PlotWindow.plot()")
        self.a = a  # 1
        self.b = b  # 0.5
        self.theta = np.arange(0, 4 * np.pi, PLOT_PRECISION)
        self.r = self.a * np.e ** (self.b * self.theta)
        self.x = self.r * np.cos(self.theta)
        self.y = self.r * np.sin(self.theta)
        self.xy_lim = self.x[-1] * PLOT_SCALING_LIMITS_FACTOR + 1

        ax = self.fig.add_subplot("111")
        ax.spines['top'].set_color('none')
        ax.spines['bottom'].set_position('zero')
        ax.spines['left'].set_position('zero')
        ax.spines['right'].set_color('none')

        ax.set_xlim([-self.xy_lim, self.xy_lim])
        ax.set_ylim([-self.xy_lim, self.xy_lim])

        ax.plot(self.x, self.y, color='b', label="Логарифмічна спіраль")
        ax.legend()

        ax.set_title('ЛОГАРИФМІЧНА СПІРАЛЬ')

        self.draw()
