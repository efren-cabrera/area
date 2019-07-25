# geoarea

[![travis](https://travis-ci.org/efren-cabrera/area.svg?branch=master)](https://travis-ci.org/efren-cabrera/area)


This is a fork from [geojson-area (python)](https://github.com/scisco/area). 
Calculate the area from lists of latitude and longitude coordinates.

Installation
------------

```
  $ pip install git+https://github.com/efren-cabrera/geoarea
```

Usage
-----

Simply pass a list of latitude and longitude

```
>>> from geoarea import area
>>> latitude_world = [-90, 90, 90, -90, -90]
>>> longitude_world = [-180, -180, 180, 180, -180]  
>>> area(latitude_world, longitude_world)
511207893395811.06
```

Test
----

```
  $ python test.py
```

Credit
------

- [geojson-area (python)](https://github.com/scisco/area)
- [geojson-area](https://github.com/mapbox/geojson-area)


References
----------

- https://trs.jpl.nasa.gov/bitstream/handle/2014/41271/07-0286.pdf
