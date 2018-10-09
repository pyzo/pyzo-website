# Why Python


<img src='python_logo.png' width='50%' align='right'>


[Python](http://www.python.org/about/) is a very-high-level dynamic
object-oriented programming language. It's designed to be easy to
program and easy to read. [Guido van Rossum](http://en.wikipedia.org/wiki/Guido_van_Rossum) started the design
of Python in 1980. Over the years, Python has gained popularity in a
broad range of fields from web development, games, usage as a scripting
language, and of course science and engineering. Guido still plays the
lead role in the development of Python and is sometimes referred to as
the Benevolent Dictator For Life.


## Python is open

Python is [open source software](http://www.opensource.org/), distributed under a liberal license,
and can thus be distributed freely, even for commercial use. This
openness makes that Python plays well with with other languages and is
easily extendible.


## Python is general purpose

Python is a general purpose language, which means that many things are
made easy. Examples are string processing, reading/writing files,
sockets, websites (such as this one), databases, GUI's. This is why it has been adopted
by so many people, and for such a wide range of tasks. The large 
[user community](http://python.org/community/) is very active and 
known as one of the friendliest around.

It's ease of use for general tasks makes Python very suitable for
education. For science this is also an advantage, as scientist often
need to load data, visualize it, and maybe control it via a user
interface. For commercial applications this means that many things work
out of the box, saving time and money.

## Python is dynamic

*Note: Strictly speaking Python is a language specification, and might be
compiled as well as interpreted. Pyzo is based on cPython, the most
common Python implementation which uses an interpreter written in C.*

Being a [dynamic language](http://en.wikipedia.org/wiki/Dynamic_programming_language) 
means that new code can be executed during
runtime without limitations. This is incredibly useful in science and
engineering, or any other situation in which the programmer is designing
a complex algorithm. It means that the user does not have to go through
the compile-run-debug cycle every time he makes a change to the code.
Instead, a piece of code (a part of an algorithm, for example) can be
repeatedly changed and executed in the same interpreter. This results
in a highly interactive environment, which shortens the development
cycle significantly (rapid prototyping). When using with large datasets
(for instance CT or MRI) these only have to be loaded once into the
interpreter, after which the user can repeatedly change and execute a
piece of code.


## Python is easy to read

Python is designed to be easy to read. This is more important than you
might think, because a common problem with software is that 
[it's harder to read code than to write it](http://www.joelonsoftware.com/articles/fog0000000069.html). 
Better readability makes that it easier
to share code or to work on software projects with other people. As
your algorithms become more complex (as they often do in science) it
is great to be able to focus on the algorithm without having to write
complex code to do simple things: it helps keep your algorithms as
simple as possible. For education it's clear that readability counts.

Python uses indentation to give structure to the code. People who are
used to another language often [complain](http://forums.xkcd.com/viewtopic.php?f=11&t=22725) about the absence of braces.
But this one of the key advantages of Python! In languages that use
braces, people also use indentation to make it more readable for other
people. So they use braces to tell the program what they mean, and
indentation to tell other people what they mean. This gives room for
ambiguity. In Python there is just one way to denote structure, in a
way that is easy for both humans and computers to read. There is just
one thing to watch out for: never mix tabs and spaces. A proper
IDE will prevent you from doing that.


## Python is great at introspection

In Python, everything is an object. And these objects are very "open".
Strictly speaking there are no private variables. Instead, by convention
a variable that starts with an underscore is said to be private. This
helps a lot during debugging, because all objects of interest can
generally be accessed and inspected.

This "openness" means that it is possible to write dirty programs, or
apply "hacks" to solve a certain problem. This is ok if the programmer
is testing something, but it is the responsibility of the programmer
to avoid these, or rewrite them to nicer code as soon as possible.

Further, Python uses the concept of [docstrings](http://en.wikipedia.org/wiki/Docstring), 
which are multi-line strings defined right below a function or class
definition and which contains the documentation for that object. These
can be accessed at runtime, allowing the IDE to display them to the
user at the right moment.
