# Configuring shells

<img src='pyzo_shell2.png' align='right'>

Via *Shell > Edit shell configurations*, you can edit and add
shell configurations. This allows you to for example select the
initial directory, or use a custom PYTHONPATH.

Each config has the following fields:

* **name**: the name of the shell config.
* **exe**: the executable for the Python interpreter to use. Use the dropdown
  menu to see what interpreters were detected by Pyzo.
* **ipython**: whether to use the IPython shell or not.
* **gui**: The gui toolkit to use. Enabling this allows you to do
  interactive plotting. By default this value is set on "auto".
* **pythonpath**: provide a directory name on each line. These directories are
  used by Python to search for modules. 
* **startupScript**: a script to run at startup. You can also just write a few
  lines of code here.
* **startDir**: the initial directory.
* **argv**: simulate command-line arguments passed to the interpreter.
* **environ**: environment variables to pass to the interpreter.
