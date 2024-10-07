# Run fast code in Python

Speed is a controversial issue. Is C# faster than Java? Is C faster
than C++? Is Python faster than Matlab? These questions always lead to
people stating that one is faster than another, and others claiming the
contrary. Some even take the trouble performing benchmarks.

Python is an interpreted language (just like Matlab), which means that
rather than compiling the complete program, bits of code can executed
in a running program/session. This is what makes it so suitable for
scientific computing: you can very quickly run snippets of code in a
sequence, or run the same piece of code repeatedly while improving it
(rapid prototyping).

Unfortunately, this brings the disadvantage of speed; for-loops are
interpreted and thus much slower than for-loops in C or C++. Remember
though, that *writing* a program in C/C++ rather than Python would often
cost you a considerable amount more time. Matlab and Python are about
equally fast as they suffer from the same problem, but both implement
functions like convolution etc. in C and will thus be as fast as they
can get.

Fortunately, there are several solutions that allow you to write
code that will run fast in Python:

  * [Cython](http://cython.org/) is allows you to write normal Python
    code and then add type annotations. This code is first translated
    to C code, which is in turn compiled to machine code. In effect,
    if you do it right, your code will become as fast as C. The downside
    is that you need a C compiler on your machine.

  * [Numba](http://numba.pydata.org/) allows compilation (via LLVM)
    of array-oriented Python code with only adding a single line of
    code. To use Numba in Pyzo,  do ``conda install numba``.

  * Ctypes is a built-in library that allows one to call function in a
    dynamic library. This can be a very effective means to communicate
    with existing code. No compilation required.

  * Cython can also be used to wrap your existing C/C++ code for Python.
    You are then using Cython in a way that is similar to Matlab's mex-files.
