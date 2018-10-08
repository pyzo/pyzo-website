Interactive mode vs running as script
=====================================

In Pyzo, you can run the current file or the current project's
main file as a script. This will first restart the shell to provide
a clean environment. The shell is also initialized differently:

Things done on shell startup in **interactive mode**:

  * sys.argv = ['']
  * sys.path is prepended with an empty string (current working directory)
  * The working dir is set to the "Initial directory" of the shell config
  * The ``PYTHONSTARTUP`` script is run

Things done on shell startup in **script mode**:

  * ``__file__ = <script_filename>``
  * ``sys.argv = [ <script_filename> ]``
  * ``sys.path`` is prepended with the directory containing the script
  * The working dir is set to the directory containing the script 

Depending on the settings of the *Project mananger*, the current project
directory may also be inserted in ``sys.path``.

When running a file (not as script) the working dir is not set to the directory
containing the script, unless the corresponding option is set.

Other than what is listed above, there are no differences between the two modes. 
In script mode, the GUI event loop is still integrated and you can interactively inspect your app.
