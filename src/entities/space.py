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

    def check_ship_destruction(self):
        for collide_point in self.ship.collide_points:
            for asteroid in self.asteroids:
                if pygame.Rect.collidepoint(asteroid.rect, tuple(collide_point)):
                    return True
        return False

    def handle_plasma_hits(self):
        # points = 0
        # for a in self.asteroids:
        #     pygame.sprite.sprite_collide(a, self.plasmas, True)
        #     child_asteroids = a.fragment()
        #     for child in child_asteroids:
        #         self.add_sprite(child)
        #     points += 1
        # return points
        return len(pygame.sprite.groupcollide(self.plasmas, self.asteroids, True, True))

    def handle_asteroid_collision(self):
        pass

    def handle_collisions(self):
        return self.check_ship_destruction()
        # self.handle_plasma_hits()
        # self.handle_asteroid_collision()

    def random_parameters(self, w, h):
        # Creates a random position on the outer rim of space
        # and a direction towards inner space
        coordinates = choice([(randint(-w,self.scale*640 + w),choice([-h, self.scale*480 + h])),
            (choice([-w, self.scale*640 + w]), randint(-h, self.scale*480))])
        random_point = pygame.math.Vector2(randint(0,self.scale*640),randint(0,self.scale*480))
        direction =  random_point - pygame.math.Vector2(coordinates)
        normalized_direction = direction/pygame.math.Vector2.length(direction)
        return coordinates, normalized_direction

    def create_asteroid(self):
        if randint(20*self.difficulty,500) == 100:
            coordinates, direction = self.random_parameters(111,137)
            asteroid = Asteroid(coordinates, direction, self.difficulty/3, 1)
            self.add_sprite(asteroid, self.asteroids)
