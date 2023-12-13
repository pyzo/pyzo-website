# Install Pyzo on Windows


## Option 1: install using the binary

We [provide binaries](https://github.com/pyzo/pyzo/releases) to run Pyzo on Windows.

* The easiest way to install Pyzo on Windows is to use the installer
  (which does not require admin rights).
* If your AntiVirus complaints, [read this](https://github.com/pyzo/pyzo/issues/800).
* Alternatively, you can download and unpack the zip-file. You can place
  the Pyzo directory anywhere you like.
* If you have a 32bit Windows distribution, select the win32 zipfile.


## Uninstalling

To remove Pyzo, either run the uninstaller (when you used the
installer on Windows), or simply remove the directory that you unpacked
from the archive.


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

You can also create a shortcut on your desktop for it. Create a new shortcut with "python.exe" as a target.
Then edit it and make the target end with "pythonw.exe -m pyzo". To set the Pyzo icon
use the *pyzo/resources/appicons* folder.


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
