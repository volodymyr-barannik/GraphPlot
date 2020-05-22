import numpy as np
from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import matplotlib.image as mpimg
from matplotlib.text import Text

from src.Constants import DEFAULT_PLOT_PRECISION, PLOT_SCALING_LIMITS_FACTOR, INITIAL_XY_LIMITS, \
    PLOT_SCALING_LIMITS_UNIT_FACTOR, PLOT_WINDOW_BACKGROUND_COLOR, PLOTWINDOW_TEXT_SIZE, PLOTWINDOW_DOT_SIZE


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
        #self.ax.set_title(r"Ця програма будує графік функції $r=a\cdot e^{b\varphi }$", **{'fontname':'Calibri'})
        self.fig.tight_layout()


        # Init parameters
        self.a, self.b = None, None
        self.range = None
        self.step = None

        self.grid_on = False
        self.dots_on = True
        self.last_point_on = False

        self.lx, self.ly = None, None
        self.rx, self.ry = None, None

        # Plots
        self.spiral = None
        self.ldot, self.rdot = None, None

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

    def show_grid(self, toggle = False):
        if toggle:
            self.grid_on = not self.grid_on
        self.ax.grid(self.grid_on)
        self.draw()

    def show_dots(self, toggle = False):
        if toggle:
            self.dots_on = not self.dots_on

        if self.dots_on and self.lx is not None:
            if self.range[2] is True and self.range[3] is True:
                self.ldot = self.ax.scatter([self.lx, self.lx], [self.ly, self.ly], s=PLOTWINDOW_DOT_SIZE,
                                    edgecolors='b', facecolors='b', zorder=1, gid="5")
                self.rdot = self.ax.scatter([self.rx, self.rx], [self.ry, self.ry], s=PLOTWINDOW_DOT_SIZE,
                                    edgecolors='b', facecolors='b', zorder=1, gid="6")

            elif self.range[2] is True and self.range[3] is False:
                self.ldot = self.ax.scatter([self.lx, self.lx], [self.ly, self.ly], s=PLOTWINDOW_DOT_SIZE,
                                    edgecolors='b', facecolors='b', zorder=1)
                self.rdot = self.ax.scatter([self.rx, self.rx], [self.ry, self.ry], s=PLOTWINDOW_DOT_SIZE,
                                    edgecolors='b', facecolors=PLOT_WINDOW_BACKGROUND_COLOR, zorder=1)

            elif self.range[2] is False and self.range[3] is True:
                self.ldot = self.ax.scatter([self.lx, self.lx], [self.ly, self.ly], s=PLOTWINDOW_DOT_SIZE,
                                    edgecolors='b', facecolors=PLOT_WINDOW_BACKGROUND_COLOR, zorder=1)
                self.rdot = self.ax.scatter([self.rx, self.rx], [self.ry, self.ry], s=PLOTWINDOW_DOT_SIZE,
                                    edgecolors='b', facecolors='b', zorder=1)

            elif self.range[2] is False and self.range[3] is False:
                self.ldot = self.ax.scatter([self.lx, self.lx], [self.ly, self.ly], s=PLOTWINDOW_DOT_SIZE,
                                    edgecolors='b', facecolors=PLOT_WINDOW_BACKGROUND_COLOR, zorder=1)
                self.rdot = self.ax.scatter([self.rx, self.rx], [self.ry, self.ry], s=PLOTWINDOW_DOT_SIZE,
                                    edgecolors='b', facecolors=PLOT_WINDOW_BACKGROUND_COLOR, zorder=1)

        elif self.dots_on is False and self.lx is not None and self.ax.collections != []:
            self.ldot.remove()
            self.rdot.remove()
        self.draw()

    def force_last_point(self, toggle = False, is_plotted_first_time=False):
        if toggle:
            self.last_point_on = not self.last_point_on

        if self.lx is None:
            self.last_point_on = not self.last_point_on
            return

        if self.range[0] == self.range[1]:
            return

        if self.spiral is not None:
            self.spiral[0].remove()

            if self.last_point_on is True:
                self.x = np.append(self.x, self.a * np.e ** (self.b * self.range[1]) * (np.cos(self.range[1])))
                self.y = np.append(self.y, self.a * np.e ** (self.b * self.range[1]) * (np.sin(self.range[1])))
            else:
                if not is_plotted_first_time:
                    self.x = np.delete(self.x, -1)
                    self.y = np.delete(self.y, -1)

        # Delete old includity dots if they exist
        if self.ldot is not None and self.ax.collections != []:
            self.ldot.remove()
            self.rdot.remove()

        self.update_dots()
        self.update_boundaries()

        self.update_spiral_plot()

    def update_dots(self):
        self.lx, self.ly = self.x[0], self.y[0]
        self.rx, self.ry = self.x[-1], self.y[-1]

    def update_boundaries(self):
        # Calculating spiral graph boundaries
        self.abs_max = max(max(self.x), max(self.y), -min(self.x), -min(self.y))
        if self.abs_max >= 1:
            self.xy_lim = self.abs_max * PLOT_SCALING_LIMITS_FACTOR + 1
        elif 0 < self.abs_max < 1:
            self.xy_lim = self.abs_max * PLOT_SCALING_LIMITS_FACTOR * PLOT_SCALING_LIMITS_UNIT_FACTOR
        elif self.abs_max == 0:
            self.xy_lim = INITIAL_XY_LIMITS
        elif 0 > self.abs_max > -1:
            self.xy_lim = -self.abs_max * PLOT_SCALING_LIMITS_FACTOR * PLOT_SCALING_LIMITS_UNIT_FACTOR
        else:
            self.xy_lim = -self.abs_max * PLOT_SCALING_LIMITS_FACTOR + 1

        # Setting up spiral graph boundaries
        self.ax.set_xlim([-self.xy_lim, self.xy_lim])
        self.ax.set_ylim([-self.xy_lim, self.xy_lim])

    def update_spiral_plot(self):
        if self.range[0] != self.range[1]:
            self.spiral = self.ax.plot(self.x, self.y, color='b', label="Логарифмічна спіраль", zorder=0)
            self.show_dots()
        else:
            self.spiral = self.ax.scatter(self.x, self.y, color='b', label="Логарифмічна спіраль", zorder=0)
        self.ax.legend(prop={'size': 9})

        self.show_grid()

    def plot_spiral(self, a=1, b=0.1, range= [0, 4*np.pi], step=DEFAULT_PLOT_PRECISION):
        # Deleting previous axes and creating new one
        self.ax.remove()
        self.create_axes()
        self.range = range
        self.a, self.b = a, b
        self.step = step

        # Setting up polar coordinates needed for further calculations
        if(range[0] != range[1]):
            self.phi = np.arange(range[0], range[1], step)
        else:
            self.phi = np.array([range[0], range[1]])
        self.r = a * np.e ** (b * self.phi)

        # and converting them into cartesian coordinates
        self.x = self.r * (np.cos(self.phi))
        self.y = self.r * (np.sin(self.phi))

        self.update_dots()

        self.update_boundaries()
        self.update_spiral_plot()
        self.force_last_point(is_plotted_first_time=True)
