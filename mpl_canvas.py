

import matplotlib
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
from matplotlib.figure import Figure

from PyQt4.QtGui import QSizePolicy
from PyQt4.QtCore import QSize


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        matplotlib.rcParams['font.size'] = 8
        self.figure = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.figure.add_subplot(111)

        FigureCanvas.__init__(self, self.figure)
        self.setParent(parent)
        
        self.toolbar = NavigationToolbar(self, parent)
        self.toolbar.setIconSize(QSize(16, 16))

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        
    def getToolbar(self):
        return self.toolbar

    def clear(self):
        self.figure.clear()
        self.axes = self.figure.add_subplot(111)
        
    def test(self):
        self.axes.plot([1,2,3,4])
        
    def saveAs(self, fname):
        self.figure.savefig(fname)
