import unittest
from entities.sprites.ship import Ship


class TestShip(unittest.TestCase):
    def setUp(self):
        self.ship = Ship((320,240))

    def test_ship_has_attributes_set_to_zero(self):
        self.assertEqual((self.ship.rect.x, self.ship.rect.y, self.ship.angle,
                         self.ship.velocity, self.ship.angular_velocity), (265, 185, 0, 0, 0))
    def test_move_ship_method_does_not_move_ship_if_velocity_unchanged(self):
        self.ship.move()
        self.assertEqual(self.space.pos, (265, 185))
