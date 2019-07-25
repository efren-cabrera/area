import json
import unittest

from area import area, area_from_lat_lon_list


f = open('illinois.json', 'U')
illinois = json.loads(f.read())

world = {
    'type': 'Polygon',
    'coordinates': [
        [
            [-180, -90],
            [-180, 90],
            [180, 90],
            [180, -90],
            [-180, -90]
        ]
    ]
}

latitude_world = [-90, 90, 90, -90, -90]
longitude_world = [-180, -180, 180, 180, -180]

illinois_area = 145978332359.36746
world_area = 511207893395811.06


class AreaTestCase(unittest.TestCase):

    def test_area_illinois_with_string(self):
        """ Computer the area of illinois with string input """

        # Go the top of the file
        f.seek(0)
        illinois = f.read()
        self.assertEqual(round(area(illinois), 2), round(illinois_area, 2))

    def test_area_illinois(self):
        """ Compute the area of illinois """
        self.assertEqual(round(area(illinois), 2), round(illinois_area, 2))

    def test_area_world(self):
        """ Compute the area of the whole world """
        self.assertEqual(area(world), world_area)

    def test_point_area(self):
        """ Compute the area of a point """
        self.assertEqual(area({'type': 'Point', 'coordinates': [0, 0]}), 0)

    def test_liststring_area(self):
        """ Compute the area of a line string """
        self.assertEqual(area({'type': 'LineString', 'coordinates': [[0, 0], [1, 1]]}), 0)

    def test_geometry_collection_area(self):
        """ Compute the area of a geometry collection """
        total = illinois_area + world_area
        self.assertEqual(area({'type': 'GeometryCollection', 'geometries': [world, illinois]}), total)

    def test_lat_lon_list_area(self):
        self.assertEqual(area_from_lat_lon_list(latitude_world, longitude_world), world_area)


if __name__ == '__main__':
    unittest.main()
