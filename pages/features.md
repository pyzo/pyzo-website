# List of features of the Pyzo IDE

General
-------

  * Powerful introspection (see below).
  * Allows various ways to interactively run code (see below).
  * Using an intuitive shortcut editor, a shortcut can be created for any item in the menu.
  * Various handy tools, plus the ability to make your own.
  * Choose between different Qt themes.
  * Full Unicode support in both editor and shell (this seems obvious, but was not trivial at the time :)).

Shell
-----

  * The pythonic shells run in a subprocess and can therefore be interrupted or killed. 
  * Several shells can be used simultaneously, and can be of different Python versions (v2.4 - v3.x).
  * Pypy is supported, Jython and IronPython may be too (untested).
  * Command history.
  * Text in the shell can be selected and copied. Text can be pasted to the command line.
  * The original stdout and stderr are printed to the shell (for C programs that print to file 1 or 2).
  * It is guaranteed that no stdout or stderr messages are dropped; 
    if the shell cannot keep up with displaying messages, the kernel is slowed down automatically 
    (try `while True: print(time.time())`).
  * Debugging next/step/continue.
  * Post-mortem debugging.
  * Enables using several GUI toolkits interactively: PySide, PyQt4, Tk, wx, fltk, GTK.
  * Supports removing previously printed text by using the backspace char.
  * Supports magic commands similar to IPython.
  * You can create multiple shell configurations 
    (different Python version, different GUI integration, etc.)
  * Use 'pip' or 'conda' commands to manage your packages.

Editor
------

  * Supports auto indentation.
  * Automatically determines the indentation width when loading a file.
  * Matlab-style cell system to mark code sections (by starting a line with '`##`').  
  * Syntax highlighting for Python, Cython, C, and more to come.
  * todo: Syntax schemes easily editable and extendable
  * Supports commenting and uncommenting selected lines.
  * Drag-'n-drop files or directories to open them.
  * Find/Replace (also supports regular expressions).
  * The line ending style can be changed.
  * Optionally use tabs, or insert tabs as spaces. 
  * Indentation guides.
  * todo: Brace matching.
  * View whitespace / line endings.
  * Zooming.
  * Undo / redo.
  * Highlighting of current line.  
  * Long line indicator.
  * Chooice of multiple fonts, Pyzo comes with two beautiful fonts by default.  
  * Breakpoints for debugging.


Introspection
-------------

  * Introspection information is queried from the active shell, and from the source code 
    (by continuously parsing the file in a separate thread). 
    (This is going to be integrated with the syntax parsing)
  * Auto completion for any object in the active Python session and all `__builtins__`.
  * Optional auto completion for Python keywords.
  * Auto completion for functions, classes, and class attributes defined in the current file in the editor 
    (taking inheritance into account, even if a super class is defined in the shell).
  * Shows signature of functions (from the shell or from the source) using a call-tip.
  * Interactive help for all objects in the active Python session by moving up/down the 
    auto completion list, by double-clicking on a name, or by filling in the name directly. 
  * Interactive help show the docstrings of properties (rather than of the returned object).

Interactivity (ways to run code)
--------------------------------
  * Run code by typing directly in the interactive shell.
  * Run selection:
    * Run current line if there is no selection.
    * Evaluate selection if there is a selection and it is on one line.
    * Run all (whole) selected lines if selection spans multiple lines.
  * Run cell (a cell is the piece of code between two lines starting with '`##`').
  * Run current file.
  * Run main file.
  * Run current file as a script.
  * Run main file as a script.

Standard tools
--------------

  * File browser: List all files in your projects by bookmarking the directories of your projects. 
    Easy switching between projects.
  * Source structure: a tool that lists the structure of the source in a tree widget. It can 
    list classes, functions (and methods), import statements, cells, and todo items.
  * Interactive help: a tool that displays help information interactively (on selection and 
    scrolling through an autocompletion list.)  
  * Workspace: lists all variables (also in debug mode).
  * File browser: browse files and search inside files.
  * Logger: a logger shell that displays Pyzo's log messaged and can be used for development or 
    for changing advanced settings.

  