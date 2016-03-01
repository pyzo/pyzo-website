.. _faq:

--------------------------
Frequently asked questions
--------------------------

Technical issues
----------------

How do I install additional packages in Pyzo?
=============================================

See :ref:`packages <packages>`.


On Windows, after a conda update, numpy is broken, and the IDE won't start
==========================================================================

On Windows, you should avoid updating numpy with the IDE open,
also if numpy is updated as a side effect of installing/updating
another package. The IDE has a spurious import to numpy, and it may 
break the numpy package. To fix or avoid this:

* Open a command shell
* cd to ``c:\pyzo2013c\Scripts``
* run ``conda install -f numpy``


On OSX, after a conda update, IEP fails to start
================================================

See https://bitbucket.org/pyzo/pyzo/issue/30. To work around this, we
recommend installing IEP separately (http://iep-project.org) and manage
the Pyzo distribution from there.


The shell is very slow and unresponsive on OS X Mavericks
=========================================================

Apparently, the new AppNap feature of OS X Maverick is causing
problems, see https://bitbucket.org/iep-project/iep/issue/278
This will be fixed in IEP 3.4. To fix it on earlier versions, run
``pip install appnope`` and ``appnope.nope()`` at the start of your 
script (or in a startup script).


IEP does not look native on Linux GTK
=====================================

For various reasons, the IEP binaries do not come with the GTK theme.
However, you can force IEP to use you system PySide/PyQt4 libraries.
Note that this only works if you Python version is ABI compatible with the 
one used to freeze IEP. See the file 'qt.conf' for more information.
Of course, you can also simply run IEP from source.

