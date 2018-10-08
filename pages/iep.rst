.. _iepmerge:

================================
Merging the Pyzo and IEP project
================================


.. image:: _static/pyzo_iep_merge.png

We merged the Pyzo and IEP projects into a single project:

* The new name is Pyzo
* The logo is the one from IEP
* It is not longer a distribution, but a lightweight IDE (like IEP was)
  that helps the user install a (miniconda) environment.

Why? In short, there are two main reasons:

* Bundling the environment with the IDE caused several problems.
* It was a lot of work to maintain for us (which we do in our free time).


Some history ...

Previously, there were two projects. IEP was the IDE, and Pyzo was a
distribution that made it easy to install a Python environment and the
IEP IDE.

Over the years, the conda environment (with miniconda and anaconda as
its installers) have become increasingly powerful. In fact, Pyzo has
been based on conda for a while. Nevertheless, the maintenance of Pyzo
proved a significant burden, and we found that we were not releasing
as often as we wanted.

Furthermore, there were several cases of problems causes by the fact
that the IDE worked from the same environment in which the computing
was done, especially for updating packages.

Therefore we decided to decouple the distribution; people can just
install a conda environment. We made changes to the IDE to guide the
user in this process, so that getting started is still easy as py.
