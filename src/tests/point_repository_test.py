import unittest
from datetime import datetime
from services.point_repository import PointRepository
from build import build

class TestPointRepository(unittest.TestCase):
    def setUp(self):
        build()
        self.point_repository = PointRepository()
        self.time = datetime.now().strftime("%d.%m.%Y")
        self.points_a = ("user_a", 12, self.time)
        self.points_b = ("user_b", 34, self.time)

    def test_file_is_empty_after_build(self):
        self.assertEqual(len(self.point_repository.points_list()),
        0)

    def test_add(self):
        self.point_repository.add(self.points_a[0], self.points_a[1])
        points = self.point_repository.points_list()
        entry = points[0]
        self.assertEqual((entry[0], entry[1], entry[2]),
        self.points_a)

    def test_points_list(self):
        point_entries = [self.points_b, self.points_a]
        for entry in point_entries:
            self.point_repository.add(entry[0], entry[1])
        #entries = list(map(lambda x: (x[0],(x[1], self.time.strftime("%d.%m.%Y"))),point_entries))
        self.assertEqual(self.point_repository.points_list(), point_entries)

        for i in range(15):
            self.point_repository.add(self.points_a[0], self.points_a[1])
        self.assertEqual(len(self.point_repository.points_list()), 10)
       