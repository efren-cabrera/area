import json
import unittest

from geoarea import area


f = open('illinois.json')
illinois = json.loads(f.read())

latitude_world = [-90, 90, 90, -90, -90]
longitude_world = [-180, -180, 180, 180, -180]

ILLINOIS_AREA = 145978332359.36746
world_area = 511207893395811.06


class AreaTestCase(unittest.TestCase):

    def test_world_area(self):
        self.assertAlmostEqual(area(latitude_world, longitude_world), world_area, places=0)

    def test_illinois_area(self):        
        illinois_area = area(*self.get_lat_lon(illinois["coordinates"][0][0]))
        self.assertAlmostEqual(illinois_area, ILLINOIS_AREA, places=3)

    def get_lat_lon(self, coordinate_pairs_list):
        latitude = [coordinate_pair[1] for coordinate_pair in coordinate_pairs_list]
        longitude = [coordinate_pair[0] for coordinate_pair in coordinate_pairs_list]
        return latitude, longitude


if __name__ == '__main__':
    unittest.main()
