import pygame
from .entity import Entity
from .plasma import Plasma

class Ship(Entity):
    def __init__(self, coordinates):
        super().__init__(coordinates, pygame.math.Vector2(1,0), 0)
        super().load_image("ship.png")
        self.og_image = self.image
        self.angle = 0
        self.angular_velocity = 0

    def change_velocity(self, direction, change):
        linear_velocity, angular_velocity = direction
        # direction is given by a tuple (v,a) where
        # v denotes the linear velocity and
        # a the angular velocity change direction
        self.velocity += change*linear_velocity
        self.angular_velocity += change*angular_velocity

    def rotate(self, angle):
        self.image = pygame.transform.rotate(self.og_image, angle)
        self.direction = pygame.math.Vector2(1,0).rotate(-angle)
        self.rect = self.image.get_rect(center = self.rect.center)

    def calculate_tip_position(self):
        center_vector = pygame.math.Vector2(self.rect.center)
        ship_length_vector = self.direction * self.og_image.get_width()/2
        return center_vector + ship_length_vector

    def fire_plasma(self):
        tip_location_vector = self.calculate_tip_position()
        return Plasma(tuple(tip_location_vector), self.direction)

    def update_position(self):
        self.angle += self.angular_velocity
        super().update_position()

    def move(self):
        self.update_position()
        angle = self.angle
        self.rotate(angle)
        super().move()
