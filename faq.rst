.. _faq:

--------------------------
Frequently asked questions
--------------------------

Questions
---------


How can I use Pyzo with a virtual env?
======================================

To use Python interpreters from a virtualenv in Pyzo, set the environment
variables ``PATH`` and ``VIRTUAL_ENV`` in the shell configuration, and
set the interpreted ``EXE`` to ``python``. Note that the ``$PATH`` is only
expanded from Pyzo version 4.4 (to be released).
See also `issue #403 <https://github.com/pyzo/pyzo/issues/403>`_:

.. code-block:: none
    
    VIRTUAL_ENV=/path/to/venv
    PATH=/path/to/venv/bin:$PATH 


Why is Matplotlib not interactive?
==================================

When working with Matplotlib, make sure you have ``pyqt`` installed
(``conda install pyqt``). The shell should integrate it automatically.
Then, you need to tell Matplotlib to be interactive:
    
.. code-block:: python

    import matplotlib.pyplot as plt
    plt.ion()


Can I still distribute a conda environment together with Pyzo?
==============================================================

Yes, Pyzo detects interpreters relative to itself, so you can just
create a conda environment, put the Pyzo binary in its root, and
distribute that as a whole.



Why does Pyzo not come with a Python environment anymore?
=========================================================

Multiple :ref:`reasons <iepmerge>`.


How do I install additional packages in Pyzo?
=============================================

See the :ref:`install section <install_packages>` in the guide.


On Windows, after a conda update, numpy is broken, and the IDE won't start
==========================================================================

This has been an issue with that way that Pyzo worked previously, but
should not occur anymore.


On OSX, after a conda update, Pyzo fails to start
=================================================

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