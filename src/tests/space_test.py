import unittest
from entities.space import Space
from entities.sprites.ship import Ship

class TestSpace(unittest.TestCase):
    def setUp(self):
        self.space = Space(1.0)

    def test_space_has_ship(self):
        self.assertNotEqual(self.space.ship, None)

    def test_spaceship_is_in_starting_position(self):
        self.assertEqual((self.space.ship.x,self.space.ship.y),(0,0))

    def test_move_ship_method_does_not_move_ship_if_velocity_unchanged(self):
        self.space.move_ship()
        self.assertEqual((self.space.ship.x,self.space.ship.y),(0,0))


