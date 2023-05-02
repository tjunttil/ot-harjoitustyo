import pygame
from .entity import Entity
from .plasma import Plasma

class Ship(Entity):
    """A class for representing ship state and changes to it.

    Args:
        Entity (pygame.sprite.Sprite): a parent class for state and methods
        common to all entities.

    Attributes:
        parent class attributes
        original_image (pygame.image): the original image of the ship
        angle (float): the angle of the ship relative to the x-axis
        angular_velocity (float): the angular velocity of the ship
        collide_points: the points delimiting the actual ship shape 
        inside the image
    """
    def __init__(self, coordinates):
        """The constructor method for the class

        Args:
            coordinates (tuple): the starting coordinates for the ship center
        """
        super().__init__(coordinates, pygame.math.Vector2(1,0), 0)
        super().load_image("ship.png")
        self.original_image = self.image
        self.angle = 0
        self.angular_velocity = 0
        self.collide_points = self.calculate_collide_points()

    def change_velocity(self, direction, change):
        linear_velocity, angular_velocity = direction
        # direction is given by a tuple (v,a) where
        # v denotes the linear velocity and
        # a the angular velocity change direction
        self.velocity += change*linear_velocity
        self.angular_velocity += change*angular_velocity

    def rotate(self, angle):
        self.image = pygame.transform.rotate(self.original_image, angle)
        self.direction = pygame.math.Vector2(1,0).rotate(-angle)
        self.collide_points = self.calculate_collide_points()
        self.rect = self.image.get_rect(center = self.rect.center)

    def calculate_collide_points(self):
        center_vector = pygame.math.Vector2(self.rect.center)
        ship_length_vector = self.direction * self.original_image.get_width()/2
        ship_width_vector = self.direction.rotate(-90) * self.original_image.get_height()/4
        tip = center_vector + ship_length_vector
        left_side = center_vector + ship_width_vector
        right_side = center_vector - ship_width_vector
        left_corner = center_vector + 2 * ship_width_vector - ship_length_vector
        right_corner = center_vector - 2 * ship_width_vector - ship_length_vector
        back = center_vector - ship_length_vector
        return [tip, left_side, right_side, left_corner, right_corner, back]

    def fire_plasma(self):
        tip_location_vector = self.calculate_collide_points()[0]
        return Plasma(tuple(tip_location_vector), self.direction)

    def update_position(self):
        self.angle += self.angular_velocity
        super().update_position()

    def move(self):
        self.update_position()
        angle = self.angle
        self.rotate(angle)
        super().move()

    def return_tip(self):
        tip_location_vector = self.calculate_collide_points()[0]
