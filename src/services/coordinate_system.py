from random import randint, choice
import pygame

class CoordinateSystem:
    """A class for handling coordinates in terms of vectors

    Attributes: 
        width (int): the width of the coordinate system
        height (int): the height of the coordinate system
    """
    def __init__(self, width, height):
        """The constructor of the class

        Args:
            width (int): the width of the coordinate system
            height (int): the height of the coordinate system
        """
        self.__width = width
        self.__height = height

    def vector(self,x_coordinate,y_coordinate):
        """Produces a pygame.math.Vector2 object with the given coordinates

        Args:
            x_coordinate (float): the x-coordinate of the vector to be produced
            y_coordinate (float): the y-coordinate of the vector to be produced

        Returns:
            pygame.math.Vector2: the vector with the given coordinates
        """
        return pygame.math.Vector2(x_coordinate,y_coordinate)

    def length(self, vector):
        """ Calculates the length of a vector using pygame.math.Vector2

        Args:
            vector (pygame.math.Vector2): the vector one wants to know the length of

        Returns:
            float: the length of the vector
        """
        return pygame.math.Vector2.length(vector)

    def random_coordinates(self, object_width, object_height):
        """ Creates a random position for an object on the outer rim
        of the coordinate system.

        Args:
            object_width (int): the width of the object
            object_height (int): the height of the object

        Returns:
            pygame.math.Vector2: first element corresponds to a random x-coordinate
            and the second to a random y-coordinate
        """
        random_x = randint(int(-self.__width - object_width/2), int(self.__width + object_width/2))
        random_y = randint(int(-self.__height - object_height/2),
        int(self.__height + object_height/2))
        coordinates = [random_x, random_y]
        max_coordinates = [self.__width + object_width/2, self.__height + object_height/2]
        max_index = choice([0,1])
        max_sign = choice([-1, 1])
        coordinates[max_index] = max_coordinates[max_index]*max_sign
        return self.vector(coordinates[0], coordinates[1])

    def random_direction(self, coordinates):
        """ Produces a random, normalized direction towards the interior of the 
        coordinate system

        Args:
            coordinates (pygame.math.Vector2): the starting coordinates for the direction-vector

        Returns:
            pygame.math.Vector2: the direction vector of length 1 towards the interior
        """
        random_point = self.vector(randint(0,self.__width),randint(0,self.__height))
        direction =  random_point - coordinates
        normalized_direction = direction/self.length(direction)
        return normalized_direction

    def center(self):
        return self.vector(self.__width/2, self.__height/2)
