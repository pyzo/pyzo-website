.. _releasenotes:

Release notes
-------------

Version 2015a (0.2.6):

  * Latest version of all packages 
  * new version of IEP (v3.6).


Version 2014a (0.2.5):
  
  * Latest version of all packages and new version of IEP (v3.5).
  * Fixed that the conda executable/script was not present (issue #17)
  * More robust activation of Pyzo
  * Shebangs in /bin are initially relative instead of wrong (Linux/OSX)
  * Shebangs in /bin can be made absolute by running pyzo_activate (Linux/OSX)
  * The installer for Windows can optionally register the distribution, making
    it easier to install more packages
  * The installer for Windows can optionally associate .py files
  * The OSX IEP app is associated with .py files
  

Version 2013c (0.2.4):
  
  * Pyzo is now build on top of Conda. This makes the build process easier
    but also makes package management easier for Pyzo's users.
  * A 64 bit version on Windows
  * The OS X version is now 64 bit 
  * Install additional packages from the shell via ``pip install X``
  * Install additional packages from the shell via ``conda install X``
  * Activating the Pyzo distro so Windows installers (e.g. from Gohlke) just work.
  * Support for Numba (`conda install numba`)!

  
Version 2013b (0.1.3):
    
  * Start naming the releases using year plus a/b/c as sequence notation.
  * Pyzo is now build for Mac too!
  * Python 3.3 is now used.
  * Added an executable to launch IPython notebook.
  * The python executable is build using Python's original C code
    (instead of cx_Freeze). Therefore the exe behaves much more like the real
    Python, with less effort. The other executables still use cx_Freeze,
    which brings us a lot of flexibility.
  * New versions of several packages, including the IDE.
    
    
Version 0.1.2:
    
  * Fixed a severe bug for Ubuntu 12.10.

Version 0.1.1:
    
  * The first release!
