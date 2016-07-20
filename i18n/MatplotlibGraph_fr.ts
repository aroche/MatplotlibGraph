<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE TS>
<TS version="2.0" language="fr_FR">
<context>
    <name>MatplotlibGraph</name>
    <message>
        <location filename="../matplotlib_graph.py" line="244"/>
        <source>&amp;Matplotlib graph generator</source>
        <translation>Générateur de graphes matplotlib</translation>
    </message>
    <message>
        <location filename="../matplotlib_graph.py" line="181"/>
        <source>Matplotlib Graph</source>
        <translation>Graphe matplotlib</translation>
    </message>
    <message>
        <location filename="../matplotlib_graph.py" line="210"/>
        <source>Open script</source>
        <translation>Ouvrir un script </translation>
    </message>
    <message>
        <location filename="../matplotlib_graph.py" line="216"/>
        <source>save script</source>
        <translation>sauvegarder le script</translation>
    </message>
    <message>
        <location filename="../matplotlib_graph.py" line="306"/>
        <source># Type here the content of the function
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
</source>
        <translation># Entrez ici le contenu de la fonction.
# Vous pouvez utiliser les arguments suivants:
# - feature : l&apos;entité sur laquelle on a cliqué
# - figure : la figure matplotlib

# Example: graphe en barres représenatant la longueur de chaque attribut
fields = [f.name() for f in feature.fields()]
ypos = range(len(fields))
length = [len(unicode(a)) for a in feature.attributes()]
axes = figure.gca()
axes.set_yticks(ypos)
axes.set_yticklabels(fields)
axes.barh(ypos, length)</translation>
    </message>
</context>
<context>
    <name>MatplotlibGraphDockWidgetBase</name>
    <message>
        <location filename="../matplotlib_graph_dockwidget_base.ui" line="17"/>
        <source>Matplotlib graph generator</source>
        <translation>Générateur de graphes matplotlib</translation>
    </message>
    <message>
        <location filename="../matplotlib_graph_dockwidget_base.ui" line="31"/>
        <source>Graph</source>
        <translation>Graphe</translation>
    </message>
    <message>
        <location filename="../matplotlib_graph_dockwidget_base.ui" line="45"/>
        <source>Function</source>
        <translation>Fonction</translation>
    </message>
    <message>
        <location filename="../matplotlib_graph_dockwidget_base.ui" line="53"/>
        <source>Load file...</source>
        <translation>Charger un fichier...</translation>
    </message>
    <message>
        <location filename="../matplotlib_graph_dockwidget_base.ui" line="60"/>
        <source>Save as...</source>
        <translation>Enregistrer sous...</translation>
    </message>
    <message>
        <location filename="../matplotlib_graph_dockwidget_base.ui" line="70"/>
        <source>Help</source>
        <translation>Aide</translation>
    </message>
    <message>
        <location filename="../matplotlib_graph_dockwidget_base.ui" line="76"/>
        <source>&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 4.0//EN&quot; &quot;http://www.w3.org/TR/REC-html40/strict.dtd&quot;&gt;
&lt;html&gt;&lt;head&gt;&lt;meta name=&quot;qrichtext&quot; content=&quot;1&quot; /&gt;&lt;style type=&quot;text/css&quot;&gt;
p, li { white-space: pre-wrap; }
&lt;/style&gt;&lt;/head&gt;&lt;body style=&quot; font-family:&apos;MS Shell Dlg 2&apos;; font-size:8.25pt; font-weight:400; font-style:normal;&quot;&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:&apos;Oxygen-Sans&apos;; font-size:10pt; font-weight:600;&quot;&gt;Matplotlib plugin&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:&apos;Oxygen-Sans&apos;; font-size:10pt;&quot;&gt;This plugin creates custom graphs when a feature is clicked.&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:&apos;Oxygen-Sans&apos;; font-size:10pt; font-weight:600;&quot;&gt;Requirements&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:&apos;Oxygen-Sans&apos;; font-size:10pt;&quot;&gt;You need to install &lt;/span&gt;&lt;a href=&quot;http://matplotlib.org&quot;&gt;&lt;span style=&quot; font-family:&apos;Oxygen-Sans&apos;; font-size:10pt; text-decoration: underline; color:#2980b9;&quot;&gt;matplotlib&lt;/span&gt;&lt;/a&gt;&lt;span style=&quot; font-family:&apos;Oxygen-Sans&apos;; font-size:10pt;&quot;&gt; and numpy.&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:&apos;Oxygen-Sans&apos;; font-size:10pt; font-weight:600;&quot;&gt;How to write a function?&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:&apos;Oxygen-Sans&apos;; font-size:10pt;&quot;&gt;You just need to write lines of python code generating the graph.&lt;br /&gt;Two variables are available: &lt;/span&gt;&lt;/p&gt;
&lt;ul style=&quot;margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;&quot;&gt;&lt;li style=&quot; font-family:&apos;Oxygen-Sans&apos;; font-size:10pt;&quot; style=&quot; margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-style:italic;&quot;&gt;feature&lt;/span&gt;: the &lt;a href=&quot;http://www.qgis.org/api/classQgsFeature.html&quot;&gt;&lt;span style=&quot; text-decoration: underline; color:#2980b9;&quot;&gt;QGIS feature&lt;/span&gt;&lt;/a&gt; that was clicked&lt;/li&gt;
&lt;li style=&quot; font-family:&apos;Oxygen-Sans&apos;; font-size:10pt;&quot; style=&quot; margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-style:italic;&quot;&gt;figure&lt;/span&gt;: the &lt;a href=&quot;http://matplotlib.org/api/figure_api.html&quot;&gt;&lt;span style=&quot; text-decoration: underline; color:#2980b9;&quot;&gt;matplotlib figure&lt;/span&gt;&lt;/a&gt; where the graph will be shown&lt;/li&gt;&lt;/ul&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:&apos;Oxygen-Sans&apos;; font-size:10pt;&quot;&gt;To get the main axes where the actual graph will be drawn, use &lt;/span&gt;&lt;span style=&quot; font-family:&apos;Courier New,courier&apos;; font-size:10pt;&quot;&gt;figure.gca()&lt;/span&gt;&lt;span style=&quot; font-family:&apos;Oxygen-Sans&apos;; font-size:10pt;&quot;&gt;. &lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
        <translation type="unfinished">&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 4.0//EN&quot; &quot;http://www.w3.org/TR/REC-html40/strict.dtd&quot;&gt;
