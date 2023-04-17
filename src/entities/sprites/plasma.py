import os
import pygame
from .entity import Entity

dirname = os.path.dirname(__file__)

class Plasma(Entity):
    def __init__(self, coordinates, direction):
        super().__init__(coordinates, direction, 20, "plasma.png")
        #self.image = pygame.image.load(os.path.join(
        #    dirname, "..", "..", "assets", "plasma.png"))
        #self.rect = self.image.get_rect()
        #self.rect.x = coordinates[0] - self.image.get_width()/2
        #self.rect.y = coordinates[1] - self.image.get_width()/2
        #self.direction = direction
        #self.velocity = 20
        