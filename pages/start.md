# Getting started with Pyzo

<img src='pyzo_conda.png' width='75%' align='center'>


To get started with Pyzo, you need to install the Pyzo IDE (in which
you *write* your code) and a Python environment (in which you *run* your code).


<br />
## Step 1: install the Pyzo IDE

<img src='download.png' width='100px' align='right'>

Most users can select one of these:

* Windows:
  [Pyzo installer](https://github.com/pyzo/pyzo/releases/download/v4.12.8/pyzo-4.12.8-win64.exe)
  (64bit). If your AntiVirus complaints, [read this](https://github.com/pyzo/pyzo/issues/800).
* MacOS:
  [Pyzo dmg](https://github.com/pyzo/pyzo/releases/download/v4.12.8/pyzo-4.12.8-macos_x86_64.dmg).
  If you get a warning about Apple being unable to check the file, you must right-click-open the file.
* Linux:
  [Pyzo tarball](https://github.com/pyzo/pyzo/releases/download/v4.12.8/pyzo-4.12.8-linux_x86_64.tar.gz)
  (build on Ubuntu 18.04, 64bit).

Otherwise, see [all releases](https://github.com/pyzo/pyzo/releases)
for more downloads (e.g. 32/64 bit Windows zipfiles, and older versions).
Linux users can also [install Pyzo using Linux system packages](install_linux).
See the [installation page](install) for more information.

<br />
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


<br />
## Step 3: Configure Pyzo shell

In Pyzo you can configure one or more shells to target your Python
environment(s). Pyzo is usually pretty good at detecting any installed
Python environments, and will try to guide you to selecting a suitable
one.


<br />
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


<br />
## Further steps

You should now be set up to start coding! You can also learn more about
[using the IDE](guide) and about [using Python](learn).


<br />
## Updating

Pyzo and the Python environment can safely be updated/reinstalled independently from each-other.
Similarly, you can install multiple Python environments and use/manage them all via Pyzo.
Individual packages within a Python environment can be updated via ``update package_name``.
