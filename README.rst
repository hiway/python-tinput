========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        |
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/python-tinput/badge/?style=flat
    :target: https://readthedocs.org/projects/python-tinput
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/hiway/python-tinput.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/hiway/python-tinput

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/hiway/python-tinput?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/hiway/python-tinput

.. |requires| image:: https://requires.io/github/hiway/python-tinput/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/hiway/python-tinput/requirements/?branch=master

.. |version| image:: https://img.shields.io/pypi/v/tinput.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/tinput

.. |commits-since| image:: https://img.shields.io/github/commits-since/hiway/python-tinput/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/hiway/python-tinput/compare/v0.1.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/tinput.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/tinput

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/tinput.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/tinput

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/tinput.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/tinput


.. end-badges

Get user input() on commandline, with timeout.

* Free software: BSD license

Installation
============

::

    pip install tinput

Documentation
=============

https://python-tinput.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
