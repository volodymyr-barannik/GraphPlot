import numpy as np
from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from src.Constants import DEFAULT_PLOT_PRECISION, PLOT_SCALING_LIMITS_FACTOR, INITIAL_XY_LIMITS, \
    PLOT_SCALING_LIMITS_UNIT_FACTOR


class windowPlot(FigureCanvas):

    def __init__(self, parent=None):
        # Init figure as widget
        self.fig = Figure(figsize=(4, 4))
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        # Init axes
        self.ax = None
        self.create_axes()
        self.init_default_boundaries()
        self.ax.set_title('ЛОГАРИФМІЧНА СПІРАЛЬ')
        self.fig.tight_layout()

    def create_axes(self):
        # Creating axes
        self.ax = self.fig.add_subplot("111")

        # Moving the origin (0,0) to the center of the screen
        self.ax.spines['top'].set_color('none')
        self.ax.spines['bottom'].set_position('zero')
        self.ax.spines['left'].set_position('zero')
        self.ax.spines['right'].set_color('none')

    def init_default_boundaries(self):
        # Setting up boundaries
        xy_lim = INITIAL_XY_LIMITS
        self.ax.set_xlim([-xy_lim, xy_lim])
        self.ax.set_ylim([-xy_lim, xy_lim])

    def plot_spiral(self, a=1, b=0.1, precision=DEFAULT_PLOT_PRECISION):
        # Deleting previous axes and creating new one
        self.ax.remove()
        self.create_axes()

        # Setting up polar coordinates needed for further calculations
        phi = np.arange(0, 4 * np.pi, precision)
        r = a * np.e ** (b * phi)

        # and converting them into cartesian coordinates
        x = r * (np.cos(phi))
        y = r * (np.sin(phi))

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
        self.ax.set_xlim([-xy_lim, xy_lim])
        self.ax.set_ylim([-xy_lim, xy_lim])

        # Plotting spiral graph
        self.ax.plot(x, y, color='b', label="Логарифмічна спіраль")
        self.ax.legend()
