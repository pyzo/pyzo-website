# Getting started with Pyzo

<img src='pyzo_conda.png' width='75%' align='center'>


To get started with Pyzo, you need to install the Pyzo IDE (in which
you *write* your code) and a Python environment (in which you *run* your code).


## Step 1: install the Pyzo IDE

<img src='download.png' width='100px' align='right'>


Download the Pyzo installer for your system:

* [Pyzo for Windows 10](https://github.com/pyzo/pyzo/releases/download/v4.8.0/pyzo-4.8.0-win64-windows10.exe) or [Pyzo for Windows 7 and higher](https://github.com/pyzo/pyzo/releases/download/v4.8.0/pyzo-4.8.0-win64.exe) (both 64bit)
* [Pyzo for OS X](https://github.com/pyzo/pyzo/releases/download/v4.8.0/pyzo-4.8.0-osx64.dmg) (OS X 10.11 El Capitan or higher)
* [Pyzo for Linux](https://github.com/pyzo/pyzo/releases/download/v4.8.0/pyzo-4.8.0-linux64.tar.gz) (Ubuntu 16.04 or equivalent/higher, or install Pyzo [the Linux way](install_linux).)
* For more downloads/information see [all releases](https://github.com/pyzo/pyzo/releases) or the [installation page](install)


## Step 2: install Python environment

<img src='download.png' width='100px' align='right'>

To run Python code, you need a Python interpreter.
Pyzo works with most Python interpreters. If you're not sure what to
use, don't worry, you can install multiple environments side-by-side, and
use each one from Pyzo. Just make sure to use Python&nbsp;3 (not&nbsp;Python&nbsp;2).

We recommend starting with either of these:

* The [regular Python](https://www.python.org/). Additional packages can be installed using `pip`.
* The [Anaconda](https://www.anaconda.com/download/) distribution comes with a lot of scientific
  packages.
* The [Miniconda](https://conda.io/miniconda.html) distribution is a lighter version that starts
  with fewer packages. Additional packages can be installed using `conda` or `pip`.

We recommend installing in the default location, or at least a location
that can be written to without admin privileges, so that addtional
packages can be installed.


## Step 3: Configure Pyzo shell

In Pyzo you can configure one or more shells to target your Python
environment(s). Pyzo is usually pretty good at detecting any installed
Python environments, and will try to guide you to selecting a suitable
one.


## Step 4: Install additional packages

Depending on you needs, you might need a few extra packages. In Pyzo's shell, type:

```
install requests
```
Hooray, you just installed a new package! For details see [this guide](install_packages).
For scienctific computing, you may want to install this set of the most important scientific packages (a.k.a. the scipy-stack):

```
install numpy scipy pandas matplotlib sympy pyqt
```


## Further steps

You should now be set up to start coding! You can also learn more about
[using the IDE](guide) and about [using Python](learn).


## Updating

Pyzo and the Python environment can safely be updated/reinstalled independently from each-other.
Similarly, you can install multiple Python environments and use/manage them all via Pyzo.
Individual packages within a Python environment can be updated via ``update package_name``.
