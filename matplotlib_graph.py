# -*- coding: utf-8 -*-
"""
/***************************************************************************
 MatplotlibGraph
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
from PyQt4.QtCore import QSettings, QTranslator, qVersion, QCoreApplication, Qt
from PyQt4.QtGui import QAction, QIcon, QFileDialog
# Initialize Qt resources from file resources.py
import resources

from qgis.core import QgsMapLayer, QgsMessageLog
from mplmaptool import MplMapTool

# Import the code for the DockWidget
from matplotlib_graph_dockwidget import MatplotlibGraphDockWidget
import os.path


class MatplotlibGraph:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface

        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)

        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'MatplotlibGraph_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&Matplotlib graph generator')
        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar(u'MatplotlibGraph')
        self.toolbar.setObjectName(u'MatplotlibGraph')

        #print "** INITIALIZING MatplotlibGraph"

        self.pluginIsActive = False
        self.dockwidget = None
        self.currentLayer = None
        
        self.tool = MplMapTool(self.iface.mapCanvas())
        
        self.graphFunction = None
        self.functionChanged = True
        self.layerRegistry = {}


    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('MatplotlibGraph', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.setCheckable(True)
        action.toggled.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action


    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/MatplotlibGraph/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'Matplotlib Graph'),
            callback=self.run,
            parent=self.iface.mainWindow())
            
        # connections
        self.iface.currentLayerChanged.connect(self.onCurrentLayerChanged)
        self.iface.mapCanvas().mapToolSet.connect(self.onToolSetChanged)
        self.tool.clicked.connect(self.onFeatureClicked)
        

    #--------------------------------------------------------------------------
    def logMessage(self, msg):
        QgsMessageLog.logMessage(str(msg), 'MplGraph', QgsMessageLog.INFO)
    
    
    def onCurrentLayerChanged(self, layer):
        self.initLayerFunction()
            
    def onFeatureClicked(self, ft):
        self.createGraph(ft)
        
    def onFunctionChanged(self):
        # save function for the layer
        layer = self.iface.activeLayer()
        if layer:
            self.layerRegistry[layer.id()] = self.dockwidget.editor.text()
        self.functionChanged = True
        
    def onLoadFileClicked(self):
        fname = QFileDialog.getOpenFileName(self.dockwidget, self.tr("Open script"), None, 'Python Files (*.py)')
        if fname :
            with open(fname, 'r') as f:
                self.dockwidget.editor.setText(f.read())
            
    def onSaveFileClicked(self):
        fname = QFileDialog.getSaveFileName(self.dockwidget, self.tr('save script'), None, 'Python Files (*.py)')
        if fname:
            with open(fname, 'w') as f:
                f.write(self.dockwidget.editor.text())
                
    def onToolSetChanged(self, tool):
        if tool == self.tool:
            return
        for action in self.actions:
            if action.isCheckable():
                action.setChecked(False)
            
    def onClosePlugin(self):
        """Cleanup necessary items here when plugin dockwidget is closed"""

        #print "** CLOSING MatplotlibGraph"

        # disconnects
        self.dockwidget.closingPlugin.disconnect(self.onClosePlugin)

        # remove this statement if dockwidget is to remain
        # for reuse if plugin is reopened
        # Commented next statement since it causes QGIS crashe
        # when closing the docked window:
        # self.dockwidget = None

        self.pluginIsActive = False


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&Matplotlib graph generator'),
                action)
            self.iface.removeToolBarIcon(action)
        # remove the toolbar
        del self.toolbar
        self.tool.deactivate()

    #--------------------------------------------------------------------------

    def run(self, checked):
        """Run method that loads and starts the plugin"""
        if not checked:
            self.iface.mapCanvas().unsetMapTool(self.tool)
            return

        if not self.pluginIsActive:
            self.pluginIsActive = True

            #print "** STARTING MatplotlibGraph"

            # dockwidget may not exist if:
            #    first run of plugin
            #    removed on close (see self.onClosePlugin method)
            if self.dockwidget == None:
                # Create the dockwidget (after translation) and keep reference
                self.dockwidget = MatplotlibGraphDockWidget()
                
                         

            # connect to provide cleanup on closing of dockwidget
            self.dockwidget.closingPlugin.connect(self.onClosePlugin)

            self.dockwidget.editor.textChanged.connect(self.onFunctionChanged)
            self.dockwidget.loadFileButton.clicked.connect(self.onLoadFileClicked)
            self.dockwidget.saveFileButton.clicked.connect(self.onSaveFileClicked)
            
            # show the dockwidget
            self.iface.addDockWidget(Qt.RightDockWidgetArea, self.dockwidget)
            self.dockwidget.show()
            
            self.initLayerFunction()
            
        self.iface.mapCanvas().setMapTool(self.tool)
            
            
    def initLayerFunction(self):
        layer = self.iface.activeLayer()
        self.logMessage(QgsMapLayer)
        if layer and layer.type() == QgsMapLayer.VectorLayer:
            if layer.id() in self.layerRegistry:
                self.dockwidget.editor.setText(self.layerRegistry[layer.id()])
            else:
                self.dockwidget.editor.setText(self.tr("""# Type here the content of the function
# You can use the following arguments:
# - feature: the feature that was clicked
# - figure: the matplotlib figure

# Example: bar graph of attribute length
fields = [f.name() for f in feature.fields()]
ypos = range(len(fields))
length = [len(unicode(a)) for a in feature.attributes()]
axes = figure.gca()
axes.set_yticks(ypos)
axes.set_yticklabels(fields)
axes.barh(ypos, length)
"""))
            self.dockwidget.tabWidget.setEnabled(True)
        else:
            self.dockwidget.tabWidget.setEnabled(False)
            

            
    def getFunction(self):
        if self.functionChanged:
            f = self.dockwidget.editor.text()
            user_source = "def user_func(feature, figure):\n" + '\n'.join(
                "    " + line for line in f.splitlines())
            d = {}
            exec user_source in d
            self.graphFunction = d['user_func']
            self.functionChanged = False
        return self.graphFunction

            
    def createGraph(self, feature):
        func = self.getFunction()
        self.dockwidget.figureCanvas.clear()
        func(feature, self.dockwidget.figureCanvas.figure)
        
        self.dockwidget.figureCanvas.draw()
        self.dockwidget.tabWidget.setCurrentIndex(0)
        

# TODO
# save functions in project
# option to save figure as image
# test exec safety
# catch exec errors