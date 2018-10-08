# Getting started with Pyzo

<img src='pyzo_conda.png' width='75%' align='center'>
    

To get started with Pyzo, you need to install the Pyzo IDE (in which
you write your code) and a Python environment (in which you run your code).


## Step 1: install the Pyzo IDE

<img src='download.png' width='100px' align='right'>

  
Here are links to download:
    
* [Pyzo for Windows](https://github.com/pyzo/pyzo/releases/download/v4.6.0/pyzo-4.6.0-win32.exe)
* [Pyzo for OS X](https://github.com/pyzo/pyzo/releases/download/v4.6.0/pyzo-4.6.0-osx64.dmg)
* [Pyzo for Linux](https://github.com/pyzo/pyzo/releases/download/v4.6.0/pyzo-4.6.0-linux64.tar.gz)
  (or install Pyzo [the Linux way](install_linux).)
* For more downloads/information see the [installation page](install)


## Step 2: install Python environment

<img src='download.png' width='100px' align='right'>

To run Python code, you need a Python interpreter.
Pyzo works with most Python interpreters.
We recommend installing [miniconda](https://conda.io/miniconda.html)
or [anaconda](https://www.anaconda.com/download/) if you intend to do science,
because these make it very easy to install additional (scientific) packages.
Make sure to use Python 3, and not Python 2.

Here are direct links to download:
    
* [Miniconda for Windows (64 bit)](https://repo.continuum.io/miniconda/Miniconda3-latest-Windows-x86_64.exe) (grapical installer)
* [Miniconda for Linux (64 bit)](https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh)
* [Anaconda for OS X (64 bit)](https://www.anaconda.com/download/)

We recommend installing in the default location, or at least a location
that can be written to without admin privileges, so that addtional
packages can be installed.


## Step 2b: Tell Pyzo what environment to use

You can usually skip this step, because the environment is generally
automatically detected. If this is not the case (e.g. it was not
installed in the default location), just open the shell configuration
dialog (menu > shell > edit shell configuration), and set the value of
"exe" to the path of the Python executable.


## Step 3: Install Scientific packages

For scienctific computing with Python, you need a few extra packages.
In Pyzo's shell, type:

```
>>> install numpy
```

Hooray, you just installed a new package! Now type:

```
>>> install scipy pyqt matplotlib pandas sympy
```

Now you have the most important scientific Python packages (a.k.a. the scipy-stack).
If you need a package that is not yet installed, and the install command does not
work, see :ref:`this guide <install_packages>`.


## Further steps

You should now be set up to start coding! You can also learn more about
[using the IDE](guide) and about [using Python](learn).


## Updating

Pyzo and the Python environment can safely be updated/reinstalled independently from each-other.
Similarly, you can install multiple Python environments and use/manage them all via Pyzo.
Individual packages within a Python environment can be updated via ``update xx``.
