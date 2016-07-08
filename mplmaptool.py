

# a tool for clicking on features on a layer

from qgis.core import QgsFeature, QgsMapLayer, QgsMessageLog
from qgis.gui import QgsMapToolIdentify
from PyQt4.QtCore import pyqtSignal


class MplMapTool(QgsMapToolIdentify):
    clicked = pyqtSignal(QgsFeature)
    
    def __init__(self, canvas):
        QgsMapToolIdentify.__init__(self, canvas)
        self.canvas = canvas
        
    def canvasPressEvent(self, evt):
        pass
        
    def canvasReleaseEvent(self, evt):
        lyr = self.canvas.currentLayer()
        QgsMessageLog.logMessage('mpl clicked', 'MplGraph', QgsMessageLog.INFO)
        if lyr and lyr.type() == QgsMapLayer.VectorLayer:
            res = self.identify(evt.x(), evt.y(), [lyr])
            #QgsMessageLog.logMessage(res, 'MplGraph', QgsMessageLog.INFO)
            if len(res) > 0:
                self.clicked.emit(res[0].mFeature)
    
    def isTransient(self):
        return False
        
    # TODO : change cursor
    
