geoarea
============

.. image:: https://travis-ci.org/efren-cabrera/area.svg?branch=master
    :target: https://travis-ci.org/efren-cabrera/area

This is a fork from `geojson-area (python) <https://github.com/scisco/area>`_. 
Calculate the area from lists of latitude and longitude coordinates.

Installation
------------

.. code::

  $ pip install git+https://github.com/efren-cabrera/geoarea

Usage
-----

Simply pass a list of latitude and longitude

.. code::

  >>> from geoarea import geoarea
  >>> latitude_world = [-90, 90, 90, -90, -90]
  >>> longitude_world = [-180, -180, 180, 180, -180]  
  >>> geoarea(latitude_world, longitude_world)
  511207893395811.06

Test
----

.. code::

  $ python test.py


Credit
------

- `geojson-area (python) <https://github.com/scisco/area>`_
- `geojson-area <https://github.com/mapbox/geojson-area>`_


References
----------

- https://trs.jpl.nasa.gov/bitstream/handle/2014/41271/07-0286.pdf
