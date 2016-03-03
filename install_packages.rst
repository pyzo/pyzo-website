.. _install_packages:
    
==============================
Installing additional packages
==============================

Installing additional (scientific) packages is generally very easy.
Try in this order to install package "xx":
    
* ``conda install xx``
* ``pip install xx``
* If you are on Windows, visit `Gohlke's collection of Python packages <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_ .
* Ask maintainers of the package how to install it.
* Ask in Pyzo mailing list.

Some background. The ``conda`` command installs binary packages, and is
therefore the easiest solution. However, a package must have been pre-build
in order for this to work. Therefore it may not work for less common packages.

The ``pip`` command downloads a package from the
`Python package index <https://pypi.python.org>`_ and installs it from source.
Probably about 95% of all packages are listed on Pypi. However, if the package
is not pure Python (i.e. it needs to be compiled) this will probably
not work unless you're using Linux.

Also note that some packages may not be suitable for Python 3. Such a
package is probably not maintained very well, so you may want to
consider an alternative.
