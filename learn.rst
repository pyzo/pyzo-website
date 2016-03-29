.. _learn:

------------
Learn Python
------------


.. image:: _static/graduation_hat.png
  :scale: 50%
  :align: center


There is plenty of material available on the web to help you learn
Python by yourself. There are also several organizations that provide
online courses. And perhaps your local school or University offers a
course as well.

Start reading
=============

  * `python.org <http://www.python.org>`_
  * `python intro <https://docs.python.org/3/tutorial/introduction.html>`_
  * `getpython3.com <http://getpython3.com>`_
  * `scipy.org <http://www.scipy.org>`_
  * `List of topical sofware at scipy.org <http://scipy.org/Topical_Software>`_
  * `Numpy for Matlab users <http://scipy.org/NumPy_for_Matlab_Users>`_



Practice
========

Once you know the basics, it's good to practice your skills in order
to improve them. Here are some sites where you can do that:

  * `Scipy lectures <http://scipy-lectures.github.io/>`_
  * `Project Euler <http://projecteuler.net/>`_ (mathematical puzzles)
  * `CheckIO <http://www.checkio.org/>`_ (game)
  * `Python challenge <http://www.pythonchallenge.com/>`_ (game with riddles)
  * `Code academy <http://www.codecademy.com/>`_ (nice exercises)


Transitioning from Matlab
=========================

If you are transitioning to Python from Matlab, you may find that some
things work differently in Python.

* Python searches for modules to import in selected directories that can be set
  in the ``PYTHONPATH``, which you can set in the shell configuration dialog.
  Modules relative to the file being executed are only found if the file
  is executed as a script.
* If a module is already imported, Python will not load it again (even if it
  has changed). You can use "execute as a script" to get a fresh interpreter.
* Arrays are provided by the numpy package. Read more on
  `differences between Numpy and Matlab <http://matlab.pyzo.org>`_.


.. _packages:

Packages
========

If you want to get started with a certain library, you can in most cases
best have a look at the library's website and search for tutorials and 
documentation. 

The `Scipy Stack <http://scipy.org/about.html#the-scipy-stack>`_:

  * `numpy <http://www.numpy.org/>`_  - using arrays in Python
  * `scipy <http://www.scipy.org/>`_ - core scientific functionality
  * `matplotlib <http://matplotlib.org/>`_ - 2D plotting library
  * `pandas <http://pandas.pydata.org/>`_ - data structures and analysis
  * `sympy <http://sympy.org>`_ - symbolic math
  * `nose <http://nose.readthedocs.org/>`_ - software testing
  * `IPython <http://www.ipython.org/>`_ - advanced interactive shell
  

Further scientific packages:
  
  * `pyopengl <http://pyopengl.sourceforge.net/>`_ - talk to your GPU
  * `visvis <https://code.google.com/p/visvis/>`_ - 3D plotting and visualization
  * `skimage <http://scikit-learn.org>`_ - 2D and 3D image processing
  * `sklearn <http://www.numpy.org/>`_ - machine learning
  * `imageio <http://imageio.readthedocs.org/>`_ - read and write image data


Further non-science-specific packages:
  
  * `PySide <http://qt-project.org/wiki/PySide>`_ - bindings to the Qt widget toolkit
  * `cx_freeze <http://cx-freeze.sourceforge.net/‎>`_ - Deploy your applications
  * `requests <http://www.python-requests.org/‎>`_ - networking


Community
=========

The Python community is known to be large and friendly. Python is used
in a lot of areas, from web frameworks to scripting and GUI design. The
scienfitic community is a fastly growing sub-community with many active
members.
`Scipy.org <http://www.scipy.org>`_ is the best place to start for
the scientific Python community. 

Typically, each Python library has its own mailing list. 
Here are a few general ones:

  * `Pyzo group <http://groups.google.com/forum/#!forum/pyzo>`_
  * `Read <http://dir.gmane.org/gmane.comp.python.scientific.user>`_ or 
    `signup <http://mail.scipy.org/mailman/listinfo/scipy-user>`_
    for the Scipy mailing list (Scientific Python)
  * `Python group <https://groups.google.com/forum/?fromgroups#!forum/comp.lang.python>`_ 
    (general Python)

It is also common to communicate with developers of a package via an
issue on `Github <http:github.com>`_.

