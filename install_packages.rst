.. _install_packages:
    
==============================
Installing additional packages
==============================

Installing additional (scientific) packages is generally very easy.
Note that some packages may not be suitable for Python 3. Such a
package is probably not maintained very well, so you may want to
consider an alternative. Try in this order to install package "xx":

Command for convenience
-----------------------

Pyzo provides three sommands as a convenience that use the conda commands below:
``install xx``, ``update xx``, ``remove xx``.


Install using conda
-------------------

.. code-block:: none
    
    conda install xx


The ``conda`` command installs binary packages, and is
therefore the easiest solution. However, a package must have been pre-build
in order for this to work. Therefore it may not work for less common packages.

If the package is not available on the main channel, you can search on http://anaconda.org
for available packages. If you find that "John" has build the package
that you need, use ``conda install -c john xx``.


Install using Pip
-----------------

.. code-block:: none

    pip install xx

The ``pip`` command downloads a package from the
`Python package index <https://pypi.python.org>`_ and installs it from source.
Probably about 95% of all packages are listed on Pypi. However, if the package
is not pure Python (i.e. it needs to be compiled) this will probably
not work unless you're using Linux.


Other solutions
---------------

If you are on Windows, you can visit 
`Gohlke's collection of Python packages <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_ .
Download the required ``.whl`` file and use ``pip install location/to/xxx.whl``.

You can always ssk maintainers of the package how to install it, or ask
in Pyzo mailing list.

 

Usefull packages
----------------

* The scipy stack: ``conda install numpy scipy, matplotlib, pandas, sympy``
* Other usefull tools: ``conda install scikit-image scikit-learn``
* 3D visualization: ``pip install visvis``
* Reading images, volumes and movies: ``pip install imageio``

