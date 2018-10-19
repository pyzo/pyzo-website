# Installing additional packages

The Python ecosystem is "blessed" with (at least) two package managers.
Pip is Python's built-in solution. In earlier years, Pip was not well
suited for distributing scientific packages. Therefore, the Conda
package manager has been instrumental to make Python suitable for
scientific use on a large scale.

Currently, most scientific packages can be installed using both Pip and
Conda. Some packages may be easier to install with Conda. But the
reverse may also happen. You can install some packages with Pip and some
with Conda, but you should probably avoid mixing these two where possible.
You can only use Conda in a Miniconda or Anaconda environment.


## Command for convenience

Pyzo provides three sommands as a convenience that use conda if available, and otherwise pip:
``install xx``, ``update xx``, ``remove xx``.


## Install using Pip

```
pip install xx
```

The ``pip`` command downloads a package from the official [Python package
index](https://pypi.org). If the package is not  pure Python (i.e. needs
compilation) the package maintainer may have made a pre-compiled version
available. If not, you may want to try Conda.


## Install using conda

```
conda install xx
```

The ``conda`` command always installs pre-build packages. However, someone
must have made these pre-build package available for others to download.
Therefore it may not work for less common packages.

If the package is not available on the main channel, you can search on http://anaconda.org
for available packages. If you find that "John" has build the package
that you need, use ``conda install -c john xx``.

Otherwise, if a package is not available, you can always try Pip!


## Other solutions

If you are on Windows, you can visit 
[Gohlke's collection of Python packages](http://www.lfd.uci.edu/~gohlke/pythonlibs/).
Download the required ``.whl`` file and use ``pip install location/to/xxx.whl``.

You can always ask maintainers of the package how to install it, or ask
in Pyzo mailing list.
