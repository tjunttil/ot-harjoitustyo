import os
import pygame

dirname = os.path.dirname(__file__)


class Ship(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.og_image = pygame.image.load(os.path.join(
            dirname, "..", "..", "assets", "ship.png"))
        self.image = self.og_image
        self.rect = self.image.get_rect()
        self.rect.x = x - self.image.get_width()/2
        self.rect.y = y - self.image.get_width()/2
        self.angle = 0
        self.velocity = 0
        self.angular_velocity = 0

    def change_velocity(self, direction, change):
        linear_velocity, angular_velocity = direction
        # direction is given by a tuple (v,a) where v denotes the linear velocity and a the angular velocity change direction
        self.velocity += change*linear_velocity
        self.angular_velocity += change*angular_velocity

    def rotate(self, angle):
        self.image = pygame.transform.rotate(self.og_image, angle)
        self.rect = self.image.get_rect(center = self.rect.center)

    @property
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, value):
        self._angle = value
