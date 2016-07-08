# -*- coding: utf-8 -*-
"""
/***************************************************************************
 MatplotlibGraphDockWidget
                                 A QGIS plugin
 Creates a custom matplotlib graph based on vector feature data
                             -------------------
        begin                : 2016-07-06
        git sha              : $Format:%H$
        copyright            : (C) 2016 by A. Roche
        email                : aroche@photoherbarium.fr
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt4 import QtGui, uic
from PyQt4.QtCore import pyqtSignal
from qgis.gui import QgsCodeEditorPython

from mpl_canvas import MplCanvas


FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'matplotlib_graph_dockwidget_base.ui'))


class MatplotlibGraphDockWidget(QtGui.QDockWidget, FORM_CLASS):

    closingPlugin = pyqtSignal()

    def __init__(self, parent=None):
        """Constructor."""
        super(MatplotlibGraphDockWidget, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        
        self.editor = QgsCodeEditorPython(self.tab_2)
        self.tab_2.layout().addWidget(self.editor)
        self.figureCanvas = MplCanvas(self)
        self.verticalLayout.addWidget(self.figureCanvas)

    def closeEvent(self, event):
        self.closingPlugin.emit()
        event.accept()

