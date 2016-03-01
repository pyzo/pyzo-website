.. _pyzolinux:

-------------
Pyzo on Linux
-------------

On Linux, one can of course :ref:`download <downloads>` the binary 
version of Pyzo, but one can also install a fully compatible
Python environment via your package manager.

This guide assumes Ubuntu, but with minor modifications it should
also work for other distributions and even OSX (via macports).
You should not need a compiler except if you want scikit-learn. If your
package manager does not have a certain package, you can always try 
installing it via pip.


Limitations
-----------

* Your Linux version should support Python 3, preferably version 3.3.
* Using ``conda install X`` might result in incompatible libraries for 
  non-pure-Python packages.
* You cannot use ``conda install X`` or ``pip install X`` in the shell
  because you'd need root access.


Recipe
------

Via your package manager:

* ``sudo apt-get install python3 python3-pip`` - for Python and pip
* ``sudo apt-get install libqt4-opengl python3-pyside`` - for Pyside
* ``sudo apt-get install python3-numpy python3-scipy python3-matplotlib python3-pandas python3-nose`` - scipy stack (part1)
* ``sudo  apt-get install ipython3 ipython3-notebook ipython3-qtconsole`` - for IPython
* ``sudo  apt-get install python3-skimage`` - scikit-image

Via pip:

* ``sudo python3 -m pip install sympy nose`` - scipy stack (part 2)
* ``sudo python3 -m pip install sklearn`` - scikit-learn (need compiler)
* ``sudo python3 -m pip install imageio pyopengl visvis`` - 3D Visualization 
* ``sudo python3 -m pip install pygments pyzolib iep`` - the IDE

In just two commands:

``sudo apt-get install python3 python3-pip libqt4-opengl python3-pyside python3-numpy python3-scipy python3-matplotlib python3-pandas python3-nose ipython3 ipython3-notebook ipython3-qtconsole python3-skimage``

``sudo python3 -m pip install sympy nose imageio pyopengl visvis pygments pyzolib iep scikit-learn``



