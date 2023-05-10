import os
import pygame

dirname = os.path.dirname(__file__)

class Entity(pygame.sprite.Sprite):
    """A superclass for all entities

        Inherits the pygame.sprite.Sprite-class

        Attributes:
            image (pygame.image): the image of the entity
            rect (pygame.rect): the rect-object
            pos (pygame.math.Vector2): position of the entity as a vector
            direction (pygame.math.Vector2): direction of the entity as a vector
            velocity (float): the velocity
            radius (int): the radius of the smallest circle that fits inside the rect,
            used for collision detection
    """
    def __init__(self, coordinates, direction, velocity):
        """A constructor method for the class

        Args:
            coordinates (tuple): the starting coordinates of the entity,
            in the format (x,y) for x- and y-coordinates
            direction (pygame.math.Vector2): a vector describing the intitial direction
            of the entity
            velocity (float): the starting velocity of the entity
        """
        super().__init__()
        self.image = None
        self.rect = pygame.Rect(coordinates[0], coordinates[1], 0,0)
        self.pos = pygame.Vector2(coordinates)
        self.direction = direction
        self._velocity = velocity
        self.radius = 0

    def _update_position(self):
        """A method for updating the positon of the entity over one timestep based on
        the direction and the velocity
        """
        self.pos += self.direction * self._velocity

    def move(self):
        """A method used for moving entities in space. First updates the position,
        and then determines if this corresponds to a change in the integer-valued
        pygame-coordinates
        """
        self._update_position()
        delta = self.pos - pygame.math.Vector2(self.rect.center)
        self.rect.move_ip(int(delta[0]),int(delta[1]))

    def _load_image(self, image_name):
        """A method to load the entity image and create a corresponding rect-object

        Args:
            image_name (String): the file name for the image-file
        """
        self.image = pygame.image.load(os.path.join(
            dirname, "..", "..", "assets", image_name))
        self.rect = self.image.get_rect()
        self.radius = self.image.get_height()/2
        self.rect.x = self.pos[0] - self.image.get_width()/2
        self.rect.y = self.pos[1] - self.image.get_width()/2
