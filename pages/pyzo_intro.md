# A short introduction to working with Pyzo

## The Pyzo IDE consists of two main components

<img src='pyzo_two_components.png' align='center'>

You can use execute commands directly in the **shell**,
or you can write code in the **editor** and execute that.


## The editor is where you write your code

<img src='pyzo_editor.png' align='right'>

In the editor, each open file is represented as a tab. By
right-clicking on a tab, files can be run, saved, closed, etc.

The right mouse button also enables one to make a file the 
**main file** of a project. This file can be recognized by its star
symbol, and it enables running the file more easily.


## The shell is where your code gets executed

<img src='pyzo_shell1.png' align='right'>
    
When Pyzo starts, a default shell is created. You can add more
shells that run simultaneously, and which may be of different
Python versions. 

Shells run in a sub-process, such
that when it is busy, Pyzo itself stays responsive, allowing you
to keep coding and even run code in another shell.


## Running code

<img src='pyzo_run1.png' align='right' width='250px'>

Pyzo supports several ways to run source code in the editor. 
(see also the "Run" menu):

  * **Run selection:** if there is no selected text, the
    current line is executed; if the selection is on a single line, the
    selection is evaluated; if the selection spans multiple lines, Pyzo
    will run the the (complete) selected lines.
  * **Run cell:** a cell is everything between two commands starting
    with ``##`` or ``#%%``.
  * **Run file:** this runs all the code in the current file. 
  * **Run project main file:** runs the code in the current project's
    main file.


## Tools for your convenience

<img src='pyzo_tools1.png' align='right'>

Via the *Tools menu*, one can select which tools to use. The tools can
be positioned in any way you want, and can also be un-docked.

Note that the tools system is designed such that it's easy to
create your own tools. Look at the online wiki for more information,
or use one of the existing tools as an example. 