import os
import pygame

dirname = os.path.dirname(__file__)

class Entity(pygame.sprite.Sprite):
    def __init__(self, coordinates, direction, velocity, image_name):
        super().__init__()
        self.image = pygame.image.load(os.path.join(
            dirname, "..", "..", "assets", image_name))
        self.pos = pygame.Vector2(coordinates)
        self.rect = self.image.get_rect()
        self.rect.x = coordinates[0] - self.image.get_width()/2
        self.rect.y = coordinates[1] - self.image.get_width()/2
        self.direction = direction
        self.velocity = velocity

    def update_position(self):
        self.pos += self.direction * self.velocity

    def move(self):
        self.update_position()
        delta = self.pos - pygame.math.Vector2(self.rect.center)
        self.rect.move_ip(int(delta[0]),int(delta[1]))
