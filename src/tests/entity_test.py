import unittest
import pygame
from entities.sprites.entity import Entity

class TestEntity(unittest.TestCase):
    def setUp(self):
        self.nullvector = pygame.math.Vector2(0,0)
        self.entity = Entity(self.nullvector,self.nullvector, 0, "plasma")
    
    def test_entity_is_not_None(self):
        self.assertNotEqual(self.entity, None)

    def test_starting_values_are_correct(self):
        self.assertEqual((self.entity.pos, self.entity.direction, self.entity.velocity), (self.nullvector, self.nullvector, 0))