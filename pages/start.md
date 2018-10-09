# Getting started with Pyzo

<img src='pyzo_conda.png' width='75%' align='center'>
    

To get started with Pyzo, you need to install the Pyzo IDE (in which
you write your code) and a Python environment (in which you run your code).


## Step 1: install the Pyzo IDE

<img src='download.png' width='100px' align='right'>

  
Download the Pyzo installer for your system:
    
* [Pyzo for Windows](https://github.com/pyzo/pyzo/releases/download/v4.6.0/pyzo-4.6.0-win32.exe)
* [Pyzo for OS X](https://github.com/pyzo/pyzo/releases/download/v4.6.0/pyzo-4.6.0-osx64.dmg)
* [Pyzo for Linux](https://github.com/pyzo/pyzo/releases/download/v4.6.0/pyzo-4.6.0-linux64.tar.gz)
  (or install Pyzo [the Linux way](install_linux).)
* For more downloads/information see the [installation page](install)


## Step 2: install Python environment

<img src='download.png' width='100px' align='right'>

To run Python code, you need a Python interpreter.
Pyzo works with most Python interpreters. If you're not sure what to
use, don't worry, you can install multiple environments side-by-side, and
use each one from Pyzo. Just make sure to use Python&nbsp;3 (not&nbsp;Python&nbsp;2).

We recommend starting with either of these:

* The [regular Python](https://www.python.org/). Use `pip` to install additional packages.
* The [Anaconda](https://www.anaconda.com/download/) distribution comes with a lot of scientific
  packages. 
* The [Miniconda](https://conda.io/miniconda.html) distribution is a lighter version that starts
  with fewer packages. Use `conda` or `pip` to install additional packages.

We recommend installing in the default location, or at least a location
that can be written to without admin privileges, so that addtional
packages can be installed.


## Step 3: Configure Pyzo shell

In Pyzo you can configure one or more shells to target your Python
environment(s). Pyzo is usually pretty good at detecting any installed
Python environments, and will try to guide you to selecting a suitable
one.

You may need to open the shell configuration dialog (e.g. via menu >
shell > edit shell configuration), and set the value of "exe" to the
path of the Python executable.


## Step 4: Install Scientific packages

For scienctific computing with Python, you need a few extra packages.
In Pyzo's shell, type:

```
>>> install numpy
```
(On regular Python, you may need to do `pip install ...`.)
Hooray, you just installed a new package! Now type:

```
>>> install scipy pyqt matplotlib pandas sympy
```

Now you have the most important scientific Python packages (a.k.a. the scipy-stack).
If you need a package that is not yet installed, and the install command does not
work, see [this guide](install_packages).


## Further steps

You should now be set up to start coding! You can also learn more about
[using the IDE](guide) and about [using Python](learn).


## Updating

Pyzo and the Python environment can safely be updated/reinstalled independently from each-other.
Similarly, you can install multiple Python environments and use/manage them all via Pyzo.
Individual packages within a Python environment can be updated via ``update xx``.
