import unittest
from entities.sprites.ship import Ship


class TestShip(unittest.TestCase):
    def setUp(self):
        self.ship = Ship(320,240)

    def test_ship_has_attributes_set_to_zero(self):
        self.assertEqual((self.ship.rect.x, self.ship.rect.y, self.ship.angle,
                         self.ship.velocity, self.ship.angular_velocity), (265, 220, 0, 0, 0))
