import unittest
import pygame
from entities.space import Space
from math import *


class TestSpace(unittest.TestCase):
    def setUp(self):
        self.space = Space(1.0)

    def test_space_has_ship(self):
        self.assertNotEqual(self.space.ship, None)

    def test_spaceship_is_in_starting_position(self):
        self.assertEqual(
            (self.space.ship.rect.x, self.space.ship.rect.y), (265, 185))

    # def test_adding_sprite_adds_it_to_all_sprites(self):
    #     sprite = pygame.sprite.Sprite()
    #     self.space.add_sprite(sprite, self.space.plasmas)
    #     new_group = pygame.sprite.Group()
    #     for sprite in [self.space.ship, sprite]:
    #         new_group.add(sprite)
    #     self.assertEqual(self.space.all_sprites, new_group)

    # def test_changed_velocity_changes_ship_position_with_move_ship(self):
    #     self.space.change_ship_velocity((1, 0), 1)
    #     self.space.move_ship()
    #     self.assertNotEqual(
    #         (self.space.ship.rect.x, self.space.ship.rect.y), (265, 220))
               
    # def test_changed_angular_velocity_changes_ship_angle_when_ship_moved(self):
    #     self.space.change_ship_velocity((0, 1), 1)
    #     self.space.move_ship()
    #     self.assertNotEqual(self.space.ship.angle, 0)
