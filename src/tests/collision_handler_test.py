import unittest
import pygame
from services.collision_handler import CollisionHandler
from entities.sprites.asteroid import Asteroid
from entities.sprites.plasma import Plasma
from entities.sprites.ship import Ship

class TestCollisionHandler(unittest.TestCase):
    def setUp(self):
        self.collision_handler = CollisionHandler()
        self.test_position = pygame.math.Vector2(0,0)
        self.ship = Ship(self.test_position)
        self.asteroids = pygame.sprite.Group()
        self.plasmas = pygame.sprite.Group()
        self.test_positions = self.create_test_positions()

    def create_test_positions(self):
        test_positions = []
        start = pygame.math.Vector2((10,10))
        shift = pygame.math.Vector2((50,0))
        previous = start
        for i in range(10):
            shift = (i+1)*shift.rotate(-90)
            new = previous + shift
            test_positions.append(new)
            previous = new
        return test_positions

    def test_check_ship_destruction_returns_false_when_no_collisions(self):
        ship_destruction = self.collision_handler.check_ship_destruction(self.ship, self.asteroids)
        self.assertEqual(ship_destruction, False)

    def test_check_ship_destruction_returns_true_when_superimposed(self):
        asteroid = Asteroid(self.test_position,1,1)
        self.asteroids.add(asteroid)
        ship_destruction = self.collision_handler.check_ship_destruction(self.ship, self.asteroids)
        self.assertEqual(ship_destruction, True)

    def test_handle_plasma_hits_returns_zero_when_no_plasma_hits(self):
        plasma_hits = self.collision_handler.handle_plasma_hits(self.plasmas, self.asteroids)
        self.assertEqual(plasma_hits, 0)

    def test_handle_plasma_hits_causes_hits_when_superimposed(self):
        hits = 0
        for position in self.test_positions:
            self.asteroids.add(Asteroid(position, 1,1))
            self.plasmas.add(Plasma(position,position))
        self.collision_handler.handle_plasma_hits(self.plasmas, self.asteroids)
        for asteroid in self.asteroids:
            hits += asteroid.hits
        self.assertEqual(hits, 10)

    def test_handle_plasma_hits_returns_number_of_destroyed_asteroids_when_superimposed(self):
        destroyed = 0
        for position in self.test_positions:
            self.asteroids.add(Asteroid(position, 1,1))
        for i in range(3):
            for asteroid in self.asteroids:
                position = asteroid.pos
                self.plasmas.add(Plasma(position, position))
            destroyed += self.collision_handler.handle_plasma_hits(self.plasmas, self.asteroids)
        self.assertEqual(destroyed, 10)
