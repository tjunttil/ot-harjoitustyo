from math import *
import pygame
from entities.sprites.ship import Ship


class Space:
    def __init__(self, scale):
        self.ship = Ship(320*scale, 240*scale)
        self.ship_pos = pygame.math.Vector2(self.ship.rect.center)
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.ship)

    def change_ship_velocity(self, direction, change):
        self.ship.change_velocity(direction, change)

    def update_object_positions(self):
        self.update_ship_position()
        #self.update_asteroid_positions()

    def move_objects(self):
        self.move_ship()
        self.move_asteroids()

    def update_ship_position(self):
        self.ship.angle += self.ship.angular_velocity
        movement = self.ship.velocity*self.ship.direction
        self.ship_pos += movement

    def move_ship(self):
        self.update_ship_position()
        angle = self.ship.angle
        self.ship.rotate(angle)
        delta = self.ship_pos - pygame.math.Vector2(self.ship.rect.center)
        self.ship.rect.move_ip(int(delta[0]),int(delta[1]))

    def update_asteroid_positions(self):
        pass

    def move_asteroids(self):
        pass