&lt;html&gt;&lt;head&gt;&lt;meta name=&quot;qrichtext&quot; content=&quot;1&quot; /&gt;&lt;style type=&quot;text/css&quot;&gt;
p, li { white-space: pre-wrap; }
&lt;/style&gt;&lt;/head&gt;&lt;body style=&quot; font-family:&apos;MS Shell Dlg 2&apos;; font-size:8.25pt; font-weight:400; font-style:normal;&quot;&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:&apos;Oxygen-Sans&apos;; font-size:10pt; font-weight:600;&quot;&gt;Extension de générateur de graphe matplotlib&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:&apos;Oxygen-Sans&apos;; font-size:10pt;&quot;&gt;Cette extension crée des graphes personnalisés pour chaque entité d&apos;une couche.&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:&apos;Oxygen-Sans&apos;; font-size:10pt; font-weight:600;&quot;&gt;Dépendances&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;a href=&quot;http://matplotlib.org&quot;&gt;&lt;span style=&quot; font-family:&apos;Oxygen-Sans&apos;; font-size:10pt; text-decoration: underline; color:#2980b9;&quot;&gt;matplotlib&lt;/span&gt;&lt;/a&gt;&lt;span style=&quot; font-family:&apos;Oxygen-Sans&apos;; font-size:10pt;&quot;&gt; doit être installé.&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:&apos;Oxygen-Sans&apos;; font-size:10pt; font-weight:600;&quot;&gt;Comment écrire une fonction ?&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:&apos;Oxygen-Sans&apos;; font-size:10pt;&quot;&gt;Vous devez juste écrire les lignes de code servant à générer le graphe.&lt;br /&gt;Deux variables sont utilisables : &lt;/span&gt;&lt;/p&gt;
&lt;ul style=&quot;margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;&quot;&gt;&lt;li style=&quot; font-family:&apos;Oxygen-Sans&apos;; font-size:10pt;&quot; style=&quot; margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-style:italic;&quot;&gt;feature&lt;/span&gt;: the &lt;a href=&quot;http://www.qgis.org/api/classQgsFeature.html&quot;&gt;&lt;span style=&quot; text-decoration: underline; color:#2980b9;&quot;&gt;l&apos;entité QGIS&lt;/span&gt;&lt;/a&gt; qui a été cliquée&lt;/li&gt;
&lt;li style=&quot; font-family:&apos;Oxygen-Sans&apos;; font-size:10pt;&quot; style=&quot; margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-style:italic;&quot;&gt;figure&lt;/span&gt;: la &lt;a href=&quot;http://matplotlib.org/api/figure_api.html&quot;&gt;&lt;span style=&quot; text-decoration: underline; color:#2980b9;&quot;&gt; figure matplotlib&lt;/span&gt;&lt;/a&gt; qui contient le graphe&lt;/li&gt;&lt;/ul&gt;
&lt;p style=&quot; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-family:&apos;Oxygen-Sans&apos;; font-size:10pt;&quot;&gt;To get the main axes where the actual graph will be drawn, use &lt;/span&gt;&lt;span style=&quot; font-family:&apos;Courier New,courier&apos;; font-size:10pt;&quot;&gt;figure.gca()&lt;/span&gt;&lt;span style=&quot; font-family:&apos;Oxygen-Sans&apos;; font-size:10pt;&quot;&gt;. &lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</translation>
    </message>
</context>
</TS>
