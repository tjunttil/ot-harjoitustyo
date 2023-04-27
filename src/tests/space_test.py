import unittest
from entities.space import Space
from services.collision_handler import CollisionHandler
from services.group_handler import GroupHandler
from services.coordinate_system import CoordinateSystem


class TestSpace(unittest.TestCase):
    def setUp(self):
        collision_handler = CollisionHandler()
        coordinate_system = CoordinateSystem(640, 480)
        self.group_handler = GroupHandler()
        self.space = Space(self.group_handler, collision_handler, coordinate_system)

    def test_space_has_ship(self):
        self.assertNotEqual(self.space.ship, None)

    def test_spaceship_is_in_starting_position(self):
        self.assertEqual(
            (self.space.ship.pos[0], self.space.ship.pos[1]), (320, 240))

    # def test_add_entity_adds_it_to_all_sprites(self):
    #     entity = Entity((0,0), )
    #     self.space.add_sprite(sprite, self.space.plasmas)
    #     new_group = pygame.sprite.Group()
    #     for sprite in [self.space.ship, sprite]:
    #         new_group.add(sprite)
    #     self.assertEqual(self.space.all_sprites, new_group)

    def test_changed_velocity_changes_ship_position_with_move_ship(self):
        self.space.change_ship_velocity((1, 0), 1)
        self.space.move_objects()
        self.assertNotEqual(
            (tuple(self.space.ship.pos)), (320, 240))

    def test_changed_angular_velocity_changes_ship_angle_when_ship_moved(self):
        self.space.change_ship_velocity((0, 1), 1)
        self.space.move_objects()
        self.assertNotEqual(self.space.ship.angle, 0)

    def test_firing_ship_cannon_adds_plasma_to_plasmas_group(self):
        self.space.fire_ship_cannon()
        self.assertNotEqual(self.group_handler.elements(self.space.plasmas), [])
