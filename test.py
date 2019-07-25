import json
import unittest

from area import area


f = open('illinois.json')
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

    def test_lat_lon_list_area(self):
        self.assertAlmostEqual(area(latitude_world, longitude_world), world_area, places=0)


if __name__ == '__main__':
    unittest.main()
