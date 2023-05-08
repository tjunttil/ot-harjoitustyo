import unittest
from datetime import datetime
from services.point_repository import PointRepository
from build import build

class TestPointRepository(unittest.TestCase):
    def setUp(self):
        self.point_repository = PointRepository()
        self.time = datetime.now()
        self.points_a = ("user_a", 12)
        self.points_b = ("user_b", 34)

    def test_file_is_empty_after_build(self):
        build()
        self.assertEqual(len(self.point_repository.points_list()),
        0)

    def test_add(self):
        self.point_repository.add(self.points_a[0], self.points_a[1])
        points = self.point_repository.points_list()
        self.assertEqual(((points[0])[0], (points[0])[1], (points[0])[2]),
        self.points_a)

    def test_points_list(self):
        point_entries = [self.points_a, self.points_b]
        for entry in point_entries:
            self.point_repository.add(entry[0], entry[1])
        entries = list(map(lambda x,y: (x,y, self.time.strftime("%d.%m.%Y")),point_entries))
        self.assertEqual(self.point_repository.points_list(), entries)
        