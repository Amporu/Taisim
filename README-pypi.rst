Simple and Easy API Wrapper for `r-spacex/SpaceX-API`_!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Documentation
-------------

This API Wrapper aims to provide a simple and easy way to use the
`SpaceX-API`_ in Python projects. See the `Wiki`_ for full wrapper
documentation.

Installation
------------

To install via ``pip`` use: ``pip install spacexPython``

Basic Usage
-----------

The usage of the wrapper is very easy. It does not require any
initialisation. Just import and start coding:

.. code:: python

   import spacexpython

   rocket_data = spacexpython.rockets.falconHeavy()
   print(rocket_data)

.. _r-spacex/SpaceX-API: https://github.com/r-spacex/SpaceX-API
.. _SpaceX-API: https://github.com/r-spacex/SpaceX-API
.. _Wiki: https://github.com/phadnisvinay30/SpaceX-Python/wiki
