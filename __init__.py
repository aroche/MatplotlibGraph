# -*- coding: utf-8 -*-
"""
/***************************************************************************
 MatplotlibGraph
                                 A QGIS plugin
 Creates a custom matplotlib graph based on vector feature data
                             -------------------
        begin                : 2016-07-06
        copyright            : (C) 2016 by A. Roche
        email                : aroche@photoherbarium.fr
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load MatplotlibGraph class from file MatplotlibGraph.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .matplotlib_graph import MatplotlibGraph
    return MatplotlibGraph(iface)
