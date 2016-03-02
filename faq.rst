.. _faq:

--------------------------
Frequently asked questions
--------------------------

Questions
---------


Why does Pyzo not come with a Python environment anymore?
=========================================================

Multiple :ref:`reasons <iepmerge>`.


How do I install additional packages in Pyzo?
=============================================

See the :ref:`install section <install>` in the guide.


On Windows, after a conda update, numpy is broken, and the IDE won't start
==========================================================================

This has been an issue with that way that Pyzo worked previously, but
should not occur anymore.


On OSX, after a conda update, Pyzo fails to start
================================================

This has been an issue with that way that Pyzo worked previously, but
should not occur anymore. See https://bitbucket.org/pyzo/pyzo/issue/30.


Pyzo does not look native on Linux GTK
======================================

For various reasons, the Pyzo binaries do not come with the GTK theme.
However, you can force Pyzo to use you system PySide/PyQt4 libraries.
Note that this only works if you Python version is ABI compatible with the 
one used to freeze Pyzo. See the file 'qt.conf' for more information.
Of course, you can also simply run Pyzo from source.


Pyzo loses some key hits when running from source on new Ubuntu
===============================================================

See `issue #247 <https://bitbucket.org/iep-project/iep/issue/247/lost-key-hits>`_.
It probably helps to re-install PySide/Qt