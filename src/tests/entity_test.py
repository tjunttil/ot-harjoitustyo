import unittest
import pygame
from entities.sprites.entity import Entity

class TestEntity(unittest.TestCase):
    def setUp(self):
        self.nullvector = pygame.math.Vector2(0,0)
        self.entity = Entity(self.nullvector,self.nullvector, 0)

    def test_entity_is_not_none(self):
        self.assertNotEqual(self.entity, None)

    def test_starting_values_are_correct(self):
        self.assertEqual((self.entity.pos, self.entity.direction,
        self.entity._velocity), (self.nullvector, self.nullvector, 0))

    def test_update_position_does_nothing_if_velocity_zero(self):
        self.entity._update_position()
        self.assertEqual(self.entity.pos, self.nullvector)

    def test_update_position_changes_position_if_velocity_and_direction_nonzero(self):
        not_null_vector = pygame.math.Vector2(0,1)
        self.entity.direction = not_null_vector
        self.entity._velocity = 1
        self.entity._update_position()
        self.assertEqual(self.entity.pos, not_null_vector)
