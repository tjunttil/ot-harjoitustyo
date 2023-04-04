import unittest
from entities.space import Space

class TestSpace(unittest.TestCase):
    def setUp(self):
        self.space = Space(1.0)

    def test_space_has_ship(self):
        self.assertNotEqual(self.space.ship, None)

    def test_spaceship_is_in_starting_position(self):
        self.assertEqual((self.space.ship.rect.x,self.space.ship.rect.y),(265,185))

    def test_move_ship_method_does_not_move_ship_if_velocity_unchanged(self):
        self.space.move_ship()
        self.assertEqual((self.space.ship.rect.x,self.space.ship.rect.y),(265,185))

    def test_change_velocity_changes_ship_velocity(self):
        self.space.change_ship_velocity((1,0), 1)
        self.assertEqual((self.space.ship.velocity), 1)

    def test_changed_velocity_changes_ship_position_with_move_ship(self):
        self.space.change_ship_velocity((1,0), 1)
        self.space.move_ship()
        self.assertNotEqual((self.space.ship.rect.x,self.space.ship.rect.y),(265,185))
