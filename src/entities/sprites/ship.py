import pygame
from .entity import Entity

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
        super()._load_image("ship.png")
        self.__original_image = self.image
        self.__angle = 0
        self.__angular_velocity = 0
        self.collide_points = self.__calculate_collide_points()

    def change_velocity(self, direction, change):
        """A method for changing the (linear or angular) velocity of the ship.

        Args:
            direction (tuple): the direction of the change, with the x-coordinate corresponding
            to a change in linear velocity and the y-coordinate to a change in angular velocity,
            with a positive value corresponding to a change in the positive direction
            change (integer): a value (1 or -1) indicating whether the change itself is
            positive, increasing the velocity, or negative, setting it to zero.
        """
        linear_velocity, angular_velocity = direction
        self._velocity += change*linear_velocity
        self.__angular_velocity += change*angular_velocity

    def __rotate(self, angle):
        self.image = pygame.transform.rotate(self.__original_image, angle)
        self.direction = pygame.math.Vector2(1,0).rotate(-angle)
        self.collide_points = self.__calculate_collide_points()
        self.rect = self.image.get_rect(center = self.rect.center)

    def __calculate_collide_points(self):
        center_vector = pygame.math.Vector2(self.rect.center)
        ship_length_vector = self.direction * self.__original_image.get_width()/2
        ship_width_vector = self.direction.rotate(-90) * self.__original_image.get_height()/4
        tip = center_vector + ship_length_vector
        left_side = center_vector + ship_width_vector
        right_side = center_vector - ship_width_vector
        left_corner = center_vector + 2 * ship_width_vector - ship_length_vector
        right_corner = center_vector - 2 * ship_width_vector - ship_length_vector
        back = center_vector - ship_length_vector
        return [tip, left_side, right_side, left_corner, right_corner, back]

    def _update_position(self):
        """An override of the Entity update_position-method, updating the ship's
        angle as well.
        """
        self.__angle += self.__angular_velocity
        super()._update_position()

    def move(self):
        """An override of the Entity move-method, taking into account that the ship
        has an angle and the direction of movement is in the direction of the tip
        """
        self._update_position()
        angle = self.__angle
        self.__rotate(angle)
        super().move()

    def get_tip(self):
        """A method for getting the location vector of the ship's tip

        Returns:
            pygame.Vector2: the location vector of the ship's tip
        """
        return self.collide_points[0]

    @property
    def velocity(self):
        return self._velocity

    @property
    def angle(self):
        return self.__angle

    @property
    def angular_velocity(self):
        return self.__angular_velocity
