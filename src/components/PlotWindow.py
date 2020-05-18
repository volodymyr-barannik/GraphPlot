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

        self.ax = self.fig.add_subplot("111")
        self.ax.spines['top'].set_color('none')
        self.ax.spines['bottom'].set_position('zero')
        self.ax.spines['left'].set_position('zero')
        self.ax.spines['right'].set_color('none')

        self.xy_lim=5
        self.ax.set_xlim([-self.xy_lim, self.xy_lim])
        self.ax.set_ylim([-self.xy_lim, self.xy_lim])

        self.ax.set_title('ЛОГАРИФМІЧНА СПІРАЛЬ')

    def plotSpiral(self, a=1, b=0.1, precision = PLOT_PRECISION):

        print("inside PlotWindow.plot()")
        self.a = a  # 1
        self.b = b  # 0.5
        self.theta = np.arange(0, 4 * np.pi, precision)
        self.r = self.a * np.e ** (self.b * self.theta)
        self.x = self.r * np.cos(self.theta)
        self.y = self.r * np.sin(self.theta)
        self.xy_lim = self.x[-1] * PLOT_SCALING_LIMITS_FACTOR + 1

        self.ax.set_xlim([-self.xy_lim, self.xy_lim])
        self.ax.set_ylim([-self.xy_lim, self.xy_lim])

        self.ax.plot(self.x, self.y, color='b', label="Логарифмічна спіраль")
        self.ax.legend()



        #self.draw()
