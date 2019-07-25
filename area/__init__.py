from math import pi, sin, radians

WGS84_RADIUS = 6_378_137


def _ring_area(coordinates) -> float:
    """
    Calculate the approximate _area of the polygon were it projected onto
        the earth.  Note that this _area will be positive if ring is oriented
        clockwise, otherwise it will be negative.

    Reference:
        Robert. G. Chamberlain and William H. Duquette, "Some Algorithms for
        Polygons on a Sphere", JPL Publication 07-03, Jet Propulsion
        Laboratory, Pasadena, CA, June 2007 http://trs-new.jpl.nasa.gov/dspace/handle/2014/40409

    @Returns

    {float} The approximate signed geodesic _area of the polygon in square meters.
    """
    coordinates_length = len(coordinates)
    if coordinates_length <= 2:
        return 0
    area = 0
    for i in range(0, coordinates_length):
        if i == (coordinates_length - 2):
            lower_index = coordinates_length - 2
            middle_index = coordinates_length - 1
            upper_index = 0
        elif i == (coordinates_length - 1):
            lower_index = coordinates_length - 1
            middle_index = 0
            upper_index = 1
        else:
            lower_index = i
            middle_index = i + 1
            upper_index = i + 2

        p1 = coordinates[lower_index]
        p2 = coordinates[middle_index]
        p3 = coordinates[upper_index]

        area += (radians(p3[0]) - radians(p1[0])) * sin(radians(p2[1]))
    area *= WGS84_RADIUS**2 / 2
    return area

def area(latitude, longitude) -> float:
    coordinates = [coodinates_pair for coodinates_pair in zip(longitude, latitude)]
    return _ring_area(coordinates)
