.. _quickstart:

=========================
Getting started with Pyzo
=========================

.. image:: _static/pyzo_conda.png
    :scale: 75%
    :align: center

To get started with Pyzo, you need to install the Pyzo IDE (in which
you write your code), a Python environment (in which you run your code),
and scientific packages.


Install the Pyzo IDE
--------------------

.. image:: _static/download.png
  :align: right
  :width: 100px
  
Here are links to download:
    
* `Pyzo for Windows <https://github.com/pyzo/pyzo/releases/download/v4.0/pyzo-4.0-win32.exe>`_
* `Pyzo for OS X <https://github.com/pyzo/pyzo/releases/download/v4.0/pyzo-4.0-osx64.dmg>`_
* `Pyzo for Linux (64 bit) <https://github.com/pyzo/pyzo/releases/download/v4.0/pyzo-4.0-linux64.tar.gz>`_
* For more downloads/information see the :ref:`installation page <install>`


Install Python environment
--------------------------

.. image:: _static/download.png
  :align: right
  :width: 100px

To run Python code, you need a Python interpreter.
Pyzo works with most Python interpreters, but
we recommend installing `miniconda <http://conda.pydata.org/miniconda.html>`_,
or `anaconda <https://www.continuum.io/downloads>`_ if you intend to do science,
because these make it very easy to install additional (scientific) packages.
Make sure to use Python 3, and not Python 2.

Here are direct links to download:
    
* `miniconda for Windows (64 bit) <https://repo.continuum.io/miniconda/Miniconda-latest-Windows-x86_64.exe>`_
* `miniconda for OS X (64 bit) <https://repo.continuum.io/miniconda/Miniconda-latest-MacOSX-x86_64.sh>`_
* `miniconda for Linux (64 bit) <https://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh>`_

We recommend installing in the default location, or at least a location
that can be written to without admin privileges, so that addtional
packages can be installed.


Manually specify an interpreter
-------------------------------

You can usually skip this step, because the environment is generally
automatically detected. If this is not the case (e.g. it was not
installed in the default location), just open the shell configuration
dialog (menu > shell > edit shell configuration), and set the value of
"exe" to the path of the Python executable.


Install Scientific packages
---------------------------

For scienctific computing with Python, you need a few extra package.
In Pyzo's shell, type:

.. code-block:: none
    
    conda install scipy

Hooray, you just installed a new package! Now type:

.. code-block:: none
    
    conda install pyqt matplotlib pandas sympy
    
Now you have the most important scientific Python packages (a.k.a. the scipy-stack).
If you need a package that is not yet installed, and conda does not
work, see :ref:`this guide <install_packages>`.


Further steps
-------------

You should now be set up to start coding! You can also learn more about
:ref:`using the IDE <guide>` and about :ref:`using Python <learn>`.
