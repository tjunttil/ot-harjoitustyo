import unittest
from services.coordinate_system import CoordinateSystem

class TestCoordinateSystem(unittest.TestCase):
    def setUp(self):
        self.coordinate_system1 = CoordinateSystem(1000,1000)
        self.coordinate_system2 = CoordinateSystem(200,300)
        self.coordinate_system3 = CoordinateSystem(124,816)

    def test_center_returns_center(self):
        points = [(500,500), (100,150), (62,408)]
        vectors = [self.coordinate_system1.vector(*point) for point in points]
        self.assertEqual(self.coordinate_system1.center(), vectors[0])
        self.assertEqual(self.coordinate_system2.center(), vectors[1])
        self.assertEqual(self.coordinate_system3.center(), vectors[2])

    def test_random_coordinates_returns_point_outside_space(self):
        random_coordinates = self.coordinate_system1.random_coordinates(2,2)
        first = random_coordinates[0]
        second = random_coordinates[1]
        self.assertTrue(first > 1000 or second > 1000
        or first < 0 or second < 0)
