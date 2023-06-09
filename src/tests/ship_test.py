import unittest
from entities.sprites.ship import Ship


class TestShip(unittest.TestCase):
    def setUp(self):
        self.ship = Ship((320,240))

    def test_ship_has_attributes_set_to_zero(self):
        self.assertEqual((self.ship.angle,
                         self.ship.velocity, self.ship.angular_velocity), (0, 0, 0))

    def test_move_ship_method_does_not_move_ship_if_velocity_unchanged(self):
        self.ship.move()
        self.assertEqual(tuple(self.ship.pos), (320, 240))

    def test_update_position_changes_angle_when_angular_velocity_nonzero(self):
        self.ship.change_velocity((0,1),1)
        self.ship._update_position()
        self.assertEqual(self.ship.angle, 1)

    def test_change_velocity_changes_ship_velocities_positive(self):
        self.ship.change_velocity((1,1),1)
        self.assertEqual((self.ship.velocity, self.ship.angular_velocity), (1,1))

    def test_update_position_changes_coordinates_when_linear_velocity_positive(self):
        self.ship.change_velocity((1,0),1)
        self.ship._update_position()
        self.assertEqual(tuple(self.ship.pos), (321,240))

    def test_change_velocity_changes_ship_velocities_negative(self):
        self.ship.change_velocity((1,1),-1)
        self.assertEqual((self.ship.velocity, self.ship.angular_velocity), (-1,-1))

    def test_rotating_by_90_degrees_changes_direction_to_perpendicular(self):
        self.ship._Ship__rotate(-90)
        self.assertEqual(tuple(self.ship.direction), (0,1))

