from random import randint
from entities.sprites.ship import Ship
from entities.sprites.asteroid import Asteroid
from entities.sprites.plasma import Plasma


class Space:
    """A class to model the space that holds all entities

    Attributes:
        group_handler: The GroupHandler object used to handle the entity-groups of the space
        collision_handler: The CollisionHandler object used to check for entity collisions
        coordinate_system: The coordinate system of the space
        ship: The spaceship directed by the player, initially at the center of space
        asteroids: A group of Asteroid objects, initially empty
        plasmas: A group of Plasma objects, initially empty
        all_entities: the group of all entities in the space, initialised to hold just the ship

    """
    def __init__(self, group_handler, collision_handler, coordinate_system):
        """The class constructor

        Args:
            group_handler (GroupHandler): used to handle the entity-groups of the space
            collision_handler (CollisionHandler): used to check for entity collisions
            coordinate_system (CoordinateSystem): models coordinates and their transformations
        """
        self.__group_handler = group_handler
        self.__collision_handler = collision_handler
        self.__coordinate_system = coordinate_system
        center = self.__coordinate_system.center()
        self.__ship = Ship((center[0], center[1]))
        self.__asteroids = self.__group_handler.group()
        self.__plasmas = self.__group_handler.group()
        self.__all_entities = self.__group_handler.group()
        self.__add_entity(self.__ship, self.__all_entities)

    def __add_entity(self,entity, group):
        """Method to add an entity to a group and the all_entities group
        using the group_handler

        Args:
            entity (Entity): the entity to be added
            group (pygame.sprite.Group): the sprite group one wished to add the entity to
        """
        self.__group_handler.add(entity, group)
        self.__group_handler.add(entity, self.__all_entities)

    def __move_objects(self):
        for entity in self.__all_entities:
            entity.move()

    def fire_ship_cannon(self):
        """A method for adding a plasma object to plasmas with
        the direction and location of the ship's tip
        """
        position = self.__ship.get_tip()
        direction = self.__ship.direction
        plasma = Plasma(tuple(position), direction)
        self.__add_entity(plasma, self.__plasmas)

    def change_ship_velocity(self, direction, change):
        self.__ship.change_velocity(direction, change)

    def __check_collisions(self):
        asteroid_destructions = self.__collision_handler.handle_plasma_hits(self.__plasmas,
        self.__asteroids)
        ship_destruction = self.__collision_handler.check_ship_destruction(
            self.__ship, self.__asteroids)
        return asteroid_destructions, ship_destruction
        # self.handle_asteroid_collision()

    def __create_asteroid(self, difficulty):
        if randint(20*difficulty,500) == 100:
            coordinates = self.__coordinate_system.random_coordinates(111,137)
            direction = self.__coordinate_system.random_direction(coordinates)
            asteroid = Asteroid(coordinates, direction, difficulty/3)
            self.__add_entity(asteroid, self.__asteroids)

    def update(self, difficulty):
        self.__create_asteroid(difficulty)
        self.__move_objects()
        plasma_hits, ship_destruction = self.__check_collisions()
        if ship_destruction:
            return False
        return plasma_hits

    @property
    def ship(self):
        return self.__ship

    @property
    def plasmas(self):
        return self.__plasmas

    @property
    def all_entities(self):
        return self.__all_entities
