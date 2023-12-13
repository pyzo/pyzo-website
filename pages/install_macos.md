# Install Pyzo on MacOS


## Option 1: install using the binary

We [provide binaries](https://github.com/pyzo/pyzo/releases) to run Pyzo on MacOS.

* Download the `.dmg` disk image and mount it.
* Copy the Pyzo app to to the Applications directory.
* If you get a warning about Apple being unable to check the file, you must right-click-open the file.

The binaries are build on a relatively old version of macOS. If it does
not work, consider upgrading your OS or read on.


## Option 2: install from source

You can install Pyzo into most Python interpreters.
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
