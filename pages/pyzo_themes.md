# Themes in Pyzo

In Pyzo, the theme for the IDE itself can be modified via "View > Qt Theme".
The syntax color theme is fixed to a variant of
[Solarized](http://ethanschoonover.com/solarized). At this time, there is not
an easy way to change this theme. 

For the persistent, it is possible to modify syntax colors by modifying the
``__init__()`` of ``CodeEditorBase`` in ``pyzo-source-dir/codeeditor/base.py``.
The location of the Pyzo source directory can be found via "Help > About Pyzo".
