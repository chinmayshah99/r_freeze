========
r_freeze
========


.. image:: https://img.shields.io/pypi/v/r_freeze.svg
        :target: https://pypi.python.org/pypi/r_freeze

.. image:: https://img.shields.io/travis/chinmayshah99/r_freeze.svg
        :target: https://travis-ci.com/chinmayshah99/r_freeze

.. image:: https://readthedocs.org/projects/r-freeze/badge/?version=latest
        :target: https://r-freeze.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/chinmayshah99/r_freeze/shield.svg
     :target: https://pyup.io/repos/github/chinmayshah99/r_freeze/
     :alt: Updates



Pipreqs for R


* Free software: MIT license
* Documentation: https://r-freeze.readthedocs.io.


Features
--------

* Generates the list of packages used in the project
* If the output file is specified as R, R script file is generated

Usage
-----


For printing the name of packages::

   r_freeze .

For creating a requirments file::

   r_freeze -o req.txt .

For creating a requirments as R script::

   r_freeze -o req.R .

For overwriting a requirments file::

   r_freeze -o req.R --overwrite .


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
