from random import randint, choice
import pygame
from entities.sprites.ship import Ship
from entities.sprites.asteroid import Asteroid


class Space:
    def __init__(self, scale):
        self.difficulty = 1
        self.scale = scale
        self.ship = Ship((320*scale, 240*scale))
        self.asteroids = pygame.sprite.Group()
        self.plasmas = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.ship)

    def add_sprite(self,sprite, group):
        group.add(sprite)
        self.all_sprites.add(sprite)

    def move_objects(self):
        for entity in self.all_sprites:
            entity.move()

    def fire_ship_cannon(self):
        plasma = self.ship.fire_plasma()
        self.add_sprite(plasma, self.plasmas)

    def random_parameters(self, w, h):
        # Creates a random position on the outer rim of space
        # and a direction towards inner space
        coordinates = choice([(randint(-w,self.scale*640 + w),choice([-h, self.scale*480])),
            (choice([-w, self.scale*640]), randint(-h, self.scale*480))])
        random_point = pygame.math.Vector2(randint(0,self.scale*640),randint(0,self.scale*480))
        direction =  random_point - pygame.math.Vector2(coordinates)
        normalized_direction = direction/pygame.math.Vector2.length(direction)
        return coordinates, normalized_direction

    def create_asteroid(self):
        if randint(self.difficulty,200) == 9:
            coordinates, direction = self.random_parameters(111,137)
            asteroid = Asteroid(coordinates, direction)
            self.add_sprite(asteroid, self.asteroids)
