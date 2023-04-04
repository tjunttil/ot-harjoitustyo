import pygame
import math
from entities.sprites.ship import Ship

class Space:
    def __init__(self, scale):
        self.ship = Ship()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.ship)

    def change_ship_velocity(self, direction, change):
        self.ship.change_velocity(direction, change)

    def move_ship(self):
        self.ship.angle += self.ship.angular_velocity
        angle = self.ship.angle
        x = self.ship.velocity
        self.ship.rect.move_ip(int(x*math.cos(angle)),int(x*math.sin(angle)))