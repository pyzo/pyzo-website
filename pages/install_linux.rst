.. _install_linux:

=====================
Install Pyzo on Linux
=====================

Natively Linux install
======================

Although we provide binaries to run Pyzo on Linux, these sometimes suffer from
problems (most notably ugly/nonnative fonts) on certain distributions.

If this is the case for you, you can install Pyzo the "Linux-way". Pyzo runs
on Python 3 and only further needs PyQt4/PyQt5. Therefore, it's enough to do:
    
.. code-block:: none
    
    $ sudo apt-get install python3-pip python3-pyqt5
    $ sudo python3 -m pip install pyzo --upgrade
    $ pyzo

Instead of ``apt-get`` you may need to use ``yum`` or other, depending on your
distribution.

For the Python environment to run your code in, you can either use the Python
interpreter that comes with your system, or install miniconda/anaconda
as explained in the :ref:`quickstart <quickstart>`.


Install via Flatpak
===================

Pyzo is also available as a `Flatpak <https://flatpak.org/>`_ package on
`Flathub <https://flathub.org/apps/details/org.pyzo.pyzo>`_.
