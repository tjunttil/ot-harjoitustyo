import pygame
from entities.sprites.ship import Ship


class Space:
    def __init__(self, scale):
        self.ship = Ship((320*scale, 240*scale))
        self.asteroids = pygame.sprite.Group()
        self.plasmas = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.ship)

    def add_sprite(self,sprite, group):
        group.add(sprite)
        self.all_sprites.add(sprite)

    def change_ship_velocity(self, direction, change):
        self.ship.change_velocity(direction, change)

    def move_objects(self):
        for entity in self.all_sprites:
            entity.move()

    def fire_ship_cannon(self):
        plasma = self.ship.fire_plasma()
        self.add_sprite(plasma, self.plasmas)
