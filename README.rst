geodesic-area
============

.. image:: https://travis-ci.org/efren-cabrera/area.svg?branch=master
    :target: https://travis-ci.org/efren-cabrera/area

Calculate the area inside of any `GeoJSON <http://geojson.org/>`_ geometry. This is a port of Mapbox's `geojson-area <https://github.com/mapbox/geojson-area>`_ for Python.

Installation
------------

.. code::

  $ pip install area

Usage
-----

Simply pass a geojson string or python dictionary to the area function and get the area.

.. code::

  >>> from area import area
  >>> obj = {'type':'Polygon','coordinates':[[[-180,-90],[-180,90],[180,90],[180,-90],[-180,-90]]]}
  >>> area(obj)
  511207893395811.06

Test
----

.. code::

  $ python test.py


Credit
------

- `geojson-area <https://github.com/mapbox/geojson-area>`_
