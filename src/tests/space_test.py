import unittest
from entities.space import Space
from math import *


class TestSpace(unittest.TestCase):
    def setUp(self):
        self.space = Space(1.0)

    def test_space_has_ship(self):
        self.assertNotEqual(self.space.ship, None)

    def test_spaceship_is_in_starting_position(self):
        self.assertEqual(
            (self.space.ship.rect.x, self.space.ship.rect.y), (265, 220))

    def test_move_ship_method_does_not_move_ship_if_velocity_unchanged(self):
        self.space.move_ship()
        self.assertEqual(
            (self.space.ship.rect.x, self.space.ship.rect.y), (265, 220))

    def test_change_velocity_changes_ship_velocity(self):
        self.space.change_ship_velocity((1, 0), 1)
        self.assertEqual((self.space.ship.velocity), 1)

    def test_changed_velocity_changes_ship_position_with_move_ship(self):
        self.space.change_ship_velocity((1, 0), 1)
        self.space.move_ship()
        self.assertNotEqual(
            (self.space.ship.rect.x, self.space.ship.rect.y), (265, 220))
    
    def test_changed_angular_velocity_changes_ship_angle_when_ship_moved(self):
        self.space.change_ship_velocity((0, 1), 1)
        self.space.move_ship()
        self.assertNotEqual(self.space.ship.angle, 0)

    def test_changing_angle_by_pi_leads_to_perpendicular_movement(self):
        self.space.ship.angle = pi/2
        ship_x,ship_y = self.space.ship.rect.x, self.space.ship.rect.y
        self.space.change_ship_velocity((1,0), 1)
        self.space.move_ship()
        self.assertEqual((self.space.ship.rect.x, self.space.ship.rect.y),(ship_x, ship_y + 1))

