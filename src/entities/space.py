from random import randint
from entities.sprites.ship import Ship
from entities.sprites.asteroid import Asteroid


class Space:
    def __init__(self, group_handler, collision_handler, coordinate_system):
        self.difficulty = 3
        self.group_handler = group_handler
        self.collision_handler = collision_handler
        self.coordinate_system = coordinate_system
        center = self.coordinate_system.center()
        self.ship = Ship((center[0], center[1]))
        self.asteroids = self.group_handler.group()
        self.plasmas = self.group_handler.group()
        self.all_entities = self.group_handler.group()
        self.add_entity(self.ship, self.all_entities)

    def add_entity(self,entity, group):
        self.group_handler.add(entity, group)
        self.group_handler.add(entity, self.all_entities)

    def move_objects(self):
        for entity in self.all_entities:
            entity.move()

    def fire_ship_cannon(self):
        plasma = self.ship.fire_plasma()
        self.add_entity(plasma, self.plasmas)

    def change_ship_velocity(self, direction, change):
        self.ship.change_velocity(direction, change)

    def handle_collisions(self):
        plasma_hits = self.collision_handler.handle_plasma_hits(self.plasmas, self.asteroids)
        ship_destruction = self.collision_handler.check_ship_destruction(self.ship, self.asteroids)
        return plasma_hits, ship_destruction
        # self.handle_asteroid_collision()

    def create_asteroid(self):
        if randint(20*self.difficulty,500) == 100:
            coordinates = self.coordinate_system.random_coordinates(111,137)
            direction = self.coordinate_system.random_direction(coordinates)
            asteroid = Asteroid(coordinates, direction, self.difficulty/3, 1)
            self.add_entity(asteroid, self.asteroids)
