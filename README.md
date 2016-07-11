# MatplotlibGraph

This is a QGIS plugin that generates custom graphs based on clicked feature.

Using it in QGIS requires knowledge in python and matplotlib library.

Requirements
------------

You need to install [matplotlib](http://matplotlib.org) and (not mandatory) numpy.

How to write a function
-----------------------

You just need to write lines of python code generating the graph.

Two variables are available: 
* feature: a [QGIS Feature](http://www.qgis.org/api/classQgsFeature.html) that was clicked
* figure: the [matplotlib figure](http://matplotlib.org/api/figure_api.html) where the graph will be shown

To get the main axes where the actual graph will be drawn, use `figure.gca()`.
