import os
import pygame

dirname = os.path.dirname(__file__)

class Entity(pygame.sprite.Sprite):
    def __init__(self, coordinates, direction, velocity):
        super().__init__()
        self.image = None
        self.rect = pygame.Rect(coordinates[0], coordinates[1], 0,0)
        self.pos = pygame.Vector2(coordinates)
        self.direction = direction
        self.velocity = velocity

    def update_position(self):
        self.pos += self.direction * self.velocity

    def move(self):
        self.update_position()
        delta = self.pos - pygame.math.Vector2(self.rect.center)
        self.rect.move_ip(int(delta[0]),int(delta[1]))

    def load_image(self, image_name):
        self.image = pygame.image.load(os.path.join(
            dirname, "..", "..", "assets", image_name))
        self.rect = self.image.get_rect()
        self.rect.x = self.pos[0] - self.image.get_width()/2
        self.rect.y = self.pos[1] - self.image.get_width()/2
