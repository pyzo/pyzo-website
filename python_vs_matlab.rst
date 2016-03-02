.. _pythonmatlab:
  
================
Python vs Matlab
================

We regularly hear of people (and whole research groups) that 
transition from Matlab to Python. The scientific Python ecosystem
is maturing fast and Python is an appealing alternative, because it's 
free, open source, and becoming ever more powerful.
This page tries to explain the differences between these two tools.


Matlab and Python and their ecosystems
--------------------------------------

Python, by definition, is a
programming language. The most common implementation is that in C (also
known as `CPython <http://en.wikipedia.org/wiki/CPython>`_) 
and is what is mostly refered to as "Python". Apart from the programming
language and interpreter, Python also consists of an extensive standard
library. This library is aimed at programming in general and contains
modules for os specific stuff, threading, networking, databases, etc.

`Matlab <http://en.wikipedia.org/wiki/MATLAB>`_ 
is a commercial numerical computing environment and programming language.
The concept of Matlab refers to the whole package, including the IDE.
The standard library does not contain as much generic programming
functionality, but does include matrix algebra and an extensive library
for data processing and plotting. For extra functionality the Mathworks
provides toolkits (but these cose you extra).

.. image:: _static/pythonvsmatlab.png
    :align: center

*Diagram illustrating the differences between Python and
Matlab in terms of their ecosystem.*
    

To do scientific computing in Python, you need additional packages (e.g.
Numpy, Scipy, Matplotlib). Additionally, you'll need an IDE. Many
pythoneers come from a Linux environment and use a Python shell and an
editor (like vi or Emacs), but people coming from Matlab prefer a
feature-rich IDE (us included). There are a handful of `IDE's
<http://wiki.python.org/moin/IntegratedDevelopmentEnvironments>`_
available, some of which are for free.

Because Python is open and free, it is very easy for other parties to
design packages or other software tools that extend Python. It is
possible to create applications using any of the mayor GUI libraries
(e.g. `Qt <http://qt-project.org/>`_), use OpenGL, drive your USB port, 
etc. Another example is `Cython <http://www.cython.org/>`_ to enhance 
the speed of algorithms by converting Python to C code, and cx_Freeze
to create a standalone application from your source.

Each package is being developed by a different (but often overlapping)
group of people, who are also users of the package. Many packages are
available for different purposes. In this open source ecosystem most
packages are driven by a handful of core developers, but many of a
package users contribute to the development by reporting issues, helping
with documentation, and making small improvements to the code.


The problem with Matlab
-----------------------

We do not intend to make Matlab look bad. We used to love Matlab
ourselves! However, we think that Matlab has a few fundamental
shortcomings. Most of these arise from its commercial nature:


  * The algorithms are **proprietary**, which means you can not see the
    code of most of the algorithms you are using and have to trust that
    they were implemented correctly.
  * Matlab is quite **expensive**, which means that code that is written
    in Matlab can only be used by people with sufficient funds to
    buy a license.
  * Naturally, the Mathworks puts restrictions on code **portability**,
    the ability to run your code on someone elses computer. You can run
    your "compiled" application using the Matlab Component Runtime
    (MCR), but your portbale app must exactly match the version of the
    installed MCR, which can be a nuisance considering that Matlab
    releases a new version every 6 months.
  * The proprietary nature also makes it difficult/impossible for 3th
    parties to extend the functionality of Matlab.
    
Furtheremore, there are some other issues that stem from Matlabs origins
as a matrix manipulation package:

  * The semicolon. It can be usefull to show the result when you type
    code in the console, but in scripts it does not make any sense that
    one must end a line with a semicolon in order to suppress output.
  * Indexing is done with braces rather than brackets, making it 
    difficult to distinguish it from a function call.
        

Advantages of Matlab 
--------------------

Of course, Matlab has its advantages too:

  * It has a solid amount of functions. 
  * Simulink is a product for which there is no good alternative yet. 
  * It might be easier for beginners, because the package includes all
    you need, while in Python you need to install extra packages and
    an IDE. (Pyzo tries to solve this issue.)
  * It has a large scientific community; it is used on many universities
    (although few companies have the money to buy a license).


Advantages of Python
--------------------

  * **Free**. As in speech and as in beer. (It won't cost you a thing, and
    you are allowed to view and modify the source.)
  * **Beautiful programming language**. Python
    was created to be a generic language that is easy to read, while
    Matlab started as a matrix manipulation package to which they added
    a programming language. As you become more familiar with Python,
    you will be amazed with how well it is designed. There is only one
    word for that: Beautiful.
  * **Powerful**. Because it's so well designed, it's easier than other
    languages to transform your ideas into code. Further, Python comes
    with extensive standard libraries, and has a powerful datatypes
    such as lists, sets and dictionaries. These really help to organize
    your data.
  * **Namespaces**. Matlab supports namespaces for the functions that
    you write, but the core of Matlab is without namespaces; every
    function is defined in the global namespace. Python works with
    modules, which you need to import if you want to use them. (For
    example ``from skimage import morphology``.) Therefore Python
    starts up in under a second. Using namespaces gives structure to a
    program and keeps it clean and clear. In Python everything is an
    object, so each object has a namespace itself. This is one of the
    reasons Python is so good at introspection.
  * **Introspection**. This is what follows from the object oriented nature
    of Python. Because a program has a clear structure, introspection
    is easy. Private variables only exist by convention, so you can access any part of the application, including some of Python's internals. Of course, in good programming practice you would not use private variables of other
    classes, but it's great for debugging!
  * **String manipulation**. This is incredibly easy in Python. What about
    this line of code which returns a right justified line of 30
    characters: ``"I code in Matlab".replace('Matlab','Python').rjust(30)``
  * **Portability**. Because Python is for free, your code can run
    everywhere. Further, it works on Windows, Linux, and OS X.
  * **Class and function definitions**. Functions and classes can be defined
    anywhere. In one file (whether it is a module or a script) you can
    design as many functions and classes as you like. You can even
    define one in the command shell if you really want to ...
  * **Great GUI toolkits**. With Python you can create a front-end for
    your application that looks good and works well. You can chose any
    of the major GUI toolkits like Wx or Qt. Pyzo comes with PySide (a
    wrapper for Qt).
