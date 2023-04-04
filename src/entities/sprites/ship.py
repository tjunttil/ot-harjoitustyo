import pygame
import os

dirname = os.path.dirname(__file__)

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(dirname, "..", "..", "assets", "ship.png"))
        self.rect = self.image.get_rect()
        self.rect.x = 320 - self.image.get_width()/2
        self.rect.y = 240 - self.image.get_width()/2
        self.angle = 0
        self.velocity = 0
        self.angular_velocity = 0
    
    def change_velocity(self, direction, change):
        v,a = direction
        self.velocity += change*v
        self.angular_velocity += change*a

    @property
    def angle(self):
        return self._angle
    
    @angle.setter
    def angle(self, value):
        self._angle = value      