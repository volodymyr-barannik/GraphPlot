import numpy as np
from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from src.Constants import DEFAULT_PLOT_PRECISION, PLOT_SCALING_LIMITS_FACTOR, INITIAL_XY_LIMITS, \
    PLOT_SCALING_LIMITS_UNIT_FACTOR, PLOT_WINDOW_BACKGROUND_COLOR, PLOTWINDOW_TEXT_SIZE


class windowPlot(FigureCanvas):

    def __init__(self, parent=None):
        # Init figure as widget
        self.fig = Figure(figsize=(4, 4))
        self.fig.set_facecolor(PLOT_WINDOW_BACKGROUND_COLOR)
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
        self.ax.set_aspect('equal', adjustable='box')
        self.ax.set_facecolor(PLOT_WINDOW_BACKGROUND_COLOR)
        # Moving the origin (0,0) to the center of the screen
        self.ax.spines['top'].set_color('none')
        self.ax.spines['bottom'].set_position('zero')
        self.ax.spines['left'].set_position('zero')
        self.ax.spines['right'].set_color('none')

        for tick_x,tick_y in zip(self.ax.xaxis.get_major_ticks(), self.ax.yaxis.get_major_ticks()):
            tick_x.label.set_fontsize(PLOTWINDOW_TEXT_SIZE)
            tick_y.label.set_fontsize(PLOTWINDOW_TEXT_SIZE)

    def init_default_boundaries(self):
        # Setting up boundaries
        xy_lim = INITIAL_XY_LIMITS
        self.ax.set_xlim([-xy_lim, xy_lim])
        self.ax.set_ylim([-xy_lim, xy_lim])

    def plot_spiral(self, a=1, b=0.1, range = [0, 4*np.pi], step=DEFAULT_PLOT_PRECISION):
        # Deleting previous axes and creating new one
        self.ax.remove()
        self.create_axes()

        # Setting up polar coordinates needed for further calculations
        if(range[0] != range[1]):
            phi = np.arange(range[0], range[1], step)
        else:
            phi = np.array([range[0], range[1]])
        r = a * np.e ** (b * phi)

        # and converting them into cartesian coordinates
        x = r * (np.cos(phi))
        y = r * (np.sin(phi))

        # Calculating spiral graph boundaries
        abs_max = max(max(x), max(y), -min(x), -min(y))
        if abs_max >= 1:
            xy_lim = abs_max * PLOT_SCALING_LIMITS_FACTOR + 1
        elif 0 < abs_max < 1:
            xy_lim = abs_max * PLOT_SCALING_LIMITS_FACTOR * PLOT_SCALING_LIMITS_UNIT_FACTOR
        elif abs_max == 0:
            xy_lim = INITIAL_XY_LIMITS
        elif 0 > abs_max > -1:
            xy_lim = -abs_max * PLOT_SCALING_LIMITS_FACTOR * PLOT_SCALING_LIMITS_UNIT_FACTOR
        else:
            xy_lim = -abs_max * PLOT_SCALING_LIMITS_FACTOR + 1

        # Setting up spiral graph boundaries
        self.ax.set_xlim([-xy_lim, xy_lim])
        self.ax.set_ylim([-xy_lim, xy_lim])

        # Plotting spiral graph
        if range[0] != range[1]:
            self.ax.plot(x, y, color='b', label="Логарифмічна спіраль")
        else:
            self.ax.scatter(x, y, label= "Логарифмічна спіраль")
        self.ax.legend(prop={'size': 9})
