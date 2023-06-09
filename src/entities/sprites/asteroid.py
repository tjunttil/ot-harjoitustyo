from .entity import Entity

class Asteroid(Entity):
    def __init__(self, coordinates, direction, velocity):
        super().__init__(coordinates, direction, velocity)
        super()._load_image("asteroid.png")
        self.__hits = 0

    def get_hit(self):
        self.__hits += 1

    @property
    def hits(self):
        return self.__hits
