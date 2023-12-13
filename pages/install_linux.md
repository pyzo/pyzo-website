# Install Pyzo on Linux


## Option 1: install using the binary

We [provide binaries](https://github.com/pyzo/pyzo/releases) to run Pyzo on Linux.

* To install Pyzo on Linux, download and extract the archive
  corresponding to your architecture.
* In case you want to place a link on your desktop for convenience,
  icons are in the *source/pyzo/resources/appicons* folder.
* The binaries for Linux are build on a relatively old Linux
  and should therefore work on most modern Linux distros.

Unfortunately, these binaries sometimes suffer from problems (most
notably ugly/nonnative fonts) on certain distributions. If this is the
case for you, read on.


## Option 2: install via Flatpak

Pyzo is also available as a [Flatpak](https://flatpak.org) package on
[Flathub](https://flathub.org/apps/details/org.pyzo.pyzo).


## Option 3: install using native Python and Qt

You can also install Pyzo via the system packages. Pyzo runs on Python
3.6 and up, and needs a Qt lib (one of PySide6, PySide2, PyQt6, PyQt5).
It has no further dependencies, so there is little risk of version
conflicts for packages that your system relies on. This should do the
trick:

```
$ sudo apt-get install python3-pip python3-pyqt5
$ sudo python3 -m pip install pyzo --upgrade
```

Then start Pyzo using:
```
$ pyzo
```

Instead of ``apt-get`` you may need to use ``yum`` or other, depending on your
distribution.

For the Python environment to run your code in, you can either use the Python
interpreter that comes with your system, or install miniconda/anaconda
as explained in the [quickstart](start).


## Option 4: install from source

You can install Pyzo into most Python interpreters. This is similar to the method above,
except we use `pip` also to install Qt.
In the below command you can replace "pyside6" with "pyqt6", "pyside2" or "pyqt5":
```
$ python -m pip install -U pyside6 pyzo
```
Then run it with:
```
$ pyzo
```


## Hacking on Pyzo

If you want to hack on Pyzo, install the source using pip in developer mode:
```
$ git pull https://github.com/pyzo/pyzo.git
$ cd pyzo
$ python -m pip install -e .
```


## Eula

Pyzo distro is free software. No limitations, no DRM. Please read the Pyzo
distro end user agreement for details: [Pyzo EULA](pyzo_eula.txt).
